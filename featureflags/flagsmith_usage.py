from flagsmith import Flagsmith

flagsmith = Flagsmith(environment_key="")

traits = {
    "email": "mattias.persson@omegapoint.se",
    "first_name": "Mattias",
    "last_name": "Persson",
    "custom_trait": "custom_value"  
}

# Identify the user
identity_flags = flagsmith.get_identity_flags(identifier="Development_user_123456", traits=traits)

#Hanterar inte att flaggor inte finns
is_enabled = identity_flags.is_feature_enabled("test-feature")
print(f"test-feature is enabled: {is_enabled}")
feature_value = identity_flags.get_feature_value("nother_feature")
print(f"nother_feature value: {feature_value}")