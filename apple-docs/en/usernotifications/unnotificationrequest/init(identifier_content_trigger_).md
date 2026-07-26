---
title: 'init(identifier:content:trigger:)'
framework: User Notifications
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unnotificationrequest/init(identifier:content:trigger:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationrequest/init(identifier:content:trigger:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationrequest/init%28identifier%3Acontent%3Atrigger%3A%29.json'
content_hash: 'sha256:24d96565e75e247e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationRequest](../unnotificationrequest.md)

# init(identifier:content:trigger:)

<sub>Initializer</sub>

Creates a notification request object that you use to schedule a notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(identifier: String, content: UNNotificationContent, trigger: UNNotificationTrigger?)
```

## Parameters

- `identifier` — An identifier for the request; this parameter must not be `nil`. You can use this identifier to cancel the request if it’s still pending (see the [- removePendingNotificationRequestsWithIdentifiers:](<../unusernotificationcenter/removependingnotificationrequests(withidentifiers_).md>) method).

- `content` — The content of the notification. This parameter must not be `nil`.

- `trigger` — The condition that causes the system to deliver the notification. Specify `nil` to deliver the notification right away.

## Return Value

A new notification request object.

## Discussion

Use this method when you want to schedule the delivery of a local notification. This method creates the request object that you subsequently pass to the [- addNotificationRequest:withCompletionHandler:](<../unusernotificationcenter/add(__withcompletionhandler_).md>) method.

The system uses the `identifier` parameter to determine how to handle the request:

- **If you provide a unique identifier,** the system creates a new notification.
- **If the identifier matches a previously delivered notification,** the system alerts the user again, replaces the old notification with the new one, and places the new notification at the top of the list.
- **If the identifier matches a pending request,** the new request replaces the pending request.
