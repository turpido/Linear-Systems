from pathlib import Path

class FileHandler:
    """
    A simple utility class for reading and saving files (e.g., audio files).
    Works with any binary file format.
    """

    def __init__(self, base_dir: str = "./"):
        """
        base_dir: default directory for saving or reading files.
        """
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def read_file(self, file_path: str) -> bytes:
        """
        Reads any file (audio/file/etc.) in binary mode and returns its bytes.
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(path, "rb") as f:
            return f.read()

    def save_file(self, filename: str, data: bytes) -> str:
        """
        Saves bytes to a file under base_dir.
        Returns the full output path.
        """
        output_path = self.base_dir / filename
        
        with open(output_path, "wb") as f:
            f.write(data)

        return str(output_path)

    def exists(self, file_path: str) -> bool:
        """
        Checks if a file exists.
        """
        return Path(file_path).exists()
