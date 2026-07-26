---
title: SortComparator
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/sortcomparator
source_url: 'https://developer.apple.com/documentation/foundation/sortcomparator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/sortcomparator.json'
content_hash: 'sha256:6658a52545254d9e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# SortComparator

<sub>Protocol</sub>

A comparison algorithm for a specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol SortComparator<Compared> : Hashable, Sendable
```

## Overview

Objects that conform to [SortComparator](sortcomparator.md) provide a comparison algorithm and storage for the sort order to use when comparing.

## Relationships

- **Inherits From**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [ComparableComparator](comparablecomparator.md), [KeyPathComparator](keypathcomparator.md), [SortDescriptor](sortdescriptor.md)

## Topics

### Inspecting a Comparator

- [order](sortcomparator/order.md) — The sort order that the comparator uses to compare.
- [localized](sortcomparator/localized.md) — A comparator that compares a string using a localized comparison in the current locale.
- [localizedStandard](sortcomparator/localizedstandard.md) — A comparator that compares a string using a localized, numeric comparison in the current locale.

### Using a Comparator

- [compare(_:_:)](<sortcomparator/compare(____).md>) — Provides the relative ordering of two elements based on the sort order of the comparator.
- [Compared](sortcomparator/compared.md) — A type that the sort comparator can compare.

## See Also

### Sorting

- [NSSortDescriptor](nssortdescriptor.md) — An immutable description of how to order a collection of objects according to a property common to all the objects.
- [ComparisonResult](comparisonresult.md) — Constants that indicate sort order.
- [SortDescriptor](sortdescriptor.md) — A serializable description of how to sort numerics and strings.
- [ComparableComparator](comparablecomparator.md) — A comparator that compares types according to their conformance to the comparable protocol.
- [KeyPathComparator](keypathcomparator.md) — A comparator that uses another sort comparator to provide the comparison of values at a key path.
- [SortOrder](sortorder.md) — The orderings that you can perform sorts with.
