from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")

result = nr.run(
    task=netmiko_send_command,
    command_string='show ip int bri'
)

print_result(result)
