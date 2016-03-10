# -*- coding: UTF-8 -*-
import libvirt
import plugin
from log import logger

client = libvirt.open('qemu:///system')
config = {}


def createContainerConfig(containerConfig, str_id):
    config[str_id] = containerConfig;
    return


def deleteContainerConfig(str_id):
    if str_id in config:
        del config[str_id]
    return


def getContainerConfig(str_id):
    if str_id in config:
        return config[str_id]
    return None


def checkID(id, common):
    containers = client.listDomainsID()
    if id not in containers:
        logger.error("{common} {id} error! Don't have dom that id is {id}!!".format(common=common, id=id))
        return False
    else:
        logger.info("{common} {id} success".format(common=common, id=id))
    return True


def getAllContainersID():
    containers = client.listDomainsID()
    for index in range(len(containers)):
        containers[index] = plugin.int_to_str_id(containers[index])
    return containers


def getContainerInfoByID(str_id):
    id = plugin.str_to_int_id(str_id)
    ret = {"Id": str_id}
    if not checkID(id, "getContainerInfoByID"):
        return "get containerInfo failed! Don't have dom that id is {str_id}".format(str_id=str_id)

    dom = client.lookupByID(id)
    dom_info = dom.info()
    dic_dom_info = {"status": dom_info[0], "maxMemory": dom_info[1], "usedMemory": dom_info[2], "virtCpu": dom_info[3],
                    "cpuTime": dom_info[4]}
    ret["Name"] = dom.name()
    ret["DomInfo"] = dic_dom_info
    ret["CpuInfo"] = dom.getCPUStats(1, 0)[0]
    ret["ContainerConfig"] = getContainerConfig(str_id)
    return ret


def createContainer(dicts):
    xml = plugin.dict_to_xml(dicts)
    logger.debug('Container xml is {xml}'.format(xml=xml))

    dom = client.createXML(xml)
    str_id = plugin.int_to_str_id(dom.ID())
    logger.info('Created success,ID is {str_id}'.format(str_id=str_id))
    if 'ContainerConfig' in dicts:
        createContainerConfig(dicts['ContainerConfig'], str_id)
    return str_id


def updateContainer(dicts, str_id):
    deleteContainerByID(str_id)
    return createContainer(dicts)


def deleteContainerByID(str_id):
    deleteContainerConfig(str_id)

    id = plugin.str_to_int_id(str_id)
    if not checkID(id, "deleteContainerByID"):
        return "delete failed! Don't have dom that id is {str_id}".format(str_id=str_id)

    dom = client.lookupByID(id)
    dom.destroy()
    return "delete success"


def stopContainerByID(str_id):
    id = plugin.str_to_int_id(str_id)
    checkID(id, "stopContainerByID")

    dom = client.lookupByID(id)
    dom.shutdown()
    return dom.state()


def startContainerByID(str_id):
    id = plugin.str_to_int_id(str_id)
    checkID(id, "startContainerByID")

    dom = client.lookupByID(id)
    dom.reboot()
    return dom.state()


def findContaienrIDByName(name):
    dom = client.lookupByName(name)
    return dom.ID()
