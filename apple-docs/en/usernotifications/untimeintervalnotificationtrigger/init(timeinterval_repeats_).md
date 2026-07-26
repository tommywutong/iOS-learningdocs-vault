---
title: 'init(timeInterval:repeats:)'
framework: User Notifications
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/untimeintervalnotificationtrigger/init(timeinterval:repeats:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/untimeintervalnotificationtrigger/init(timeinterval:repeats:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/untimeintervalnotificationtrigger/init%28timeinterval%3Arepeats%3A%29.json'
content_hash: 'sha256:5e004b38e2942bcc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNTimeIntervalNotificationTrigger](../untimeintervalnotificationtrigger.md)

# init(timeInterval:repeats:)

<sub>Initializer</sub>

Creates a time interval trigger using the time value parameter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(timeInterval: TimeInterval, repeats: Bool)
```

## Parameters

- `timeInterval` — The time (in seconds) that must elapse from the current time before the trigger fires. This value must be greater than zero.

- `repeats` — Specify [false](../../swift/false.md) to deliver the notification one time. Specify [true](../../swift/true.md) to reschedule the notification request each time the system delivers the notification. If this parameter is [true](../../swift/true.md), the value in the `timeInterval` parameter must be 60 seconds or greater.

## Return Value

A new time interval trigger based on the specified temporal information.

## Discussion

If you specify `true` for the `repeats` parameter, you must explicitly remove the notification request to stop the delivery of the associated notification. Use the methods of [UNUserNotificationCenter](../unusernotificationcenter.md) to remove notification requests that are no longer needed.
