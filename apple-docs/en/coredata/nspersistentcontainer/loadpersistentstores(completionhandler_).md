---
title: 'loadPersistentStores(completionHandler:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcontainer/loadpersistentstores(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/loadpersistentstores(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/loadpersistentstores%28completionhandler%3A%29.json'
content_hash: 'sha256:4db32a6689ba3d5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# loadPersistentStores(completionHandler:)

<sub>Instance Method</sub>

Loads the persistent stores.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadPersistentStores(completionHandler block: @escaping (NSPersistentStoreDescription, (any Error)?) -> Void)
```

## Parameters

- `block` — Once the loading of the persistent stores has completed, this block will be executed on the calling thread.

## Discussion

Once the persistent container has been initialized, you need to execute [- loadPersistentStoresWithCompletionHandler:](<loadpersistentstores(completionhandler_).md>) to instruct the container to load the persistent stores and complete the creation of the Core Data stack.

Once the completion handler has fired, the stack is fully initialized and is ready for use. The completion handler will be called once for each persistent store that is created.

If there is an error in the loading of the persistent stores, the [NSError](../../foundation/nserror.md) value will be populated.

## See Also

### Managing Persistent Stores

- [persistentStoreDescriptions](persistentstoredescriptions.md) — The descriptions of the container’s persistent stores.
