---
title: 'Query(filter:sort:animation:sectionBy:)'
framework: SwiftData
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftdata/query(filter:sort:animation:sectionby:)-1s3xp'
source_url: 'https://developer.apple.com/documentation/swiftdata/query(filter:sort:animation:sectionby:)-1s3xp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query%28filter%3Asort%3Aanimation%3Asectionby%3A%29-1s3xp.json'
content_hash: 'sha256:2cc15d64fcc97eec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# Query(filter:sort:animation:sectionBy:)

<sub>Macro</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(accessor) @attached(peer, names: prefixed(`_`)) macro Query<Element>(filter: Predicate<Element>? = nil, sort descriptors: [SortDescriptor<Element>] = [], animation: Animation, sectionBy sectionKeyPath: KeyPath<Element, String?>) where Element : PersistentModel
```

## See Also

### Predicate-based queries

- [Query(filter:sort:animation:)](<query(filter_sort_animation_).md>) — Fetches a sorted subset of the attached model type that satisfy the specified predicate.
- [Query(filter:sort:order:animation:)](<query(filter_sort_order_animation_)-80h6f.md>) — Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.
- [Query(filter:sort:order:animation:)](<query(filter_sort_order_animation_)-pb15.md>) — Fetches a subset of the attached model type, in a specific order, by sorting on an optional attribute.
- [Query(filter:sort:animation:sectionBy:)](<query(filter_sort_animation_sectionby_)-82mot.md>) _(beta)_
- [Query(filter:sort:order:animation:sectionBy:)](<query(filter_sort_order_animation_sectionby_)-132tv.md>) _(beta)_
- [Query(filter:sort:order:animation:sectionBy:)](<query(filter_sort_order_animation_sectionby_)-66vd3.md>) _(beta)_
- [Query(filter:sort:order:animation:sectionBy:)](<query(filter_sort_order_animation_sectionby_)-75r20.md>) _(beta)_
- [Query(filter:sort:order:animation:sectionBy:)](<query(filter_sort_order_animation_sectionby_)-7o0vo.md>) _(beta)_
- [Query(filter:sort:transaction:)](<query(filter_sort_transaction_).md>) — Fetches and sorts the subset of the attached model type that satisfy the specified predicate.
- [Query(filter:sort:order:transaction:)](<query(filter_sort_order_transaction_)-6kkiu.md>) — Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.
- [Query(filter:sort:order:transaction:)](<query(filter_sort_order_transaction_)-8tk8u.md>) — Fetches a subset of the attached model type, in a specific order, by sorting on an optional attribute.
- [Query(filter:sort:order:transaction:sectionBy:)](<query(filter_sort_order_transaction_sectionby_)-3cn7t.md>) _(beta)_
- [Query(filter:sort:order:transaction:sectionBy:)](<query(filter_sort_order_transaction_sectionby_)-6c6ho.md>) _(beta)_
- [Query(filter:sort:order:transaction:sectionBy:)](<query(filter_sort_order_transaction_sectionby_)-9mbr6.md>) _(beta)_
- [Query(filter:sort:order:transaction:sectionBy:)](<query(filter_sort_order_transaction_sectionby_)-i779.md>) _(beta)_
