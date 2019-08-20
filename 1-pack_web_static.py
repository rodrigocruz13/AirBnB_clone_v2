#!/usr/bin/python3
"""
Fabric script. Creates a tgz file with all the file from web_static
"""

from datetime import datetime
import os
import tarfile


def do_pack():
    """It generates a TGZ archive"""

    try:
        if not os.path.exists("./versions"):
            os.mkdir("versions/")
        now = datetime.now
        full_date = now().strftime("%Y%m%d%H%M%S")
        full_name = "versions/web_static_{}.tgz".format(full_date)

        """ c = create, v = verbose, z = zip, f = file """
        local("tar -cvzf {} web_static".format(full_name))
        return full_name

    except:
        return None
