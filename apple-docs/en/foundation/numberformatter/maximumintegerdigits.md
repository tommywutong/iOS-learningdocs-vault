---
title: maximumIntegerDigits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/maximumintegerdigits
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/maximumintegerdigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/maximumintegerdigits.json'
content_hash: 'sha256:cc11fcebdff2253e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# maximumIntegerDigits

<sub>Instance Property</sub>

The maximum number of digits before the decimal separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var maximumIntegerDigits: Int { get set }
```

## Discussion

By default, this property is set to `42`.

The following code demonstrates the effect of setting [maximumIntegerDigits](maximumintegerdigits.md) when formatting a number:

```swift
var numberFormatter = NumberFormatter()

numberFormatter.maximumIntegerDigits = 42 // default
numberFormatter.string(from: 12345) // 12345

numberFormatter.maximumIntegerDigits = 3
numberFormatter.string(from: 12345) // 345
```

## See Also

### Configuring Integer and Fraction Digits

- [minimumIntegerDigits](minimumintegerdigits.md) — The minimum number of digits before the decimal separator.
- [minimumFractionDigits](minimumfractiondigits.md) — The minimum number of digits after the decimal separator.
- [maximumFractionDigits](maximumfractiondigits.md) — The maximum number of digits after the decimal separator.
