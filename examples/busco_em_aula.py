import requests

def get_ortho_id_from_busco_id(busco_id):
    url_query = f"https://www.orthodb.org/search?query={busco_id}"

    data = requests.get(url_query).json()

    ortho_id = data["data"][0]

    return ortho_id


def get_ortho_descriptions(ortho_id):
    url_query = f"https://www.orthodb.org/group?id={ortho_id}" 
    data = requests.get(url_query).json()

    interpro_domains = data["data"]["interpro_domains"]

    descriptions = []

    for domain in interpro_domains:
        descriptions.append(domain["description"])

    return descriptions

busco_ids = ["EOG093714Q2", "EOG09370GHP", "EOG09370OS5"]

for busco_id in busco_ids:
    ortho_id = get_ortho_id_from_busco_id(busco_id)
    descriptions = get_ortho_descriptions(ortho_id)

    for description in descriptions:
        print(f"{busco_id}\t{description}")