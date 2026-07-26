---
title: diacriticInsensitive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscomparisonpredicate/options-swift.struct/diacriticinsensitive
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate/options-swift.struct/diacriticinsensitive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate/options-swift.struct/diacriticinsensitive.json'
content_hash: 'sha256:28bb4ec9d8e7272a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSComparisonPredicate](../../nscomparisonpredicate.md) · [Options](../options-swift.struct.md)

# diacriticInsensitive

<sub>Type Property</sub>

A diacritic-insensitive predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var diacriticInsensitive: NSComparisonPredicate.Options { get }
```

## Discussion

You represent this option in a predicate format string using a `[d]` following a string operation (for example, `"naïve" like[d] "naive"`).

## See Also

### Constants

- [NSCaseInsensitivePredicateOption](caseinsensitive.md) — A case-insensitive predicate.
- [NSNormalizedPredicateOption](normalized.md) — A predicate that indicates you’ve preprocessed the strings to compare.
