from __future__ import print_function
from conans import ConanFile, CMake, tools
from glob import glob
from time import sleep

import os
import subprocess

class LibToolConan(ConanFile):
    name = 'libtool'
    version = '2.4.6'
    license = 'MIT'
    url = 'https://github.com/sztomi/libtool-conan'
    description = 'This is a tooling package for GNU libtool'
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake', 'virtualenv'
    requires = 'm4/latest@sztomi/testing'

    def source(self):
        tarball_url = 'https://gnu.cu.be/libtool/libtool-{}.tar.gz'.format(self.version)
        tgz = tarball_url.split('/')[-1]
        tools.download(tarball_url, tgz)
        tools.untargz(tgz)
        os.unlink(tgz)

    def build(self):
        self.dirname = glob('libtool-*')[0]
        os.chdir(self.dirname)
        self.run('. ../activate.sh && ./configure --prefix={}'.format(self.package_folder))
        self.run('make')
        self.run('make install')

    def package(self):
        pass

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, 'bin'))

