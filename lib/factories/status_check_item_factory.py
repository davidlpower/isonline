from lib.status_check_item import StatusCheckItem
from lib.service import Service
from lib.check import Check


class StatusCheckItemFactory:

    def build(self, service, check):
        new_service = Service(service['name'], service['url'], service['status'], service['mature_content_check'])
        new_check = Check(check['name'], check['uri'])
        return StatusCheckItem(new_service, new_check)
