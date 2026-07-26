---
title: NSCompoundPredicate.LogicalType
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscompoundpredicate/logicaltype
source_url: 'https://developer.apple.com/documentation/foundation/nscompoundpredicate/logicaltype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscompoundpredicate/logicaltype.json'
content_hash: 'sha256:272f27797d120810'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCompoundPredicate](../nscompoundpredicate.md)

# NSCompoundPredicate.LogicalType

<sub>Enumeration</sub>

Constants that describe the possible types of a compound predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum LogicalType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSNotPredicateType](logicaltype/not.md) — A logical NOT predicate.
- [NSAndPredicateType](logicaltype/and.md) — A logical AND predicate.
- [NSOrPredicateType](logicaltype/or.md) — A logical OR predicate.

### Initializers

- [init(rawValue:)](<logicaltype/init(rawvalue_).md>)

## See Also

### Getting Information About a Compound Predicate

- [compoundPredicateType](compoundpredicatetype.md) — The predicate type for the receiver.
- [subpredicates](subpredicates.md) — The receiver’s subpredicates.
