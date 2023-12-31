import requests
import json
from .models import CarDealer, DealerReview 
from requests.auth import HTTPBasicAuth

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None

    try:
        json_data = response.json()
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return None

    status_code = response.status_code
    print("With status {} ".format(status_code))
    return json_data


def get_dealers_data(url):
    
    json_result = requests.get(url).json()
    return json_result
    


def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, **kwargs)
    
    if not json_result:
        # Handle the case where the request did not return valid JSON
        print("Error: No valid JSON data received")
        return results

    # For each dealer object
    for dealer in json_result:
        if not isinstance(dealer, dict):
            # Handle the case where a dealer is not a dictionary
            print("Error: Dealer object is not a dictionary")
            continue

        # Create a CarDealer object with values in the dealer dictionary
        dealer_obj = CarDealer(
            address=dealer.get("address", ""),
            city=dealer.get("city", ""),
            full_name=dealer.get("full_name", ""),
            id=dealer.get("id", ""),
            lat=dealer.get("lat", ""),
            long=dealer.get("long", ""),
            short_name=dealer.get("short_name", ""),
            st=dealer.get("st", ""),
            zip=dealer.get("zip", "")
        )
        results.append(dealer_obj)
    # print(results)

    return results

def post_request(url, payload, **kwargs):
    print(url)
    print(payload)
    print(kwargs)
    try:
        response = requests.post(url, params=kwargs, json=payload)
    except Exception as e:
        print("Error" ,e)
    print("Status Code ", {response.status_code})
    data = json.loads(response.text)
    return data


def get_reviews_from_api(dealer_id):
    print(dealer_id)
    url = f"http://localhost:5000/api/get_reviews?id={dealer_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None

    try:
        json_result = response.json()
    except ValueError as e:
        print(f"JSON decoding error: {e}")
        return None
    # results = [
    #     DealerReview(
    #         dealership=review.get("dealership", ""),
    #         name=review.get("full_name", ""),
    #         purchase=review.get("purchase", ""),
    #         review=review.get("review", ""),
    #         purchase_date=review.get("purchase_date", ""),
    #         car_make=review.get("car_make", ""),
    #         car_model=review.get("car_model", ""),
    #         car_year=review.get("car_year", ""),
    #         ,
    #         id=review.get("id", "")
    #     )
    #     for review in json_result
    # ]

    return json_result


def analyze_review_sentiments(dealerreview, **kwargs):
    API_KEY="YviJ5LYMbYHv4uX4zoAtfVnRm3UyTLSVCW-HGf6Hcy_a"
    #API_KEY="0614ccd0-1e9f-4d49-923e-e7741f963747:Q3ZX2R1b3oBEb0XebEO99rpulJ31yoY7X5GfjoQykN4RpM9eThYrrs14If0aOHtG"
    NLU_URL='https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/53d02b4a-b8c1-4c70-8600-864e75ebb468'
    params = json.dumps({"text": dealerreview, "features": {"sentiment": {}}})
    response = requests.post(NLU_URL,data=params,headers={'Content-Type':'application/json'},auth=HTTPBasicAuth("apikey", API_KEY))
    
    #print(response.json())
    try:
        sentiment=response.json()['sentiment']['document']['label']
        return sentiment
    except:
        return "neutral"