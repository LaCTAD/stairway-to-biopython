"""
busco.py é um exemplo didático usado no curso de bioinformática 1s2020.
Esse código é uma conversão do script R presente em

https://thackl.github.io/BUSCO-gene-descriptions

Script atual:

    library(tidyverse)
    library(jsonlite)

    busco_ids <- c("EOG093714Q2", "EOG09370GHP", "EOG09370OS5")
    names(busco_ids) <- busco_ids # so map_df gets .id right

    # a tibble of interpro profile associated with each busco_id
    busco_ipr <- map_df(busco_ids, .id="busco_id",  function(busco_id){
    write(busco_id, stderr()) # just so we can monitor progress

    # map the BUSCO ID to OrthoDB group ID
    query <- read_json(paste0("https://www.orthodb.org/search?query=", busco_id))
    odb_id <- query$data[1]

    # get all info on the orthogroup
    odb_info <- read_json(paste0("https://www.orthodb.org/group?id=", odb_id),
        simplifyVector = TRUE)

    # return the interpro table
    odb_info$data$interpro_domains

    })

    busco_ipr %>% select(busco_id, description)

Resultado atual:
        busco_id                                              description
    1 EOG093714Q2                          Mediator complex, subunit Med31
    2 EOG093714Q2       Mediator complex, subunit Med31 domain superfamily
    3 EOG09370GHP                       Reduced growth phenotype protein 1
    4 EOG09370OS5 Ribosomal protein S2, flavodoxin-like domain superfamily
    5 EOG09370OS5                                     Ribosomal protein S2
    6 EOG09370OS5      Ribosomal protein S2, bacteria/mitochondria/plastid
    7 EOG09370OS5                     Ribosomal protein S2, conserved site
"""

import requests

def get_descriptions(busco_id):
    """
    get_descriptions returns the OrthoDB descriptions from a given BUSCO ID
    """

    # Primeiro buscamos pelo ID equivalente no OrthoDB
    query_url = f"https://www.orthodb.org/search?query={busco_id}"
    data = requests.get(query_url).json()

    # O ID no OrthoDB estará dentro da chave "data", na primeira posição
    orthodb_id = data["data"][0]

    # Agora que temos o ID no OrthoDB, podemos pesquisar dentro do OrthoDB
    orthodb_url = f"https://www.orthodb.org/group?id={orthodb_id}"
    orthodb_data = requests.get(orthodb_url)
    
    # A informação retornada é um dicionário, dentro da chave 'data' temos um
    # outro dicionário. Por sua vez, esse outro dicionário contém a chave
    # 'interpro_domains', que contém o valor que queremos
    domains = orthodb_data.json()["data"]["interpro_domains"]


    # Um mesmo registro no OrthoDB pode ter várias descrições Vamos
    # guardar todas elas em uma lista para retornar todas.
    # Poderíamos fazer isso através de uma list comprehension também!
    descriptions = []

    for domain in domains:
        # Cada domínio em si é um dicionário que contém a chave 'description'
        # Essa chave possui o valor que buscamos.
        descriptions.append(domain["description"])

    # Por fim, retornamos as descrições.
    return descriptions

# Os busco_ids que queremos
busco_ids = ["EOG093714Q2", "EOG09370GHP", "EOG09370OS5"]

# Percorremos todos eles
for busco_id in busco_ids:

    # Obtemos todas as descrições
    descriptions = get_descriptions(busco_id)

    # Imprimos todas!
    for description in descriptions:
        print(f"{busco_id}\t{description}")