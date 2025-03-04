from pydantic import BaseModel


class Price(BaseModel):
    open: float
    close: float
    high: float
    low: float
    volume: int
    time: str = \"N/A\" # Fallback value for missing calendar_date


class PriceResponse(BaseModel):
    ticker: str
    prices: list[Price]
