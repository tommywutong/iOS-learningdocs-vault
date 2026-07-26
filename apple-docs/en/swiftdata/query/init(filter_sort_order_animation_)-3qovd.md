---
title: 'init(filter:sort:order:animation:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/query/init(filter:sort:order:animation:)-3qovd'
source_url: 'https://developer.apple.com/documentation/swiftdata/query/init(filter:sort:order:animation:)-3qovd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query/init%28filter%3Asort%3Aorder%3Aanimation%3A%29-3qovd.json'
content_hash: 'sha256:65a51e72340145bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Query](../query.md)

# init(filter:sort:order:animation:)

<sub>Initializer</sub>

Creates a query with a predicate, a key path to a property for sorting, and the order to sort by.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init<Value>(filter: Predicate<Element>? = nil, sort keyPath: KeyPath<Element, Value>, order: SortOrder = .forward, animation: Animation) where Result == [Element], Value : Comparable
```

## Parameters

- `filter` — A predicate on `Element`

- `sort` — Key path to property used for sorting.

- `order` — Whether to sort in forward or reverse order.

- `animation` — The animation to use for user interface changes that result from changes to the fetched results.

## Discussion

Use `Query` within a view by wrapping the variable for the query’s result:

```swift
struct RecipeList: View {
    // Recipes sorted by date of creation
    @Query(sort: \.dateCreated)
    var favoriteRecipes: [Recipe]

    var body: some View {
        List(favoriteRecipes) { RecipeDetails($0) }
    }
}
```

## See Also

### Creating a query

- [init(_:animation:)](<init(__animation_).md>) — Create a query with a SwiftData fetch descriptor.
- [init(filter:sort:animation:)](<init(filter_sort_animation_).md>) — Create a query with a predicate, and a list of sort descriptors.
- [init(filter:sort:order:animation:)](<init(filter_sort_order_animation_)-1qfoj.md>) — Creates a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init(_:transaction:)](<init(__transaction_).md>) — Create a query with a SwiftData fetch descriptor.
- [init(filter:sort:transaction:)](<init(filter_sort_transaction_).md>) — Create a query with a predicate, and a list of sort descriptors.
- [init(filter:sort:order:transaction:)](<init(filter_sort_order_transaction_)-2bx9a.md>) — Create a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init(filter:sort:order:transaction:)](<init(filter_sort_order_transaction_)-8q7vs.md>) — Create a query with a predicate, a key path to a property for sorting, and the order to sort by.
