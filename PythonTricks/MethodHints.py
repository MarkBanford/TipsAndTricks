from typing import Annotated


def get_velocity(distance: Annotated[float, "meters"], time: Annotated[float, "seconds"]) -> float:
    return distance / time


