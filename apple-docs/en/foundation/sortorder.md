---
title: SortOrder
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/sortorder
source_url: 'https://developer.apple.com/documentation/foundation/sortorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/sortorder.json'
content_hash: 'sha256:3aed530b15db2283'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# SortOrder

<sub>Enumeration</sub>

The orderings that you can perform sorts with.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum SortOrder
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Using Sort Orders

- [SortOrder.forward](sortorder/forward.md) — The ordering that places the first item before the second when comparing two items using an ascending order.
- [SortOrder.reverse](sortorder/reverse.md) — The ordering that places the first item after the second when comparing two items using an ascending order.

## See Also

### Sorting

- [NSSortDescriptor](nssortdescriptor.md) — An immutable description of how to order a collection of objects according to a property common to all the objects.
- [ComparisonResult](comparisonresult.md) — Constants that indicate sort order.
- [SortDescriptor](sortdescriptor.md) — A serializable description of how to sort numerics and strings.
- [SortComparator](sortcomparator.md) — A comparison algorithm for a specified type.
- [ComparableComparator](comparablecomparator.md) — A comparator that compares types according to their conformance to the comparable protocol.
- [KeyPathComparator](keypathcomparator.md) — A comparator that uses another sort comparator to provide the comparison of values at a key path.
