---
title: fetchError
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/query/fetcherror
source_url: 'https://developer.apple.com/documentation/swiftdata/query/fetcherror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query/fetcherror.json'
content_hash: 'sha256:b0c851af52b1a731'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Query](../query.md)

# fetchError

<sub>Instance Property</sub>

An error encountered during the most recent attempt to fetch data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var fetchError: (any Error)? { get }
```

## Discussion

This value is `nil` unless an fetch attempt failed. It contains the latest error from SwiftData. Access it from Query’s stored property:

```swift
struct RecipeList: View {
    @Query var recipes: [Recipe]
    var body: some View {
        ErrorIndicatorView(_recipes.fetchError)
    }
}
```

> [!note] Note
> Only access this property within of a view’s `body` property, otherwise its value may be invalid.

> [!note] Note
> When an fetch error occurs, `wrappedValue` retains results from the last successful fetch. Its value will update once a new fetch succeeds.

## See Also

### Getting query configuration

- [modelContext](modelcontext.md) — Current model context `Query` interacts with.
