---
title: current
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/current
source_url: 'https://developer.apple.com/documentation/foundation/locale/current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/current.json'
content_hash: 'sha256:c6b329b97535b4c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# current

<sub>Type Property</sub>

A locale representing the user’s region settings at the time the property is read.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var current: Locale { get }
```

## Discussion

This value represents the locale currently used by the app, based on the following:

- The current system locale.
- Any app-specific locale choice made in the Settings app.
- The availability of the preferred locale in the app. For example, if the person using an app has set their device to use a Spanish-language locale, but the app only supports English, this value returns an English locale.

Use this property when you need to rely on a consistent locale. A locale instance obtained this way does not change even when the person using the device changes language or region settings. If you want a locale instance that always reflects the current configuration, use the one provided by the [autoupdatingCurrent](autoupdatingcurrent.md) property instead.

To receive notification of locale changes in Swift, add an observer for [CurrentLocaleDidChangeMessage](currentlocaledidchangemessage.md). In Objective-C, you can add your object as an observer of [NSCurrentLocaleDidChangeNotification](../nslocale/currentlocaledidchangenotification.md).

## See Also

### Getting the user’s locale

- [autoupdatingCurrent](autoupdatingcurrent.md) — A locale which tracks the user’s current preferences.
