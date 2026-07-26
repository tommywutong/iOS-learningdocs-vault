---
title: UNPushNotificationTrigger
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unpushnotificationtrigger
source_url: 'https://developer.apple.com/documentation/usernotifications/unpushnotificationtrigger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unpushnotificationtrigger.json'
content_hash: 'sha256:b0a279774f07b53a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNPushNotificationTrigger

<sub>Class</sub>

A trigger condition that indicates Apple Push Notification Service (APNs) has sent the notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UNPushNotificationTrigger
```

## Overview

You don’t create instances of this class yourself. The system creates [UNPushNotificationTrigger](unpushnotificationtrigger.md) objects and associates them with requests that originated from Apple Push Notification service. You encounter instances of this class when managing your app’s delivered notification requests, which store an object of this type in their [trigger](unnotificationrequest/trigger.md) property.

## Relationships

- **Inherits From**: [UNNotificationTrigger](unnotificationtrigger.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

### Triggers

- [UNCalendarNotificationTrigger](uncalendarnotificationtrigger.md) — A trigger condition that causes a notification the system delivers at a specific date and time.
- [UNTimeIntervalNotificationTrigger](untimeintervalnotificationtrigger.md) — A trigger condition that causes the system to deliver a notification after the amount of time you specify elapses.
- [UNLocationNotificationTrigger](unlocationnotificationtrigger.md) — A trigger condition that causes the system to deliver a notification when the user’s device enters or exits a geographic region you specify.
- [UNNotificationTrigger](unnotificationtrigger.md) — The common behavior for subclasses that trigger the delivery of a local or remote notification.
