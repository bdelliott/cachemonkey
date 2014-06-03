# Copyright 2014 Rackspace Hosting
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from cachemonkey.openstack.common import log as logging
from cachemonkey.openstack.common import service

LOG = logging.getLogger(__name__)


class Service(service.Service):

    def start(self):
        LOG.info("Cachemonkey service initializing...")
        super(Service, self).start()

    def stop(self):
        LOG.info("Cachemonkey service shutting down...")
        super(Service, self).stop()
