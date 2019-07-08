import os
import testinfra.utils.ansible_runner
import requests

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_node_exporter_service_running(host):
    assert(host.service('node-exporter').is_running)

def test_node_exporter_running(host):
    response = requests.get('http://localhost:9100')
    assert(response.status_code == 200)
