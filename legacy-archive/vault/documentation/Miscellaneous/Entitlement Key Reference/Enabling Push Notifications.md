---
title: Entitlement Key Reference
apple_id: TP40011195
resource_type: Guide
platform: iOS|macOS
topic: General
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingLocalAndPushNotifications.html
archived_at: '2026-07-15T08:17:10.435514Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Entitlement Key Reference](About%20Entitlements.md)


[Next](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/ApplePayandPassKitEntitlements/ApplePayandPassKitEntitlements.html)[Previous](Enabling%20iCloud%20Storage.md)

# Enabling Push Notifications

To enable your app to alert the user through push (also known as _remote_) notifications, set a value for the appropriate entitlement.

For a complete discussion about push notifications, see _[Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194)_.

You set a value for the push notification entitlement by way of your development and distribution provisioning profiles, as described in _[Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194)_.

The following table shows the push notification entitlement keys that apply to the iOS and macOS platforms:

Notification entitlement keyCapability

aps-environment

Receive push notifications in iOS

com.apple.developer.aps-environment

Receive push notifications in macOS

The entitlement key is different for iOS than it is for macOS. On either platform, however, the provisioning portal assigns a value of `development` or `production` to the key, depending only on which activity you are creating the provisioning profile for.

[Next](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/ApplePayandPassKitEntitlements/ApplePayandPassKitEntitlements.html)[Previous](Enabling%20iCloud%20Storage.md)

