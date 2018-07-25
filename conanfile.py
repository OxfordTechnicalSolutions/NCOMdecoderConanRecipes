import os

from conans import ConanFile, CMake, tools, MSBuild


class NcomDecoderPackageConan(ConanFile):
    name = "NcomDecoderPackageConan"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Ncomdecoderpackage here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "compiler_args", "visual_studio"

    def source(self):
        self.run("git clone https://github.com/OxfordTechnicalSolutions/NCOMdecoder.git")
        self.run("cd NCOMdecoder && git checkout compiler-support")

    def build(self):
        if self.settings.compiler == "Visual Studio":
            self.output.info("Starting build for visual studio")
            self.run("dir")
            msbuild = MSBuild(self)
            path = os.getcwd() + r"\NCOMdecoder\MSVC_2017\NComRxC.sln"
            msbuild.build(path, upgrade_project=False)

        elif self.settings.compiler == "gcc":
            self.output.info("Starting build for gcc")
            self.run("mkdir NCOMdecoder\\src\\bin")
            self.run("gcc -c NCOMdecoder\\src\\NComRxC.c -o NCOMdecoder\\src\\bin\\NComRxC.o")
            self.run("ar rcs libNComRxC.a NCOMdecoder\\src\\bin\\NComRxC.o")
        else:
            self.output.info("Compiler not supported in recipe")
            exit()

    def package(self):
        self.output.info("Copying files to package")
        self.copy("NCOMdecoder\\src\\*.h", dst="include", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["NComRxC"]

