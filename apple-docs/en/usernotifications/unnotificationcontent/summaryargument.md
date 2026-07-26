---
title: summaryArgument
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+（15.0 起废弃）, iPadOS 12.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.14+, tvOS 12.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 5.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/usernotifications/unnotificationcontent/summaryargument
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcontent/summaryargument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcontent/summaryargument.json'
content_hash: 'sha256:156f98b9d58d00b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationContent](../unnotificationcontent.md)

# summaryArgument

<sub>Instance Property</sub>

The text the system adds to the notification summary to provide additional context.

> [!warning] Deprecated
> summaryArgument is ignored

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var summaryArgument: String { get }
```

## See Also

### Retrieving group information

- [threadIdentifier](threadidentifier.md) — The identifier that groups related notifications.
- [categoryIdentifier](categoryidentifier.md) — The identifier of the notification’s category.
- [summaryArgumentCount](summaryargumentcount.md) — The number the system adds to the notification summary when the notification represents multiple items. _(deprecated)_
