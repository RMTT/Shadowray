import subprocess
from shadowray.config.v2ray import EXECUTE_ARGS, V2RAY_PID_FILE, CONFIG_STREAM_FILE
from shadowray.common.utils import write_to_file
import multiprocessing
import time
import os, sys


class Execute:
    def __init__(self, binary):
        self.v2ray_binary = binary
        self.config = None

    def __exec(self):
        s = subprocess.Popen([self.v2ray_binary, EXECUTE_ARGS], stdin=subprocess.PIPE)
        write_to_file(V2RAY_PID_FILE, "w", str(s.pid))
        s.communicate(self.config)

    def exec(self, config: str, daemon=False):
        self.config = bytes(config, encoding='utf8')

        process = multiprocessing.Process(target=self.__exec, daemon=daemon)
        process.start()

        if daemon is True:
            time.sleep(1)

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
