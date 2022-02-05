import configparser


class BackUpConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self._parse()

    def _parse(self):
        pass

    def get_profiles(self):
        return self.config.sections()

    def get_config_for_profile(self, profile):
        return dict(self.config[profile])
