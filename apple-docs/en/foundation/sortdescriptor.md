---
title: SortDescriptor
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/sortdescriptor
source_url: 'https://developer.apple.com/documentation/foundation/sortdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/sortdescriptor.json'
content_hash: 'sha256:b776afd3418b3657'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# SortDescriptor

<sub>Structure</sub>

A serializable description of how to sort numerics and strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SortDescriptor<Compared>
```

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SortComparator](sortcomparator.md)

## Topics

### Creating Sort Descriptors

- [init(_:comparing:)](<sortdescriptor/init(__comparing_).md>) — Creates a sort descriptor using a sort descriptor and a type that you specify.

### Using Sort Descriptors

- [compare(_:_:)](<sortdescriptor/compare(____).md>) — Provides the relative ordering of two elements.

### Inspecting Sort Descriptors

- [order](sortdescriptor/order.md) — The sort order that the sort descriptor uses to compare.

### Initializers

- [init(_:comparator:)](<sortdescriptor/init(__comparator_)-16bsg.md>)
- [init(_:comparator:)](<sortdescriptor/init(__comparator_)-1xorc.md>)
- [init(_:comparator:)](<sortdescriptor/init(__comparator_)-7vg3x.md>)
- [init(_:comparator:)](<sortdescriptor/init(__comparator_)-9m8l9.md>)
- [init(_:comparator:order:)](<sortdescriptor/init(__comparator_order_)-2ouai.md>)
- [init(_:comparator:order:)](<sortdescriptor/init(__comparator_order_)-4qaip.md>)
- [init(_:comparator:order:)](<sortdescriptor/init(__comparator_order_)-76h8b.md>)
- [init(_:comparator:order:)](<sortdescriptor/init(__comparator_order_)-pz7l.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-1t1a5.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-29e6k.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-29pto.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-2u61k.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-3fgjr.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-3iwfh.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-3wlt2.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-3wozy.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-49ozr.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-4b7jd.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-4doe9.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-4uo4r.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-4z0c9.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-51msp.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-52see.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-5lbot.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-5myfn.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-5s8d4.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-5y1wt.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-7rdjb.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-86gfd.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-8flg7.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-8jc9k.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-8tm2c.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-95o7r.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-9noh7.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-9xg3w.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-ks7r.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-kwgp.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-qlnj.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-rnot.md>)
- [init(_:order:)](<sortdescriptor/init(__order_)-z7th.md>)

### Instance Properties

- [keyPath](sortdescriptor/keypath.md) — The key path to the field for comparison.
- [stringComparator](sortdescriptor/stringcomparator.md) — A `String.StandardComparator` value.

## See Also

### Sorting

- [NSSortDescriptor](nssortdescriptor.md) — An immutable description of how to order a collection of objects according to a property common to all the objects.
- [ComparisonResult](comparisonresult.md) — Constants that indicate sort order.
- [SortComparator](sortcomparator.md) — A comparison algorithm for a specified type.
- [ComparableComparator](comparablecomparator.md) — A comparator that compares types according to their conformance to the comparable protocol.
- [KeyPathComparator](keypathcomparator.md) — A comparator that uses another sort comparator to provide the comparison of values at a key path.
- [SortOrder](sortorder.md) — The orderings that you can perform sorts with.
