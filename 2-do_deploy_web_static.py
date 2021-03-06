#!/usr/bin/python3

from datetime import datetime
from fabric.operations import local, run, env, put
import os.path
import re

env.hosts = ['35.229.75.124', '54.173.156.111']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
        Method do_deploy
    """

    if not os.path.exists(archive_path):
        return False

    fname = re.search('web_static_[0-9]*.tgz', archive_path).group(0)
    fpath = "/data/web_static/releases/{}".format(fname.replace('.tgz', ''))
    put(archive_path, '/tmp')
    run("mkdir -p {}".format(fpath))
    run("tar -zxf /tmp/{} -C {}".format(fname, fpath))
    run("rm /tmp/{}".format(fname))
    run("mv {}/web_static/* {}".format(fpath, fpath))
    run("rm -rf {}/web_static".format(fpath))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(fpath))
    print("New version deployed!")

