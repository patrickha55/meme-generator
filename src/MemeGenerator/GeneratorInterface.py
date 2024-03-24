from abc import ABC, abstractmethod


class GeneratorInterface(ABC):
    """Abstract base class for creating a meme generator class.

    Args:
        ABC (_type_): Abstract base class.
    """

    @abstractmethod
    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        """Generate a meme from an image by resizing, attaching quote(text) and author to the resized image.

        Args:
            img_path (str): Image's path.
            text (str): Quote to display inside a meme.
            author (str): Quote's author.
            width (int, optional): Image width for resizing. Defaults to 500.

        Returns:
            str: Generated meme's path.
        """
        pass
