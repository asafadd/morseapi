gcloud builds submit --tag gcr.io/morseAPI/morsetranslate
gcloud beta run deploy --image gcr.io/morseapi/morsetranslate --platform managed