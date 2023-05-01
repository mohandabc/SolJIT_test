import requests
import json

# Get access token with provided credentials 
auth_url = "https://login.salesforce.com/services/oauth2/token"
client_id = "3MVG9I9urWjeUW051PumYX1mbS5HkS3kpZsbCEzYWjgivRyDno1MjvM08EfVf2be52s0vrthHamsgMpQCrm5Z"
client_secret = "EC97DAFBF9F6F2399DE5E7BADA2E9BBEF6B3B6E832DC435668AA452940AD9501"
username = "soljit_algeria2@soljit.com"
password = "entretient_1235zoLmTaUDLiouUaOAN6WhOQPi"

instance_url = "https://soljit35-dev-ed.my.salesforce.com"


def authenticate():
    """Connect to API and get access tocken and instance url"""

    headers = {
    "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {
        "grant_type": "password",
        "client_id": client_id,
        "client_secret": client_secret,
        "username": username,
        "password": password
    }

    response = requests.post(auth_url, headers=headers, data=payload)

    result = json.loads(response.content.decode('utf-8'))
    access_token = result['access_token']
    return access_token


#1. Get Candidature a004L000002gCJK
def question_1(access_token):
    """First question answer"""

    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    url = f'''{instance_url}/services/data/v55.0/sobjects/Candidature__c/a004L000002gCJK?fields=First_Name__c,Last_Name__c,Year__c,Year_Of_Experience__c'''

    response = requests.get(url, headers=headers)
    accounts = json.loads(response.content.decode('utf-8'))

    return accounts

#2. create candidature

def create_candidature(access_token):
    url = f'{instance_url}/services/data/v55.0/sobjects/Candidature__c/'
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    new_record = {
        "First_Name__c": "Mohand",
        "Last_Name__c":"ABCHICHE",
        "Year_Of_Experience__c": "5"
    }
    response = requests.post(url, headers=headers, data=json.dumps(new_record))
    result = json.loads(response.content.decode('utf-8'))

    return result

# 3. Edit
def edit_candidature(access_token):
    url = f'{instance_url}/services/data/v55.0/sobjects/Candidature__c/a004L000002gCJK'
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    updated_record = {
        'Last_Name__c' : "ABCHICHE"
    }
    response = requests.patch(url, headers=headers, data=json.dumps(updated_record))
    # result = json.loads(response.content.decode('utf-8'))
    return response


# 4. Get all
def get_candidatures(access_token):

    url = f'{instance_url}/services/data/v55.0/sobjects/candidature__c'
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    result = json.loads(response.content.decode('utf-8'))

    candidature_name_list = []

    for candidature in result["recentItems"]:
        candidature_name_list.append({'name':candidature.get('Name')})

        # We can get details of each candidature by accessing the url of each one as follow

        # candidat_url = candidature['attributes'].get('url')
        # c_url = f'{instance_url}{candidat_url}'
        # response = requests.get(c_url, headers=headers)
        # result = json.loads(response.content.decode('utf-8'))
        # print(result)
    return candidature_name_list


#5. fonction recherche
def search_candidature(id:str, access_token):
    """Search a candidature based on a given id"""

    url = f'{instance_url}/services/data/v55.0/sobjects/candidature__c/{id}'
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    result = json.loads(response.content.decode('utf-8'))
    return result


def main():
    print("Estabilishing connection\n")
    access_token = authenticate()
    print(access_token)

    print('\n1. Get candidature a004L000002gCJK------------------------------------')
    accounts = question_1(access_token=access_token)

    print(accounts.get('First_Name__c'))
    print(accounts.get('Last_Name__c'))
    print(accounts.get('Year__c'))
    print(accounts.get('Year_Of_Experience__c'))


    print('\n2. create my candidature------------------------------------')
    id = create_candidature(access_token=access_token)
    print(id)


    print('\n3. Edit candidature------------------------------------')
    id = edit_candidature(access_token=access_token)
    print(id)


    print('\n4. Get all candidatures------------------------------------')
    candidatures = get_candidatures(access_token=access_token)
    print(candidatures)

    print('\n5. search candidature------------------------------------')
    result = search_candidature('a004L000002gCJK', access_token)
    print(result)
