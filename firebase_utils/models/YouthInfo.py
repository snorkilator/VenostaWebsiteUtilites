from fireo.models import Model
from fireo.fields import TextField


class YouthInfo(Model):
    name = TextField()
    email = TextField()
    cell = TextField()
    parent_or_guardian = TextField()

    @staticmethod
    def create_empty():
        return YouthInfo.create_with('', '', '', '')

    @staticmethod
    def create_with(name, email, cell, parent_or_guardian):
        youth_info = YouthInfo()
        youth_info.update(name, email, cell, parent_or_guardian)
        return youth_info

    @staticmethod
    def download():
        return list(YouthInfo.fetch_all())

    @staticmethod
    def fetch_all():
        return YouthInfo.collection.fetch()

    @staticmethod
    def from_dict(model_dict):
        youth_info = YouthInfo()
        youth_info.name = model_dict.get('name')
        youth_info.email = model_dict.get('email')
        youth_info.cell = model_dict.get('cell')
        youth_info.parent_or_guardian = model_dict.get('parent_or_guardian')
        return youth_info

    def delete(self):
        YouthInfo.collection.delete(self.key)

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'cell': self.cell,
            'parent_or_guardian': self.parent_or_guardian
        }

    def update(self, name, email, cell, parent_or_guardian):
        self.name = name
        self.email = email
        self.cell = cell
        self.parent_or_guardian = parent_or_guardian
        return self
