import os

from conans import ConanFile, CMake, tools


class NcomdecoderpackageTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "compiler_args"

    def build(self):
        # self.run("dir")
        print("hello my man, were about to make a test application!")
        self.run("more conanbuildinfo.args")
        self.run("gcc ..\..\example.c @conanbuildinfo.args -o example")

    def test(self):
        if not tools.cross_building(self.settings):
            self.run("example.exe ..\..\test_file")
