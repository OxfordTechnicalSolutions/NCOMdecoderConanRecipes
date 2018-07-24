from conans import ConanFile, CMake, tools


class NcomDecoderPackageConan(ConanFile):
    name = "NcomDecoderPackageConan"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Ncomdecoderpackage here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "compiler_args"

    def source(self):
        self.run("git clone https://github.com/OxfordTechnicalSolutions/NCOMdecoder.git")
    def build(self):
        self.output.info("+++++++++Starting build+++++++++")
        self.run("mkdir NCOMdecoder\\nav\\bin")
        self.output.success("+++++++++Created directory+++++++++")

        self.run("gcc -c NCOMdecoder\\nav\\NComRxC.c -o NCOMdecoder\\nav\\bin\\NComRxC.o")
        self.run("ar rcs libNComRxC.a NCOMdecoder\\nav\\bin\\NComRxC.o")

    def package(self):
        self.copy("NCOMdecoder\\nav\\*.h", dst="include")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["NComRxC"]

