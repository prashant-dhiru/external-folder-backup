import sys
import logging
from backup_config import BackUpConfig
from backup_utility import BackUpProfile

# noinspection PyArgumentList
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s %(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)


def external_folder_backup():
    config = BackUpConfig()

    for profile in config.get_profiles():
        logging.info(f"Running backup for {profile} profile")
        profile_config = config.get_config_for_profile(profile)
        backup_profile_process = BackUpProfile(profile_config)
        backup_profile_process.start()


if __name__ == "__main__":
    external_folder_backup()
