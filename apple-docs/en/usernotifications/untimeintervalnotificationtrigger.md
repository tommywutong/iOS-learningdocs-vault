---
title: UNTimeIntervalNotificationTrigger
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/untimeintervalnotificationtrigger
source_url: 'https://developer.apple.com/documentation/usernotifications/untimeintervalnotificationtrigger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/untimeintervalnotificationtrigger.json'
content_hash: 'sha256:fdd8074ed2c1f634'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNTimeIntervalNotificationTrigger

<sub>Class</sub>

A trigger condition that causes the system to deliver a notification after the amount of time you specify elapses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UNTimeIntervalNotificationTrigger
```

## Overview

Create a [UNTimeIntervalNotificationTrigger](untimeintervalnotificationtrigger.md) object when you want to schedule the delivery of a local notification after the number of seconds you specify elapses. You use this type of trigger to implement timers.

Listing 1 creates a trigger that delivers its notification one time after 30 minutes have elapsed.

Listing 1. Creating a trigger that fires in 30 minutes

**Swift**

```swift
// Fire in 30 minutes (60 seconds times 30)
let trigger = UNTimeIntervalNotificationTrigger(timeInterval: (30*60), repeats: false)
```

**Objective-C**

```objc
// Fire in 30 minutes (60 seconds times 30)
UNTimeIntervalNotificationTrigger* trigger = [UNTimeIntervalNotificationTrigger
                     triggerWithTimeInterval:(30*60) repeats: NO];
```

## Relationships

- **Inherits From**: [UNNotificationTrigger](unnotificationtrigger.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a Time Interval Trigger

- [+ triggerWithTimeInterval:repeats:](<untimeintervalnotificationtrigger/init(timeinterval_repeats_).md>) — Creates a time interval trigger using the time value parameter.

### Getting the Trigger Information

- [- nextTriggerDate](<untimeintervalnotificationtrigger/nexttriggerdate().md>) — The next date at which the trigger conditions are met.
- [timeInterval](untimeintervalnotificationtrigger/timeinterval.md) — The time interval to create the trigger.

## See Also

### Triggers

- [UNCalendarNotificationTrigger](uncalendarnotificationtrigger.md) — A trigger condition that causes a notification the system delivers at a specific date and time.
- [UNLocationNotificationTrigger](unlocationnotificationtrigger.md) — A trigger condition that causes the system to deliver a notification when the user’s device enters or exits a geographic region you specify.
- [UNPushNotificationTrigger](unpushnotificationtrigger.md) — A trigger condition that indicates Apple Push Notification Service (APNs) has sent the notification.
- [UNNotificationTrigger](unnotificationtrigger.md) — The common behavior for subclasses that trigger the delivery of a local or remote notification.
