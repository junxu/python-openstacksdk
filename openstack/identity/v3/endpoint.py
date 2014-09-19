# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.identity import identity_service
from openstack import resource


class Endpoint(resource.Resource):
    resource_key = 'endpoint'
    resources_key = 'endpoints'
    base_path = '/endpoints'
    service = identity_service.IdentityService()

    # capabilities
    allow_create = True
    allow_retrieve = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # Properties
    enabled = resource.prop('enabled', type=bool)
    interface = resource.prop('interface')
    region_id = resource.prop('region_id')
    service_id = resource.prop('service_id')
    url = resource.prop('url')