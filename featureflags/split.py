from featureflags.client import CfClient
from featureflags.evaluations.auth_target import Target

api_key = ''

cf = CfClient(api_key)

target = Target(identifier="user1", name="user1")


result = cf.bool_variation("My_Test_Flag", target, False)
print(f"result: {result}")

