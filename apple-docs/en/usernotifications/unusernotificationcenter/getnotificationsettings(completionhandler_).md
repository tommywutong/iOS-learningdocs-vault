---
title: 'getNotificationSettings(completionHandler:)'
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unusernotificationcenter/getnotificationsettings(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/getnotificationsettings(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter/getnotificationsettings%28completionhandler%3A%29.json'
content_hash: 'sha256:e0b60623092fab4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNUserNotificationCenter](../unusernotificationcenter.md)

# getNotificationSettings(completionHandler:)

<sub>Instance Method</sub>

Retrieves the authorization and feature-related settings for your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getNotificationSettings(completionHandler: @escaping @Sendable (UNNotificationSettings) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func notificationSettings() async -> UNNotificationSettings
```

## Parameters

- `completionHandler` — The block to execute asynchronously with the results. Your app may execute this block on a background thread. The block has no return value and takes the following parameter: - **settings** — The [UNNotificationSettings](../unnotificationsettings.md) object containing the current authorization settings for your app.

## Discussion

> [!important] Important
> You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func notificationSettings() async -> UNNotificationSettings
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../swift/calling-objective-c-apis-asynchronously.md).

Use this method to determine the user interactions and notification-related features that the system authorizes your app to use. You might then use this information to enable or disable specific notification-related features of your app.

```swift
let center = UNUserNotificationCenter.current()
let settings = await center.notificationSettings()
// Add code here to inspect or act on the settings.
```

When the user initially grants authorization to your app, the system gives your app a set of default notification-related settings. The user may change those settings at any time to enable or disable specific capabilities. For example, the user might disable the playing of sounds when a notification arrives.

## See Also

### Managing the notification center

- [+ currentNotificationCenter](<current().md>) — Returns your app’s notification center.
- [- setBadgeCount:withCompletionHandler:](<setbadgecount(__withcompletionhandler_).md>) — Updates the badge count for your app’s icon.
