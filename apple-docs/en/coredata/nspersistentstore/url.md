---
title: url
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstore/url
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/url.json'
content_hash: 'sha256:ffb3c56205d9049d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# url

<sub>Instance Property</sub>

The URL for the persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var url: URL? { get set }
```

## Discussion

To alter the location of a store, send the persistent store coordinator a [- setURL:forPersistentStore:](<../nspersistentstorecoordinator/seturl(__for_).md>) message.

## See Also

### Managing Store Attributes

- [identifier](identifier.md) — The unique identifier for the persistent store.
- [readOnly](isreadonly.md) — A Boolean value that indicates whether the persistent store is read-only.
