---
title: ComparableComparator
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/comparablecomparator
source_url: 'https://developer.apple.com/documentation/foundation/comparablecomparator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/comparablecomparator.json'
content_hash: 'sha256:63827101bfbd5c50'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ComparableComparator

<sub>Structure</sub>

A comparator that compares types according to their conformance to the comparable protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ComparableComparator<Compared> where Compared : Comparable
```

## Overview

The comparator uses the relevant type’s [Comparable](../swift/comparable.md) implementation to compare instances.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SortComparator](sortcomparator.md)

## Topics

### Using a Comparator

- [compare(_:_:)](<comparablecomparator/compare(____).md>) — Provides the relative ordering of two elements.

### Inspecting a Comparator

- [order](comparablecomparator/order.md) — The sort order that the comparator uses to compare.

### Initializers

- [init(order:)](<comparablecomparator/init(order_).md>)

## See Also

### Sorting

- [NSSortDescriptor](nssortdescriptor.md) — An immutable description of how to order a collection of objects according to a property common to all the objects.
- [ComparisonResult](comparisonresult.md) — Constants that indicate sort order.
- [SortDescriptor](sortdescriptor.md) — A serializable description of how to sort numerics and strings.
- [SortComparator](sortcomparator.md) — A comparison algorithm for a specified type.
- [KeyPathComparator](keypathcomparator.md) — A comparator that uses another sort comparator to provide the comparison of values at a key path.
- [SortOrder](sortorder.md) — The orderings that you can perform sorts with.
