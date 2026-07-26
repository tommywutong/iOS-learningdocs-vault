---
title: 'getDeliveredNotifications(completionHandler:)'
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unusernotificationcenter/getdeliverednotifications(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/getdeliverednotifications(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter/getdeliverednotifications%28completionhandler%3A%29.json'
content_hash: 'sha256:41f0510c4bf889c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNUserNotificationCenter](../unusernotificationcenter.md)

# getDeliveredNotifications(completionHandler:)

<sub>Instance Method</sub>

Fetches all of your app’s delivered notifications that are still present in Notification Center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func getDeliveredNotifications(completionHandler: @escaping @Sendable ([UNNotification]) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func deliveredNotifications() async -> [UNNotification]
```

## Parameters

- `completionHandler` — The block to execute with the results. This block may be executed on a background thread. The block has no return value and takes the following parameter: - **notifications** — An array of [UNNotification](../unnotification.md) objects representing the local and remote notifications of your app that have been delivered and are still visible in Notification Center. If none of your app’s notifications are visible in Notification Center, the array is empty.

## Discussion

> [!important] Important
> You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func deliveredNotifications() async -> [UNNotification]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../swift/calling-objective-c-apis-asynchronously.md).

This method executes asynchronously, returning immediately and executing the provided block on a background thread when the results become available.

## See Also

### Removing delivered notifications

- [- removeDeliveredNotificationsWithIdentifiers:](<removedeliverednotifications(withidentifiers_).md>) — Removes your app’s notifications from Notification Center that match the specified identifiers.
- [- removeAllDeliveredNotifications](<removealldeliverednotifications().md>) — Removes all of your app’s delivered notifications from Notification Center.
