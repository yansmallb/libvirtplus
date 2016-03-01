# -*- coding: UTF-8 -*-
import requests
import urllib
import urllib2

json_kvm = '{"name":"centos_65","memory":"1048576","vcpu":4,"boot":"hd",' \
           '"disk_source":"/var/lib/libvirt/images/centos_65.qcow2",' \
           '"cdrom_source":"/var/lib/libvirt/images/CentOS-6.5-x86_64-bin-DVD1.iso",' \
           '"bridge": "virbr0"}'

dict_kvm = {'cdrom_source': '/var/lib/libvirt/images/CentOS-6.5-x86_64-bin-DVD1.iso',
            'name': 'centos65', 'vcpu': 4, 'boot': 'hd',
            'disk_source': '/var/lib/libvirt/images/centos65.qcow2', 'memory': '1048576'}


if __name__ == "__main__":
    url = 'http://192.168.11.51:2376/'
    #url = 'http://127.0.0.1:2376/'

    r = requests.get(url+'containers')
    print r.text

    if 1:
        r = requests.get(url+'containers/192.168.11.51_11')
        print r.text

        r = requests.post(url+'containers/192.168.11.51_11', data=json_kvm)
        print r.text
    else:
        r = requests.post(url+'containers', data=json_kvm)
        print r.text
