---
title: localizesFormat
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/localizesformat
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/localizesformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/localizesformat.json'
content_hash: 'sha256:dd8d5ba582dd5c16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# localizesFormat

<sub>Instance Property</sub>

Determines whether the dollar sign character (`$`), decimal separator character (`.`), and thousand separator character (`,`) are converted to appropriately localized characters as specified by the user’s localization preference.

<sub>macOS</sub>

```swift
var localizesFormat: Bool { get set }
```

## Discussion

While the currency-symbol part of this feature may be useful in certain types of applications, it’s probably more likely that you would tie a particular application to a particular currency (that is, that you would “hard-code” the currency symbol and separators instead of having them dynamically change based on the user’s configuration). The reason for this, of course, is that `NSNumberFormatter` doesn’t perform currency conversions, it just formats numeric data. You wouldn’t want one user interpreting the value `"56324"` as US currency and another user who’s accessing the same data interpreting it as Japanese currency, simply based on each user’s localization preferences.

## See Also

### Managing Localization of Numbers

- [locale](locale.md) — The locale of the receiver.
