---
title: predicate
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/fetchdescriptor/predicate
source_url: 'https://developer.apple.com/documentation/swiftdata/fetchdescriptor/predicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/fetchdescriptor/predicate.json'
content_hash: 'sha256:54b25d077151c9ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [FetchDescriptor](../fetchdescriptor.md)

# predicate

<sub>Instance Property</sub>

The logical condition that determines whether the fetch includes a specific model in its results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var predicate: Predicate<T>?
```

## Discussion

Use this property to replace or remove the fetch descriptor’s predicate. If the value is `nil`, any fetch using the descriptor will return all models of the associated type.

The default value is the predicate you specify when calling [init(predicate:sortBy:)](<init(predicate_sortby_).md>).

## See Also

### Constraining the fetch

- [sortBy](sortby.md) — The sort descriptors that tell the fetch how to order its results.
- [fetchLimit](fetchlimit.md) — The maximum number of models the fetch can return.
- [fetchOffset](fetchoffset.md) — The offset of the first matching model to fetch.
- [includePendingChanges](includependingchanges.md) — A Boolean value that indicates whether, when the fetch runs, it matches against currently unsaved changes in the model context.
