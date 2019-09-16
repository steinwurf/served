#! /usr/bin/env python
# encoding: utf-8

import os
from waflib import Task, TaskGen

APPNAME = 'served'
VERSION = '2.0.0'


def configure(conf):
    if conf.is_mkspec_platform('linux') and not conf.env['LIB_PTHREAD']:
        conf.check_cxx(lib='pthread')


def build(bld):
    bld.env.append_unique(
        'DEFINES_STEINWURF_VERSION',
        'STEINWURF_SERVED_VERSION="{}"'.format(VERSION))

    use_flags = ["boost_system"]
    if bld.is_mkspec_platform('linux'):
        use_flags += ['PTHREAD']

    served_path = bld.root.find_dir(bld.dependency_path('served-source'))
    all_cpp = served_path.ant_glob('src/served/**/*.cpp')
    test_cpp = served_path.ant_glob('src/served/**/*.test.cpp') + served_path.ant_glob('src/test/**/*.cpp')
    lib_cpp = list(set(all_cpp) - set(test_cpp))
    include_path = served_path.find_dir('src/')

    includes = [include_path, bld.path.find_dir('src/')]
    defines =[
        'APPLICATION_NAME="Served HTTP REST Library"',
        'APPLICATION_CODENAME="Codename"',
        'APPLICATION_COPYRIGHT_YEARS="2014"',
        'APPLICATION_VENDOR_ID="com.datasift"',
        'APPLICATION_VENDOR_NAME="DataSift"',
        'APPLICATION_VENDOR_URL="datasift.com"'
    ]
    bld.stlib(
        features='cxx',
        source=lib_cpp,
        includes=includes,
        target='served',
        use=use_flags,
        defines=defines,
        export_defines=defines,
        export_includes=includes)
    if bld.is_toplevel():
        # Only build tests when executed from the top-level wscript,
        # i.e. not when included as a dependency

        bld.program(
            features='cxx test',
            source=test_cpp,
            target='served_tests',
            use=['served'])

        bld.program(
            features='cxx',
            source=[served_path.find_node('src/examples/binary_data/main.cpp')],
            target='binary_data',
            use=['served'])

        bld.program(
            features='cxx',
            source=[served_path.find_node('src/examples/form_data/main.cpp')],
            target='form_data',
            use=['served'])

        bld.program(
            features='cxx',
            source=[served_path.find_node('src/examples/handlers/main.cpp')],
            target='handlers',
            use=['served'])

        bld.program(
            features='cxx',
            source=[served_path.find_node('src/examples/hello_world/main.cpp')],
            target='hello_world',
            use=['served'])

        bld.program(
            features='cxx',
            source=[served_path.find_node('src/examples/list_endpoints/main.cpp')],
            target='list_endpoints',
            use=['served'])

        bld.program(
            features='cxx',
            source=[served_path.find_node('src/examples/query_params/main.cpp')],
            target='query_params',
            use=['served'])

        bld.program(
            features='cxx',
            source=[served_path.find_node('src/examples/request_logger_plugin/main.cpp')],
            target='request_logger_plugin',
            use=['served'])

        bld.program(
            features='cxx',
            source=[served_path.find_node('src/examples/rest_resource/main.cpp')],
            target='rest_resource',
            use=['served'])
