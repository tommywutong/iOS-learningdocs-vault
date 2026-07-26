---
title: filterCriteria
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationcontent/filtercriteria
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcontent/filtercriteria'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcontent/filtercriteria.json'
content_hash: 'sha256:1ee0ac088985e087'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationContent](../unnotificationcontent.md)

# filterCriteria

<sub>Instance Property</sub>

The criteria the system evaluates to determine if it displays the notification in the current Focus.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var filterCriteria: String? { get }
```

## Discussion

For more information, see [SetFocusFilterIntent](../../appintents/setfocusfilterintent.md).

## See Also

### Reading system configuration

- [sound](sound.md) — The sound that plays when the system delivers the notification.
- [interruptionLevel](interruptionlevel.md) — The notification’s importance and required delivery timing.
- [UNNotificationInterruptionLevel](../unnotificationinterruptionlevel.md) — Constants that indicate the importance and delivery timing of a notification.
- [relevanceScore](relevancescore.md) — The score the system uses to determine if the notification is the summary’s featured notification.
