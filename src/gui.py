import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QTextEdit, QLineEdit, QPushButton, QTreeView, QFileSystemModel,
    QListWidget
)
import os
import glob
from PySide6.QtCore import QDir, QThread, Signal, QObject

# Import agent components
from main import Proposer, Governor, Executor
from tools.file_system import read_file, write_file, list_directory
from tools.web_search import search_web

class AgentWorker(QObject):
    """
    Worker thread for running the Conscience Agent.
    Communicates with the main GUI thread via signals.
    """
    log_message = Signal(str)
    task_finished = Signal()

    def __init__(self, task):
        super().__init__()
        self.task = task
        self._is_running = True

    def run(self):
        """Execute the agent's task."""
        self.log_message.emit("Starting agent...")

        proposer = Proposer()
        governor = Governor("constitution.yaml")
        tools = {
            "read_file": read_file,
            "write_file": write_file,
            "list_directory": list_directory,
            "search_web": search_web,
        }
        executor = Executor(tools)

        if not self._is_running:
            self.log_message.emit("Agent stopped before starting.")
            self.task_finished.emit()
            return

        action = proposer.propose_action(self.task)
        self.log_message.emit(f"Proposer suggests: {action}")

        if self._is_running and governor.approve_action(action):
            self.log_message.emit(f"Governor approves: {action}")
            if self._is_running:
                result = executor.execute_action(action)
                self.log_message.emit(f"Executor result: {result}")
        elif self._is_running:
            self.log_message.emit(f"Governor denies: {action}")

        self.log_message.emit("Agent task complete.")
        self.task_finished.emit()

    def stop(self):
        self._is_running = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conscience Agent")
        self.setGeometry(100, 100, 1200, 800)

        # Main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # --- Left Pane: Tabs ---
        left_pane = QTabWidget()
        main_layout.addWidget(left_pane, 1) # 1/3 of the width

        # File Explorer Tab
        file_explorer_tab = QWidget()
        left_pane.addTab(file_explorer_tab, "File Explorer")
        
        file_layout = QVBoxLayout(file_explorer_tab)
        self.file_model = QFileSystemModel()
        self.file_model.setRootPath(QDir.currentPath())
        self.file_tree = QTreeView()
        self.file_tree.setModel(self.file_model)
        file_layout.addWidget(self.file_tree)

        # Constitution Editor Tab
        constitution_tab = QWidget()
        left_pane.addTab(constitution_tab, "Constitution Editor")
        
        constitution_layout = QVBoxLayout(constitution_tab)
        self.constitution_editor = QTextEdit()
        constitution_layout.addWidget(self.constitution_editor)
        
        save_constitution_button = QPushButton("Save Constitution")
        save_constitution_button.clicked.connect(self.save_constitution)
        constitution_layout.addWidget(save_constitution_button)

        # Documentation Tab
        docs_tab = QWidget()
        left_pane.addTab(docs_tab, "Documentation")
        docs_layout = QHBoxLayout(docs_tab)
        self.doc_list = QListWidget()
        self.doc_viewer = QTextEdit()
        self.doc_viewer.setReadOnly(True)
        docs_layout.addWidget(self.doc_list, 1)
        docs_layout.addWidget(self.doc_viewer, 2)
        self.doc_list.itemSelectionChanged.connect(self.display_documentation)

        # --- Right Pane: Main Interaction ---
        right_pane = QWidget()
        main_layout.addWidget(right_pane, 2) # 2/3 of the width
        right_layout = QVBoxLayout(right_pane)

        # Task Input
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter your task here...")
        right_layout.addWidget(self.task_input)

        # Control Buttons
        button_layout = QHBoxLayout()
        self.run_button = QPushButton("Run Task")
        self.stop_button = QPushButton("Stop Task")
        self.stop_button.setEnabled(False)
        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.stop_button)
        right_layout.addLayout(button_layout)

        # Log Viewer
        self.log_viewer = QTextEdit()
        self.log_viewer.setReadOnly(True)
        right_layout.addWidget(self.log_viewer)

        # Event Connections
        self.run_button.clicked.connect(self.run_task)
        self.stop_button.clicked.connect(self.stop_task)

        # Initial setup
        self.load_constitution()
        self.load_documentation_files()

    def load_documentation_files(self):
        """Finds all .md files and adds them to the documentation list."""
        try:
            markdown_files = glob.glob("*.md")
            self.doc_list.addItems(markdown_files)
        except Exception as e:
            self.log(f"Error loading documentation files: {e}")

    def display_documentation(self):
        """Displays the content of the selected documentation file."""
        try:
            selected_item = self.doc_list.currentItem()
            if selected_item:
                file_path = selected_item.text()
                with open(file_path, "r") as f:
                    self.doc_viewer.setPlainText(f.read())
        except Exception as e:
            self.log(f"Error displaying documentation: {e}")

    def run_task(self):
        """Starts the agent in a background thread."""
        task = self.task_input.text()
        if not task:
            self.log("Please enter a task.")
            return

        self.log(f"--- Starting task: {task} ---")
        self.run_button.setEnabled(False)
        self.stop_button.setEnabled(True)

        # Create and start the agent thread
        self.agent_thread = QThread()
        self.agent_worker = AgentWorker(task)
        self.agent_worker.moveToThread(self.agent_thread)

        # Connect signals
        self.agent_worker.log_message.connect(self.log)
        self.agent_worker.task_finished.connect(self.task_done)
        self.agent_thread.started.connect(self.agent_worker.run)

        self.agent_thread.start()

    def stop_task(self):
        """Stops the agent thread."""
        if hasattr(self, 'agent_worker'):
            self.agent_worker.stop()
        if hasattr(self, 'agent_thread'):
            self.agent_thread.quit()
            self.agent_thread.wait()
        self.log("--- Task stopped by user ---")
        self.task_done()

    def task_done(self):
        """Cleans up after a task is finished or stopped."""
        self.run_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        if hasattr(self, 'agent_thread'):
            self.agent_thread.quit()
            self.agent_thread.wait()

    def load_constitution(self):
        """Loads the content of constitution.yaml into the editor."""
        try:
            with open("constitution.yaml", "r") as f:
                self.constitution_editor.setPlainText(f.read())
        except FileNotFoundError:
            self.log("ERROR: constitution.yaml not found.")

    def save_constitution(self):
        """Saves the content of the editor to constitution.yaml."""
        try:
            with open("constitution.yaml", "w") as f:
                f.write(self.constitution_editor.toPlainText())
            self.log("Constitution saved successfully.")
        except Exception as e:
            self.log(f"Error saving constitution: {e}")

    def log(self, message):
        """Appends a message to the log viewer."""
        self.log_viewer.append(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
