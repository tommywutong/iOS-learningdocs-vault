---
title: UNUserNotificationCenter
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unusernotificationcenter
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter.json'
content_hash: 'sha256:4861d906228bf0ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNUserNotificationCenter

<sub>Class</sub>

The central object for managing notification-related activities for your app or app extension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UNUserNotificationCenter
```

## Overview

Use the shared [UNUserNotificationCenter](unusernotificationcenter.md) object to manage all notification-related behaviors in your app or app extension. Specifically, use this object to do the following:

- Request authorization to interact with the user through alerts, sounds, and icon badges. See [Asking permission to use notifications](asking-permission-to-use-notifications.md).
- Declare the notification types that your app supports and the custom actions the user may perform when the system delivers those notifications. See [Declaring your actionable notification types](declaring-your-actionable-notification-types.md).
- Schedule the delivery of notifications from your app. See [Scheduling a notification locally from your app](scheduling-a-notification-locally-from-your-app.md).
- Process the payloads from remote notifications the system delivers by Apple Push Notification service (APNs). See [Handling notifications and notification-related actions](handling-notifications-and-notification-related-actions.md).
- Manage the already delivered notifications the system displays in Notification Center. See Managing Delivered Notifications.
- Handle user-selected actions associated with your custom notification types. See [Handling notifications and notification-related actions](handling-notifications-and-notification-related-actions.md).
- Get the notification-related settings for your app. See Managing Settings and Authorization.

To handle incoming notifications and notification-related actions, create an object that adopts the [UNUserNotificationCenterDelegate](unusernotificationcenterdelegate.md) protocol and assign it to the [delegate](unusernotificationcenter/delegate.md) property. Always assign an object to the [delegate](unusernotificationcenter/delegate.md) property before performing any tasks that might interact with that delegate.

You may use the shared user notification center object simultaneously from any of your app’s threads. The object processes requests serially in the order that the system initiates them.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Managing the notification center

- [+ currentNotificationCenter](<unusernotificationcenter/current().md>) — Returns your app’s notification center.
- [- getNotificationSettingsWithCompletionHandler:](<unusernotificationcenter/getnotificationsettings(completionhandler_).md>) — Retrieves the authorization and feature-related settings for your app.
- [- setBadgeCount:withCompletionHandler:](<unusernotificationcenter/setbadgecount(__withcompletionhandler_).md>) — Updates the badge count for your app’s icon.

### Requesting authorization

- [- requestAuthorizationWithOptions:completionHandler:](<unusernotificationcenter/requestauthorization(options_completionhandler_).md>) — Requests a person’s authorization to allow local and remote notifications for your app.
- [UNAuthorizationOptions](unauthorizationoptions.md) — Options that determine the authorized features of local and remote notifications.

### Processing received notifications

- [delegate](unusernotificationcenter/delegate.md) — The notification center’s delegate.
- [UNUserNotificationCenterDelegate](unusernotificationcenterdelegate.md) — An interface for processing incoming notifications and responding to notification actions.
- [supportsContentExtensions](unusernotificationcenter/supportscontentextensions.md) — A Boolean value that indicates whether the device supports notification content extensions.

### Scheduling notifications

- [- addNotificationRequest:withCompletionHandler:](<unusernotificationcenter/add(__withcompletionhandler_).md>) — Schedules the delivery of a local notification.
- [- getPendingNotificationRequestsWithCompletionHandler:](<unusernotificationcenter/getpendingnotificationrequests(completionhandler_).md>) — Fetches all of your app’s local notifications that are pending delivery.
- [- removePendingNotificationRequestsWithIdentifiers:](<unusernotificationcenter/removependingnotificationrequests(withidentifiers_).md>) — Removes your app’s local notifications that are pending and match the specified identifiers.
- [- removeAllPendingNotificationRequests](<unusernotificationcenter/removeallpendingnotificationrequests().md>) — Removes all of your app’s pending local notifications.

### Removing delivered notifications

- [- getDeliveredNotificationsWithCompletionHandler:](<unusernotificationcenter/getdeliverednotifications(completionhandler_).md>) — Fetches all of your app’s delivered notifications that are still present in Notification Center.
- [- removeDeliveredNotificationsWithIdentifiers:](<unusernotificationcenter/removedeliverednotifications(withidentifiers_).md>) — Removes your app’s notifications from Notification Center that match the specified identifiers.
- [- removeAllDeliveredNotifications](<unusernotificationcenter/removealldeliverednotifications().md>) — Removes all of your app’s delivered notifications from Notification Center.

### Managing notification categories

- [- setNotificationCategories:](<unusernotificationcenter/setnotificationcategories(__).md>) — Registers the notification categories that your app supports.
- [- getNotificationCategoriesWithCompletionHandler:](<unusernotificationcenter/getnotificationcategories(completionhandler_).md>) — Fetches your app’s registered notification categories.

### Handling errors

- [UNError](unerror.md) — An object that represents a notification error.
- [Code](unerror/code.md) — Constants that identify notification errors.
- [UNErrorDomain](unerrordomain.md) — The error domain for notifications.

## See Also

### Notification management

- [UNUserNotificationCenterDelegate](unusernotificationcenterdelegate.md) — An interface for processing incoming notifications and responding to notification actions.
- [UNNotificationSettings](unnotificationsettings.md) — The object for managing notification-related settings and the authorization status of your app.
