# -*- coding: UTF-8 -*-
import requests

json_kvm = '{"name":"centos_65","memory":"1048576","vcpu":4,"boot":"hd",' \
           '"disk_source":"/var/lib/libvirt/images/centos_65.qcow2",' \
           '"cdrom_source":"/var/lib/libvirt/images/CentOS-6.5-x86_64-bin-DVD1.iso"}'

if __name__ == "__main__":
    url = 'http://192.168.11.51:2376/'
    r = requests.get(url+'containers')
    print r.text

    r = requests.get('http://192.168.11.51:2376/containers/2')
    print r.text