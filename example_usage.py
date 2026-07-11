from client import CustomerCohortValuePredictorClient
client = CustomerCohortValuePredictorClient()
print(client.predict_cohort_value(100, 50.0, 0.8))