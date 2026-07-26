---
title: immediatelyAvailableMetadataOnly
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilecoordinator/readingoptions/immediatelyavailablemetadataonly
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions/immediatelyavailablemetadataonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/readingoptions/immediatelyavailablemetadataonly.json'
content_hash: 'sha256:c9ff367eb377341a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSFileCoordinator](../../nsfilecoordinator.md) · [ReadingOptions](../readingoptions.md)

# immediatelyAvailableMetadataOnly

<sub>Type Property</sub>

Specify this constant if you want to read an item’s metadata without triggering a download.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var immediatelyAvailableMetadataOnly: NSFileCoordinator.ReadingOptions { get }
```

## Discussion

Specifying this option grants the coordinated read immediately (barring any conflicts with other readers, writers or file presenters on the same system), instead of waiting for the system to download the file’s contents and any additional metadata (for example, conflicting versions or thumbnails).

Attempting to actually read the item’s contents during this coordinated read may give unexpected results or fail.

## See Also

### Constants

- [NSFileCoordinatorReadingWithoutChanges](withoutchanges.md)
- [NSFileCoordinatorReadingResolvesSymbolicLink](resolvessymboliclink.md)
- [NSFileCoordinatorReadingForUploading](foruploading.md) — Specify this content when reading an item for the purpose of uploading its contents.
