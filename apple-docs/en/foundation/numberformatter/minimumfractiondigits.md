---
title: minimumFractionDigits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/minimumfractiondigits
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/minimumfractiondigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/minimumfractiondigits.json'
content_hash: 'sha256:874cd7d761751479'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# minimumFractionDigits

<sub>Instance Property</sub>

The minimum number of digits after the decimal separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var minimumFractionDigits: Int { get set }
```

## Discussion

By default, this property is set to `0`.

The following code demonstrates the effect of setting [minimumFractionDigits](minimumfractiondigits.md) when formatting a number:

```swift
var numberFormatter = NumberFormatter()
numberFormatter.minimumFractionDigits = 0 // default
numberFormatter.string(from: 123.456) // 123
numberFormatter.minimumFractionDigits = 5
numberFormatter.string(from: 123.456) // 123.45600
```

## See Also

### Configuring Integer and Fraction Digits

- [minimumIntegerDigits](minimumintegerdigits.md) — The minimum number of digits before the decimal separator.
- [maximumIntegerDigits](maximumintegerdigits.md) — The maximum number of digits before the decimal separator.
- [maximumFractionDigits](maximumfractiondigits.md) — The maximum number of digits after the decimal separator.
