---
title: resolvesSymbolicLink
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilecoordinator/readingoptions/resolvessymboliclink
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions/resolvessymboliclink'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/readingoptions/resolvessymboliclink.json'
content_hash: 'sha256:3223ce47915b3110'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSFileCoordinator](../../nsfilecoordinator.md) · [ReadingOptions](../readingoptions.md)

# resolvesSymbolicLink

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var resolvesSymbolicLink: NSFileCoordinator.ReadingOptions { get }
```

## Discussion

Specify this constant if you want an item that might be a symbolic link to resolve to the file pointed to by that link (instead of to the link itself). When you use this option, the system provides the resolved URL to the accessor block in place of the original URL.

> [!note] Note
> This option cannot be used with the [- prepareForReadingItemsAtURLs:options:writingItemsAtURLs:options:error:byAccessor:](<../prepare(forreadingitemsat_options_writingitemsat_options_error_byaccessor_).md>) method.

## See Also

### Constants

- [NSFileCoordinatorReadingWithoutChanges](withoutchanges.md)
- [NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly](immediatelyavailablemetadataonly.md) — Specify this constant if you want to read an item’s metadata without triggering a download.
- [NSFileCoordinatorReadingForUploading](foruploading.md) — Specify this content when reading an item for the purpose of uploading its contents.
