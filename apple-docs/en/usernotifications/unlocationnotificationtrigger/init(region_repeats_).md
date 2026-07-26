---
title: 'init(region:repeats:)'
framework: User Notifications
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unlocationnotificationtrigger/init(region:repeats:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unlocationnotificationtrigger/init(region:repeats:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unlocationnotificationtrigger/init%28region%3Arepeats%3A%29.json'
content_hash: 'sha256:54ac1f3b46082a8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNLocationNotificationTrigger](../unlocationnotificationtrigger.md)

# init(region:repeats:)

<sub>Initializer</sub>

Creates a location trigger using the region parameter.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
convenience init(region: CLRegion, repeats: Bool)
```

## Parameters

- `region` — The geographic region that must be entered or exited. Use the region object to specify whether to deliver notifications on entry, on exit, or both.

- `repeats` — Specify [false](../../swift/false.md) to deliver the notification one time. Specify [true](../../swift/true.md) to reschedule the notification request each time the system delivers the notification.

## Return Value

A new location trigger object with the specified region.

## Discussion

If you specify `true` for the `repeats` parameter, you must explicitly remove the notification request to stop the delivery of the associated notification. Use the methods of [UNUserNotificationCenter](../unusernotificationcenter.md) to remove notification requests that are no longer needed.
