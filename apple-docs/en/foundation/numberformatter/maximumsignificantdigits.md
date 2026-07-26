---
title: maximumSignificantDigits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/maximumsignificantdigits
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/maximumsignificantdigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/maximumsignificantdigits.json'
content_hash: 'sha256:794a26e37ea0a434'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# maximumSignificantDigits

<sub>Instance Property</sub>

The maximum number of significant digits for the number formatter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var maximumSignificantDigits: Int { get set }
```

## Discussion

You must set the [usesSignificantDigits](usessignificantdigits.md) property to [true](../../swift/true.md) in order for this property to affect formatting behavior.  By default, the maximum number of significant digits is 6. Values less than 1 are ignored.

The following code demonstrates the effect of setting [maximumSignificantDigits](maximumsignificantdigits.md) when formatting various numbers:

```swift
var numberFormatter = NumberFormatter()
numberFormatter.usesSignificantDigits = true
numberFormatter.maximumSignificantDigits = 4

numberFormatter.string(from: 12345) // 12340
numberFormatter.string(from: 123.456) // 123.5
numberFormatter.string(from: 100.234) // 100.2
numberFormatter.string(from: 1.230) // 1.23
numberFormatter.string(from: 0.00012345) // 0.0001234
```

## See Also

### Configuring Significant Digits

- [usesSignificantDigits](usessignificantdigits.md) — A Boolean value indicating whether the formatter uses minimum and maximum significant digits when formatting numbers.
- [minimumSignificantDigits](minimumsignificantdigits.md) — The minimum number of significant digits for the number formatter.
