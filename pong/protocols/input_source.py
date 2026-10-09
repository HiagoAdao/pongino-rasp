from typing import Protocol


class InputSourceProtocol(Protocol):
    async def start(self) -> None:
        """Inicia a fonte de entrada."""
        ...

    async def stop(self) -> None:
        """Finaliza a fonte de entrada."""
        ...

    async def is_connected(self) -> bool:
        """Indica se a fonte está conectada ao dispositivo de entrada."""
        ...
