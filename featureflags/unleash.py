from UnleashClient import UnleashClient

client = UnleashClient(
    url="https://eu.app.unleash-hosted.com/euii0016/api/",
    app_name="service-of-awesomeness",
    custom_headers={'Authorization': ''})

client.initialize_client()

context = {
    "userId": "123",
    "sessionId": "123",
    "remoteAddress": "adress",
    "properties": {
        "email": "serious@email.com"
    }
}

state = client.is_enabled("toggle-feature", context)

definitions = client.feature_definitions()

print(f"state: {state}")

