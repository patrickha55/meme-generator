from abc import ABC, abstractmethod


class GeneratorInterface(ABC):
    @abstractmethod
    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        pass
