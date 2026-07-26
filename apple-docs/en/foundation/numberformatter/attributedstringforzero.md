---
title: attributedStringForZero
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/attributedstringforzero
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/attributedstringforzero'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/attributedstringforzero.json'
content_hash: 'sha256:8881b3a9e03c4a3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# attributedStringForZero

<sub>Instance Property</sub>

The attributed string that the receiver uses to display zero values.

<sub>macOS</sub>

```swift
@NSCopying var attributedStringForZero: NSAttributedString { get set }
```

## Discussion

By default zero values are displayed according to the format specified for positive values; for more discussion of this subject see [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i).

### Special Considerations

This method is for use with formatters using `NSNumberFormatterBehavior10_0` behavior.

## See Also

### Configuring the Display of Numeric Values

- [textAttributesForNegativeValues](textattributesfornegativevalues.md) — The text attributes to be used in displaying negative values.
- [textAttributesForPositiveValues](textattributesforpositivevalues.md) — The text attributes to be used in displaying positive values.
- [textAttributesForZero](textattributesforzero.md) — The text attributes used to display a zero value.
- [attributedStringForNil](attributedstringfornil.md) — The attributed string the receiver uses to display `nil` values.
- [textAttributesForNil](textattributesfornil.md) — The text attributes used to display the `nil` symbol.
- [attributedStringForNotANumber](attributedstringfornotanumber.md) — The attributed string the receiver uses to display “not a number” values.
- [textAttributesForNotANumber](textattributesfornotanumber.md) — The text attributes used to display the NaN (“not a number”) string.
- [textAttributesForPositiveInfinity](textattributesforpositiveinfinity.md) — The text attributes used to display the positive infinity symbol.
- [textAttributesForNegativeInfinity](textattributesfornegativeinfinity.md) — The text attributes used to display the negative infinity symbol.
