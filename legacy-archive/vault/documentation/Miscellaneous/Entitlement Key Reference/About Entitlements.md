---
title: Entitlement Key Reference
apple_id: TP40011195
resource_type: Guide
platform: iOS|macOS
topic: General
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/AboutEntitlements.html
archived_at: '2026-07-15T08:17:10.394591Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Enabling%20iCloud%20Storage.md)

# About Entitlements

Entitlements confer specific capabilities or security permissions to your iOS or macOS app.

Set entitlement values in order to enable iCloud, push notifications, Apple Pay, and App Sandbox. Each entitlement has a default value, which in most cases disables the capability associated with the entitlement. When you set an entitlement, you are overriding the default by providing an appropriate key-value pair.

- iCloud entitlements let you enable the use of iCloud data storage for your iOS or macOS app.

  You set iCloud entitlement values on a target-by-target basis in your Xcode project.
- Push notifications let your app alert the user even when your iOS or macOS app is not executing.

  You set push notification entitlement values as part of configuring your development and distribution provisioning profiles.
- Apple Pay and PassKit Entitlements enable in-app payments using Apple Pay, and allow your app to access passes from the PassKit library.
- App Sandbox entitlements let you enable the security feature called _sandboxing_ for your macOS app. (In iOS, all apps are sandboxed automatically, so these sandboxing entitlements do not apply.)

  By carefully enabling only the resource access that you need, you minimize the potential for damage if malicious code successfully exploits your app. You set App Sandbox entitlement values on a target-by-target basis in your Xcode project.

You can set many entitlements using the Summary tab of the Xcode target editor. Other entitlements require editing a target’s entitlements [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) file. Finally, a few entitlements are inherited from the iOS provisioning profile used to run the app.

The sort of value to associate with an entitlement key depends on the key. Many entitlement keys take Boolean values. For entitlements defined in a property list in an Xcode project, a Boolean entitlement value is either `<true/>` or `<false/>`. Some entitlement keys take a string or an array of strings as a value. Refer to the chapters in this document for specifics on the values to apply to the various entitlement keys.

To use any entitlement keys, you must code sign your app because an app’s entitlements are built in to its code signature.

### Enable iCloud for Sharing Data Among Devices

Xcode’s target editor contains two fields that let you enable iCloud document and key-value storage for your app.

### Enable Push Notifications for Alerting the User

You can send push notifications to users, by way of the Apple Push Notification service (APNs), to let users know your app has information for them. To enable the receiving of such notifications in your app, request the appropriate entitlement within your development and distribution provisioning profiles.

### Enable Apple Pay and Access to Passes

You can accept in-app payment for goods and services. You can also access your passes in Wallet. Additional entitlements allow the suppression of the Apple Pay interface when working near NFC or other RF readers, and in-app provisioning of payment cards.

### Enable App Sandbox to Minimize Damage from Malicious Code

Employ Xcode’s target editor to turn on and configure App Sandbox for targets in an macOS project.

### Use App Sandbox Temporary Exceptions, If Needed

If you are unable to transition your entire app to App Sandbox in a single release, you can employ special temporary-exception entitlements.

Understand where entitlements fit into the development process by reading _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_ or _[Mac App Programming Guide](../../General/Mac%20App%20Programming%20Guide/About%20OS%20X%20App%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbt)_.

You set iCloud and App Sandbox entitlement values using Xcode. For an introduction to Xcode, read _[Xcode Overview](https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/index.html#//apple_ref/doc/uid/TP40010215)_.

When adding iCloud features to your app, be sure to read _[iCloud Design Guide](../../General/iCloud%20Design%20Guide/About%20Incorporating%20iCloud%20into%20Your%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaoju)_.

When adding push notification capability to your app, refer to _[Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194)_.

When configuring your sandbox, use this document in concert with _[App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183)_.

[Next](Enabling%20iCloud%20Storage.md)

