---
title: 'init(dateMatching:repeats:)'
framework: User Notifications
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/uncalendarnotificationtrigger/init(datematching:repeats:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger/init(datematching:repeats:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/uncalendarnotificationtrigger/init%28datematching%3Arepeats%3A%29.json'
content_hash: 'sha256:0894995506b0fffd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNCalendarNotificationTrigger](../uncalendarnotificationtrigger.md)

# init(dateMatching:repeats:)

<sub>Initializer</sub>

Creates a calendar trigger using the date components parameter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(dateMatching dateComponents: DateComponents, repeats: Bool)
```

## Parameters

- `dateComponents` — The temporal information to use when constructing the trigger. Provide only the date components that are relevant for your trigger.

- `repeats` — Specify [false](../../swift/false.md) to deliver the notification one time. Specify [true](../../swift/true.md) to reschedule the notification request each time the system delivers the notification.

## Return Value

A new calendar trigger based on the specified temporal information.

## Discussion

If you specify `true` for the `repeats` parameter, you must explicitly remove the notification request to stop the delivery of the associated notification. Use the methods of [UNUserNotificationCenter](../unusernotificationcenter.md) to remove notification requests that are no longer needed.
