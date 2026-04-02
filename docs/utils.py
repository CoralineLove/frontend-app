import os
import json
from typing import Optional, Dict, Any, List
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def read_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in file: {file_path}")
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
    return None

def write_json_file(file_path: str, data: Dict[str, Any], indent: int = 2) -> bool:
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=indent)
        return True
    except Exception as e:
        logger.error(f"Error writing to file {file_path}: {str(e)}")
        return False

def ensure_directory_exists(dir_path: str) -> bool:
    try:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        logger.error(f"Error creating directory {dir_path}: {str(e)}")
        return False

def get_file_extension(file_path: str) -> str:
    return os.path.splitext(file_path)[1].lower()

def list_files_in_directory(dir_path: str, extensions: Optional[List[str]] = None) -> List[str]:
    if not os.path.isdir(dir_path):
        logger.error(f"Directory not found: {dir_path}")
        return []
    
    files = []
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            if extensions is None or get_file_extension(file_path) in extensions:
                files.append(file_path)
    return files

def validate_file_path(file_path: str) -> bool:
    return os.path.exists(file_path) and os.path.isfile(file_path)

def validate_directory_path(dir_path: str) -> bool:
    return os.path.exists(dir_path) and os.path.isdir(dir_path)