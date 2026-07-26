---
title: Location Push Service Extension
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 7.0+, iPadOS 7.0+, macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.developer.location.push
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.location.push'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.developer.location.push.json'
content_hash: 'sha256:f6219cf182078691'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# Location Push Service Extension

<sub>Property List Key</sub>

An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.

## Discussion

This entitlement enables your app to monitor for Apple Push Notification service (APNs) pushes with the `location` push type, and receive pushes in your Location Push Service Extension. For more information about the `location` push type, see [Sending notification requests to APNs](../../usernotifications/sending-notification-requests-to-apns.md).

> [!note] Note
> Without this entitlement, your code receives an error when it calls [startMonitoringLocationPushes(completion:)](<../../corelocation/cllocationmanager/startmonitoringlocationpushes(completion_).md>).

Add the entitlement to your app by following these steps:

1. Open your app’s Xcode project and select your app from the target list.
2. Select the Signing & Capabilities panel.
3. Click “+ Capabilities” and enter “push” in the search field; then double-click Location Push Service Extension to add the entitlement to your app’s entitlements file.

For more information about implementing your Location Push Service Extension, see [Creating a location push service extension](../../corelocation/creating-a-location-push-service-extension.md).
