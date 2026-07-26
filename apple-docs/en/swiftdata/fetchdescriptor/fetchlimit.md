---
title: fetchLimit
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/fetchdescriptor/fetchlimit
source_url: 'https://developer.apple.com/documentation/swiftdata/fetchdescriptor/fetchlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/fetchdescriptor/fetchlimit.json'
content_hash: 'sha256:570596cf2283e2b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [FetchDescriptor](../fetchdescriptor.md)

# fetchLimit

<sub>Instance Property</sub>

The maximum number of models the fetch can return.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fetchLimit: Int?
```

## Discussion

> [!important] Important
> Use `nil` to tell the fetch to return all models of the associated type, not `0`.

The default value is `nil`.

## See Also

### Constraining the fetch

- [predicate](predicate.md) — The logical condition that determines whether the fetch includes a specific model in its results.
- [sortBy](sortby.md) — The sort descriptors that tell the fetch how to order its results.
- [fetchOffset](fetchoffset.md) — The offset of the first matching model to fetch.
- [includePendingChanges](includependingchanges.md) — A Boolean value that indicates whether, when the fetch runs, it matches against currently unsaved changes in the model context.
