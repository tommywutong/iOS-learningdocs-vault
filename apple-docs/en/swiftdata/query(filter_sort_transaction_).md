---
title: 'Query(filter:sort:transaction:)'
framework: SwiftData
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/query(filter:sort:transaction:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/query(filter:sort:transaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query%28filter%3Asort%3Atransaction%3A%29.json'
content_hash: 'sha256:7ce822941f151beb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# Query(filter:sort:transaction:)

<sub>Macro</sub>

Fetches and sorts the subset of the attached model type that satisfy the specified predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(accessor) @attached(peer, names: prefixed(`_`)) macro Query<Element>(filter: Predicate<Element>? = nil, sort descriptors: [SortDescriptor<Element>] = [], transaction: Transaction? = nil) where Element : PersistentModel
```

## Parameters

- `filter` — The logical condition the query uses to determine if it returns a specific model instance.

- `descriptors` — An array of sort descriptors to use when arranging the fetched models.

- `transaction` — The transaction to use when updates to the fetched models trigger user interface changes.

## See Also

### Predicate-based queries

- [Query(filter:sort:animation:)](<query(filter_sort_animation_).md>) — Fetches a sorted subset of the attached model type that satisfy the specified predicate.
- [Query(filter:sort:order:animation:)](<query(filter_sort_order_animation_)-80h6f.md>) — Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.
- [Query(filter:sort:order:animation:)](<query(filter_sort_order_animation_)-pb15.md>) — Fetches a subset of the attached model type, in a specific order, by sorting on an optional attribute.
- [Query(filter:sort:animation:sectionBy:)](<query(filter_sort_animation_sectionby_)-1s3xp.md>) _(beta)_
- [Query(filter:sort:animation:sectionBy:)](<query(filter_sort_animation_sectionby_)-82mot.md>) _(beta)_
- [Query(filter:sort:order:animation:sectionBy:)](<query(filter_sort_order_animation_sectionby_)-132tv.md>) _(beta)_
- [Query(filter:sort:order:animation:sectionBy:)](<query(filter_sort_order_animation_sectionby_)-66vd3.md>) _(beta)_
- [Query(filter:sort:order:animation:sectionBy:)](<query(filter_sort_order_animation_sectionby_)-75r20.md>) _(beta)_
- [Query(filter:sort:order:animation:sectionBy:)](<query(filter_sort_order_animation_sectionby_)-7o0vo.md>) _(beta)_
- [Query(filter:sort:order:transaction:)](<query(filter_sort_order_transaction_)-6kkiu.md>) — Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.
- [Query(filter:sort:order:transaction:)](<query(filter_sort_order_transaction_)-8tk8u.md>) — Fetches a subset of the attached model type, in a specific order, by sorting on an optional attribute.
- [Query(filter:sort:order:transaction:sectionBy:)](<query(filter_sort_order_transaction_sectionby_)-3cn7t.md>) _(beta)_
- [Query(filter:sort:order:transaction:sectionBy:)](<query(filter_sort_order_transaction_sectionby_)-6c6ho.md>) _(beta)_
- [Query(filter:sort:order:transaction:sectionBy:)](<query(filter_sort_order_transaction_sectionby_)-9mbr6.md>) _(beta)_
- [Query(filter:sort:order:transaction:sectionBy:)](<query(filter_sort_order_transaction_sectionby_)-i779.md>) _(beta)_
