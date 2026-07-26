---
title: UNNotificationTrigger
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationtrigger
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationtrigger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationtrigger.json'
content_hash: 'sha256:212804ff619e1e75'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationTrigger

<sub>Class</sub>

The common behavior for subclasses that trigger the delivery of a local or remote notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UNNotificationTrigger
```

## Overview

The [UNNotificationTrigger](unnotificationtrigger.md) class is an abstract class for representing an event that triggers the delivery of a notification. You don’t create instances of this class directly. Instead, you instantiate the concrete subclass that defines the trigger condition you want for your notification. You then assign the resulting object to the [UNNotificationRequest](unnotificationrequest.md) object that you use to schedule your notification.

Concrete trigger classes include the following:

- [UNTimeIntervalNotificationTrigger](untimeintervalnotificationtrigger.md)
- [UNCalendarNotificationTrigger](uncalendarnotificationtrigger.md)
- [UNLocationNotificationTrigger](unlocationnotificationtrigger.md)
- [UNPushNotificationTrigger](unpushnotificationtrigger.md)

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UNCalendarNotificationTrigger](uncalendarnotificationtrigger.md), [UNLocationNotificationTrigger](unlocationnotificationtrigger.md), [UNPushNotificationTrigger](unpushnotificationtrigger.md), [UNTimeIntervalNotificationTrigger](untimeintervalnotificationtrigger.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Configuring the Trigger’s Behavior

- [repeats](unnotificationtrigger/repeats.md) — A Boolean value indicating whether the system reschedules the notification after it’s delivered.

### Initializers

- [init(coder:)](<unnotificationtrigger/init(coder_).md>)

## See Also

### Triggers

- [UNCalendarNotificationTrigger](uncalendarnotificationtrigger.md) — A trigger condition that causes a notification the system delivers at a specific date and time.
- [UNTimeIntervalNotificationTrigger](untimeintervalnotificationtrigger.md) — A trigger condition that causes the system to deliver a notification after the amount of time you specify elapses.
- [UNLocationNotificationTrigger](unlocationnotificationtrigger.md) — A trigger condition that causes the system to deliver a notification when the user’s device enters or exits a geographic region you specify.
- [UNPushNotificationTrigger](unpushnotificationtrigger.md) — A trigger condition that indicates Apple Push Notification Service (APNs) has sent the notification.
