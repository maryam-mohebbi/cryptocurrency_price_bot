#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "cryptocurrency_price_bot"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("dir_source_main_python", "src")
    project.set_property("dir_source_unittest_python", "src/test")
    project.set_property("dir_source_main_scripts", "src/scripts")
    project.set_property("dir_docs", "documents")
    project.set_property("coverage_break_build", False)
