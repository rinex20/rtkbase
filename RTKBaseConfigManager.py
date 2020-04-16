from configparser import ConfigParser

class RTKBaseConfigManager:

    def __init__(self, settings_path):
        self.settings_path = settings_path
        self.config = self.parseconfig(settings_path)

    def parseconfig(self, settings_path):
        config = ConfigParser(interpolation=None)
        config.read(settings_path)
        return config


    def listvalues(self):
        for section in self.config.sections():
            print("SECTION: {}".format(section))
            for key in self.config[section]:
                print("{} : {} ".format(key, self.config[section].get(key)))

    def get_main_settings(self):
        ordered_main = []
        for key in ("position", "com_port", "com_port_settings", "receiver", "receiver_format", "tcp_port"):
            ordered_main.append({key : self.config.get('main', key)})
        return ordered_main

    def get_ntrip_settings(self):
        ordered_ntrip = []
        for key in ("svr_addr", "svr_port", "svr_pwd", "mnt_name", "rtcm_msg"):
            ordered_ntrip.append({key : self.config.get('ntrip', key)})
        return ordered_ntrip
    
    def get_file_settings(self):
        ordered_file = []
        for key in ("datadir", "file_name", "file_rotate_time", "file_overlap_time", "archive_name", "archive_rotate"):
            ordered_file.append({key : self.config.get('local_storage', key)})
        return ordered_file

    def get_ordered_settings(self):
        ordered_settings = {}
        ordered_settings['main'] = self.get_main_settings()
        ordered_settings['ntrip'] = self.get_ntrip_settings()
        ordered_settings['file'] = self.get_file_settings()
        return ordered_settings




