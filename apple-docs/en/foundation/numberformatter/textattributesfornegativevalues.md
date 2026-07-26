---
title: textAttributesForNegativeValues
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/textattributesfornegativevalues
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/textattributesfornegativevalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/textattributesfornegativevalues.json'
content_hash: 'sha256:9286ee0f5f722935'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# textAttributesForNegativeValues

<sub>Instance Property</sub>

The text attributes to be used in displaying negative values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var textAttributesForNegativeValues: [String : Any]? { get set }
```

## Discussion

This property is a dictionary that contains the attributes used to display negative values.

## See Also

### Configuring the Display of Numeric Values

- [textAttributesForPositiveValues](textattributesforpositivevalues.md) — The text attributes to be used in displaying positive values.
- [attributedStringForZero](attributedstringforzero.md) — The attributed string that the receiver uses to display zero values.
- [textAttributesForZero](textattributesforzero.md) — The text attributes used to display a zero value.
- [attributedStringForNil](attributedstringfornil.md) — The attributed string the receiver uses to display `nil` values.
- [textAttributesForNil](textattributesfornil.md) — The text attributes used to display the `nil` symbol.
- [attributedStringForNotANumber](attributedstringfornotanumber.md) — The attributed string the receiver uses to display “not a number” values.
- [textAttributesForNotANumber](textattributesfornotanumber.md) — The text attributes used to display the NaN (“not a number”) string.
- [textAttributesForPositiveInfinity](textattributesforpositiveinfinity.md) — The text attributes used to display the positive infinity symbol.
- [textAttributesForNegativeInfinity](textattributesfornegativeinfinity.md) — The text attributes used to display the negative infinity symbol.
