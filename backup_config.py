import configparser


class BackUpConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self._parse()

    def _parse(self):
        # todo if config_value is not propeer log indo and delete profile
        pass

    def get_profiles(self):
        return self.config.sections()

    def get_profile_values(self, profile):
        return dict(self.config[profile])
