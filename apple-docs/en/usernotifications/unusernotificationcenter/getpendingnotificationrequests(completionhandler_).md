---
title: 'getPendingNotificationRequests(completionHandler:)'
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unusernotificationcenter/getpendingnotificationrequests(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/getpendingnotificationrequests(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter/getpendingnotificationrequests%28completionhandler%3A%29.json'
content_hash: 'sha256:9dfb3d37195a6e08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNUserNotificationCenter](../unusernotificationcenter.md)

# getPendingNotificationRequests(completionHandler:)

<sub>Instance Method</sub>

Fetches all of your app’s local notifications that are pending delivery.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getPendingNotificationRequests(completionHandler: @escaping @Sendable ([UNNotificationRequest]) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func pendingNotificationRequests() async -> [UNNotificationRequest]
```

## Parameters

- `completionHandler` — A block for processing notification requests. This block may be executed on a background thread. The block has no return value and takes a single parameter. - **requests** — An array of [UNNotificationRequest](../unnotificationrequest.md) objects representing the scheduled notification requests. If there are no scheduled requests, this array is empty.

## Discussion

> [!important] Important
> You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func pendingNotificationRequests() async -> [UNNotificationRequest]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../swift/calling-objective-c-apis-asynchronously.md).

Here’s an example that obtains the pending notification requests.

```swift
let center = UNUserNotificationCenter.current()
let requests = await center.pendingNotificationRequests()
```

## See Also

### Scheduling notifications

- [- addNotificationRequest:withCompletionHandler:](<add(__withcompletionhandler_).md>) — Schedules the delivery of a local notification.
- [- removePendingNotificationRequestsWithIdentifiers:](<removependingnotificationrequests(withidentifiers_).md>) — Removes your app’s local notifications that are pending and match the specified identifiers.
- [- removeAllPendingNotificationRequests](<removeallpendingnotificationrequests().md>) — Removes all of your app’s pending local notifications.
