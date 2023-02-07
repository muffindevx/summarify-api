import cohere
import os

API_TRIAL_KEY = os.getenv('API_TRIAL_KEY')

def get_client():
  client = cohere.Client(API_TRIAL_KEY)
  return client