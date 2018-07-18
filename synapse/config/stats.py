# -*- coding: utf-8 -*-
# Copyright 2018 New Vector Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ._base import Config

import sys


class StatsConfig(Config):
    """Stats Configuration
    Configuration for the behaviour of synapse's stats engine
    """

    def read_config(self, config):
        self.stats_enable = False
        self.stats_bucket_size = 86400
        self.stats_retention = sys.maxint
        stats_config = config.get("stats", None)
        if stats_config:
            self.stats_enable = stats_config.get("enable", self.stats_enable)
            self.stats_bucket_size = stats_config.get(
                "bucket_size", self.stats_bucket_size
            )
            self.stats_retention = stats_config.get("retention", self.stats_retention)

    def default_config(self, config_dir_path, server_name, **kwargs):
        return """
        # Stats configuration
        #
        # stats:
        #    enable: false
        #    bucket_size: 86400 # 1 day
        #    retention: 31536000 # 1 year
        """