import ldclient
from ldclient import Config, Context

ldclient.set_config(Config(""))
client = ldclient.get()

if __name__ == "__main__":
    if client.is_initialized():
        print("SDK successfully initialized!")
    else:
        print("There was an issue initializing - is the SDK key correct?")

    context = Context.builder('user-id-123abc').kind('user').name('Sandy').set('email', 'sandy@testcorp.com').build()

    flag_value = client.variation("test-flag", context, False)

    print(f"Our first feature flag is: {flag_value}")
