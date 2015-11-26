#!/usr/bin/env python
# -*- coding: utf-8 -*-
#AutoUpdate

#Autor: Igor Iglesias
#Site: http://igoriglesias.com
#Programa efetua auto update de maquinas 
#que rodam linux (Debian, Ubuntu e variantes)
#Basta colocar o script dentro de um dos diretórios:
#/etc/cron.daily para update diário
#/etc/cron.weekly para update semanal
#/etc/cron.monthly para update mensal
#Após escolher o diretório de permissão de execução:
#sudo chmod +x AutoUpdate.py
#

#Importa modulos do sistema operacional
import os

#Define variaveis
update = "apt-get -y update"
upgrade = "apt-get -y upgrade"
distupgrade = "apt-get -y dist-upgrade"
extra = "apt-get autoremove && apt-get autoclean"

#Executa Update
os.system(update)
	
#Executa Upgrade
os.system(upgrade)
		
#Executa Dist-Upgrade
os.system(distupgrade) 
			
#Executa Extras
os.system(extra)
				

print (" Update Finalizado! ")
