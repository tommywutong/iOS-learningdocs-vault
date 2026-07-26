---
title: ComparisonResult
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/comparisonresult
source_url: 'https://developer.apple.com/documentation/foundation/comparisonresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/comparisonresult.json'
content_hash: 'sha256:2d09d59a2bb510bf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ComparisonResult

<sub>Enumeration</sub>

Constants that indicate sort order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum ComparisonResult
```

## Overview

These constants are used to indicate how items in a request are ordered, from the first one given in a method invocation or function call to the last (that is, left to right in code).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a comparison result

- [init(rawValue:)](<comparisonresult/init(rawvalue_).md>)

### Constants

- [NSOrderedAscending](comparisonresult/orderedascending.md) — The left operand is smaller than the right operand.
- [NSOrderedSame](comparisonresult/orderedsame.md) — The two operands are equal.
- [NSOrderedDescending](comparisonresult/ordereddescending.md) — The left operand is greater than the right operand.

## See Also

### Sorting

- [NSSortDescriptor](nssortdescriptor.md) — An immutable description of how to order a collection of objects according to a property common to all the objects.
- [SortDescriptor](sortdescriptor.md) — A serializable description of how to sort numerics and strings.
- [SortComparator](sortcomparator.md) — A comparison algorithm for a specified type.
- [ComparableComparator](comparablecomparator.md) — A comparator that compares types according to their conformance to the comparable protocol.
- [KeyPathComparator](keypathcomparator.md) — A comparator that uses another sort comparator to provide the comparison of values at a key path.
- [SortOrder](sortorder.md) — The orderings that you can perform sorts with.
