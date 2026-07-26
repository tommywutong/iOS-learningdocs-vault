---
title: withoutChanges
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilecoordinator/readingoptions/withoutchanges
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions/withoutchanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/readingoptions/withoutchanges.json'
content_hash: 'sha256:9fdb99e00eec4209'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSFileCoordinator](../../nsfilecoordinator.md) · [ReadingOptions](../readingoptions.md)

# withoutChanges

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var withoutChanges: NSFileCoordinator.ReadingOptions { get }
```

## Discussion

Specify this constant if your code does not need other objects to save changes first. If you do _not_ specify this constant, the [- savePresentedItemChangesWithCompletionHandler:](<../../nsfilepresenter/savepresenteditemchanges(completionhandler_).md>) method of relevant file presenters is called before your code reads the item.

## See Also

### Constants

- [NSFileCoordinatorReadingResolvesSymbolicLink](resolvessymboliclink.md)
- [NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly](immediatelyavailablemetadataonly.md) — Specify this constant if you want to read an item’s metadata without triggering a download.
- [NSFileCoordinatorReadingForUploading](foruploading.md) — Specify this content when reading an item for the purpose of uploading its contents.
