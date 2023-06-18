import socket

# Broker settings
broker_ip = "mqtt-dashboard.com"
broker_port = "1883"
username = ""
password = ""

# Topic settings
comm_topic = 'pr/home/AC_Filter/sts'
sub_topic = comm_topic + '#'
pub_topic = comm_topic

# Thresholds for filter replacement
# Assuming one month of usage requires filter replacement
# Approximating a month to 30 days for simplicity
filter_replacement_threshold = 30 * 24 * 60 * 60  # seconds in a month

# Check interval for filter replacement
# Setting this to 1 day
manag_time = 24 * 60 * 60  # seconds in a day

# Topic to publish warnings
warning_topic = comm_topic + 'warning'
