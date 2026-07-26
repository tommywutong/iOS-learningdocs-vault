---
title: NSUserNotificationCenter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.8+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsusernotificationcenter
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationcenter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationcenter.json'
content_hash: 'sha256:be11c8560a57c269'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUserNotificationCenter

<sub>Class</sub>

An object that delivers notifications from apps to the user.

> [!warning] Deprecated
> Use the [User Notifications](../usernotifications.md) framework instead.

<sub>macOS</sub>

```swift
class NSUserNotificationCenter
```

## Overview

When a user notification’s delivery date has been reached, or it’s manually delivered, the notification center may display the notification to the user. The user notification center reserves the right to decide if a delivered user notification is presented to the user. For example, it may suppress the notification if the application is already frontmost (the delegate can override this action). The application can check the result of this decision by examining the [presented](nsusernotification/ispresented.md) property of a delivered user notification.

[NSUserNotification](nsusernotification.md) instances the `NSUserNotificationCenter` are tracking will be in one of two states: scheduled or delivered. A scheduled user notification has a [deliveryDate](nsusernotification/deliverydate.md). On that delivery date, the notification will move from being scheduled to being delivered. Note that the user notification may be displayed later than the delivery date depending on many factors.

A delivered user notification has an [actualDeliveryDate](nsusernotification/actualdeliverydate.md). That’s the date when it moved from being scheduled to delivered, or when it was manually delivered using the [- deliverNotification:](<nsusernotificationcenter/deliver(__).md>) method.

The application and the user notification center are both ultimately subject to the user’s preferences. If the user decides to hide all alerts from your application, the `presented` property will still behave as above, but the user won’t see any animation or hear any sound.

The [NSUserNotificationCenterDelegate](nsusernotificationcenterdelegate.md) provides more information about the delivered user notification and allows forcing the display of a user notification even if the application is frontmost.

> [!note] Note
> It the user wakes more than 15 minutes after a scheduled notification is scheduled to fire, it’s discarded. If the notification repeats with an interval less than 15 minutes, then it expires in 1 minute. Expired notifications are just discarded, unless they repeat, in which case, they stay in the scheduled list and just fire again later.

> [!important] Important
> Many of the NSUserNotificationCenter class’s methods involve talking to a server process, so calling them repeatedly can have a negative effect on performance.

### Threading Information

The `NSUserNotificationCenter` class and the [NSUserNotification](nsusernotification.md) class are both thread safe.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating the Default User Notification Center

- [defaultUserNotificationCenter](nsusernotificationcenter/default.md) — Returns the default user notification center. _(deprecated)_

### Managing the Scheduled Notification Queue

- [- scheduleNotification:](<nsusernotificationcenter/schedulenotification(__).md>) — Schedules the specified user notification. _(deprecated)_
- [scheduledNotifications](nsusernotificationcenter/schedulednotifications.md) — Specifies an array of scheduled user notifications that have not yet been delivered. _(deprecated)_
- [- removeScheduledNotification:](<nsusernotificationcenter/removeschedulednotification(__).md>) — Removes the specified user notification for the scheduled notifications. _(deprecated)_

### Managing the Delivered Notifications

- [- deliverNotification:](<nsusernotificationcenter/deliver(__).md>) — Deliver the specified user notification. _(deprecated)_
- [deliveredNotifications](nsusernotificationcenter/deliverednotifications.md) — An array of all user notifications delivered to the notification center. _(deprecated)_
- [- removeDeliveredNotification:](<nsusernotificationcenter/removedeliverednotification(__).md>) — Remove a delivered user notification from the user notification center. _(deprecated)_
- [- removeAllDeliveredNotifications](<nsusernotificationcenter/removealldeliverednotifications().md>) — Remove all delivered user notifications from the user notification center. _(deprecated)_

### Getting and Setting the Delegate

- [delegate](nsusernotificationcenter/delegate.md) — Specifies the notification center delegate. _(deprecated)_

## See Also

### User Notifications

- [NSUserNotification](nsusernotification.md) — A notification that can be scheduled for display in the notification center. _(deprecated)_
- [NSUserNotificationAction](nsusernotificationaction.md) — An action that the user can take in response to receiving a notification. _(deprecated)_
- [NSUserNotificationCenterDelegate](nsusernotificationcenterdelegate.md) — An interface that enables customizing the behavior of the default notification center.
