from dataclasses import dataclass
import requests


@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: str | None
    address_2: str | None
    address_3: str | None
    city: str | None
    state_province: str | None
    postal_code: str | None
    country: str | None
    longitude: str | None
    latitude: str | None
    phone: str | None
    website_url: str | None
    state: str | None
    street: str | None

    def __str__(self) -> str:
        lokalizacja = (
            f"{self.city or 'Brak miasta'}, "
            f"{self.country or 'Brak kraju'}"
        )
        strona = self.website_url or "brak strony"
        return (
            f"[{self.brewery_type.upper()}] {self.name} "
            f"({lokalizacja}) | WWW: {strona}"
        )


def pobierz_browary() -> list[Brewery]:
    url = "https://api.openbrewerydb.org/v1/breweries"
    parametry = {"per_page": 20}

    odpowiedz = requests.get(url, params=parametry, timeout=10)
    odpowiedz.raise_for_status()

    dane_json = odpowiedz.json()

    lista_browarow: list[Brewery] = []
    for item in dane_json:
        browar = Brewery(
            id=item.get("id"),
            name=item.get("name"),
            brewery_type=item.get("brewery_type"),
            address_1=item.get("address_1"),
            address_2=item.get("address_2"),
            address_3=item.get("address_3"),
            city=item.get("city"),
            state_province=item.get("state_province"),
            postal_code=item.get("postal_code"),
            country=item.get("country"),
            longitude=item.get("longitude"),
            latitude=item.get("latitude"),
            phone=item.get("phone"),
            website_url=item.get("website_url"),
            state=item.get("state"),
            street=item.get("street"),
        )
        lista_browarow.append(browar)

    return lista_browarow


browary = pobierz_browary()
for browar in browary:
    print(browar)
