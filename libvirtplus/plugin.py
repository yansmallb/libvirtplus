# -*- coding: UTF-8 -*-
import json
import xml.dom.minidom


def readXMLTemplate():
    doc = xml.dom.minidom.parse('../template/kvm.xml')
    return doc


def jsonToXML(js):
    dicts = jsonToDict(js)
    return dictToXML(dicts)


def jsonToDict(js):
    dicts = json.loads(js, 'utf-8')
    return dicts


def dictToXML(dicts):
    doc = readXMLTemplate()
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

        doc.getElementsByTagName(k)[0].childNodes[0].nodeValue = v
    return doc.toxml()
