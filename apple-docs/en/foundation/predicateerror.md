---
title: PredicateError
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateerror
source_url: 'https://developer.apple.com/documentation/foundation/predicateerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateerror.json'
content_hash: 'sha256:2a41a3e7dcb79a2b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# PredicateError

<sub>Structure</sub>

An error thrown while evaluating a predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PredicateError
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Errors

- [forceCastFailure](predicateerror/forcecastfailure.md)
- [forceUnwrapFailure](predicateerror/forceunwrapfailure.md)
- [invalidInput](predicateerror/invalidinput.md)
- [undefinedVariable](predicateerror/undefinedvariable.md)

## See Also

### Filltering

- [Predicate](predicate.md) — A logical condition used to test a set of input values for searching or filtering.
- [PredicateCodableConfiguration](predicatecodableconfiguration.md) — A specification of the expected types and key paths found in an archived predicate.
- [PredicateCodableKeyPathProviding](predicatecodablekeypathproviding.md) — A type that provides the expected key paths found in an archived predicate.
- [PredicateExpression](predicateexpression.md) — A component expression that makes up part of a predicate.
- [StandardPredicateExpression](standardpredicateexpression.md) — A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.
- [PredicateExpressions](predicateexpressions.md) — The expressions that make up a predicate.
- [PredicateBindings](predicatebindings.md) — A mapping from a predicates’s input variables to their values.
- [NSPredicate](nspredicate.md) — A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [NSExpression](nsexpression.md) — An expression for use in a comparison predicate.
- [NSComparisonPredicate](nscomparisonpredicate.md) — A specialized predicate for comparing expressions.
- [NSCompoundPredicate](nscompoundpredicate.md) — A specialized predicate that evaluates logical combinations of other predicates.
