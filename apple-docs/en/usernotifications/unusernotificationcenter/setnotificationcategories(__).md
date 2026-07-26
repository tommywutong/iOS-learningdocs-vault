---
title: 'setNotificationCategories(_:)'
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unusernotificationcenter/setnotificationcategories(_:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/setnotificationcategories(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter/setnotificationcategories%28_%3A%29.json'
content_hash: 'sha256:bcf0d5533973b0d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNUserNotificationCenter](../unusernotificationcenter.md)

# setNotificationCategories(_:)

<sub>Instance Method</sub>

Registers the notification categories that your app supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func setNotificationCategories(_ categories: Set<UNNotificationCategory>)
```

## Parameters

- `categories` — A set of [UNNotificationCategory](../unnotificationcategory.md) objects, each of which contains the actions that are displayed with the notification interface. This parameter must contain all of your app’s supported categories.

## Discussion

Call this method at launch time to register your app’s actionable notification types. This method registers all of your categories at once, replacing any previously registered categories with the new ones in the `categories` parameter. Typically, you call this method only once.

Each object in the `categories` parameter contains a string for identifying the notification’s type. It also contains one or more custom actions that the user may perform in response to notifications of that type. When the system displays an alert for a notification, it looks in the notification payload for one of the identifier strings from your category objects. If it finds one, it adds user-selectable buttons for each action associated with that category object. Tapping a button notifies your app of the selected action, without bringing your app to the foreground.

```swift
let center = UNUserNotificationCenter.current()
let category1 = UNNotificationCategory(identifier: "com.example.mynotification", actions: [], intentIdentifiers: [])
center.setNotificationCategories([category1])
center.removeAllPendingNotificationRequests()
```

## See Also

### Managing notification categories

- [- getNotificationCategoriesWithCompletionHandler:](<getnotificationcategories(completionhandler_).md>) — Fetches your app’s registered notification categories.
