---
title: normalized
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscomparisonpredicate/options-swift.struct/normalized
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate/options-swift.struct/normalized'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate/options-swift.struct/normalized.json'
content_hash: 'sha256:9156b0f46cf0fb44'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSComparisonPredicate](../../nscomparisonpredicate.md) · [Options](../options-swift.struct.md)

# normalized

<sub>Type Property</sub>

A predicate that indicates you’ve preprocessed the strings to compare.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var normalized: NSComparisonPredicate.Options { get }
```

## Discussion

This option supersedes `NSCaseInsensitivePredicateOption` and `NSDiacriticInsensitivePredicateOption`, and is a performance optimization option.

You represent this option in a predicate format string using a `[n]` following a string operation (for example, `"WXYZlan" matches[n] ".lan"`).

## See Also

### Constants

- [NSCaseInsensitivePredicateOption](caseinsensitive.md) — A case-insensitive predicate.
- [NSDiacriticInsensitivePredicateOption](diacriticinsensitive.md) — A diacritic-insensitive predicate.
