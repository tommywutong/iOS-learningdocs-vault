---
title: multiplier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/multiplier
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/multiplier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/multiplier.json'
content_hash: 'sha256:9f8f11218933d2f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# multiplier

<sub>Instance Property</sub>

The multiplier of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var multiplier: NSNumber? { get set }
```

## Discussion

A multiplier is a factor used in conversions between numbers and strings (that is, numbers as stored and numbers as displayed). When the input value is a string, the multiplier is used to divide, and when the input value is a number, the multiplier is used to multiply. These operations allow the formatted values to be different from the values that a program manipulates internally.

## See Also

### Configuring Numeric Formats

- [format](format.md) — The receiver’s format.
- [formattingContext](formattingcontext.md) — The capitalization formatting context used when formatting a number.
- [formatWidth](formatwidth.md) — The format width used by the receiver.
- [negativeFormat](negativeformat.md) — The format the receiver uses to display negative values.
- [positiveFormat](positiveformat.md) — The format the receiver uses to display positive values.
