---
title: propertiesToFetch
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/fetchdescriptor/propertiestofetch
source_url: 'https://developer.apple.com/documentation/swiftdata/fetchdescriptor/propertiestofetch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/fetchdescriptor/propertiestofetch.json'
content_hash: 'sha256:8669e95927fcb3f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [FetchDescriptor](../fetchdescriptor.md)

# propertiesToFetch

<sub>Instance Property</sub>

The specific subset of attributes to fetch if you don’t require them all.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var propertiesToFetch: [PartialKeyPath<T>]
```

## Discussion

If you know ahead of time that you’re going to process (or display) a subset of a model’s attributes, use this property to provide the key paths of those attributes. When the fetch runs, it’ll return values for only the specified key paths, which may result in faster and more efficient fetches. However, if you subsequently access a nonfetched attribute, you’ll incur the additional overhead of fetching the corresponding value from the persistent storage.

> [!note] Note
> An empty array causes the fetch to include all attributes, not none.

The default value is an empty array.

## See Also

### Specifying the fetched attributes

- [relationshipKeyPathsForPrefetching](relationshipkeypathsforprefetching.md) — The key paths that identify any related models to include as part of the fetch.
