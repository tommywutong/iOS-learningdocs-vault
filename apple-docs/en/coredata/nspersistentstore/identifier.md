---
title: identifier
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstore/identifier
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/identifier.json'
content_hash: 'sha256:e6f09a65f05590b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# identifier

<sub>Instance Property</sub>

The unique identifier for the persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var identifier: String! { get set }
```

## Discussion

The identifier is used as part of the managed object IDs for each object in the store.

### Special Considerations

`NSPersistentStore` provides a default implementation to provide a globally unique identifier for the store instance.

## See Also

### Related Documentation

- [metadata](metadata.md) — The metadata for the persistent store.

### Managing Store Attributes

- [readOnly](isreadonly.md) — A Boolean value that indicates whether the persistent store is read-only.
- [URL](url.md) — The URL for the persistent store.
