def forecast_periods(last_historical_year: str, years: int = 5) -> list[str]:
    year = _extract_year(last_historical_year) or 2025
    return [f"FY{year + index}" for index in range(1, years + 1)]


def _extract_year(period: str) -> int | None:
    digits = "".join(character for character in period if character.isdigit())
    if len(digits) >= 4:
        return int(digits[-4:])
    return None

