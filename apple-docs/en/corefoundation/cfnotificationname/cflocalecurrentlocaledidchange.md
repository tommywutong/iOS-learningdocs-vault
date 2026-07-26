---
title: cfLocaleCurrentLocaleDidChange
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnotificationname/cflocalecurrentlocaledidchange
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationname/cflocalecurrentlocaledidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationname/cflocalecurrentlocaledidchange.json'
content_hash: 'sha256:d63d9cba1ee180c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFNotificationName](../cfnotificationname.md)

# cfLocaleCurrentLocaleDidChange

<sub>Type Property</sub>

Identifier for the notification sent if the current locale changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let cfLocaleCurrentLocaleDidChange: CFNotificationName!
```

## Discussion

This is a local notification posted when the user changes locale information in the System Preferences panel. Keep in mind that there is no order in how notifications are delivered to observers; frameworks or other parts of your code may also be observing this notification to take their own actions, and these may not have occurred at the time you receive the notification.

There is no object or user info for this notification.
