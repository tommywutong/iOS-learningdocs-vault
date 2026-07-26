---
title: 'setBadgeCount(_:withCompletionHandler:)'
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unusernotificationcenter/setbadgecount(_:withcompletionhandler:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/setbadgecount(_:withcompletionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter/setbadgecount%28_%3Awithcompletionhandler%3A%29.json'
content_hash: 'sha256:e858a9dd5130eced'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNUserNotificationCenter](../unusernotificationcenter.md)

# setBadgeCount(_:withCompletionHandler:)

<sub>Instance Method</sub>

Updates the badge count for your app’s icon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBadgeCount(_ newBadgeCount: Int, withCompletionHandler completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBadgeCount(_ newBadgeCount: Int) async throws
```

## Parameters

- `newBadgeCount` — The new value to display.

- `completionHandler` — The handler to execute after the update finishes. If the update fails, the system provides an error that contains additional information about the failure.

## Discussion

> [!important] Important
> You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func setBadgeCount(_ newBadgeCount: Int) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../swift/calling-objective-c-apis-asynchronously.md).

Here’s an example that sets the badge count to a specific number.

```swift
let center = UNUserNotificationCenter.current()
do {
     // Set the badge count to 3.
     try await center.setBadgeCount(3)
} catch {
     // Handle any errors.
}
```

## See Also

### Managing the notification center

- [+ currentNotificationCenter](<current().md>) — Returns your app’s notification center.
- [- getNotificationSettingsWithCompletionHandler:](<getnotificationsettings(completionhandler_).md>) — Retrieves the authorization and feature-related settings for your app.
