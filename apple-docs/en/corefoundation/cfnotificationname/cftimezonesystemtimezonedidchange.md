---
title: cfTimeZoneSystemTimeZoneDidChange
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnotificationname/cftimezonesystemtimezonedidchange
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationname/cftimezonesystemtimezonedidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationname/cftimezonesystemtimezonedidchange.json'
content_hash: 'sha256:a24dd87e8fd81203'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFNotificationName](../cfnotificationname.md)

# cfTimeZoneSystemTimeZoneDidChange

<sub>Type Property</sub>

Name of the notification posted when the system time zone changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let cfTimeZoneSystemTimeZoneDidChange: CFNotificationName!
```

## Discussion

The object of the notification is the previous system time zone object. This notification carries no user info.

Keep in mind that there is no order in how notifications are delivered to observers; frameworks or other parts of your code may also be observing this notification to take their own actions, and these may not have occurred by the time you receive the notification.
