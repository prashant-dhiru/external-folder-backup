class BackUpProfile:
    def __init__(self, profile_config):
        self.skip_duplicate = profile_config.get('skipDuplicate')
        self.file_loc_to_check_duplicate = profile_config.get('CheckDuplicateFilesInLocation')
        self.file_loc_of_source_path = profile_config.get('SourceLocation')

        self.report = {
            'totalFilesCopied': 0,
            'ListOfCopiedFiles': []
        }
        self.DHS_check_location = set()
        self.DHS_source_location = set()

    def start(self):
        if self.skip_duplicate:
            self._build_hash_store()

    def _build_hash_store(self):
        self.DHS_check_location = DirectoryHashStore.create(self.DHS_check_location)

    def _backup_data(self):
        pass

    def _send_report(self):
        pass


class DirectoryHashStore:
    def create(self, location):
        store = set()

        return store
