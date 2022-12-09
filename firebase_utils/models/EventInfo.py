from fireo.models import Model
from fireo.fields import TextField


class EventInfo(Model):
    title = TextField()
    location = TextField()
    description = TextField()
    begin = TextField()
    end = TextField()
    signup_form = TextField()
    recurring = TextField()
    signup_form = TextField()

    @staticmethod
    def download():
        return list(EventInfo.fetch_all())

    @staticmethod
    def fetch_all():
        return EventInfo.collection.fetch()
