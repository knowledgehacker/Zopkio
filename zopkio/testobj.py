# Copyright 2014 LinkedIn Corp.
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import zopkio.constants as constants

class Test(object):
  """
  Structure used to store information about a test during runtime
  """
  def __init__(self, name, function, **kwargs):
    """
    :param name: name of the test
    :param function: callback that will be run during test execution
    """
    self.name = name

    self.phase = kwargs.get("phase", constants.DEFAULT_TEST_PHASE)

    self.repeat_per_loop = kwargs.get("iteration", constants.DEFAULT_ITERATION)
    self.total_number_iterations = self.repeat_per_loop
    self.current_iteration = 0
    self.consecutive_failures = 0

    self.function = function
    self.validation_function = kwargs.get("validate", None)

    if 'setup' in kwargs:
      self.setup = kwargs.get('setup')
    if 'teardown' in kwargs:
      self.teardown = kwargs.get('teardown')

    self.description = function.__doc__
    if self.validation_function.__doc__  is not None:
      if self.description is not None:
        self.description = "{0}; {1}".format(self.description, self.validation_function.__doc__)
      else:
        self.description = self.validation_function.__doc__

    self.func_start_time = None
    self.func_end_time = None
    self.start_time = None
    self.end_time = None

    self.result = None
    self.iteration_results = {}
    self.exception = None

    self.naarad_config = None
    self.naarad_id = None
    self.naarad_stats = None
    self.sla_objs = None

    self.message = ""

    for i in xrange(self.total_number_iterations):
        self.iteration_results[i] = constants.SKIPPED

  def reset(self):
    """
    Reset to a 'clean' state, i.e all test data is reset and only the name and functions are kept
    """

    self.func_start_time = None
    self.func_end_time = None
    self.start_time = None
    self.end_time = None

    self.result = None
    self.exception = None
    self.consecutive_failures = 0

    self.naarad_config = None
    self.naarad_id = None
    self.naarad_stats = None
    self.sla_objs = None

    self.message = ""
    self.current_iteration = 0
    self.total_number_iterations = self.repeat_per_loop
    for i in xrange(self.total_number_iterations):
        self.iteration_results[i] = constants.SKIPPED
