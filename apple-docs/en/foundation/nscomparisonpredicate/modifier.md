---
title: NSComparisonPredicate.Modifier
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscomparisonpredicate/modifier
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate/modifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate/modifier.json'
content_hash: 'sha256:fce260f2c2d30ea9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSComparisonPredicate](../nscomparisonpredicate.md)

# NSComparisonPredicate.Modifier

<sub>Enumeration</sub>

Constants that describe the possible types of modifier for a comparison predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Modifier
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSDirectPredicateModifier](modifier/direct.md) — A predicate to compare directly the left and right hand sides.
- [NSAllPredicateModifier](modifier/all.md) — A predicate to compare all entries in the destination of a to-many relationship.
- [NSAnyPredicateModifier](modifier/any.md) — A predicate to match with any entry in the destination of a to-many relationship.

### Initializers

- [init(rawValue:)](<modifier/init(rawvalue_).md>)

## See Also

### Getting Information About a Comparison Predicate

- [comparisonPredicateModifier](comparisonpredicatemodifier.md) — The comparison predicate modifier for the receiver.
- [customSelector](customselector.md) — The selector for the receiver.
- [rightExpression](rightexpression.md) — The right expression for the receiver.
- [leftExpression](leftexpression.md) — The left expression for the receiver.
- [options](options-swift.property.md) — The options to use for the receiver.
- [Options](options-swift.struct.md) — Constants that describe the possible types of string comparison for comparison predicates.
- [predicateOperatorType](predicateoperatortype.md) — The predicate type for the receiver.
- [Operator](operator.md) — Defines the type of comparison for a comparison predicate.
