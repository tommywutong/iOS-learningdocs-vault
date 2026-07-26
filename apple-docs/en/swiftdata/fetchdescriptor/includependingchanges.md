---
title: includePendingChanges
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/fetchdescriptor/includependingchanges
source_url: 'https://developer.apple.com/documentation/swiftdata/fetchdescriptor/includependingchanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/fetchdescriptor/includependingchanges.json'
content_hash: 'sha256:4bb1baa46bf7e70e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [FetchDescriptor](../fetchdescriptor.md)

# includePendingChanges

<sub>Instance Property</sub>

A Boolean value that indicates whether, when the fetch runs, it matches against currently unsaved changes in the model context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var includePendingChanges: Bool
```

## Discussion

Set this property’s value to `false` to ignore any unsaved changes in the model context and match against a model’s persisted state instead.

The default value is `true`.

## See Also

### Constraining the fetch

- [predicate](predicate.md) — The logical condition that determines whether the fetch includes a specific model in its results.
- [sortBy](sortby.md) — The sort descriptors that tell the fetch how to order its results.
- [fetchLimit](fetchlimit.md) — The maximum number of models the fetch can return.
- [fetchOffset](fetchoffset.md) — The offset of the first matching model to fetch.
