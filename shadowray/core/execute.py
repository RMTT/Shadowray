import subprocess
from shadowray.config.v2ray import EXECUTE_ARGS


class Execute:
    def __init__(self, binary):
        self.v2ray_binary = binary

        self.v2_process = None
        self.config = None

    def exec(self, config):
        self.v2_process = subprocess.Popen([self.v2ray_binary, EXECUTE_ARGS], stdin=subprocess.PIPE)
        self.v2_process.communicate(config)
        self.config = config

    def stop(self):
        if self.v2_process is not None:
            self.v2_process.kill()
            self.v2_process = None

    def restart(self, config=None):
        if self.v2_process is not None:
            self.v2_process.kill()

        if config is not None:
            self.v2_process = self.exec(config)
        elif self.config is not None:
            self.v2_process = self.exec(self.config)
        else:
            print("No config!!!")
