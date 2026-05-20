def normalize_ebitda(reported_ebitda: float, adjustments: list[float] | None = None) -> float:
    return reported_ebitda + sum(adjustments or [])
