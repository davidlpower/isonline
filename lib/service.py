class Service:

    def __init__(self, config_service):
        self.name = config_service['name']
        self.uri = config_service['uri']
        self.check_status_selector = config_service['checks']['status']['selector']
        self.check_status_indicator = config_service['checks']['status']['indicator']
        self.checks_items = config_service['checks']['items']
        self.pre_checks = config_service['pre_checks']
    