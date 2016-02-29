# -*- coding: UTF-8 -*-
import libvirtplus.plugin


dicts = {'name': '1', 'memory': '2'}
json_obj = '{"str": "this is a string", "arr": [1, 2, "a", "b"], "sub_obj": {"sub_str": "this is sub str", "sub_list": [1, 2, 3]}, "end": "end"}'
json_obj2 = '{"name" : "jim", "sex" : "male", "age": 18}'
json_kvm = '{"name":"centos65","memory":"1048576","vcpu":4,"boot":"hd",' \
           '"disk_source":"/var/lib/libvirt/images/centos65.qcow2",' \
           '"cdrom_source":"/var/lib/libvirt/images/CentOS-6.5-x86_64-bin-DVD1.iso"}'

if __name__ == "__main__":
    di = libvirtplus.plugin.jsonToDict(json_kvm)
    print di

    xml = libvirtplus.plugin.dictToXML(di)
    print xml
