---
title: 'didAdd(to:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstore/didadd(to:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/didadd(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/didadd%28to%3A%29.json'
content_hash: 'sha256:f191d67a45254323'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# didAdd(to:)

<sub>Instance Method</sub>

Invoked after the persistent store has been added to the persistent store coordinator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func didAdd(to coordinator: NSPersistentStoreCoordinator)
```

## Parameters

- `coordinator` — The persistent store coordinator to which the receiver was added.

## Discussion

The default implementation does nothing. You can override this method in a subclass in order to perform any kind of setup necessary before the load method is invoked.

## See Also

### Responding to the Store Life Cycle

- [- willRemoveFromPersistentStoreCoordinator:](<willremove(from_).md>) — Invoked before the persistent store is removed from the persistent store coordinator.
