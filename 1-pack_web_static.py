#!/usr/bin/python3
'''
Fabric script to generate a .tgz archive
'''
from fabric.api import local
from datetime import datetime


def do_pack():
    '''
    this method generates the archive
    '''
    local("mkdir -p versions")

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    archive_name = "web_static_{}.tgz".format(timestamp)

    result = local("tar -czvf versions/{} web_static".format(archive_name))

    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None
