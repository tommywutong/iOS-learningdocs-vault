---
title: compareAnchored
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstringcompareflags/compareanchored
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/compareanchored'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcompareflags/compareanchored.json'
content_hash: 'sha256:c23baee1158b7273'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFStringCompareFlags](../cfstringcompareflags.md)

# compareAnchored

<sub>Type Property</sub>

Performs searching only on characters at the beginning or end of the range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var compareAnchored: CFStringCompareFlags { get }
```

## Discussion

No match at the beginning or end means nothing is found, even if a matching sequence of characters occurs elsewhere in the string.

## See Also

### Constants

- [kCFCompareCaseInsensitive](comparecaseinsensitive.md) — Specifies that the comparison should ignore differences in case between alphabetical characters.
- [kCFCompareBackwards](comparebackwards.md) — Specifies that the comparison should start at the last elements of the entities being compared (for example, strings or arrays).
- [kCFCompareNonliteral](comparenonliteral.md) — Specifies that loose equivalence is acceptable, especially as pertains to diacritical marks.
- [kCFCompareLocalized](comparelocalized.md) — Specifies that the comparison should take into account differences related to locale, such as the thousands separator character.
- [kCFCompareNumerically](comparenumerically.md) — Specifies that represented numeric values should be used as the basis for comparison and not the actual character values.
- [kCFCompareDiacriticInsensitive](comparediacriticinsensitive.md) — Specifies that the comparison should ignore diacritic markers.
- [kCFCompareWidthInsensitive](comparewidthinsensitive.md) — Specifies that the comparison should ignore width differences.
- [kCFCompareForcedOrdering](compareforcedordering.md) — Specifies that the comparison is forced to return either `kCFCompareLessThan` or `kCFCompareGreaterThan` if the strings are equivalent but not strictly equal.
