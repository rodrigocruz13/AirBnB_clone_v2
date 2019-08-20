#!/usr/bin/python3
"""
Fabric script. Creates a tgz file with all the file from web_static
"""

from datetime import datetime
import os
import tarfile


def do_pack():
    """It generates a TGZ archive"""

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

    with tarfile.open(full_name, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.exists(full_name):
        return full_name
    else:
        return None
