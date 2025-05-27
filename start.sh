#!/bin/bash

# run ansible
ansible-playbook site.yml --tags guitarix --ask-vault-pass