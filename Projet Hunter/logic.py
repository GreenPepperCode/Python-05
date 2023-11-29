# logic.py

import requests
import pandas as pd

def fetch_base_data(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Erreur lors de la requête de base : {response.status_code}")

def fetch_detailed_data(slugs):
    df_detailed = pd.DataFrame()
    for slug in slugs:
        response = requests.get(f'https://whiskyhunter.net/api/distillery_data/{slug}/')
        if response.status_code == 200:
            df_temp = pd.DataFrame(response.json())
            df_temp['slug'] = slug
            df_detailed = pd.concat([df_detailed, df_temp], ignore_index=True)
        else:
            print(f"Erreur pour le slug {slug}")
    return df_detailed.set_index(['slug', 'dt'])

def filter_base_data(df_base, df_detailed):
    slugs_in_detailed = df_detailed.index.get_level_values('slug').unique()
    return df_base[df_base['slug'].isin(slugs_in_detailed)]
