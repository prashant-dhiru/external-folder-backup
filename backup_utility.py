import os
import shutil
import hashlib

SKIP_DUPLICATE = 'skipduplicate'
SOURCE_LOCATION = 'sourcelocation'
DESTINATION_LOCATION = 'destinationlocation'
CHECK_DUPLICATE_FILES_IN_LOCATION = 'checkduplicatefilesinlocation'


class BackUpProfile:
    def __init__(self, profile_config):
        self.skip_duplicate = profile_config.get(SKIP_DUPLICATE) == "True"
        self.file_loc_to_check_duplicate = profile_config.get(CHECK_DUPLICATE_FILES_IN_LOCATION)
        self.file_loc_of_source_path = profile_config.get(SOURCE_LOCATION)
        self.file_loc_of_destination_path = profile_config.get(DESTINATION_LOCATION)

        self.report = {
            'totalFilesCopied': 0,
            'ListOfCopiedFiles': []
        }
        self.files_to_copy = dict()

    def __call__(self):
        self.find_files_to_copy()
        self.copy_data_to_destination()
        self.send_report()

    def find_files_to_copy(self):
        if self.skip_duplicate:
            self._get_files_based_on_hash()
        else:
            pass  # todo list of all the files in the files on source

    def _get_files_based_on_hash(self) -> None:
        dhs_builder = DirectoryHashStoreBuilder()
        dhs_check_location = dhs_builder.create_store(self.file_loc_to_check_duplicate)
        dhs_source_location = dhs_builder.create_store(self.file_loc_of_source_path)
        for source_hash, source_path in dhs_source_location.items():
            if source_hash not in dhs_check_location.keys():
                self.files_to_copy.update({source_hash: source_path})

    def copy_data_to_destination(self):
        for file_path in self.files_to_copy.values():
            print(file_path)
            shutil.copyfile(file_path, os.path.join(self.file_loc_of_destination_path, file_path.split("\\")[-1]))

    def send_report(self):
        pass


class DirectoryHashStoreBuilder:
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks! # todo check with different file size

    def create_store(self, location: str) -> dict[str, str]:
        store = dict()
        for (dir_path, dir_names, filenames) in os.walk(location):  # todo multi threading possible ??
            for file in filenames:
                file_path = os.path.join(dir_path, file)
                file_hash_path = self.get_hash_filename(file_path)
                store.update(file_hash_path)
        return store

    def get_hash_filename(self, filepath: str):
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        with open(filepath, 'rb') as f:
            while True:
                data = f.read(self.BUF_SIZE)
                if not data:
                    break
                md5.update(data)
                sha1.update(data)

        return {md5.hexdigest(): filepath}
