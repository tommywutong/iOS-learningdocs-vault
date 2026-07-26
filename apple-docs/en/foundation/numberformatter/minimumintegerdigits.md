---
title: minimumIntegerDigits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/minimumintegerdigits
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/minimumintegerdigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/minimumintegerdigits.json'
content_hash: 'sha256:56d2984f362108a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# minimumIntegerDigits

<sub>Instance Property</sub>

The minimum number of digits before the decimal separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var minimumIntegerDigits: Int { get set }
```

## Discussion

By default, this property is set to `0`.

The following code demonstrates the effect of setting [minimumIntegerDigits](minimumintegerdigits.md) when formatting a number:

```swift
var numberFormatter = NumberFormatter()

numberFormatter.minimumIntegerDigits = 0 // default
numberFormatter.string(from: 123) // 123

numberFormatter.minimumIntegerDigits = 5
numberFormatter.string(from: 123) // 00123
```

## See Also

### Configuring Integer and Fraction Digits

- [maximumIntegerDigits](maximumintegerdigits.md) — The maximum number of digits before the decimal separator.
- [minimumFractionDigits](minimumfractiondigits.md) — The minimum number of digits after the decimal separator.
- [maximumFractionDigits](maximumfractiondigits.md) — The maximum number of digits after the decimal separator.
