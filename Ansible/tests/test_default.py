import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.12")


def test_nginx_conf_file(host):
    f = host.file('/etc/nginx/nginx.conf')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_nginx_index_file(host):
    f = host.file('/usr/share/nginx/html/index.html')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled


def test_nginx_accepting_connections(host):
    nginx = host.socket("tcp://0.0.0.0:80")
    assert nginx.is_listening
