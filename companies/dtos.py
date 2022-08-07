from dataclasses import dataclass
from decimal import Decimal

from companies.models import Company

@dataclass
class AccessPointDTO:
    id: int
    name: str
    email: str
    state: bool
    longitude: Decimal
    latitude: Decimal
    company: Company
    access: bool