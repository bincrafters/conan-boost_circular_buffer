from conans import ConanFile, tools, os

class BoostCircular_BufferConan(ConanFile):
    name = "Boost.Circular_Buffer"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-circular_buffer"
    source_url = "https://github.com/boostorg/circular_buffer"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "circular_buffer"
    requires =  "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Concept_Check/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Container/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Iterator/1.64.0@bincrafters/testing", \
                      "Boost.Move/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing",\
                      "Boost.Utility/1.64.0@bincrafters/testing"

                      #assert1 concept_check5 config0 container7 core2 iterator5 move3 static_assert1 throw_exception2 type_traits3 utility5

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.source_url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()