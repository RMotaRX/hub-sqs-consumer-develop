import json
from datetime import datetime
from model.hub_log_user_active import HubLogUserActive


def run(event, context):

    recs=event.get("Records", None)
    if recs is not None:
        for rec in recs:
            save(rec.get("body", None))


def save(message):
    if message is not None:
        value = json.loads(message)
        HubLogUserActive.insert(
                app= int(value.get("idApp")),    
                profile = int(value.get("idProfile")),
                autorized = value.get("autorized"),
                datetime = value.get("datetime")
                ).execute()
