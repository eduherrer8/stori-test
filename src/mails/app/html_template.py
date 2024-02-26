import settings
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2.exceptions import UndefinedError


class HTMLTemplate:
    def __init__(self, template_name):
        self.common_data = {}
        self._template_name = template_name
        self._load_template()

    def _load_template(self):
        template_loader = FileSystemLoader(
            searchpath=settings.TEMPLATE_FILES_ROOT)
        self.template = Environment(
            loader=template_loader, autoescape=True
        ).get_template(self._template_name)

    def render(self, data):
        try:
            return self.template.render(**self.common_data, **data)
        except Exception as e:
            print(e, "/"*100)
            raise Exception("Some problems with jinja")
