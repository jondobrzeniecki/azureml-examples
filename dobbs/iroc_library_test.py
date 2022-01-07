#!/usr/bin/env python
# coding: utf-8
# %%
from azureml.core import Workspace

import sys
print(sys.version)
import pyodbc
print('Successful import of pyodbc')


# %%
from azureml.core.authentication import MsiAuthentication

msi_auth = MsiAuthentication()

ws = Workspace(subscription_id="f5052c6f-7974-48eb-b0ba-f390a5c40ab8",
               resource_group="Demos-ADS",
               workspace_name="ads-demo-aml",
               auth=msi_auth)

print("Found workspace {} at location {}".format(ws.name, ws.location))

# %%
keyvault = ws.get_default_keyvault()

print(keyvault)

# %%
shhh = keyvault.get_secret("connstring")

print("Successful fetched secret")
