# import re

# from app.models.incident import Incident


# class ComposerLogParser:

#     @staticmethod
#     def parse(log):

#         payload = str(log)

#         dag = re.search(
#             r'customer_pipeline',
#             payload
#         )

#         task = re.search(
#             r'load',
#             payload
#         )

#         return Incident(

#             dag_id=dag.group(0) if dag else None,

#             task_id=task.group(0) if task else None,

#             severity=log.get("severity"),

#             message=payload
#         )