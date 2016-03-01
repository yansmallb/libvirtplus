# -*- coding: UTF-8 -*-
import json
import socket
import fcntl
import struct
import string
import types
import os
import xml.dom.minidom


def get_ip_address(if_name):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    net = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', if_name[:15]))
    ret = socket.inet_ntoa(net[20:24])
    return ret


def int_to_str_id(id):
    ip = get_ip_address("eth0")
    str_ID = ip + '_' + str(id)
    return str_ID


def str_to_int_id(str_id):
    list_str = str(str_id).split('_')
    length = len(list_str)
    return string.atoi(list_str[length-1])


def read_xml_template():
    if os.path.isfile('../template/kvm.xml'):
        doc = xml.dom.minidom.parse('../template/kvm.xml')
    else:
        doc = xml.dom.minidom.parse('./template/kvm.xml')
    return doc


def json_to_dict(js):
    dicts = json.loads(js, 'utf-8')
    return dicts


def json_to_xml(js):
    dicts = json_to_dict(js)
    return dict_to_xml(dicts)


def dict_to_xml(dicts):
    doc = read_xml_template()
    for (k, v) in dicts.items():
        if k == "boot":
            doc.getElementsByTagName(k)[0].setAttribute("dev", v)
            continue

        if k == "disk_source":
            dev = doc.getElementsByTagName("devices")[0]
            source = dev.getElementsByTagName("disk")[0].getElementsByTagName("source")[0]
            source.setAttribute("file", v)
            continue

        if k == "cdrom_source":
            dev = doc.getElementsByTagName("devices")[0]
            source = dev.getElementsByTagName("disk")[1].getElementsByTagName("source")[0]
            source.setAttribute("file", v)
            continue

        if k == "bridge":
            dev = doc.getElementsByTagName("devices")[0]
            source = dev.getElementsByTagName("interface")[0].getElementsByTagName("source")[0]
            source.setAttribute("bridge",v)
            continue

        doc.getElementsByTagName(k)[0].childNodes[0].nodeValue = v
    return doc.toxml()
