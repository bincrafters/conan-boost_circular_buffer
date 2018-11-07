#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostCircular_BufferConan(base.BoostBaseConan):
    name = "boost_circular_buffer"
    url = "https://github.com/bincrafters/conan-boost_circular_buffer"
    lib_short_names = ["circular_buffer"]
    header_only_libs = ["circular_buffer"]
    b2_requires = [
        "boost_assert",
        "boost_concept_check",
        "boost_config",
        "boost_container",
        "boost_core",
        "boost_iterator",
        "boost_move",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_utility"
    ]


