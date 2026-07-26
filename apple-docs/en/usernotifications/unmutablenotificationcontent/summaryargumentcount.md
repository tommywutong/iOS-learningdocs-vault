---
title: summaryArgumentCount
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+（15.0 起废弃）, iPadOS 12.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.14+, tvOS 12.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 5.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/usernotifications/unmutablenotificationcontent/summaryargumentcount
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/summaryargumentcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/summaryargumentcount.json'
content_hash: 'sha256:576c7a3147ff0cd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# summaryArgumentCount

<sub>Instance Property</sub>

The number the system adds to the notification summary when the notification represents multiple items.

> [!warning] Deprecated
> summaryArgumentCount is ignored

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var summaryArgumentCount: Int { get set }
```

## See Also

### Grouping notifications

- [threadIdentifier](threadidentifier.md) — The identifier that groups related notifications.
- [categoryIdentifier](categoryidentifier.md) — The identifier of the notification’s category.
- [summaryArgument](summaryargument.md) — The text the system adds to the notification summary to provide additional context. _(deprecated)_
