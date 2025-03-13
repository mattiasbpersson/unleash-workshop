# unleash-workshop

## Requirements:
* Python
* Pip
* Curl
* jq
* Any other choice

```
pip install -r featureapp/requirements.txt
```
## Run the program
Set the following environment variables
"UNLEASH_FRONTEND_TOKEN"
"UNLEASH_BACKEND_TOKEN"

Run `featureapp/showfeature.py`

If using vscode (launch.json):
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "UNLEASH_FRONTEND_TOKEN": "",
                "UNLEASH_BACKEND_TOKEN": ""
            }
        }
    ]
}
```


Visit: 
http://127.0.0.1:5000
http://127.0.0.1:5000/frontend

Toggle toggle

## Debugging/testing
https://docs.getunleash.io/reference/api/unleash/get-features
You can use the service account token to show features:
```
# Get all features
curl -L 'https://eu.app.unleash-hosted.com/euii0016/api/admin/projects/default/features' \
-H 'Accept: application/json' \
-H "Authorization: $UNLEASH_SERVICE_ACCOUNT_TOKEN" | jq

# Turn toggle-feature on in development
curl -L -X POST 'https://eu.app.unleash-hosted.com/euii0016/api/admin/projects/default/features/toggle-feature/environments/development/on' \
-H 'Accept: application/json' \
-H "Authorization: $UNLEASH_SERVICE_ACCOUNT_TOKEN"
```

## Workshopping
With the language of your choice (frontend and/or backend) do the following:
* Toggle on my-special-user (userId)
* Toggle on my-favorit-customer (tenantId)
* Why does it take a while for the flags to toogle? Why is this good stuff?

### Unleash UI
* Get a user (one per group)
* Create your own project
* Create a new context field
* Create a flag with the new context field
* Toogle the flag
* Check event log for the flag
* Check metrics for the flag
* View [Application](https://eu.app.unleash-hosted.com/euii0016/applications) - why is this useful?

### Your own special project?
Do whatever you like using the existing featureflag or new ones.

## Ending
* Why is context important?
* Why does the client show all features in backend but only active ones in frontend?