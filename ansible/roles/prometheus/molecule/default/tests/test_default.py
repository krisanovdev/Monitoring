import os
import testinfra.utils.ansible_runner
import requests

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_configs(host):
    base_path = '/tmp/prometheus/config/'
    config_files = [base_path + 'prometheus.yml', base_path + 'rules/recording_rules.yml', base_path + 'rules/alerting_rules.yml']

    for file in config_files:
        assert(host.file(file).exists)

def test_docker_running(host):
    assert(host.docker('prometheus').is_running)

def test_prometheus_server(host):
    response = requests.get('http://localhost:9090')
    assert(response.status_code == 200)
