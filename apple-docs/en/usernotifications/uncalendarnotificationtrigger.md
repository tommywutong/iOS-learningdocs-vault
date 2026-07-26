---
title: UNCalendarNotificationTrigger
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/uncalendarnotificationtrigger
source_url: 'https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/uncalendarnotificationtrigger.json'
content_hash: 'sha256:e3ba11ec4fa48438'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNCalendarNotificationTrigger

<sub>Class</sub>

A trigger condition that causes a notification the system delivers at a specific date and time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UNCalendarNotificationTrigger
```

## Overview

Create a [UNCalendarNotificationTrigger](uncalendarnotificationtrigger.md) object when you want to schedule the delivery of a local notification at the date and time you specify. You use an [NSDateComponents](../foundation/nsdatecomponents.md) object to specify only the time values that you want the system to use to determine the matching date and time.

Listing 1 creates a trigger that delivers its notification every morning at 8:30. The repeating behavior is achieved by specifying `true` for the `repeats` parameter when creating the trigger.

Listing 1. Creating a trigger that repeats at a specific time

**Swift**

```swift
var date = DateComponents()
date.hour = 8
date.minute = 30 
let trigger = UNCalendarNotificationTrigger(dateMatching: date, repeats: true)
```

**Objective-C**

```objc
NSDateComponents* date = [[NSDateComponents alloc] init];
date.hour = 8;
date.minute = 30; 
UNCalendarNotificationTrigger* trigger = [UNCalendarNotificationTrigger
                     triggerWithDateMatchingComponents:date repeats:YES];
```

## Relationships

- **Inherits From**: [UNNotificationTrigger](unnotificationtrigger.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a Calendar Trigger

- [+ triggerWithDateMatchingComponents:repeats:](<uncalendarnotificationtrigger/init(datematching_repeats_).md>) — Creates a calendar trigger using the date components parameter.

### Getting the Trigger Information

- [- nextTriggerDate](<uncalendarnotificationtrigger/nexttriggerdate().md>) — The next date at which the trigger conditions are met.
- [dateComponents](uncalendarnotificationtrigger/datecomponents.md) — The date components to construct this object.

### Initializers

- [init(dateMatchingComponents:repeats:)](<uncalendarnotificationtrigger/init(datematchingcomponents_repeats_).md>)

## See Also

### Triggers

- [UNTimeIntervalNotificationTrigger](untimeintervalnotificationtrigger.md) — A trigger condition that causes the system to deliver a notification after the amount of time you specify elapses.
- [UNLocationNotificationTrigger](unlocationnotificationtrigger.md) — A trigger condition that causes the system to deliver a notification when the user’s device enters or exits a geographic region you specify.
- [UNPushNotificationTrigger](unpushnotificationtrigger.md) — A trigger condition that indicates Apple Push Notification Service (APNs) has sent the notification.
- [UNNotificationTrigger](unnotificationtrigger.md) — The common behavior for subclasses that trigger the delivery of a local or remote notification.
