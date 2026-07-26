---
title: filterCriteria
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unmutablenotificationcontent/filtercriteria
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/filtercriteria'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/filtercriteria.json'
content_hash: 'sha256:ece9caaaea730b7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# filterCriteria

<sub>Instance Property</sub>

The criteria the system evaluates to determine if it displays the notification in the current Focus.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var filterCriteria: String? { get set }
```

## Discussion

For more information, see [SetFocusFilterIntent](../../appintents/setfocusfilterintent.md).

## See Also

### Integrating with the system

- [sound](sound.md) — The sound that plays when the system delivers the notification.
- [interruptionLevel](interruptionlevel.md) — The notification’s importance and required delivery timing.
- [UNNotificationInterruptionLevel](../unnotificationinterruptionlevel.md) — Constants that indicate the importance and delivery timing of a notification.
- [relevanceScore](relevancescore.md) — The score the system uses to determine if the notification is the summary’s featured notification.
