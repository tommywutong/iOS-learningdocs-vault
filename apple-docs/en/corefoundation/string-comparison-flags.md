---
title: String Comparison Flags
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/string-comparison-flags
source_url: 'https://developer.apple.com/documentation/corefoundation/string-comparison-flags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/string-comparison-flags.json'
content_hash: 'sha256:18425a330b37404d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFString](cfstring.md)

# String Comparison Flags

<sub>API Collection</sub>

Flags that specify how string comparisons are performed.

## Overview

These constants are flags intended for use in the comparison-option parameters in comparison functions such as [CFStringCompare](<cfstringcompare(______).md>). If you want to request multiple options, combine them with a bitwise-OR operation.

## Topics

### Constants

- [kCFCompareCaseInsensitive](cfstringcompareflags/comparecaseinsensitive.md) — Specifies that the comparison should ignore differences in case between alphabetical characters.
- [kCFCompareBackwards](cfstringcompareflags/comparebackwards.md) — Specifies that the comparison should start at the last elements of the entities being compared (for example, strings or arrays).
- [kCFCompareAnchored](cfstringcompareflags/compareanchored.md) — Performs searching only on characters at the beginning or end of the range.
- [kCFCompareNonliteral](cfstringcompareflags/comparenonliteral.md) — Specifies that loose equivalence is acceptable, especially as pertains to diacritical marks.
- [kCFCompareLocalized](cfstringcompareflags/comparelocalized.md) — Specifies that the comparison should take into account differences related to locale, such as the thousands separator character.
- [kCFCompareNumerically](cfstringcompareflags/comparenumerically.md) — Specifies that represented numeric values should be used as the basis for comparison and not the actual character values.
- [kCFCompareDiacriticInsensitive](cfstringcompareflags/comparediacriticinsensitive.md) — Specifies that the comparison should ignore diacritic markers.
- [kCFCompareWidthInsensitive](cfstringcompareflags/comparewidthinsensitive.md) — Specifies that the comparison should ignore width differences.
- [kCFCompareForcedOrdering](cfstringcompareflags/compareforcedordering.md) — Specifies that the comparison is forced to return either `kCFCompareLessThan` or `kCFCompareGreaterThan` if the strings are equivalent but not strictly equal.

## See Also

### Constants

- [CFStringBuiltInEncodings](cfstringbuiltinencodings.md) — Encodings that are built-in on all platforms on which macOS runs.
- [Invalid String Encoding Flag](invalid-string-encoding-flag.md) — Special value returned from functions to indicate a string encoding that is not supported or recognized by CFString.
- [External String Encodings](external-string-encodings.md) — `CFStringEncoding` constants for encodings that may be supported by CFString.
