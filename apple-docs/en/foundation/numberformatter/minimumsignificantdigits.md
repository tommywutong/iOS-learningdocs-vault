---
title: minimumSignificantDigits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/minimumsignificantdigits
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/minimumsignificantdigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/minimumsignificantdigits.json'
content_hash: 'sha256:8e38518cd0aaa04f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# minimumSignificantDigits

<sub>Instance Property</sub>

The minimum number of significant digits for the number formatter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var minimumSignificantDigits: Int { get set }
```

## Discussion

You must set the [usesSignificantDigits](usessignificantdigits.md) property to [true](../../swift/true.md) in order for this property to affect formatting behavior. By default, the minimum number of significant digits is 1.

The following code demonstrates the effect of setting [minimumSignificantDigits](minimumsignificantdigits.md) when formatting various numbers:

```swift
var numberFormatter = NumberFormatter()
numberFormatter.usesSignificantDigits = true
numberFormatter.minimumSignificantDigits = 4

numberFormatter.string(from: 123) // 123.0
numberFormatter.string(from: 123.45) // 123.45
numberFormatter.string(from: 100.23) // 100.23
numberFormatter.string(from: 1.2300) // 1.230
numberFormatter.string(from: 0.000123) // 0.0001230
```

## See Also

### Configuring Significant Digits

- [usesSignificantDigits](usessignificantdigits.md) — A Boolean value indicating whether the formatter uses minimum and maximum significant digits when formatting numbers.
- [maximumSignificantDigits](maximumsignificantdigits.md) — The maximum number of significant digits for the number formatter.
