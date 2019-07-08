import os
import testinfra.utils.ansible_runner
import requests

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_configs(host):
    config_files = ['/tmp/alertmanager/alertmanager.yml']

    for file in config_files:
        assert(host.file(file).exists)

def test_docker_running(host):
    assert(host.docker('alertmanager').is_running)

def test_alertmanager_server(host):
    response = requests.get('http://localhost:9093')
    assert(response.status_code == 200)
