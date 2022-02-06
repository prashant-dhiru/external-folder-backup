import os
import hashlib


class BackUpProfile:
    def __init__(self, profile_config):
        self.skip_duplicate = profile_config.get('skipduplicate') == "True"
        self.file_loc_to_check_duplicate = profile_config.get('checkduplicatefilesinlocation')
        self.file_loc_of_source_path = profile_config.get('sourcelocation')

        self.report = {
            'totalFilesCopied': 0,
            'ListOfCopiedFiles': []
        }
        self.DHS_check_location = set()
        self.DHS_source_location = set()

    def start(self):
        if self.skip_duplicate:
            self._build_hash_store()
            self._backup_data()

    def _build_hash_store(self):
        DHS_builder = DirectoryHashStoreBuilder()
        self.DHS_check_location = DHS_builder.create_store(self.file_loc_to_check_duplicate)
        self.DHS_source_location = DHS_builder.create_store(self.file_loc_of_source_path)
        self.intersection = list(self.DHS_check_location.keys() & self.DHS_source_location.keys())

    def _backup_data(self):
        for file_hash in self.intersection:
            pass

    def _send_report(self):
        pass


class DirectoryHashStoreBuilder:

    def create_store(self, location):
        store = dict()
        for (dirpath, dirnames, filenames) in os.walk(location):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                file_hash = self.hash_from_filename(file_path)
                store.update(file_hash)
        return store

    @staticmethod
    def hash_from_filename(filename):
        BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        with open(filename, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                md5.update(data)
                sha1.update(data)

        return {md5.hexdigest(): filename}
