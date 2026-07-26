---
title: locale
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/locale
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/locale.json'
content_hash: 'sha256:774dba9ce68011c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# locale

<sub>Instance Property</sub>

The locale of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale! { get set }
```

## Discussion

The locale determines the default values for many formatter attributes, such as ISO region and language codes, currency code, calendar, system of measurement, and decimal separator.

## See Also

### Managing Localization of Numbers

- [localizesFormat](localizesformat.md) — Determines whether the dollar sign character (`$`), decimal separator character (`.`), and thousand separator character (`,`) are converted to appropriately localized characters as specified by the user’s localization preference.
