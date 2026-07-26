---
title: 'url(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/url(for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/url(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/url%28for%3A%29.json'
content_hash: 'sha256:3b5e1f5aa2916217'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# url(for:)

<sub>Instance Method</sub>

Returns the location of the provided persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func url(for store: NSPersistentStore) -> URL
```

## Parameters

- `store` — A persistent store.

## Return Value

The URL for `store`.

## See Also

### Related Documentation

- [persistentStores](persistentstores.md) — The coordinator’s persistent stores.

### Managing a store’s location

- [- setURL:forPersistentStore:](<seturl(__for_).md>) — Changes the location of the specified persistent store.
- [- persistentStoreForURL:](<persistentstore(for_).md>) — Returns the persistent store for the specified file URL.
