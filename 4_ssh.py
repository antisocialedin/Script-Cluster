#!/usr/bin/env python
# Eder Filho
# 09/05/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - SSH

import os
from dhcp_get_ip import ip_list  # Importa a lista de IPs do arquivo ip_list.py

#start no SSH
print("Iniciando servidor ssh...")
os.system("systemctl enable ssh")

#monitorar o SSH
print("Monitorando servidor ssh...")
os.system("systemctl status ssh")

""" #Saindo do sudo
os.system("su - cluster") """

#gerar key SSH 
print("Gerando chave ssh...")
os.system("ssh-keygen")

#caminho da pasta .ssh
print("Caminhando para a pasta .ssh...")
os.chdir(os.path.expanduser("~/.ssh"))

# Copia a chave para cada IP na lista
print("Copiando chave para os IPs...")
for ip in ip_list:
    os.system(f"ssh-copy-id -i ~/.ssh/id_rsa.pub cluster@{ip}")

#caminho da pasta /home
print("Caminhando para a pasta .ssh...")
os.chdir(os.path.expanduser("~"))