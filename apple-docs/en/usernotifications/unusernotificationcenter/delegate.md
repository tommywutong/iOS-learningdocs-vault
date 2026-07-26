---
title: delegate
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unusernotificationcenter/delegate
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter/delegate.json'
content_hash: 'sha256:a8bbbd1cb5056897'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNUserNotificationCenter](../unusernotificationcenter.md)

# delegate

<sub>Instance Property</sub>

The notification center’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var delegate: (any UNUserNotificationCenterDelegate)? { get set }
```

## Discussion

Use the delegate object to respond to user-selected actions and to process incoming notifications when your app is in the foreground. For example, you might use your delegate to silence notifications when your app is in the foreground.

To guarantee that your app responds to all actionable notifications, you must set the value of this property before your app finishes launching. For an iOS app, this means updating this property in the [application(_:willFinishLaunchingWithOptions:)](<../../uikit/uiapplicationdelegate/application(__willfinishlaunchingwithoptions_).md>) or [application(_:didFinishLaunchingWithOptions:)](<../../uikit/uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) method of the app delegate. Notifications that cause your app to be launched or delivered shortly after these methods finish executing.

For more information about implementing the delegate methods, see [UNUserNotificationCenterDelegate](../unusernotificationcenterdelegate.md).

## See Also

### Processing received notifications

- [UNUserNotificationCenterDelegate](../unusernotificationcenterdelegate.md) — An interface for processing incoming notifications and responding to notification actions.
- [supportsContentExtensions](supportscontentextensions.md) — A Boolean value that indicates whether the device supports notification content extensions.
