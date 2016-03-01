import logging
import logging.config
import os
import time


date = time.strftime("%Y%m%d", time.localtime())
logging.basicConfig(filename=os.path.join(os.getcwd(), date+'_libvirtplus.log'), level=logging.DEBUG,
                    filemode='a', format='%(asctime)s - %(filename)s %(levelname)s: %(message)s')
logger = logging.getLogger('libvirtplus')
