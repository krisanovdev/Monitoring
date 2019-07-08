import os
import testinfra.utils.ansible_runner
import requests

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_configs(host):
    base_path = '/tmp/grafana/'
    config_files = [base_path + 'provisioning/datasources/datasources.yml', base_path + '/provisioning/dashboards/dashboards.yml',
    base_path + '/provisioning/dashboards/dashboard.json']

    for file in config_files:
        assert(host.file(file).exists)

def test_docker_running(host):
    assert(host.docker('grafana').is_running)

def test_grafana_server(host):
    response = requests.get('http://localhost:3000')
    assert(response.status_code == 200)
