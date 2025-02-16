# version_control/version_manager.py

import json
import os
from datetime import datetime

class VersionManager:
    """
    Manages version control, rollback, and forking for AI evolution.
    """

    def __init__(self, version_directory="version_control/versions"):
        self.version_directory = version_directory
        os.makedirs(self.version_directory, exist_ok=True)

    def save_version(self, data, version_name=None):
        """
        Saves a snapshot of the current system state.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        version_name = version_name or f"version_{timestamp}.json"
        version_path = os.path.join(self.version_directory, version_name)

        with open(version_path, "w") as version_file:
            json.dump(data, version_file, indent=4)

        return f"Version saved: {version_name}"

    def rollback_version(self, version_name):
        """
        Restores a previous system state.
        """
        version_path = os.path.join(self.version_directory, version_name)

        if os.path.exists(version_path):
            with open(version_path, "r") as version_file:
                return json.load(version_file)

        return "Version not found."
