# SRAssesment# nginx-custom
#
# Requirements
* Ansible
* Virtualbox
* Vagrant

* molecule (optional but preferred)


# Getting started with Vagrant


1. Run:

vagrant up

2. Edit file:
    roles/nginx-custom/tasks/main.yml

3. Save changes

4. check changes run:

vagrant provision

5. Repeat


# Getting Started with molecule

1. Setup
   pip install molecule testinfra pytest pluggy paramiko flake8 ansible-lint

2. Run
 molecule init
 molecule converge

3. To run just tests
 molecule verify

4. start up from scratch and install everything then run tests
  molecule test



