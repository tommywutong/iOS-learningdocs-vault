---
title: repeats
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationtrigger/repeats
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationtrigger/repeats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationtrigger/repeats.json'
content_hash: 'sha256:2ab52e8d5e760692'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationTrigger](../unnotificationtrigger.md)

# repeats

<sub>Instance Property</sub>

A Boolean value indicating whether the system reschedules the notification after it’s delivered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var repeats: Bool { get }
```

## Discussion

When this property is [false](../../swift/false.md), the system delivers the notification only once. When this property is [true](../../swift/true.md), the system reschedules the notification request automatically, resulting in the system delivering the notification each time the trigger condition is met. To unschedule the notification request, use the methods of the [UNUserNotificationCenter](../unusernotificationcenter.md) to remove the notification request.
