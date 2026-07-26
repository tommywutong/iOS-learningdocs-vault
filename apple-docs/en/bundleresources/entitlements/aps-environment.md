---
title: APS Environment Entitlement
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 10.0+, iPadOS 10.0+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/aps-environment
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/aps-environment.json'
content_hash: 'sha256:2c06865a0e6386cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# APS Environment Entitlement

<sub>Property List Key</sub>

The environment for push notifications.

## Discussion

This key specifies whether to use the development or production Apple Push Notification service (APNs) environment when registering for push notifications.

Xcode sets the value of the entitlement based on your app’s current provisioning profile. For example, if you’re using a development provisioning profile, Xcode sets the value to `development`. Production provisioning profile and [Prerelease Versions and Beta Testers](../../appstoreconnectapi/prerelease-versions-and-beta-testers.md) use `production`. These default settings can be modified. The `development` environment is also referred to as the `sandbox` environment.

Use this entitlement for both the UserNotifications and PushKit frameworks.

To add this entitlement to your app, enable the Push Notifications capability in Xcode.

## See Also

### Related Documentation

- [Registering your app with APNs](../../usernotifications/registering-your-app-with-apns.md) — Communicate with Apple Push Notification service (APNs) and receive a unique device token that identifies your app.
- [PushKit](../../pushkit.md) — Respond to push notifications related to your app’s complications, file providers, and VoIP services.

### Notifications

- [APS Environment (macOS) Entitlement](com.apple.developer.aps-environment.md) — The environment for push notifications in macOS apps.
- [Critical Alerts](com.apple.developer.usernotifications.critical-alerts.md) — An entitlement that permits an app to receive critical alert notifications.
- [com.apple.developer.usernotifications.filtering](com.apple.developer.usernotifications.filtering.md) — Enable receiving notifications without displaying the notification to the user.
