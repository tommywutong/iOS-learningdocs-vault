---
title: KeyPathComparator
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/keypathcomparator
source_url: 'https://developer.apple.com/documentation/foundation/keypathcomparator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/keypathcomparator.json'
content_hash: 'sha256:e9354a5b882ce9e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# KeyPathComparator

<sub>Structure</sub>

A comparator that uses another sort comparator to provide the comparison of values at a key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct KeyPathComparator<Compared>
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SortComparator](sortcomparator.md)

## Topics

### Using Key Path Comparators

- [compare(_:_:)](<keypathcomparator/compare(____).md>) — Provides the relative ordering of two items according to the ordering of the properties that the comparator’s key path references.

### Inspecting Key Path Comparators

- [keyPath](keypathcomparator/keypath.md) — The key path that the comparator uses to compare properties.
- [order](keypathcomparator/order.md) — The sort order that the comparator uses to compare properties.

### Initializers

- [init(_:comparator:)](<keypathcomparator/init(__comparator_)-8b13q.md>)
- [init(_:comparator:)](<keypathcomparator/init(__comparator_)-284rt.md>)
- [init(_:comparator:order:)](<keypathcomparator/init(__comparator_order_)-749jk.md>)
- [init(_:comparator:order:)](<keypathcomparator/init(__comparator_order_)-3gjxd.md>)
- [init(_:order:)](<keypathcomparator/init(__order_)-6r8gw.md>)
- [init(_:order:)](<keypathcomparator/init(__order_)-4hyoi.md>)

## See Also

### Sorting

- [NSSortDescriptor](nssortdescriptor.md) — An immutable description of how to order a collection of objects according to a property common to all the objects.
- [ComparisonResult](comparisonresult.md) — Constants that indicate sort order.
- [SortDescriptor](sortdescriptor.md) — A serializable description of how to sort numerics and strings.
- [SortComparator](sortcomparator.md) — A comparison algorithm for a specified type.
- [ComparableComparator](comparablecomparator.md) — A comparator that compares types according to their conformance to the comparable protocol.
- [SortOrder](sortorder.md) — The orderings that you can perform sorts with.
