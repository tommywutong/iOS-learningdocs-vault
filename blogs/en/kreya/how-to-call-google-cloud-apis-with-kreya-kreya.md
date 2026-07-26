---
title: 'How to call Google Cloud APIs with Kreya | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/how-to-call-google-cloud-apis/'
original_language: en
published: 2026-04-28
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5d6a137becef9c55'
translated: false
---

> 原文：[How to call Google Cloud APIs with Kreya | Kreya](https://kreya.app/blog/how-to-call-google-cloud-apis/)　·　Kreya Blog

In this post, we'll show you how to use Kreya to automate the Google Cloud authentication flow, allowing you to call Google Cloud Platform services effortlessly.

## Setting up authentication in Kreya

One of the major benefits of Kreya is that authentication is built into the core of the app. Instead of manually adding `Authorization: Bearer ...` headers to every request, you define a Google Cloud authentication configuration once and reuse it throughout your project.

Navigate in Kreya to the **Project** menu and select **Authentications** (or use the shortcut Ctrl+⇧+a).

### Google Cloud authentication types

Kreya supports different ways to authenticate against Google Cloud, depending on whether you are acting as a system (Service Account) or a developer (User).

### Service Account Authentication

When you need to test with a specific set of permissions or simulate a backend-to-backend call, using a **Service Account** is the way to go.

If you don't have a service account yet, you can go to the [Google Cloud Console](https://console.cloud.google.com/), and navigate to **IAM & Admin \> Service Accounts** (a project is required).  
 You can use an existing service account (which already has the necessary permissions), or create a new one.

![Google Cloud service accounts overview](https://kreya.app/blogposts/calling-google-apis/gcloud-iam-service-accounts-1.png)

If you create a new one, make sure it has the necessary roles to send API requests to the service you want to test.

![Google Cloud service account roles](https://kreya.app/blogposts/calling-google-apis/gcloud-iam-service-accounts-2.png)

To view the "login key" of a service account, click on the service account, then go to the **Keys** tab.  
 To create a new key click **Add key** and select key type **JSON**.

After generating the key, the JSON file will automatically be downloaded to your computer (this is the only copy!).

![Google Cloud service account key and key auto-download](https://kreya.app/blogposts/calling-google-apis/gcloud-iam-service-accounts-4.png)

Move this JSON file to a secure location and note the path, as you'll need it to configure the Kreya authentication:

| Property | Value |
|---|---|
| **Type** | Google Service Account |
| **Key file (json)** | `PATH_TO_KEY_JSON_FILE` |
| **Scope** | [See https://developers.google.com/identity/protocols/oauth2/scopes](https://developers.google.com/identity/protocols/oauth2/scopes?hl=de) |

It should look similar to this:

![Kreya Google Service Account config](https://kreya.app/blogposts/calling-google-apis/kreya-gcloud-service-account.png)

note

You can use environment variables like `{{ env.gcp.keyPath }}` to point to your JSON key. This keeps your project configuration portable and prevents you from hardcoding absolute paths that might differ between team members.

### User Authentication (OAuth2 / OpenID-Connect)

If you want to login with a specific user (which has permissions to access the API), you can use the Kreya authentication type `OAuth2 / OpenID-Connect`.

You need to setup a **OAuth 2.0 Client ID** credential in the Google Cloud Console.  
 If you don't have one yet, navigate to **API & Services \> Credentials** and create one.

![Google Cloud credentials overview](https://kreya.app/blogposts/calling-google-apis/gcloud-oauth-1.png)

You can find the **Client ID** and **Client secret** in the credential details.

note

The **Client secret** has to be copied during the credential or secret creation.

![Google Cloud Client ID details](https://kreya.app/blogposts/calling-google-apis/gcloud-oauth-2.png)

The user which signs in, also needs to have the necessary roles to access the API.  
 This can be verified in the **IAM & Admin \> IAM** section of the Google Cloud Console.

![Google Cloud User permissions](https://kreya.app/blogposts/calling-google-apis/gcloud-iam-test-user-2.png)

If everything is setup correctly, you can use the following configuration in Kreya to authenticate with Google Cloud:

| Property | Value |
|---|---|
| **Type** | OAuth2 / OpenID-Connect |
| **Grant type** | Authorization code |
| **Issuer** | [https://accounts.google.com](https://accounts.google.com) |
| **Client Authorize Method** | Basic |
| **Client-ID** | `#GOOGLE_OAUTH_CLIENT_ID` (can be found in the Google Auth Platform client info) |
| **Client-Secret** | `#GOOGLE_OAUTH_CLIENT_SECRET` (can be found in the Google Auth Platform client info) |
| **Use native browser** | Check (optional) |
| **Scope** | [See https://developers.google.com/identity/protocols/oauth2/scopes](https://developers.google.com/identity/protocols/oauth2/scopes?hl=de) |
| **Token-Type to authorize on APIs** | Access-Token |

It should look similar to this:

![Kreya Googe OAuth 2.0 config](https://kreya.app/blogposts/calling-google-apis/kreya-gcloud-user.png)

### Invoking the request

To use your new Google Cloud authentication configuration, go to the **Auth** tab of your request and select the configuration.

![Kreya Auth Configuration selection](https://kreya.app/blogposts/calling-google-apis/kreya-auth-update-1.png)

To explicitly fetch a token, click the **Update** Button.  
 Kreya handles the background communication with Google's authentication servers. If the retrieval is successful, you'll see the token and its expiry date.

![Kreya Auth refresh](https://kreya.app/blogposts/calling-google-apis/kreya-auth-update-2.png)

Depending on your authentication configuration, it will directly fetch the token or open your browser, where you can login with an authorized user.

If the retrieval is successful, Kreya displays the JWT and its expiry date directly in the UI. You don't need to re-authenticate for every request, Kreya caches the token and automatically includes it in the request.

### Examples

In this section, we'll call different Google Cloud APIs using Kreya with the authentication configuration we set up in the previous sections.

As an improvement, we have moved several Google Cloud values to the Kreya environment variables, so that we can reuse them across multiple requests and easily switch between different Google Cloud projects.

![Kreya Auth refresh](https://kreya.app/blogposts/calling-google-apis/env-1.png)

![Kreya Auth refresh](https://kreya.app/blogposts/calling-google-apis/env-2.png)

#### Google Cloud Compute Engine API

Lists all Google Cloud Compute Engine instances of the project.

Endpoint:  
 `https://compute.googleapis.com/compute/v1/projects/{{env.gcp.projectId}}/zones/{{env.gcp.zone}}/instances`

![Kreya Auth refresh](https://kreya.app/blogposts/calling-google-apis/gcloud-example-1.png)

#### Google Cloud Run API

Lists all Google Cloud Run services of the project.

Endpoint:  
 `https://run.googleapis.com/apis/serving.knative.dev/v1/namespaces/{{env.gcp.projectId}}/services`

![Kreya Auth refresh](https://kreya.app/blogposts/calling-google-apis/gcloud-example-2.png)

### Pro tip: Set the auth per directory settings

Instead of manually assigning the authentication configuration to every single request, you can use **Directory settings**.

By setting the authentication at the directory level, all requests within that directory and its subdirectories will automatically inherit those credentials.

![Kreya Auth per Directory Settings](https://kreya.app/blogposts/calling-google-apis/directory-settings.png)

## Conclusion

Testing Google Cloud APIs doesn't have to be a manual burden involving the terminal and copy-pasting long strings.  
 By using Kreya's native Google Cloud and OAuth support, you can automate token retrieval and focus on building your services.

Whether you're querying the Cloud Storage API or testing Google Cloud Platform backend calls, Kreya's automated token management makes your development workflow significantly smoother.

**Ready to try it out?** [Download Kreya](https://kreya.app/downloads/) today and start testing your Google Cloud services the easy way.
