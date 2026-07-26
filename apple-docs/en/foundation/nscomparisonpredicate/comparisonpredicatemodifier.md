---
title: comparisonPredicateModifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscomparisonpredicate/comparisonpredicatemodifier
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate/comparisonpredicatemodifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate/comparisonpredicatemodifier.json'
content_hash: 'sha256:14b09c141df7ada9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSComparisonPredicate](../nscomparisonpredicate.md)

# comparisonPredicateModifier

<sub>Instance Property</sub>

The comparison predicate modifier for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var comparisonPredicateModifier: NSComparisonPredicate.Modifier { get }
```

## Discussion

The default value is [NSDirectPredicateModifier](modifier/direct.md).

## See Also

### Getting Information About a Comparison Predicate

- [Modifier](modifier.md) — Constants that describe the possible types of modifier for a comparison predicate.
- [customSelector](customselector.md) — The selector for the receiver.
- [rightExpression](rightexpression.md) — The right expression for the receiver.
- [leftExpression](leftexpression.md) — The left expression for the receiver.
- [options](options-swift.property.md) — The options to use for the receiver.
- [Options](options-swift.struct.md) — Constants that describe the possible types of string comparison for comparison predicates.
- [predicateOperatorType](predicateoperatortype.md) — The predicate type for the receiver.
- [Operator](operator.md) — Defines the type of comparison for a comparison predicate.
