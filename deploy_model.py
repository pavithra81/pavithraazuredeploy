
from azureml.core import Workspace
from azureml.core.model import Model

model_name ="Health-Care-Chat-Bot-master"
endpoint_name="Health-Care-Chat-Bot-master-ep"

ws=Workspace.from_config()
model=Model(ws,name=model_name)
service=Model.deploy(ws.endpoint_name,[model])
service.wait_for_deployment(show_output=True)

