from ScoutSuite.providers.oci.resources.base import OracleCompositeResources
from ScoutSuite.providers.oci.resources.identity.users import Users
from ScoutSuite.providers.oci.resources.identity.policies import Policies
from ScoutSuite.providers.oci.facade.facade import OracleFacade


class Identity(OracleCompositeResources):
    _children = [
        (Users, 'users'),
        (Policies, 'policies'),
    ]

    def __init__(self, facade: OracleCompositeResources):
        self.facade = facade
        self.service = 'identity'

    async def fetch_all(self, credentials):
        await self._fetch_children(resource_parent=self, facade=self.facade)
