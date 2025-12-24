import logging
import os
import re
import json

from frontend_app.exceptions import MissingConfigFile

logger = logging.getLogger(__name__)

def load_config(config_path):
    """Load config from file."""
    if not os.path.exists(config_path):
        raise MissingConfigFile(f"Config file not found at {config_path}")
    try:
        with open(config_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON: {e}")
        raise

def validate_email(email):
    """Check if email is valid."""
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    if pattern.match(email):
        return True
    return False