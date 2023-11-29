# main.py

from logic import fetch_base_data, fetch_detailed_data, filter_base_data

# Endpoint pour les données de base
endpoint_base = 'https://whiskyhunter.net/api/distilleries_info/'

# Récupérer les données de base
df_base = fetch_base_data(endpoint_base)

# Récupérer les données détaillées
df_detailed = fetch_detailed_data(df_base['slug'])

# Filtrer le DataFrame de base
df_base_filtered = filter_base_data(df_base, df_detailed)

# Enregistrer le DataFrame détaillé au format JSON
df_detailed.to_json("data.json", orient='split', index=True)

# Vous pouvez maintenant effectuer des opérations supplémentaires sur df_base_filtered et df_detailed
