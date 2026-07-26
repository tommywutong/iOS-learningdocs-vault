---
title: current()
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unusernotificationcenter/current()
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/current()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter/current%28%29.json'
content_hash: 'sha256:6728716788cb9a61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNUserNotificationCenter](../unusernotificationcenter.md)

# current()

<sub>Type Method</sub>

Returns your app’s notification center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func current() -> UNUserNotificationCenter
```

## Return Value

The notification center object to use.

## Discussion

Always use this method to retrieve the shared notification center object for your app. Do not try to create instances of the [UNUserNotificationCenter](../unusernotificationcenter.md) class directly.

## See Also

### Managing the notification center

- [- getNotificationSettingsWithCompletionHandler:](<getnotificationsettings(completionhandler_).md>) — Retrieves the authorization and feature-related settings for your app.
- [- setBadgeCount:withCompletionHandler:](<setbadgecount(__withcompletionhandler_).md>) — Updates the badge count for your app’s icon.
