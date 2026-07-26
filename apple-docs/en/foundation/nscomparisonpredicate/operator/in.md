---
title: NSComparisonPredicate.Operator.in
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscomparisonpredicate/operator/in
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate/operator/in'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate/operator/in.json'
content_hash: 'sha256:e2e1dd3824a99798'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSComparisonPredicate](../../nscomparisonpredicate.md) · [Operator](../operator.md)

# NSComparisonPredicate.Operator.in

<sub>Case</sub>

A predicate to determine if the left hand side is in the right hand side.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case `in`
```

## Discussion

For strings, returns [true](../../../swift/true.md) if the left hand side is a substring of the right hand side . For collections, returns [true](../../../swift/true.md) if the left hand side is in the right hand side .

## See Also

### Constants

- [NSLessThanPredicateOperatorType](lessthan.md) — A less-than predicate.
- [NSLessThanOrEqualToPredicateOperatorType](lessthanorequalto.md) — A less-than-or-equal-to predicate.
- [NSGreaterThanPredicateOperatorType](greaterthan.md) — A greater-than predicate.
- [NSGreaterThanOrEqualToPredicateOperatorType](greaterthanorequalto.md) — A greater-than-or-equal-to predicate.
- [NSEqualToPredicateOperatorType](equalto.md) — An equal-to predicate.
- [NSNotEqualToPredicateOperatorType](notequalto.md) — A not-equal-to predicate.
- [NSMatchesPredicateOperatorType](matches.md) — A full regular expression matching predicate.
- [NSLikePredicateOperatorType](like.md) — A simple subset of the MATCHES predicate, similar in behavior to SQL `LIKE`.
- [NSBeginsWithPredicateOperatorType](beginswith.md) — A begins-with predicate.
- [NSEndsWithPredicateOperatorType](endswith.md) — An ends-with predicate.
- [NSCustomSelectorPredicateOperatorType](customselector.md) — A predicate that uses a custom selector that takes a single argument and returns a `BOOL` value.
- [NSContainsPredicateOperatorType](contains.md) — A predicate to determine if the left hand side contains the right hand side.
- [NSBetweenPredicateOperatorType](between.md) — A predicate to determine if the left hand side lies at or between bounds specified by the right hand side.
