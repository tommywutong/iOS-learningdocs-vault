---
title: NSComparisonPredicate.Options
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscomparisonpredicate/options-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate/options-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate/options-swift.struct.json'
content_hash: 'sha256:42b998f63051898e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSComparisonPredicate](../nscomparisonpredicate.md)

# NSComparisonPredicate.Options

<sub>Structure</sub>

Constants that describe the possible types of string comparison for comparison predicates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Options
```

## Overview

The system supports these options for `LIKE`, as well as all of the equality/comparison operators.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSCaseInsensitivePredicateOption](options-swift.struct/caseinsensitive.md) — A case-insensitive predicate.
- [NSDiacriticInsensitivePredicateOption](options-swift.struct/diacriticinsensitive.md) — A diacritic-insensitive predicate.
- [NSNormalizedPredicateOption](options-swift.struct/normalized.md) — A predicate that indicates you’ve preprocessed the strings to compare.

### Initializers

- [init(rawValue:)](<options-swift.struct/init(rawvalue_).md>)

## See Also

### Getting Information About a Comparison Predicate

- [comparisonPredicateModifier](comparisonpredicatemodifier.md) — The comparison predicate modifier for the receiver.
- [Modifier](modifier.md) — Constants that describe the possible types of modifier for a comparison predicate.
- [customSelector](customselector.md) — The selector for the receiver.
- [rightExpression](rightexpression.md) — The right expression for the receiver.
- [leftExpression](leftexpression.md) — The left expression for the receiver.
- [options](options-swift.property.md) — The options to use for the receiver.
- [predicateOperatorType](predicateoperatortype.md) — The predicate type for the receiver.
- [Operator](operator.md) — Defines the type of comparison for a comparison predicate.
