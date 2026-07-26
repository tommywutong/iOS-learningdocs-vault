---
title: autoupdatingCurrent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/autoupdatingcurrent
source_url: 'https://developer.apple.com/documentation/foundation/locale/autoupdatingcurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/autoupdatingcurrent.json'
content_hash: 'sha256:f5abb9e69df84c48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# autoupdatingCurrent

<sub>Type Property</sub>

A locale which tracks the user’s current preferences.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var autoupdatingCurrent: Locale { get }
```

## Discussion

This value represents the locale currently used by the app, based on the following:

- The current system locale.
- Any app-specific locale choice made in the Settings app.
- The availability of the preferred locale in the app. For example, if the person using an app has set their device to use a Spanish-language locale, but the app only supports English, this value returns an English locale.

Use this property when you want a locale that always reflects the latest configuration settings. When the person using the app changes settings, reading properties from a locale instance obtained from this property provides the latest values. If you need to rely on a locale that does not change, use the locale given by the [current](current.md) property instead.

Although the locale obtained here automatically follows the latest language and region settings, it provides no indication when the settings change. To receive notification of locale changes in Swift, add an observer for [CurrentLocaleDidChangeMessage](currentlocaledidchangemessage.md). In Objective-C, you can add your object as an observer of `NSCurrentLocaleDidChangeNotification`.

If mutated, this `Locale` no longer tracks the user’s preferences.

> [!note] Note
> The autoupdating `Locale` only compares as equal to another autoupdating `Locale`.

## See Also

### Getting the user’s locale

- [current](current.md) — A locale representing the user’s region settings at the time the property is read.
