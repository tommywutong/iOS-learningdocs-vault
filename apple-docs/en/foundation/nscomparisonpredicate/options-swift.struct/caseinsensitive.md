---
title: caseInsensitive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscomparisonpredicate/options-swift.struct/caseinsensitive
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate/options-swift.struct/caseinsensitive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate/options-swift.struct/caseinsensitive.json'
content_hash: 'sha256:427f006f16d7bae6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSComparisonPredicate](../../nscomparisonpredicate.md) · [Options](../options-swift.struct.md)

# caseInsensitive

<sub>Type Property</sub>

A case-insensitive predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var caseInsensitive: NSComparisonPredicate.Options { get }
```

## Discussion

You represent this option in a predicate format string using a `[c]` following a string operation (for example, `"NeXT" like[c] "next"`).

## See Also

### Constants

- [NSDiacriticInsensitivePredicateOption](diacriticinsensitive.md) — A diacritic-insensitive predicate.
- [NSNormalizedPredicateOption](normalized.md) — A predicate that indicates you’ve preprocessed the strings to compare.
