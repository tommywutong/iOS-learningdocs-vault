---
title: fetchOffset
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/fetchdescriptor/fetchoffset
source_url: 'https://developer.apple.com/documentation/swiftdata/fetchdescriptor/fetchoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/fetchdescriptor/fetchoffset.json'
content_hash: 'sha256:44d767e7fcd28766'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [FetchDescriptor](../fetchdescriptor.md)

# fetchOffset

<sub>Instance Property</sub>

The offset of the first matching model to fetch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fetchOffset: Int?
```

## Discussion

Use this property to skip a number of models that the fetch would otherwise return. For example, given a fetch that typically returns A, B, C, and D, specifying a fetch offset of 1 will return B, C, D, and a fetch offset of 4 will return an empty set of results. In combination with [fetchLimit](fetchlimit.md), you can create a subrange of an arbitrary result set.

The default value is `0`.

## See Also

### Constraining the fetch

- [predicate](predicate.md) — The logical condition that determines whether the fetch includes a specific model in its results.
- [sortBy](sortby.md) — The sort descriptors that tell the fetch how to order its results.
- [fetchLimit](fetchlimit.md) — The maximum number of models the fetch can return.
- [includePendingChanges](includependingchanges.md) — A Boolean value that indicates whether, when the fetch runs, it matches against currently unsaved changes in the model context.
