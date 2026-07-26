---
title: usesSignificantDigits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/usessignificantdigits
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/usessignificantdigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/usessignificantdigits.json'
content_hash: 'sha256:603f9b436ebd9e4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# usesSignificantDigits

<sub>Instance Property</sub>

A Boolean value indicating whether the formatter uses minimum and maximum significant digits when formatting numbers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var usesSignificantDigits: Bool { get set }
```

## Discussion

The [NumberFormatter](../numberformatter.md) class has two ways of determining how many digits to represent:_ _using integer and fraction digits and using significant digits.

When this property is set to [false](../../swift/false.md), numbers are formatted according to whether you want them formatted as fractions or as integers. For more information, see Configuring Integer and Fraction Digits. This property is [false](../../swift/false.md) by default.

Set this property to [true](../../swift/true.md) to format numbers according to the significant digits configuration specified by the [minimumSignificantDigits](minimumsignificantdigits.md) and [maximumSignificantDigits](maximumsignificantdigits.md) properties. By default, the minimum number of significant digits is 1, and the maximum number of significant digits is 6.

> [!note] Note
> When a number formatter is configured to use significant digits, it ignores any minimum or maximum values used to set integer or fraction digits.

The following code demonstrates the effect of configuring [usesSignificantDigits](usessignificantdigits.md) when formatting various numbers:

```swift
var numberFormatter = NumberFormatter()

// Using significant digits
numberFormatter.usesSignificantDigits = true
numberFormatter.string(from: 12345678) // 12345700
numberFormatter.string(from: 1234.5678) // 1234.57
numberFormatter.string(from: 100.2345678) // 100.235
numberFormatter.string(from: 1.230000) // 1.23
numberFormatter.string(from: 0.00000123) // 0.00000123

// Using integer and fraction digits
numberFormatter.usesSignificantDigits = false
numberFormatter.string(from: 12345678) // 12345678
numberFormatter.string(from: 1234.5678) // 1235
numberFormatter.string(from: 100.2345678) // 100
numberFormatter.string(from: 1.230000) // 1
numberFormatter.string(from: 0.00000123) // 0
```

## See Also

### Configuring Significant Digits

- [minimumSignificantDigits](minimumsignificantdigits.md) — The minimum number of significant digits for the number formatter.
- [maximumSignificantDigits](maximumsignificantdigits.md) — The maximum number of significant digits for the number formatter.
