---
title: Testing App Store server notifications
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/testing-app-store-server-notifications
source_url: 'https://developer.apple.com/documentation/storekit/testing-app-store-server-notifications'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/testing-app-store-server-notifications.json'
content_hash: 'sha256:8d54bd6e63c3dcf6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)

# Testing App Store server notifications

<sub>Article</sub>

Confirm that App Store Server Notifications service responds properly in the sandbox environment.

## Overview

If you enabled notifications from the App Store for your app, test your logic for transactions in the sandbox environment. To determine if a notification for a subscription event occurred in the test environment, check whether the value of the `environment` field equals `Sandbox` in the [data](../appstoreservernotifications/data.md) object of the App Store Server Notifications [responseBodyV2DecodedPayload](../appstoreservernotifications/responsebodyv2decodedpayload.md) object.

For more information about the App Store Server Notifications service, see [App Store Server Notifications](../appstoreservernotifications.md). To ask the App Store to send test notifications, and to get a history of notifications sent to your server, see [Request a Test Notification](../appstoreserverapi/request-a-test-notification.md) and [Get Notification History](../appstoreserverapi/get-notification-history.md) in the [App Store Server API](../appstoreserverapi.md).
