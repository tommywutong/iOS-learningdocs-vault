---
title: 'getNotificationCategories(completionHandler:)'
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unusernotificationcenter/getnotificationcategories(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/getnotificationcategories(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter/getnotificationcategories%28completionhandler%3A%29.json'
content_hash: 'sha256:828fed6e63c6c242'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNUserNotificationCenter](../unusernotificationcenter.md)

# getNotificationCategories(completionHandler:)

<sub>Instance Method</sub>

Fetches your app’s registered notification categories.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func getNotificationCategories(completionHandler: @escaping @Sendable (Set<UNNotificationCategory>) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func notificationCategories() async -> Set<UNNotificationCategory>
```

## Parameters

- `completionHandler` — The block to execute asynchronously with the results. This block may be executed on a background thread. The block has no return value and takes the following parameter: - **categories** — The set of [UNNotificationCategory](../unnotificationcategory.md) objects containing your registered notification types. If your app has not yet registered any categories, this parameter is an empty set.

## Discussion

> [!important] Important
> You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func notificationCategories() async -> Set<UNNotificationCategory>
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../swift/calling-objective-c-apis-asynchronously.md).

Use this method to retrieve your app’s currently registered notification types. You might use this method when you want to augment the current set of categories with new categories later on. Simply merge the returned set with any new category objects and register the updated set.

```swift
let center = UNUserNotificationCenter.current()
let categories = await center.notificationCategories()
```

## See Also

### Managing notification categories

- [- setNotificationCategories:](<setnotificationcategories(__).md>) — Registers the notification categories that your app supports.
