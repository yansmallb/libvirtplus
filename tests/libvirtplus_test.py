# -*- coding: UTF-8 -*-
import requests

json_kvm = '{"name":"centos_65_2","memory":"1048576","vcpu":4,"boot":"hd",' \
           '"disk_source":"/var/lib/libvirt/images/centos_65.qcow2",' \
           '"cdrom_source":"",' \
           '"bridge": "virbr0"}'


if __name__ == "__main__":
    url = 'http://192.168.11.59:2376/'
    #url = 'http://127.0.0.1:2376/'

    r = requests.get(url+'containers')
    print r.text

    if 0:
        r = requests.post(url+'containers/192.168.11.51_11', data=json_kvm)
        print r.text
    else:
        r = requests.post(url+'containers', data=json_kvm)
        print r.text
