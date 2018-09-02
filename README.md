Ansible Role: safe-fstab
=========

A simple wrapper for the `mount` module for Linux that rolls-back changes if any mount operation fails without leaving the system in an half-configured state, unless desired otherwise (on a per-device basis).

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

````
devices: []
````
A list of devices to manage with the `mount` module. See the commented example in `defaults/main.yml` for available options and the [`mount` module documentation](https://docs.ansible.com/ansible/latest/modules/mount_module.html) for all the relevant options.

The `continue_on_fail` option, specified on each device in the list, is the core of the role: it defaults to `false` and when the mount operations on any device with the option set to false fails, the role will roll-back any device-related changes on the system, rolling back to the setup before the execution of the role. It even rolls-back mounted devices that are not set up with fstab (such as with the Linux `mount` command).

If the `continue_on_fail` option is set to true, that device will be ignored if the mount operation fails, and the role will not roll-back changes. Do note that if any other device with the `continue_on_fail` option set to false fails, changes will be rolled-back for all devices.

````
devices:
  - mountpoint: "/mnt/disk1"
    src: "UUID=5b0659b2-d643-4bc1-ac8f-0cedfb42dfe4"
    fstype: "ext4"
    opts: "defaults"
    state: "mounted"
    dump: 0
    passno: 2
    continue_on_fail: true
````
An example of a fully-populated device entry for mounting and configuring the line in the fstab file.

````
devices:
  - mountpoint: "/mnt/disk2"
    src: "/dev/sdb1"
    fstype: "ext4"
````
An example of a minimal device entry for mounting and configuring the line in the fstab file, using defaults for all the unspecified options.

````
devices:
  - mountpoint: "/mnt/disk3"
    state: absent
````
An example of a minimal device entry for unmounting and removing the line from the fstab file.

````
fstab_path: '/etc/fstab'
````
The path to the fstab file to manage.

````
print_debug: false
````
If set to true ansible will print debug information on supported tasks.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: server
      roles:
        - role: safe-fstab
          vars:
            devices:
              - { mountpoint: "/mnt/disk1", src: "/dev/sdb1", fstype: "ext4", opts: "defaults" }
              - { mountpoint: "/mnt/disk2", src: "UUID=5b0659b2-d643-4bc1-ac8f-0cedfb42dfe4", fstype: "ext4", opts: "defaults", continue_on_fail: true }
              - { mountpoint: "/mnt/disk3", state: absent }

Testing
-------

This role is manually tested with [Molecule](https://molecule.readthedocs.io/en/latest/) and [Vagrant](https://www.vagrantup.com/) (check the `molecule` directory for the details). Automated CI testing is in the works.

This role is tested against the following platforms:

````
- name: CentOS
  versions:
    - 6
    - 7
- name: Fedora
  versions:
    - 27
    - 28
- name: Debian
  versions:
    - jessie
    - stretch
- name: Ubuntu
  versions:
    - trusty
    - xenial
    - bionic
````

License
-------

MIT

Author Information
------------------

This role was created in 2018 by [Francesco Spilla](https://gitlab.com/francesco.spilla/ansible-role-safe-fstab).
