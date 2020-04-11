#!/usr/bin/python3
""" Compress before sending """

from datetime import datetime
from fabric.operations import local, run
import os.path


def do_pack():
    """ Method  generates a .tgz """

    date = datetime.now()
    my_date = date.strftime("%Y%m%d%H%M%S")

    try:
        if not os.path.isdir("versions"):
            local("mkdir versions")

        file1 = "versions/web_static_{}.tgz web_static".format(my_date)
        file2 = local("tar -cvzf {}".format(file1))
        return file2
    except Exception:
        return None

