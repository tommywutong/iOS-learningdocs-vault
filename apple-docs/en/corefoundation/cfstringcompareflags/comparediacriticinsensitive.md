---
title: compareDiacriticInsensitive
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstringcompareflags/comparediacriticinsensitive
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/comparediacriticinsensitive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcompareflags/comparediacriticinsensitive.json'
content_hash: 'sha256:72fb9b50dd18dede'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFStringCompareFlags](../cfstringcompareflags.md)

# compareDiacriticInsensitive

<sub>Type Property</sub>

Specifies that the comparison should ignore diacritic markers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var compareDiacriticInsensitive: CFStringCompareFlags { get }
```

## Discussion

For example, “ö” (“o-umlaut”) is equivalent to “o”.

Diacritic markers are designated as all non-spacing marks below `U+0510`.

## See Also

### Constants

- [kCFCompareCaseInsensitive](comparecaseinsensitive.md) — Specifies that the comparison should ignore differences in case between alphabetical characters.
- [kCFCompareBackwards](comparebackwards.md) — Specifies that the comparison should start at the last elements of the entities being compared (for example, strings or arrays).
- [kCFCompareAnchored](compareanchored.md) — Performs searching only on characters at the beginning or end of the range.
- [kCFCompareNonliteral](comparenonliteral.md) — Specifies that loose equivalence is acceptable, especially as pertains to diacritical marks.
- [kCFCompareLocalized](comparelocalized.md) — Specifies that the comparison should take into account differences related to locale, such as the thousands separator character.
- [kCFCompareNumerically](comparenumerically.md) — Specifies that represented numeric values should be used as the basis for comparison and not the actual character values.
- [kCFCompareWidthInsensitive](comparewidthinsensitive.md) — Specifies that the comparison should ignore width differences.
- [kCFCompareForcedOrdering](compareforcedordering.md) — Specifies that the comparison is forced to return either `kCFCompareLessThan` or `kCFCompareGreaterThan` if the strings are equivalent but not strictly equal.
