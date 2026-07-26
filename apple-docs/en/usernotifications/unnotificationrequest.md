---
title: UNNotificationRequest
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationrequest
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationrequest.json'
content_hash: 'sha256:5c0073c17ae31559'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationRequest

<sub>Class</sub>

A request to schedule a local notification, which includes the content of the notification and the trigger conditions for delivery.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UNNotificationRequest
```

## Overview

Create a [UNNotificationRequest](unnotificationrequest.md) object when you want to schedule the delivery of a local notification. A notification request object contains a [UNNotificationContent](unnotificationcontent.md) object with the payload and the [UNNotificationTrigger](unnotificationtrigger.md) object with the conditions that trigger the delivery of the notification. To schedule the delivery of your notification, pass your request object to the [- addNotificationRequest:withCompletionHandler:](<unusernotificationcenter/add(__withcompletionhandler_).md>) method of the shared user notification center object.

After scheduling a request, you interact with `UNNotificationRequest` objects in the following ways:

- View your app’s pending notifications by calling the [- getPendingNotificationRequestsWithCompletionHandler:](<unusernotificationcenter/getpendingnotificationrequests(completionhandler_).md>) method of your shared user notification center object.
- When the system delivers a notification to your app, the provided [UNNotification](unnotification.md) object contains a `UNNotificationRequest` object that you can inspect to get the notification details.
- Use the request’s [identifier](unnotificationrequest/identifier.md) to remove delivered notifications from Notification Center.

When receiving a local or remote notification, use the provided [UNNotificationRequest](unnotificationrequest.md) object to fetch details about the notification.

```swift
// Create a content object with the message to convey.
let content = UNMutableNotificationContent()
content.title = "Lunch time"
content.body = "Food is cooked... let's eat!"
// Create a notification trigger for 60 seconds in the future.
let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 60.0, repeats: false)
// Create the request with the content and the trigger.
let request = UNNotificationRequest(identifier: "com.example.mynotification", content: content, trigger: trigger)
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a Notification Request

- [+ requestWithIdentifier:content:trigger:](<unnotificationrequest/init(identifier_content_trigger_).md>) — Creates a notification request object that you use to schedule a notification.

### Getting the Request Details

- [identifier](unnotificationrequest/identifier.md) — The unique identifier for this notification request.
- [content](unnotificationrequest/content.md) — The content associated with the notification.
- [trigger](unnotificationrequest/trigger.md) — The conditions that trigger the delivery of the notification.

### Initializers

- [init(coder:)](<unnotificationrequest/init(coder_).md>)

## See Also

### Notification requests

- [Scheduling a notification locally from your app](scheduling-a-notification-locally-from-your-app.md) — Create and schedule notifications from your app when you want to get the user’s attention.
- [UNNotification](unnotification.md) — The data for a local or remote notification the system delivers to your app.
