"""
Models and supports "attitude determination and control system" subsystem
"""

class ADCS:
    def __init__(self):
        self.P_peak = 0
        self.P_transmit = 0
        self.P_control = 0
        self.P_low = 0

        self.P_1 = 0
        self.P_2 = 0
        self.P_3 = 0
        self.P_4 = 0

        self.D_ADCS = 0
