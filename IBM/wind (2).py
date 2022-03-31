import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "ZKFx7FCwNsBynhEn2Mf8n7t5T5s2Saj5w4MAeepp4MrI"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": 
			[{"field": [["Theoretical_Power_Curve (KWh)", "WindSpeed(m/s)"]], 
			"values": [[609.081469,5.952496]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/13b820e1-3b60-4f94-bc85-383adc1989c4/predictions?version=2022-03-29', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions =response_scoring.json()
print(predictions)
print('Final Prediction Result',predictions['predictions'][0]['values'][0][0])

#['Theoretical_Power_Curve (KWh)', 'WindSpeed(m/s)']

