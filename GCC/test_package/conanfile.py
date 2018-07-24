import os

from conans import ConanFile, CMake, tools


class NcomdecoderpackageTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "compiler_args"

    def build(self):
        print("hello man, were about to make a test application!")
        self.run("gcc ..\..\example.c conanbuildinfo.args -o example")

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run(".%sexample" % os.sep)
