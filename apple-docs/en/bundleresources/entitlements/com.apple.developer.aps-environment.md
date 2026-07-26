---
title: APS Environment (macOS) Entitlement
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [macOS 10.14+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.developer.aps-environment
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.aps-environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.developer.aps-environment.json'
content_hash: 'sha256:4b4f24f08117bec3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# APS Environment (macOS) Entitlement

<sub>Property List Key</sub>

The environment for push notifications in macOS apps.

## Discussion

This key specifies whether to use the development or production Apple Push Notification service (APNs) environment when registering for push notifications with [registerForRemoteNotifications()](<../../appkit/nsapplication/registerforremotenotifications().md>).

Xcode sets the value of the entitlement based on your app’s current provisioning profile. For example, if you’re using a development provisioning profile, Xcode sets the value to `development`.

To add this entitlement to your app, enable the Push Notifications capability in Xcode.

## See Also

### Related Documentation

- [Registering your app with APNs](../../usernotifications/registering-your-app-with-apns.md) — Communicate with Apple Push Notification service (APNs) and receive a unique device token that identifies your app.

### Notifications

- [APS Environment Entitlement](aps-environment.md) — The environment for push notifications.
- [Critical Alerts](com.apple.developer.usernotifications.critical-alerts.md) — An entitlement that permits an app to receive critical alert notifications.
- [com.apple.developer.usernotifications.filtering](com.apple.developer.usernotifications.filtering.md) — Enable receiving notifications without displaying the notification to the user.
