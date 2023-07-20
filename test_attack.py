import unittest
from unittest.mock import patch, Mock
from main import Attack
from scapy.layers.inet import IP, TCP


class TestAttack(unittest.TestCase):

    @patch.dict('os.environ', {'DESTINATION': '127.0.0.1', 'FLAGS': 'S'})
    def test_create_packet(self):
        attack = Attack()
        packet = attack._create_packet()

        # Check if packet has correct destination
        self.assertEqual(packet[IP].dst, '127.0.0.1')
        # Check if packet has correct flags
        self.assertEqual(packet[TCP].flags, 'S')


if __name__ == '__main__':
    unittest.main()
