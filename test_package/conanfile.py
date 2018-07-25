import os

from conans import ConanFile, CMake, tools, MSBuild


class NcomdecoderpackageTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "compiler_args","visual_studio"

    def build(self):
        self.output.info("Building test application")
        if self.settings.compiler == "Visual Studio":
            self.output.info("Starting build for visual studio")
            msbuild = MSBuild(self)
            path = os.getcwd() + r"\..\..\test_application.sln"
            print(path)
            msbuild.build(path, upgrade_project=False)

        elif self.settings.compiler == "gcc":
            self.output.info("Starting build for gcc")
            self.run("gcc ..\..\example.c @conanbuildinfo.args -o example")

        else:
            self.output.info("Compiler not supported in recipe")
            exit()
            
    def test(self):
        self.output.info("Running test application")
        if self.settings.compiler == "Visual Studio":
            self.run("\\..\\..\\x64\\Release\\test_application.exe ..\\..\\test_file.ncom ..\\..\\output.csv")
        elif self.settings.compiler == "gcc":
            self.run("example.exe ..\\..\\test_file.ncom ..\\..\\output.csv")
        else:
            self.output.info("Compiler not supported in recipe")