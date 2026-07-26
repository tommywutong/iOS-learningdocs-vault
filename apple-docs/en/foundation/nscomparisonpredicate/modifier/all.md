---
title: NSComparisonPredicate.Modifier.all
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscomparisonpredicate/modifier/all
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate/modifier/all'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate/modifier/all.json'
content_hash: 'sha256:acfab69e7eae79b0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSComparisonPredicate](../../nscomparisonpredicate.md) · [Modifier](../modifier.md)

# NSComparisonPredicate.Modifier.all

<sub>Case</sub>

A predicate to compare all entries in the destination of a to-many relationship.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case all
```

## Discussion

The left hand side must be a collection. The corresponding predicate compares each value in the left hand side with the right hand side, and returns [false](../../../swift/false.md) when it finds the first mismatch—or [true](../../../swift/true.md) if all match.

## See Also

### Constants

- [NSDirectPredicateModifier](direct.md) — A predicate to compare directly the left and right hand sides.
- [NSAnyPredicateModifier](any.md) — A predicate to match with any entry in the destination of a to-many relationship.
