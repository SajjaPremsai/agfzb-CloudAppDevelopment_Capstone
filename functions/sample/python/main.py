"""IBM Cloud Function that gets all reviews for a dealership

Returns:
    List: List of reviews for the given dealership
"""
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests


def main(param_dict):
    """Main Function

    Args:
        param_dict (Dict): input paramater

    Returns:
        _type_: _description_ TODO
    """

    try:
        client = Cloudant.iam(
            account_name=param_dict["COUCH_USERNAME"],
            api_key=param_dict["IAM_API_KEY"],
            connect=True,
        )
        print(f"Databases: {client.all_dbs()}")
    except CloudantException as cloudant_exception:
        print(f"unable to connect  {cloudant_exception}")
        return {"error": cloudant_exception}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {"dbs": client.all_dbs()}

main({
    "COUCH_URL": "https://1019b037-d6c8-437c-bdca-d8f02dd27dd5-bluemix.cloudantnosqldb.appdomain.cloud",
    "IAM_API_KEY": "NzfXNIB_O7o4ozaVk1TWRKvvqQL7w4K1gm5L-Df38Zv2",
    "COUCH_USERNAME": "1019b037-d6c8-437c-bdca-d8f02dd27dd5-bluemix"
})
