---
title: compareBackwards
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstringcompareflags/comparebackwards
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/comparebackwards'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcompareflags/comparebackwards.json'
content_hash: 'sha256:f3a9b9c028d1659d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFStringCompareFlags](../cfstringcompareflags.md)

# compareBackwards

<sub>Type Property</sub>

Specifies that the comparison should start at the last elements of the entities being compared (for example, strings or arrays).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var compareBackwards: CFStringCompareFlags { get }
```

## See Also

### Constants

- [kCFCompareCaseInsensitive](comparecaseinsensitive.md) — Specifies that the comparison should ignore differences in case between alphabetical characters.
- [kCFCompareAnchored](compareanchored.md) — Performs searching only on characters at the beginning or end of the range.
- [kCFCompareNonliteral](comparenonliteral.md) — Specifies that loose equivalence is acceptable, especially as pertains to diacritical marks.
- [kCFCompareLocalized](comparelocalized.md) — Specifies that the comparison should take into account differences related to locale, such as the thousands separator character.
- [kCFCompareNumerically](comparenumerically.md) — Specifies that represented numeric values should be used as the basis for comparison and not the actual character values.
- [kCFCompareDiacriticInsensitive](comparediacriticinsensitive.md) — Specifies that the comparison should ignore diacritic markers.
- [kCFCompareWidthInsensitive](comparewidthinsensitive.md) — Specifies that the comparison should ignore width differences.
- [kCFCompareForcedOrdering](compareforcedordering.md) — Specifies that the comparison is forced to return either `kCFCompareLessThan` or `kCFCompareGreaterThan` if the strings are equivalent but not strictly equal.
