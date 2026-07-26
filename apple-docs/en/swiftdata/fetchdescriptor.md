---
title: FetchDescriptor
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/fetchdescriptor
source_url: 'https://developer.apple.com/documentation/swiftdata/fetchdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/fetchdescriptor.json'
content_hash: 'sha256:6595651dbc33770f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# FetchDescriptor

<sub>Structure</sub>

A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FetchDescriptor<T> where T : PersistentModel
```

## Overview

Use a fetch descriptor to capture the criteria necessary to select, and optionally sort, a specific collection of models from your app’s persistent storage. A fetch descriptor retrieves only a single type of persistent model, and relies on type inference to determine the appropriate type. However, you can configure a fetch descriptor to prefetch related models of different types using the [relationshipKeyPathsForPrefetching](fetchdescriptor/relationshipkeypathsforprefetching.md) property.

To fetch a collection of models, first create a fetch descriptor and specify a predicate and one or more sort descriptors. The predicate describes the attributes to filter by and the constraints to apply to those attributes. If you don’t specify a predicate, the fetch returns all models of the inferred type. You can further tweak a fetch by limiting the number of models it returns, or indicating whether the fetch evaluates any unsaved changes when it selects the models to return. After configuring the fetch descriptor, pass it to the model context’s [fetch(_:)](<modelcontext/fetch(__).md>) method to run the fetch.

```swift
let descriptor = FetchDescriptor<Recipe>(
    predicate: #Predicate { $0.isFavorite == true },
    sortBy: [
        .init(\.createdAt)
    ]
)
descriptor.fetchLimit = 10

let favoriteRecipes = try modelContext.fetch(descriptor)
```

If you’re displaying the fetched models in a SwiftUI view, use the descriptor with the [Query(_:animation:)](<query(__animation_).md>) macro instead.

```swift
struct FavoriteRecipesList: View {
    static var fetchDescriptor: FetchDescriptor<Recipe> {
        let descriptor = FetchDescriptor<Recipe>(
            predicate: #Predicate { $0.isFavorite == true },
            sortBy: [
                .init(\.createdAt)
            ]
        )
        descriptor.fetchLimit = 10
        return descriptor
    }

    @Query(FavoriteRecipesList.fetchDescriptor) private var favoriteRecipes: [Recipe]
    
    var body: some View {
        List(favoriteRecipes) { RecipeRowView($0) }
    }
} 
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a fetch descriptor

- [init(predicate:sortBy:)](<fetchdescriptor/init(predicate_sortby_).md>) — Creates a fetch descriptor with the specified predicate that, optionally, arranges the fetched models in a particular order.
- [Predicate](../foundation/predicate.md) — A logical condition used to test a set of input values for searching or filtering.
- [SortDescriptor](../foundation/sortdescriptor.md) — A serializable description of how to sort numerics and strings.

### Constraining the fetch

- [predicate](fetchdescriptor/predicate.md) — The logical condition that determines whether the fetch includes a specific model in its results.
- [sortBy](fetchdescriptor/sortby.md) — The sort descriptors that tell the fetch how to order its results.
- [fetchLimit](fetchdescriptor/fetchlimit.md) — The maximum number of models the fetch can return.
- [fetchOffset](fetchdescriptor/fetchoffset.md) — The offset of the first matching model to fetch.
- [includePendingChanges](fetchdescriptor/includependingchanges.md) — A Boolean value that indicates whether, when the fetch runs, it matches against currently unsaved changes in the model context.

### Specifying the fetched attributes

- [relationshipKeyPathsForPrefetching](fetchdescriptor/relationshipkeypathsforprefetching.md) — The key paths that identify any related models to include as part of the fetch.
- [propertiesToFetch](fetchdescriptor/propertiestofetch.md) — The specific subset of attributes to fetch if you don’t require them all.

## See Also

### Model fetch

- [Filtering and sorting persistent data](filtering-and-sorting-persistent-data.md) — Manage data store presentation using predicates and dynamic queries.
- [Query()](<query().md>) — Fetches all instances of the attached model type.
- [Additional query macros](additionalquerymacros.md) — Supplementary macros that enable you to narrow query results and tell SwiftData how to sort, order, and section those results.
- [Query](query.md) — A type that fetches models using the specified criteria, and manages those models so they remain in sync with the underlying data.
