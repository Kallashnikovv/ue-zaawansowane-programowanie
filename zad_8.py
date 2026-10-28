import argparse
import requests


class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        address_1: str | None,
        address_2: str | None,
        address_3: str | None,
        city: str | None,
        state_province: str | None,
        postal_code: str | None,
        country: str | None,
        longitude: float | str | None,
        latitude: float | str | None,
        phone: str | None,
        website_url: str | None,
        state: str | None,
        street: str | None,
    ) -> None:
        self.id: str = id
        self.name: str = name
        self.brewery_type: str = brewery_type
        self.address_1: str | None = address_1
        self.address_2: str | None = address_2
        self.address_3: str | None = address_3
        self.city: str | None = city
        self.state_province: str | None = state_province
        self.postal_code: str | None = postal_code
        self.country: str | None = country
        self.longitude: float | str | None = longitude
        self.latitude: float | str | None = latitude
        self.phone: str | None = phone
        self.website_url: str | None = website_url
        self.state: str | None = state
        self.street: str | None = street

    def __str__(self) -> str:
        return (
            f"Brewery(id={self.id}, name={self.name}, "
            f"type={self.brewery_type}, city={self.city}, "
            f"state={self.state}, country={self.country}, "
            f"street={self.street}, postal_code={self.postal_code}, "
            f"phone={self.phone}, website_url={self.website_url})"
        )


def fetch_breweries(
    limit: int = 20, city: str | None = None
) -> list[Brewery]:
    url: str = "https://api.openbrewerydb.org/v1/breweries"
    params: dict[str, int | str] = {"per_page": limit}
    if city:
        params["by_city"] = city

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    breweries: list[Brewery] = []
    for item in data:
        brewery = Brewery(
            id=item.get("id", ""),
            name=item.get("name", ""),
            brewery_type=item.get("brewery_type", ""),
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
        breweries.append(brewery)

    return breweries


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Pobieranie listy browarów z Open Brewery DB API."
    )
    parser.add_argument(
        "--city",
        type=str,
        default=None,
        help="Miasto, dla którego mają zostać pobrane browary",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    breweries_list: list[Brewery] = fetch_breweries(20, city=args.city)
    for brewery in breweries_list:
        print(brewery)

