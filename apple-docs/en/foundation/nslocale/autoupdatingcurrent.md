---
title: autoupdatingCurrent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslocale/autoupdatingcurrent
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/autoupdatingcurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/autoupdatingcurrent.json'
content_hash: 'sha256:8ae526fb3249bdc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# autoupdatingCurrent

<sub>Type Property</sub>

A locale which tracks the user’s current preferences.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var autoupdatingCurrent: Locale { get }
```

## Discussion

This value represents the locale currently used by the app, based on the following:

- The current system locale.
- Any app-specific locale choice made in the Settings app.
- The availability of the preferred locale in the app. For example, if the person using an app has set their device to use a Spanish-language locale, but the app only supports English, this value returns an English locale.

Use this property when you want a locale that always reflects the latest configuration settings. When the person using the app changes settings, reading properties from a locale instance obtained from this property provides the latest values. If you need to rely on a locale that does not change, use the locale given by the [currentLocale](current.md) property instead.

Although the locale obtained here automatically follows the latest region settings, it provides no indication when the settings change. To receive notification of locale changes, add your object as an observer of [NSCurrentLocaleDidChangeNotification](currentlocaledidchangenotification.md).

## See Also

### Getting the User’s Locale

- [currentLocale](current.md) — A locale that represents the user’s region settings at the time the property is read.
- [NSCurrentLocaleDidChangeNotification](currentlocaledidchangenotification.md) — A notification that indicates that the user’s locale changed.
- [systemLocale](system.md) — A locale representing the generic root values with little localization.
