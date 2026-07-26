---
title: attributedStringForNil
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/attributedstringfornil
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/attributedstringfornil'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/attributedstringfornil.json'
content_hash: 'sha256:d044e4656cfcb87c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# attributedStringForNil

<sub>Instance Property</sub>

The attributed string the receiver uses to display `nil` values.

<sub>macOS</sub>

```swift
@NSCopying var attributedStringForNil: NSAttributedString { get set }
```

## Discussion

By default `nil` values are displayed as an empty string.

### Special Considerations

This method is for use with formatters using `NSNumberFormatterBehavior10_0` behavior.

## See Also

### Configuring the Display of Numeric Values

- [textAttributesForNegativeValues](textattributesfornegativevalues.md) — The text attributes to be used in displaying negative values.
- [textAttributesForPositiveValues](textattributesforpositivevalues.md) — The text attributes to be used in displaying positive values.
- [attributedStringForZero](attributedstringforzero.md) — The attributed string that the receiver uses to display zero values.
- [textAttributesForZero](textattributesforzero.md) — The text attributes used to display a zero value.
- [textAttributesForNil](textattributesfornil.md) — The text attributes used to display the `nil` symbol.
- [attributedStringForNotANumber](attributedstringfornotanumber.md) — The attributed string the receiver uses to display “not a number” values.
- [textAttributesForNotANumber](textattributesfornotanumber.md) — The text attributes used to display the NaN (“not a number”) string.
- [textAttributesForPositiveInfinity](textattributesforpositiveinfinity.md) — The text attributes used to display the positive infinity symbol.
- [textAttributesForNegativeInfinity](textattributesfornegativeinfinity.md) — The text attributes used to display the negative infinity symbol.
