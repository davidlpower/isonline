class StatusCheckItem:
    def __init__(self, service, check):
        self.service = service.name
        self.id = f"{service.name} - {check.name}"
        self.url = f"{service.url}{check.uri}"
        self.selector = service.status['selector']
        self.indicator = service.status['indicator']
