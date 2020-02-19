import requests
import pandas as pd
import io


dati = requests.get("http://dati.lazio.it/catalog/it/dataset/79dfc4f3-6872-4fd9-84e3-786a824509cf/resource/60550f81-105b-460b-ad47-d4feb8aa0a2e/download/standardcomunali2018.csv").text
df = pd.read_csv(io.StringIO(dati), sep=";")

with open("masiero.json", "w") as f:
  f.write(df.to_json(indent=2))
  
