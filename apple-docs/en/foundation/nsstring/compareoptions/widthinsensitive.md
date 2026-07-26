---
title: widthInsensitive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/compareoptions/widthinsensitive
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/compareoptions/widthinsensitive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/compareoptions/widthinsensitive.json'
content_hash: 'sha256:28a8c3dd978aa549'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSString](../../nsstring.md) · [CompareOptions](../compareoptions.md)

# widthInsensitive

<sub>Type Property</sub>

Search ignores width differences in characters that have full-width and half-width forms, as occurs in East Asian character sets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var widthInsensitive: NSString.CompareOptions { get }
```

## Discussion

For example, with this option, the full-width Latin small letter ‘ａ’ (`U+FF41`) is equal to the basic Latin small letter ‘a’ (`U+0061`).

## See Also

### Constants

- [NSCaseInsensitiveSearch](caseinsensitive.md) — A case-insensitive search.
- [NSLiteralSearch](literal.md) — Exact character-by-character equivalence.
- [NSBackwardsSearch](backwards.md) — Search from end of source string.
- [NSAnchoredSearch](anchored.md) — Search is limited to start (or end, if `NSBackwardsSearch`) of source string.
- [NSNumericSearch](numeric.md) — Numbers within strings are compared using numeric value, that is, `Name2.txt` \< `Name7.txt` \< `Name25.txt`.
- [NSDiacriticInsensitiveSearch](diacriticinsensitive.md) — Search ignores diacritic marks.
- [NSForcedOrderingSearch](forcedordering.md) — Comparisons are forced to return either `NSOrderedAscending` or `NSOrderedDescending` if the strings are equivalent but not strictly equal.
- [NSRegularExpressionSearch](regularexpression.md) — The search string is treated as an ICU-compatible regular expression. If set, no other options can apply except [NSCaseInsensitiveSearch](caseinsensitive.md) and [NSAnchoredSearch](anchored.md). You can use this option only with the `rangeOfString:`… methods and [- stringByReplacingOccurrencesOfString:withString:options:range:](<../replacingoccurrences(of_with_options_range_).md>).
