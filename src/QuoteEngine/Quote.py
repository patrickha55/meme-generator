class Quote():
    """Quote model
    """

    def __init__(self, body: str, author: str) -> None:
        self.body = body
        self.author = author

    def __str__(self) -> str:
        f"{self.body} - {self.author}"
