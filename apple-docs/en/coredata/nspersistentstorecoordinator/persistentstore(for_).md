---
title: 'persistentStore(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/persistentstore(for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/persistentstore(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/persistentstore%28for%3A%29.json'
content_hash: 'sha256:b1ba59923ba907f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# persistentStore(for:)

<sub>Instance Method</sub>

Returns the persistent store for the specified file URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func persistentStore(for URL: URL) -> NSPersistentStore?
```

## Parameters

- `URL` — An URL object that specifies the location of a persistent store.

## Return Value

The persistent store at the location specified by `URL`.

## See Also

### Managing a store’s location

- [- setURL:forPersistentStore:](<seturl(__for_).md>) — Changes the location of the specified persistent store.
- [- URLForPersistentStore:](<url(for_).md>) — Returns the location of the provided persistent store.
