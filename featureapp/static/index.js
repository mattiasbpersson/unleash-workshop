import { UnleashClient } from 'unleash-proxy-client';

const unleash = new UnleashClient({
    url: "https://unleash.ut.umetrics.io/api/frontend",
    clientKey:
        "<TOKEN>",
    appName: "featureapp_frontend",
});

unleash.start();

setInterval(() => {
    document.getElementById("app").innerHTML = `Flag is ${
        unleash.isEnabled("funny_feature") ? "enabled" : "disabled"
    }`;
}, 1000);