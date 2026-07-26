---
title: textAttributesForZero
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/textattributesforzero
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/textattributesforzero'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/textattributesforzero.json'
content_hash: 'sha256:bb969c775ee041a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# textAttributesForZero

<sub>Instance Property</sub>

The text attributes used to display a zero value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var textAttributesForZero: [String : Any]? { get set }
```

## Discussion

This property is a dictionary that contains the text attributes used to display zero values.

## See Also

### Configuring the Display of Numeric Values

- [textAttributesForNegativeValues](textattributesfornegativevalues.md) — The text attributes to be used in displaying negative values.
- [textAttributesForPositiveValues](textattributesforpositivevalues.md) — The text attributes to be used in displaying positive values.
- [attributedStringForZero](attributedstringforzero.md) — The attributed string that the receiver uses to display zero values.
- [attributedStringForNil](attributedstringfornil.md) — The attributed string the receiver uses to display `nil` values.
- [textAttributesForNil](textattributesfornil.md) — The text attributes used to display the `nil` symbol.
- [attributedStringForNotANumber](attributedstringfornotanumber.md) — The attributed string the receiver uses to display “not a number” values.
- [textAttributesForNotANumber](textattributesfornotanumber.md) — The text attributes used to display the NaN (“not a number”) string.
- [textAttributesForPositiveInfinity](textattributesforpositiveinfinity.md) — The text attributes used to display the positive infinity symbol.
- [textAttributesForNegativeInfinity](textattributesfornegativeinfinity.md) — The text attributes used to display the negative infinity symbol.
