import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_absent_to_mounted(host):
    mountpoint = host.file('/mnt/disk1')

    assert not mountpoint.exists


def test_absent_to_mounted_files(host):
    files = ['/mnt/disk1/a_File', '/mnt/disk1/another_File',
             '/mnt/disk1/yet_Another_File', '/mnt/disk1/does_Not_Exists']

    files_on_host = [host.file(path) for path in files]

    assert not files_on_host[0].exists
    assert not files_on_host[1].exists
    assert not files_on_host[2].exists
    assert not files_on_host[3].exists


def test_mounted_to_absent(host):
    mountpoint = host.file('/mnt/disk2')

    assert mountpoint.exists


def test_present_to_unmounted(host):
    mountpoint = host.file('/mnt/disk3')

    assert not mountpoint.exists


def test_not_in_fstab_to_unmounted(host):
    mountpoint = host.file('/mnt/not-in-fstab')

    assert mountpoint.exists


def test_absent_to_present(host):
    mountpoint = host.file('/mnt/disk5')

    assert not mountpoint.exists


def test_device_missing(host):
    mountpoint = host.file('/mnt/disk6')

    assert not mountpoint.exists
