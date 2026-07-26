---
title: 'init(_:transaction:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/query/init(_:transaction:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/query/init(_:transaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query/init%28_%3Atransaction%3A%29.json'
content_hash: 'sha256:45e21b984937f79d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Query](../query.md)

# init(_:transaction:)

<sub>Initializer</sub>

Create a query with a SwiftData fetch descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ descriptor: FetchDescriptor<Element>, transaction: Transaction? = nil) where Result == [Element]
```

## Parameters

- `descriptor` — A `SwiftData.FetchDescriptor`.

- `transaction` — A transaction to use for user interface changes that result from changes to the fetched results.

## See Also

### Creating a query

- [init(_:animation:)](<init(__animation_).md>) — Create a query with a SwiftData fetch descriptor.
- [init(filter:sort:animation:)](<init(filter_sort_animation_).md>) — Create a query with a predicate, and a list of sort descriptors.
- [init(filter:sort:order:animation:)](<init(filter_sort_order_animation_)-1qfoj.md>) — Creates a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init(filter:sort:order:animation:)](<init(filter_sort_order_animation_)-3qovd.md>) — Creates a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init(filter:sort:transaction:)](<init(filter_sort_transaction_).md>) — Create a query with a predicate, and a list of sort descriptors.
- [init(filter:sort:order:transaction:)](<init(filter_sort_order_transaction_)-2bx9a.md>) — Create a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init(filter:sort:order:transaction:)](<init(filter_sort_order_transaction_)-8q7vs.md>) — Create a query with a predicate, a key path to a property for sorting, and the order to sort by.
