"""Base class and utilities for all hacking tools in the toolkit."""

import os
import subprocess
import shutil
from abc import ABC, abstractmethod
from typing import Optional


class BaseTool(ABC):
    """Abstract base class for all tools in the hackingtool suite.

    Each tool category should subclass this and implement the required methods.
    """

    def __init__(
        self,
        name: str,
        description: str,
        install_command: Optional[str] = None,
        repo_url: Optional[str] = None,
    ):
        """
        Initialize a tool entry.

        Args:
            name: Human-readable name of the tool.
            description: Short description of what the tool does.
            install_command: Shell command used to install the tool.
            repo_url: GitHub/GitLab URL to clone the tool from.
        """
        self.name = name
        self.description = description
        self.install_command = install_command
        self.repo_url = repo_url

    @abstractmethod
    def run(self) -> None:
        """Launch the tool. Must be implemented by subclasses."""
        raise NotImplementedError

    def is_installed(self) -> bool:
        """Check whether the tool binary/directory is available on the system."""
        # Check if the tool name resolves to an executable in PATH
        return shutil.which(self.name.lower().replace(" ", "")) is not None

    def install(self) -> bool:
        """Attempt to install the tool using the configured install command.

        Returns:
            True if installation succeeded, False otherwise.
        """
        if not self.install_command:
            print(f"[!] No install command defined for '{self.name}'.")
            return False

        print(f"[*] Installing {self.name} ...")
        try:
            result = subprocess.run(
                self.install_command,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            print(result.stdout)
            print(f"[+] {self.name} installed successfully.")
            return True
        except subprocess.CalledProcessError as exc:
            print(f"[-] Failed to install {self.name}: {exc.stderr}")
            return False

    def clone_repo(self, target_dir: str = "/opt") -> bool:
        """Clone the tool's repository into target_dir if a repo URL is set.

        Args:
            target_dir: Directory under which the repo will be cloned.

        Returns:
            True if cloning succeeded, False otherwise.
        """
        if not self.repo_url:
            print(f"[!] No repository URL defined for '{self.name}'.")
            return False

        repo_name = self.repo_url.rstrip("/").split("/")[-1].replace(".git", "")
        dest = os.path.join(target_dir, repo_name)

        if os.path.isdir(dest):
            print(f"[*] Repository already exists at {dest}. Skipping clone.")
            return True

        print(f"[*] Cloning {self.repo_url} into {dest} ...")
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", self.repo_url, dest],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            print(f"[+] Cloned successfully to {dest}.")
            return True
        except subprocess.CalledProcessError as exc:
            print(f"[-] Git clone failed: {exc.stderr}")
            return False

    def __repr__(self) -> str:  # pragma: no cover
        return f"<Tool name={self.name!r} installed={self.is_installed()}>"
