---
title: 'setURL(_:for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/seturl(_:for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/seturl(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/seturl%28_%3Afor%3A%29.json'
content_hash: 'sha256:c1a5daacd92574c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# setURL(_:for:)

<sub>Instance Method</sub>

Changes the location of the specified persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setURL(_ url: URL, for store: NSPersistentStore) -> Bool
```

## Parameters

- `url` — The new location for `store`.

- `store` — A persistent store associated with the receiver.

## Return Value

[true](../../swift/true.md) if the store was relocated, otherwise [false](../../swift/false.md).

## Discussion

For atomic stores, this method alters the location to which the next save operation will write the file; for non-atomic stores, invoking this method will relinquish the existing connection and create a new one at the specified URL. (For non-atomic stores, a store must already exist at the destination URL; a new store will not be created.)

## See Also

### Managing a store’s location

- [- persistentStoreForURL:](<persistentstore(for_).md>) — Returns the persistent store for the specified file URL.
- [- URLForPersistentStore:](<url(for_).md>) — Returns the location of the provided persistent store.
