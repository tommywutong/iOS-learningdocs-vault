---
title: 'willRemove(from:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstore/willremove(from:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/willremove(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/willremove%28from%3A%29.json'
content_hash: 'sha256:b7c605df5ce27ed0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# willRemove(from:)

<sub>Instance Method</sub>

Invoked before the persistent store is removed from the persistent store coordinator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func willRemove(from coordinator: NSPersistentStoreCoordinator?)
```

## Parameters

- `coordinator` — The persistent store coordinator from which the receiver was removed.

## Discussion

The default implementation does nothing. You can override this method in a subclass in order to perform any clean-up before the store is removed from the coordinator (and deallocated).

## See Also

### Responding to the Store Life Cycle

- [- didAddToPersistentStoreCoordinator:](<didadd(to_).md>) — Invoked after the persistent store has been added to the persistent store coordinator.
