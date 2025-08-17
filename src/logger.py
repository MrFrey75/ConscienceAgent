# Logger Module
import logging

def setup_logger():
    """
    Set up the logger for the application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename="audit.log",
        filemode="w",
    )
    return logging.getLogger(__name__)
