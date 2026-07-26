---
title: currentLocaleDidChangeNotification
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslocale/currentlocaledidchangenotification
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/currentlocaledidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/currentlocaledidchangenotification.json'
content_hash: 'sha256:8b67e0aaeab18ae8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# currentLocaleDidChangeNotification

<sub>Type Property</sub>

A notification that indicates that the user’s locale changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let currentLocaleDidChangeNotification: NSNotification.Name
```

## Discussion

Register for this notification if your app displays content (dates, times, numbers, and so on) that is affected by the locale. Use the notification to trigger updates to your app’s interface.

## See Also

### Related Documentation

- [NSNotification](../nsnotification.md) — A container for information broadcast through a notification center to all registered observers.

### Getting the User’s Locale

- [autoupdatingCurrentLocale](autoupdatingcurrent.md) — A locale which tracks the user’s current preferences.
- [currentLocale](current.md) — A locale that represents the user’s region settings at the time the property is read.
- [systemLocale](system.md) — A locale representing the generic root values with little localization.
