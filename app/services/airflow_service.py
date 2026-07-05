# import requests

# import google.auth.transport.requests

# import google.oauth2.id_token


# class AirflowService:

#     def __init__(self, base_url):

#         self.base_url = base_url

#     def get_dag(self, dag):

#         endpoint = f"{self.base_url}/api/v1/dags/{dag}"

#         auth_req = google.auth.transport.requests.Request()

#         token = google.oauth2.id_token.fetch_id_token(

#             auth_req,

#             endpoint

#         )

#         response = requests.get(

#             endpoint,

#             headers={

#                 "Authorization": f"Bearer {token}"

#             }

#         )

#         response.raise_for_status()

#         return response.json()

#     def get_latest_run(self, dag):

#         endpoint = (

#             f"{self.base_url}"

#             f"/api/v1/dags/{dag}/dagRuns"

#             "?order_by=-start_date&limit=1"

#         )

#         auth_req = google.auth.transport.requests.Request()

#         token = google.oauth2.id_token.fetch_id_token(

#             auth_req,

#             endpoint

#         )

#         response = requests.get(

#             endpoint,

#             headers={

#                 "Authorization": f"Bearer {token}"

#             }

#         )

#         return response.json()