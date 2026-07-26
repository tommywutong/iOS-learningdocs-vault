---
title: Additional query macros
framework: SwiftData
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/additionalquerymacros
source_url: 'https://developer.apple.com/documentation/swiftdata/additionalquerymacros'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/additionalquerymacros.json'
content_hash: 'sha256:dfb7ad080576c669'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# Additional query macros

<sub>API Collection</sub>

Supplementary macros that enable you to narrow query results and tell SwiftData how to sort, order, and section those results.

## Topics

### Basic queries

- [Query(animation:)](<query(animation_).md>) — Fetches all instances of the attached model type, using the specified animation to animate any subsequent changes.
- [Query(_:animation:sectionBy:)](<query(__animation_sectionby_)-91gkm.md>) _(beta)_
- [Query(_:animation:sectionBy:)](<query(__animation_sectionby_)-9futr.md>) _(beta)_
- [Query(transaction:)](<query(transaction_).md>) — Fetches all instances of the attached model type, using the specified transaction to animate any subsequent changes.
- [Query(_:transaction:sectionBy:)](<query(__transaction_sectionby_)-1poj9.md>) _(beta)_
- [Query(_:transaction:sectionBy:)](<query(__transaction_sectionby_)-2iol.md>) _(beta)_
- [Query(filter:sort:transaction:sectionBy:)](<query(filter_sort_transaction_sectionby_)-4wwsy.md>) _(beta)_
- [Query(filter:sort:transaction:sectionBy:)](<query(filter_sort_transaction_sectionby_)-6qrae.md>) _(beta)_

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
- [Query(filter:sort:transaction:)](<query(filter_sort_transaction_).md>) — Fetches and sorts the subset of the attached model type that satisfy the specified predicate.
- [Query(filter:sort:order:transaction:)](<query(filter_sort_order_transaction_)-6kkiu.md>) — Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.
- [Query(filter:sort:order:transaction:)](<query(filter_sort_order_transaction_)-8tk8u.md>) — Fetches a subset of the attached model type, in a specific order, by sorting on an optional attribute.
- [Query(filter:sort:order:transaction:sectionBy:)](<query(filter_sort_order_transaction_sectionby_)-3cn7t.md>) _(beta)_
- [Query(filter:sort:order:transaction:sectionBy:)](<query(filter_sort_order_transaction_sectionby_)-6c6ho.md>) _(beta)_
- [Query(filter:sort:order:transaction:sectionBy:)](<query(filter_sort_order_transaction_sectionby_)-9mbr6.md>) _(beta)_
- [Query(filter:sort:order:transaction:sectionBy:)](<query(filter_sort_order_transaction_sectionby_)-i779.md>) _(beta)_

### Descriptor-based queries

- [Query(_:animation:)](<query(__animation_).md>) — Fetches only the subset of the attached model type that satisfy the provided fetch descriptor’s criteria.
- [Query(_:transaction:)](<query(__transaction_).md>) — Fetches only the subset of the attached model type that satisfy the provided fetch descriptor’s criteria.

## See Also

### Model fetch

- [Filtering and sorting persistent data](filtering-and-sorting-persistent-data.md) — Manage data store presentation using predicates and dynamic queries.
- [Query()](<query().md>) — Fetches all instances of the attached model type.
- [Query](query.md) — A type that fetches models using the specified criteria, and manages those models so they remain in sync with the underlying data.
- [FetchDescriptor](fetchdescriptor.md) — A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.
