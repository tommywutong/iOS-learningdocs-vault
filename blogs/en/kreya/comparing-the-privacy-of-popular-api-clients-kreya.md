---
title: 'Comparing the privacy of popular API clients | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/comparing-privacy-of-popular-api-clients/'
original_language: en
published: 2025-06-13
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:764673874fd8e9ca'
translated: false
---

> 原文：[Comparing the privacy of popular API clients | Kreya](https://kreya.app/blog/comparing-privacy-of-popular-api-clients/)　·　Kreya Blog

API clients hold sensitive data, from auth tokens to proprietary endpoints. But much control do users retain over their data? And is their privacy respected?

When choosing an API client, developers often focus on features and performance. However, with growing concerns over data privacy, understanding how these tools handle your information is more critical than ever. This comparison examines the privacy postures of four popular API clients: Postman, Kreya, Insomnia, and Bruno.

All API clients were tested with their newest version as of 13 June 2025. Only free editions without login were used. A fresh "workspace" was initiatilized before any telemetry data was collected.

## Postman

Postman is one of the oldest API clients and certainly the most popular. Since its inception, Postman shifted the approach from a simple GUI client to a cloud platform. And this cloud-centric approach is clear to see: Almost all data is stored in the Postman cloud and this cannot be changed. The only exception is using Postman without an account through the [lightweight API client](https://learning.postman.com/docs/getting-started/basics/using-api-client/). This stores the data locally, but the lightweight API client has a heavily restricted feature set. Postman heavily encourages creating an account, since otherwise syncing your data is not possible. Other features, such as environments, workspaces and collections, are also locked behind an account.

To get back control over their data, Postman users often export their collections as a big JSON file and sync that via git. However, Postman seems to restrict this export feature. For example, gRPC and WebSocket requests cannot be exported and remain locked into the Postman world.

Not only do users barely have any control over their data, it is also uploaded to Postman's servers. There are possibilities to keep data (such as "current values" of variables) local only, but one small misstep and a secret is leaked to Postman. Postman knows everything about your APIs. Confidential URLs, hidden features, secret upcoming changes deployed to your staging environment are just some of the examples that are exposed to Postman's servers.

Let's take a look at the collected telemetry. As with all tested clients, telemetry is automatically being collected. **Postman does not offer a way to disabled telemetry.** Interestingly, it also does not list which third party services it uses to collect telemetry data in its [privacy policy](https://www.postman.com/legal/privacy-policy/).

To see how much Postman phones home, opening the lightweight API client (version 11.49.4) and sending a request while intercepting the traffic resulted in 10 requests being sent to external servers:

- Some of them were simple update checks, for example to [https://dl.pstmn.io](https://dl.pstmn.io).
- Two requests went to LaunchDarkly, which can be used for telemetry as well as for feature flags. One call returned a staggering 112 KB message of feature flags.
- [https://bifrost-https-v10.gw.postman.com/ws/proxy](https://bifrost-https-v10.gw.postman.com/ws/proxy) was contacted with information about the installation.
- [https://events.getpostman.com/events](https://events.getpostman.com/events) was called with the following telemetry data:

  View JSON data

  ```json
  {    "type": "events-general",    "indexType": "client-events",    "env": "production",    "propertyId": "{redacted uuid}",    "userId": "0",    "teamId": "",    "propertyVersion": "11.49.4",    "property": "windows_app",    "timestamp": "2025-06-13T08:26:22.573Z",    "category": "offline_api_client",    "action": "ad_viewed",    "label": "collections",    "value": 1}
  ```
- [https://api2.amplitude.com/2/httpapi](https://api2.amplitude.com/2/httpapi) is also used for detail telemetry data:

  View JSON data

  ```json
  {  "api_key": "56d4a7f42486e1c4ec95a892fd96c402",  "events": [    {      "user_id": null,      "device_id": "{redacted uuid}",      "session_id": 1749803181864,      "time": 1749803181873,      "platform": "Web",      "language": "de",      "ip": "$remote",      "insert_id": "9f584529-db9c-45c9-bbe4-9aa675a91358",      "event_type": "$identify",      "user_properties": {},      "event_id": 0,      "library": "amplitude-ts/2.7.2",      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Postman/11.49.4 Electron/32.3.3 Safari/537.36",      "event_properties": {}    },    {      "user_id": null,      "device_id": "{redacted uuid}",      "session_id": 1749803181864,      "time": 1749803181864,      "platform": "Web",      "language": "de",      "ip": "$remote",      "insert_id": "d232976f-6ba7-4151-8d60-6d347c4be793",      "event_type": "session_start",      "event_id": 1,      "library": "amplitude-ts/2.7.2",      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Postman/11.49.4 Electron/32.3.3 Safari/537.36",      "event_properties": {},      "user_properties": {}    },    {      "user_id": null,      "device_id": "{redacted uuid}",      "session_id": 1749803181864,      "time": 1749803181953,      "platform": "Web",      "language": "de",      "ip": "$remote",      "insert_id": "d0230992-17d9-4952-a3db-514a18e6bd1d",      "event_type": "[Amplitude] Page Viewed",      "event_properties": {        "[Amplitude] Page Domain": "",        "[Amplitude] Page Location": "{redacted path}/Postman/app-11.49.4/resources/app.asar/html/scratchpad.html?browserWindowId=1&logPath={redacted path}\\Postman\\logs&sessionId=6712&startTime=1749802966409&preloadFile={redacted path}\\Postman\\app-11.49.4\\resources\\app.asar\\preload_desktop.js&scratchpadPartitionId=e60a4656-25bf-4ff4-b8aa-7576cc4eb535&isFirstRequester=true",        "[Amplitude] Page Path": "/{redacted path}/Postman/app-11.49.4/resources/app.asar/html/scratchpad.html",        "[Amplitude] Page Title": "Postman",        "[Amplitude] Page URL": "{redacted path}/Postman/app-11.49.4/resources/app.asar/html/scratchpad.html",        "release_channel": "",        "platform": "desktop",        "current_url": "/{redacted path}/Postman/app-11.49.4/resources/app.asar/html/scratchpad.html",        "event_source": "client_app",        "team_user_id": null,        "company_size": 0,        "workspace_visibility": null,        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Postman/11.49.4 Electron/32.3.3 Safari/537.36",        "[Amplitude] Page Counter": 1      },      "event_id": 2,      "library": "amplitude-ts/2.7.2",      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Postman/11.49.4 Electron/32.3.3 Safari/537.36",      "user_properties": {}    },    {      "user_id": null,      "device_id": "{redacted uuid}",      "session_id": 1749803181864,      "time": 1749803181966,      "platform": "Web",      "language": "de",      "ip": "$remote",      "insert_id": "845fff32-2de2-40f9-974f-621a4a6ec6e2",      "event_type": "$identify",      "user_properties": {},      "event_id": 3,      "library": "amplitude-ts/2.7.2",      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Postman/11.49.4 Electron/32.3.3 Safari/537.36",      "event_properties": {}    },    {      "user_id": null,      "device_id": "{redacted uuid}",      "session_id": 1749803181864,      "time": 1749803182616,      "platform": "Web",      "language": "de",      "ip": "$remote",      "insert_id": "fd0f1c4d-8f88-4616-9d4a-32c39cee7456",      "event_type": "LAC - Micro Ads - Ad - Viewed",      "event_properties": {        "ad_id": "collections",        "release_channel": "",        "platform": "desktop",        "current_url": "/{redacted path}/Postman/app-11.49.4/resources/app.asar/html/scratchpad.html",        "event_source": "client_app",        "team_user_id": null,        "company_size": 0,        "workspace_visibility": null,        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Postman/11.49.4 Electron/32.3.3 Safari/537.36"      },      "event_id": 4,      "library": "amplitude-ts/2.7.2",      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Postman/11.49.4 Electron/32.3.3 Safari/537.36",      "user_properties": {}    }  ],  "options": {},  "client_upload_time": "2025-06-13T08:26:26.885Z"}
  ```
- Postman also loads some SVGs from the internet, such as [https://postman.com/_aether-assets/illustrations/dark/illustration-hit-send.svg](https://postman.com/_aether-assets/illustrations/dark/illustration-hit-send.svg).

All of this was just during a very short session. Using Postman for longer generates even more telemetry data.

I couldn't reproduce [reports that Postman logs all endpoints include query parameters](https://anonymousdata.medium.com/postman-is-logging-all-your-secrets-and-environment-variables-9c316e92d424), maybe this has been fixed or only happens when using the full Postman version.

Regarding privacy, Postman has also been involved in some controversies in the past. One of the most recent questionable change to Postman was implemented in 2023 when the Postman Scratchpad was removed. If users were not careful during this period and migrated their local Scratchpad data to the Postman cloud, they lost access to it with the following Postman updates. The Scratchpad was eventually replaced by the lightweight API client with a reduced functionality. Most users needed to create an account and upload their data to continue using Postman as they were accustomed to.

All in all, Postman scores pretty badly in regard to privacy and data ownership. It is still the most popular application in this space since it has been around for longer and probably has the most features.

## Kreya

New API clients appear as quickly as some disappear again. With four years under its belt, Kreya is already an established tool. Created with a strong focus on privacy, it should score better than most alternatives.

One interesting approach that has gained popularity (again) in recent years is the local storage of data. In contrast to most competitors, Kreya does not store its data as a proprietary blob or on some external server. Instead, Kreya project data is stored in JSON files in a location of the users choosing. The data format is even optimized for syncing via git. For example, the JSON is formatted and stringified JSON fields were avoided to help with reviewing changes and possible merge conflicts. But syncing the data via git is not the only option. Users may use any software they wish to transfer the data to other users to collaborate on Kreya projects.

This approach decouples Kreya from the "data ownership", leaving complete control to users. Users are also able to work completely offline, since all data is stored on their computer.

Since Kreya does not sync anything to external servers, the need for an account is not there. All free features are usable without an account.

An account (basically only the email address) is only required for validating the license of a paid subscription and has no other impact. Enterprise customers may even request an "offline license key". This does not require an account nor any communication to the Kreya license server.

As for telemetry, let's open Kreya (version 1.17.0) and perform some actions. After closing the app, three requests have been sent to external servers:

- One request to [https://kreya.app/user-messages/user-messages.json](https://kreya.app/user-messages/user-messages.json), which is used to display (urgent) messages to users.
- One request to [https://stable-downloads.kreya.app/appcast.json](https://stable-downloads.kreya.app/appcast.json) to check for new versions.
- One request to [https://api.mixpanel.com](https://api.mixpanel.com) for [anonymous telemetry](https://kreya.app/docs/telemetry/) with the following content:

  View JSON data

  ```json
  [  {    "event": "AppStarted",    "properties": {      "$os": "win-x64",      "token": "{redacted}",      "distinct_id": "{redacted uuid}",      "version": "1.17.0",      "launchInfo": "NoUpdate",      "arch": "X64",      "osArch": "X64",      "subscriptionPlan": "Free",      "authenticated": false,      "appKind": "Ui",      "packageManager": "None",      "time": 1749805404    }  },  {    "event": "OperationInvoked",    "properties": {      "token": "{redacted}",      "distinct_id": "{redacted uuid}",      "invokerName": "rest",      "sendMode": "all",      "operationType": "unary",      "hasScript": false,      "httpMethod": "GET",      "time": 1749805421    }  },  {    "event": "AppClosed",    "properties": {      "token": "{redacted}",      "distinct_id": "{redacted uuid}",      "openDurationSeconds": 22,      "time": 1749805427    }  }]
  ```

Telemetry and update checks can be disabled via [configuration](https://kreya.app/docs/configuration/#available-configuration-options). Disabling those two features would cut the requests down, resulting in only one call to [https://kreya.app/user-messages/user-messages.json](https://kreya.app/user-messages/user-messages.json). Kreya is also the only of the tools to [explicitly declare what telemetry data it collects](https://kreya.app/docs/telemetry/).

As we can see, Kreya is much more focused on privacy and data ownership than Postman. **Kreya is also the only API client out of the four to be able to completely disable telemetry.**

## Insomnia

Insomnia was created by Gregory Schier as a slick alternative to Postman. It has since been sold to Kong Inc.

While Insomnia has been pretty focused on privacy in the past, it shows that Insomnia has been bought by a big company. For example [Insomnia 8.0 introduced an account requirement](https://github.com/Kong/insomnia/issues/6577) for most of the existing features. If users did create an account, **all their data was uploaded to Insomnia's servers**. As a response, users created the fork [Insomnium](https://github.com/ArchGPT/insomnium), but was later abandoned.

Insomnia has three storage options, which give the user some control over their data:

- Local vault: Stores data locally in a proprietary format
- Secure cloud: Syncs all data to Insomnia's servers, end-to-end encrypted on paid plans. If the user does not provide a passphrase, Insomnia generates one and stores it on their server.
- Git sync: Insomnia automatically syncs changes to a git repository. For paid plans only.

As for telemetry, using Insomnia 11.2.0 to view the requests performed by the app:

- [https://api.github.com/repos/Kong/insomnia](https://api.github.com/repos/Kong/insomnia), maybe to get information about GitHub stars?
- Two calls to [https://updates.insomnia.rest/](https://updates.insomnia.rest/) with installation information
- One call to [https://github.com/Kong/insomnia/releases/download/[email protected]/RELEASES](https://github.com/Kong/insomnia/releases/download/core@11.2.0/RELEASES)
- One call to [https://api.segment.io/v1/batch](https://api.segment.io/v1/batch) with the following content:

  View JSON data

  ```json
  {  "batch": [{    "timestamp": "2025-06-13T08:47:55.077Z",    "integrations": {},    "event": "App Started",    "type": "track",    "properties": {      "localProjects": 0,      "remoteProjects": 0,      "createdRequests": 1,      "deletedRequests": 0,      "executedRequests": 1    },    "context": {      "app": {        "name": "Insomnia",        "version": "11.2.0"      },      "os": {        "name": "windows",        "version": "10.0.26100"      },      "library": {        "name": "@segment/analytics-node",        "version": "2.2.1"      }    },    "userId": "",    "anonymousId": "{redacted uuid}",    "messageId": "node-next-1749804475077-a0e58dd8-978c-4181-b720-d1393391fc2d",    "_metadata": {      "nodeVersion": "v22.14.0",      "jsRuntime": "node"    }  }, {    "timestamp": "2025-06-13T08:47:56.396Z",    "integrations": {},    "type": "page",    "properties": {},    "name": "/organization/org_scratchpad/project/proj_scratchpad/workspace/wrk_scratchpad/debug/request/req_id",    "context": {      "app": {        "name": "Insomnia",        "version": "11.2.0"      },      "os": {        "name": "windows",        "version": "10.0.26100"      },      "library": {        "name": "@segment/analytics-node",        "version": "2.2.1"      }    },    "anonymousId": "{redacted uuid}",    "userId": "",    "messageId": "node-next-1749804476396-d8978cb1-81f7-40d1-b933-91fc2d0bcb28",    "_metadata": {      "nodeVersion": "v22.14.0",      "jsRuntime": "node"    }  }],  "writeKey": "4l7QUfACrIcqvC913hiIwAA2BDYP2OJ1",  "sentAt": "2025-06-13T08:48:05.089Z"}
  ```
- One call to [https://redacted-subdomain.ingest.sentry.io/api/](https://redacted-subdomain.ingest.sentry.io/api/) with

  View JSON data

  ```json
  {  "sent_at": "2025-06-13T08:49:37.343Z",  "sdk": {    "name": "sentry.javascript.electron",    "version": "6.5.0"  }}{  "type": "session"}{  "sid": "172e49db6845452b84f79c0d081b82eb",  "init": true,  "started": "2025-06-13T08:47:53.975Z",  "timestamp": "2025-06-13T08:49:37.343Z",  "status": "exited",  "errors": 0,  "duration": 103.36775422096252,  "attrs": {    "release": "11.2.0",    "environment": "production",    "user_agent": "Node.js/22"  }}
  ```

Interestingly, Insomnia tracks every click in the UI with Sentry (as seen in the DevTools), but does not send this information to its servers. Maybe this data is sampled and only a subset is sent or maybe this is only sent in case an error occurs.

What's even more interesting is that users without an account are able to disable the telemetry, but [users logged into Insomnia do not have this option](https://github.com/Kong/insomnia/blob/core%4011.2.0/packages/insomnia/src/main/analytics.ts#L109)! The telemetry for users is also not really anonymous like in the other tools, as it sends the hashed (SHA256) user id as part of the message.

## Bruno

The first version of Bruno was released at around the same time as Kreya with a similar idea for local data storage. The main difference is that Bruno stores the data in the custom Bru markup language, whereas Kreya stores it as JSON.

There are a lot of other similarities between Bruno and Kreya. Both do not require an account for the free version and only an email address to verify the license for paid plans.

As for telemetry and other requests, opening Bruno 2.5.0 yielded the following requests:

- Two requests to [https://github.com/usebruno/bruno](https://github.com/usebruno/bruno), maybe to get star and release information?
- One request to [https://objects.githubusercontent.com](https://objects.githubusercontent.com)
- One telemetry request to [https://us.i.posthog.com/batch/](https://us.i.posthog.com/batch/):

  View JSON data

  ```json
  {  "api_key": "{redacted}",  "batch": [{    "distinct_id": "RVIvKzCa5iF0kThDLRAh8",    "event": "start",    "properties": {      "os": "Windows",      "version": "2.5.0",      "$lib": "posthog-node",      "$lib_version": "4.2.1",      "$geoip_disable": true    },    "type": "capture",    "library": "posthog-node",    "library_version": "4.2.1",    "timestamp": "2025-06-13T09:09:18.213Z",    "uuid": "0197688b-f706-7f98-2b0b-ae2c1068eab1"  }],  "sent_at": "2025-06-13T09:09:28.215Z"}
  ```

The telemetry data is pretty slim, **but cannot be disabled**.

All in all, there is not much to complain about Bruno's privacy approach with the exception that telemetry cannot be disabled.

## Conclusion

When it comes to privacy and data control, there are clear differences among these popular API clients.

| Tool | Data storage | Account requirement | Telemetry | Key takeaway |
|---|---|---|---|---|
| **Postman** | Cloud-first | Heavily encouraged | Cannot be disabled | Heavy cloud integration with little data control. |
| **Kreya** | Local-first | No | Can be disabled | Excellent privacy, full data control. |
| **Insomnia** | Cloud-encouraged | Heavily encouraged | Cannot be disabled while logged in | Lost its way after acquisition, forcing cloud-centric features. |
| **Bruno** | Local-first | No | Cannot be disabled | Strong privacy, full data control. |

Which API client should you choose? As one of the creators of Kreya, my choice is clear :)  
 But choose for yourself. Apart from the privacy and data ownership, there may also be features that one API client solves better than others.

Do you have questions or feedback? Do no hesitate to reach out to us at [[email protected]](https://kreya.app/cdn-cgi/l/email-protection#68000d04040728031a0d110946091818)!
