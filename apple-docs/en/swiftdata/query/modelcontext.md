---
title: modelContext
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/query/modelcontext
source_url: 'https://developer.apple.com/documentation/swiftdata/query/modelcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query/modelcontext.json'
content_hash: 'sha256:1189185bf5c363be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Query](../query.md)

# modelContext

<sub>Instance Property</sub>

Current model context `Query` interacts with.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var modelContext: ModelContext { get }
```

## Discussion

Access this value from `Query` property wrapper’s stored property:

```swift
struct RecipeList: View {
    @Query var recipes: [Recipe]
    var body: some View {
        ChangesIndicator(
            hasChanges: _recipes.modelContext.hasChanges)
    }
}
```

Only access this property within of a view’s `body` property, otherwise its value may be invalid.

## See Also

### Getting query configuration

- [fetchError](fetcherror.md) — An error encountered during the most recent attempt to fetch data.
