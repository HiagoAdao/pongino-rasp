from typing import Protocol


class ButtonReaderProtocol(Protocol):
    @property
    def is_pressed(self) -> bool:
        """Retorna se o botão está pressionado."""
        ...

    def close(self) -> None:
        """Libera os recursos associados ao botão."""
        ...
