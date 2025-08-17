# persona.py
import yaml

class PersonaManager:
    """
    Manages the agent's persona from a YAML configuration file.
    """
    def __init__(self, persona_path="persona.yaml"):
        try:
            with open(persona_path, 'r') as f:
                self.persona = yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Warning: {persona_path} not found. Using default messages.")
            self.persona = {}

    def get_message(self, key, **kwargs):
        """
        Formats a message from the persona template.
        
        Args:
            key (str): The key of the message template (e.g., "proposing_action").
            **kwargs: The variables to substitute into the template.
        
        Returns:
            str: The formatted message.
        """
        template = self.persona.get(key, "No message template found for '{key}'.")
        return template.format(**kwargs)
