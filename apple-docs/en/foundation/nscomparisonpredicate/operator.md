---
title: NSComparisonPredicate.Operator
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscomparisonpredicate/operator
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate/operator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate/operator.json'
content_hash: 'sha256:98550a1c45d7a28a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSComparisonPredicate](../nscomparisonpredicate.md)

# NSComparisonPredicate.Operator

<sub>Enumeration</sub>

Defines the type of comparison for a comparison predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Operator
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSLessThanPredicateOperatorType](operator/lessthan.md) — A less-than predicate.
- [NSLessThanOrEqualToPredicateOperatorType](operator/lessthanorequalto.md) — A less-than-or-equal-to predicate.
- [NSGreaterThanPredicateOperatorType](operator/greaterthan.md) — A greater-than predicate.
- [NSGreaterThanOrEqualToPredicateOperatorType](operator/greaterthanorequalto.md) — A greater-than-or-equal-to predicate.
- [NSEqualToPredicateOperatorType](operator/equalto.md) — An equal-to predicate.
- [NSNotEqualToPredicateOperatorType](operator/notequalto.md) — A not-equal-to predicate.
- [NSMatchesPredicateOperatorType](operator/matches.md) — A full regular expression matching predicate.
- [NSLikePredicateOperatorType](operator/like.md) — A simple subset of the MATCHES predicate, similar in behavior to SQL `LIKE`.
- [NSBeginsWithPredicateOperatorType](operator/beginswith.md) — A begins-with predicate.
- [NSEndsWithPredicateOperatorType](operator/endswith.md) — An ends-with predicate.
- [NSInPredicateOperatorType](operator/in.md) — A predicate to determine if the left hand side is in the right hand side.
- [NSCustomSelectorPredicateOperatorType](operator/customselector.md) — A predicate that uses a custom selector that takes a single argument and returns a `BOOL` value.
- [NSContainsPredicateOperatorType](operator/contains.md) — A predicate to determine if the left hand side contains the right hand side.
- [NSBetweenPredicateOperatorType](operator/between.md) — A predicate to determine if the left hand side lies at or between bounds specified by the right hand side.

### Initializers

- [init(rawValue:)](<operator/init(rawvalue_).md>)

## See Also

### Getting Information About a Comparison Predicate

- [comparisonPredicateModifier](comparisonpredicatemodifier.md) — The comparison predicate modifier for the receiver.
- [Modifier](modifier.md) — Constants that describe the possible types of modifier for a comparison predicate.
- [customSelector](customselector.md) — The selector for the receiver.
- [rightExpression](rightexpression.md) — The right expression for the receiver.
- [leftExpression](leftexpression.md) — The left expression for the receiver.
- [options](options-swift.property.md) — The options to use for the receiver.
- [Options](options-swift.struct.md) — Constants that describe the possible types of string comparison for comparison predicates.
- [predicateOperatorType](predicateoperatortype.md) — The predicate type for the receiver.
