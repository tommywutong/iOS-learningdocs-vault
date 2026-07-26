---
title: forUploading
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilecoordinator/readingoptions/foruploading
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions/foruploading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/readingoptions/foruploading.json'
content_hash: 'sha256:9d614efb6bc2fa74'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSFileCoordinator](../../nsfilecoordinator.md) · [ReadingOptions](../readingoptions.md)

# forUploading

<sub>Type Property</sub>

Specify this content when reading an item for the purpose of uploading its contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var forUploading: NSFileCoordinator.ReadingOptions { get }
```

## Discussion

When this option is used, the file coordinator creates a temporary snapshot of the item being read and relinquishes its claim on the original file. This action prevents the read operation from blocking other coordinated writes during a potentially long upload.

If the item being read is a directory (such as a document package), then the snapshot is a new file containing the zipped contents of the directory. The URL passed to the accessor block points to the zipped file.

When using this option, you may upload the document outside the accessor block. However, you should open a file descriptor to the file or relocate the file within the accessor block before doing so. The file coordinator unlinks the file after the block returns, rendering it inaccessible through the URL.

## See Also

### Constants

- [NSFileCoordinatorReadingWithoutChanges](withoutchanges.md)
- [NSFileCoordinatorReadingResolvesSymbolicLink](resolvessymboliclink.md)
- [NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly](immediatelyavailablemetadataonly.md) — Specify this constant if you want to read an item’s metadata without triggering a download.
