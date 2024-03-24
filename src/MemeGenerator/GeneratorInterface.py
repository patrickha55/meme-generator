from abc import ABC, abstractmethod


class GeneratorInterface(ABC):
    """TODO: add doc

    Args:
        ABC (_type_): _description_
    """

    @abstractmethod
    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        """TODO: add doc

        Args:
            img_path (str): _description_
            text (str): _description_
            author (str): _description_
            width (int, optional): _description_. Defaults to 500.

        Returns:
            str: _description_
        """
        pass
