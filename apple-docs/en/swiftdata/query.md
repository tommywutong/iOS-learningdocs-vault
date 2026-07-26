---
title: Query
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/query
source_url: 'https://developer.apple.com/documentation/swiftdata/query'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query.json'
content_hash: 'sha256:a4b0138d4c4752c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# Query

<sub>Structure</sub>

A type that fetches models using the specified criteria, and manages those models so they remain in sync with the underlying data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct Query<Element, Result> where Element : PersistentModel
```

## Relationships

- **Conforms To**: [DynamicProperty](../swiftui/dynamicproperty.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a query

- [init(_:animation:)](<query/init(__animation_).md>) — Create a query with a SwiftData fetch descriptor.
- [init(filter:sort:animation:)](<query/init(filter_sort_animation_).md>) — Create a query with a predicate, and a list of sort descriptors.
- [init(filter:sort:order:animation:)](<query/init(filter_sort_order_animation_)-1qfoj.md>) — Creates a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init(filter:sort:order:animation:)](<query/init(filter_sort_order_animation_)-3qovd.md>) — Creates a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init(_:transaction:)](<query/init(__transaction_).md>) — Create a query with a SwiftData fetch descriptor.
- [init(filter:sort:transaction:)](<query/init(filter_sort_transaction_).md>) — Create a query with a predicate, and a list of sort descriptors.
- [init(filter:sort:order:transaction:)](<query/init(filter_sort_order_transaction_)-2bx9a.md>) — Create a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init(filter:sort:order:transaction:)](<query/init(filter_sort_order_transaction_)-8q7vs.md>) — Create a query with a predicate, a key path to a property for sorting, and the order to sort by.

### Creating an unsorted, sectioned query

- [init(_:animation:sectionBy:)](<query/init(__animation_sectionby_)-2em2m.md>) — Creates a sectioned query from a fetch descriptor, grouped into sections by a String key path. _(beta)_
- [init(_:animation:sectionBy:)](<query/init(__animation_sectionby_)-2pqhv.md>) — Creates a sectioned query from a fetch descriptor, grouped by an optional String key path. _(beta)_
- [init(_:transaction:sectionBy:)](<query/init(__transaction_sectionby_)-5814o.md>) — Creates a sectioned query from a fetch descriptor, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(_:transaction:sectionBy:)](<query/init(__transaction_sectionby_)-9sb87.md>) — Creates a sectioned query from a fetch descriptor, grouped into sections by a String key path. Pass `nil` to disable sectioning. _(beta)_

### Creating a sorted, sectioned query

- [init(filter:sort:animation:sectionBy:)](<query/init(filter_sort_animation_sectionby_)-5wk67.md>) — Creates a sectioned query with sort descriptors, grouped into sections by a String key path. Pass `nil` to disable sectioning. _(beta)_
- [init(filter:sort:animation:sectionBy:)](<query/init(filter_sort_animation_sectionby_)-8e78r.md>) — Creates a sectioned query with sort descriptors, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(filter:sort:order:animation:sectionBy:)](<query/init(filter_sort_order_animation_sectionby_)-2e9oh.md>) — Creates a sectioned query sorted by a key path, grouped by an optional String key path. `nil` values share the empty-string section. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(filter:sort:order:animation:sectionBy:)](<query/init(filter_sort_order_animation_sectionby_)-2e9oh.md>) — Creates a sectioned query sorted by a key path, grouped by an optional String key path. `nil` values share the empty-string section. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(filter:sort:order:animation:sectionBy:)](<query/init(filter_sort_order_animation_sectionby_)-4pdmu.md>) — Creates a sectioned query sorted by an optional key path, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(filter:sort:order:animation:sectionBy:)](<query/init(filter_sort_order_animation_sectionby_)-6b4tq.md>) — Creates a sectioned query sorted by a key path, grouped into sections by a String key path. Pass `nil` to disable sectioning. _(beta)_
- [init(filter:sort:order:animation:sectionBy:)](<query/init(filter_sort_order_animation_sectionby_)-7d51r.md>) — Creates a sectioned query sorted by an optional key path, grouped into sections by a String key path. Pass `nil` to disable sectioning. _(beta)_
- [init(filter:sort:order:transaction:sectionBy:)](<query/init(filter_sort_order_transaction_sectionby_)-5ym3e.md>) — Creates a sectioned query sorted by a key path, grouped into sections by a String key path. Pass `nil` to disable sectioning. _(beta)_
- [init(filter:sort:order:transaction:sectionBy:)](<query/init(filter_sort_order_transaction_sectionby_)-8hx6i.md>) — Creates a sectioned query sorted by an optional key path, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(filter:sort:order:transaction:sectionBy:)](<query/init(filter_sort_order_transaction_sectionby_)-930wx.md>) — Creates a sectioned query sorted by a key path, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(filter:sort:order:transaction:sectionBy:)](<query/init(filter_sort_order_transaction_sectionby_)-l6d4.md>) — Creates a sectioned query sorted by an optional key path, grouped into sections by a String key path. Pass `nil` to disable sectioning. _(beta)_
- [init(filter:sort:transaction:sectionBy:)](<query/init(filter_sort_transaction_sectionby_)-2b0zd.md>) — Creates a sectioned query with sort descriptors, grouped into sections by a String key path. _(beta)_
- [init(filter:sort:transaction:sectionBy:)](<query/init(filter_sort_transaction_sectionby_)-965mg.md>) — Creates a sectioned query with sort descriptors, grouped by an optional String key path. _(beta)_

### Getting query configuration

- [modelContext](query/modelcontext.md) — Current model context `Query` interacts with.
- [fetchError](query/fetcherror.md) — An error encountered during the most recent attempt to fetch data.

### Accessing the value

- [wrappedValue](query/wrappedvalue.md) — The most recent fetched result from the Query.

### Accessing sections

- [sections](query/sections.md) — The sections computed from the current results, grouped by the `sectionBy` key path. _(beta)_
- [ResultsSectionCollection](resultssectioncollection.md) — A collection of sections as returned by [sections](resultsobserver/sections.md) or `Query.sections`. _(beta)_

## See Also

### Model fetch

- [Filtering and sorting persistent data](filtering-and-sorting-persistent-data.md) — Manage data store presentation using predicates and dynamic queries.
- [Query()](<query().md>) — Fetches all instances of the attached model type.
- [Additional query macros](additionalquerymacros.md) — Supplementary macros that enable you to narrow query results and tell SwiftData how to sort, order, and section those results.
- [FetchDescriptor](fetchdescriptor.md) — A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.
