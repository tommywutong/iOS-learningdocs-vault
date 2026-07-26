---
title: NSCompoundPredicate
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscompoundpredicate
source_url: 'https://developer.apple.com/documentation/foundation/nscompoundpredicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscompoundpredicate.json'
content_hash: 'sha256:7b156ed968a7760b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCompoundPredicate

<sub>Class</sub>

A specialized predicate that evaluates logical combinations of other predicates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSCompoundPredicate
```

## Overview

Use [NSCompoundPredicate](nscompoundpredicate.md) to create an `AND` or `OR` compound predicate of one or more other predicates, or the `NOT` of a single predicate. For the logical `AND` and `OR` operations:

- An `AND` predicate with no subpredicates evaluates to [true](../swift/true.md).
- An `OR` predicate with no subpredicates evaluates to [false](../swift/false.md).
- A compound predicate with one or more subpredicates evaluates to the truth of its subpredicates.

## Relationships

- **Inherits From**: [NSPredicate](nspredicate.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Compound Predicates

- [+ andPredicateWithSubpredicates:](<nscompoundpredicate/init(andpredicatewithsubpredicates_).md>) — Returns a new predicate that you form using an AND operation on the predicates in a specified array.
- [+ notPredicateWithSubpredicate:](<nscompoundpredicate/init(notpredicatewithsubpredicate_).md>) — Returns a new predicate that you form using a NOT operation on a specified predicate.
- [+ orPredicateWithSubpredicates:](<nscompoundpredicate/init(orpredicatewithsubpredicates_).md>) — Returns a new predicate that you form using an OR operation on the predicates in a specified array.
- [- initWithType:subpredicates:](<nscompoundpredicate/init(type_subpredicates_).md>) — Returns the receiver that a specified type initializes using predicates from a specified array.
- [- initWithCoder:](<nscompoundpredicate/init(coder_).md>) — Creates a predicate by decoding from the coder you specify.

### Getting Information About a Compound Predicate

- [compoundPredicateType](nscompoundpredicate/compoundpredicatetype.md) — The predicate type for the receiver.
- [subpredicates](nscompoundpredicate/subpredicates.md) — The receiver’s subpredicates.
- [LogicalType](nscompoundpredicate/logicaltype.md) — Constants that describe the possible types of a compound predicate.

## See Also

### Filltering

- [Predicate](predicate.md) — A logical condition used to test a set of input values for searching or filtering.
- [PredicateError](predicateerror.md) — An error thrown while evaluating a predicate.
- [PredicateCodableConfiguration](predicatecodableconfiguration.md) — A specification of the expected types and key paths found in an archived predicate.
- [PredicateCodableKeyPathProviding](predicatecodablekeypathproviding.md) — A type that provides the expected key paths found in an archived predicate.
- [PredicateExpression](predicateexpression.md) — A component expression that makes up part of a predicate.
- [StandardPredicateExpression](standardpredicateexpression.md) — A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.
- [PredicateExpressions](predicateexpressions.md) — The expressions that make up a predicate.
- [PredicateBindings](predicatebindings.md) — A mapping from a predicates’s input variables to their values.
- [NSPredicate](nspredicate.md) — A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [NSExpression](nsexpression.md) — An expression for use in a comparison predicate.
- [NSComparisonPredicate](nscomparisonpredicate.md) — A specialized predicate for comparing expressions.
