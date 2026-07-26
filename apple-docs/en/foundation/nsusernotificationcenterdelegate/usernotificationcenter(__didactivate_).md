---
title: 'userNotificationCenter(_:didActivate:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter(_:didactivate:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter(_:didactivate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter%28_%3Adidactivate%3A%29.json'
content_hash: 'sha256:109d90e38c299513'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotificationCenterDelegate](../nsusernotificationcenterdelegate.md)

# userNotificationCenter(_:didActivate:)

<sub>Instance Method</sub>

Sent to the delegate when a user clicks on a user notification presented by the user notification center.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
optional func userNotificationCenter(_ center: NSUserNotificationCenter, didActivate notification: NSUserNotification)
```

## Parameters

- `center` — The user notification center.

- `notification` — The user notification object.

## Discussion

This would be a good time to take action in response to user interacting with a specific notification.

To take an action when your application is launched as a result of a user clicking on a notification, be sure to implement the [applicationDidFinishLaunching(_:)](<../../appkit/nsapplicationdelegate/applicationdidfinishlaunching(__).md>) method in the application class that implements the [NSApplicationDelegate](../../appkit/nsapplicationdelegate.md) protocol. The notification parameter to that method has a `userInfo` dictionary, and if that dictionary has the `NSApplicationLaunchUserNotificationKey` key. The value of that key is the [NSUserNotification](../nsusernotification.md) object that caused the application to launch. The `NSUserNotification` object is delivered to the `NSApplication` delegate because that message will be sent before your application has a chance to set a delegate for the `NSUserNotificationCenter`.

## See Also

### User Notification Delivery Information

- [- userNotificationCenter:didDeliverNotification:](<usernotificationcenter(__diddeliver_).md>) — Sent to the delegate when a notification delivery date has arrived. _(deprecated)_
