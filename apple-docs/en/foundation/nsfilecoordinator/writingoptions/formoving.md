---
title: forMoving
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilecoordinator/writingoptions/formoving
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions/formoving'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/writingoptions/formoving.json'
content_hash: 'sha256:4c6ca76f709123f4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSFileCoordinator](../../nsfilecoordinator.md) · [WritingOptions](../writingoptions.md)

# forMoving

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var forMoving: NSFileCoordinator.WritingOptions { get }
```

## Discussion

When specified for a directory item, the file coordinator waits for already running read and write operations of the directory’s contents, which were themselves initiated through a file coordinator, to finish before moving the directory. Queued, but not executing, read and write operations on the directory’s contents wait until the move operation finishes.

This option has no effect on files. You can safely use it when moving file-system items without checking to see whether those items are files or directories.

## See Also

### Constants

- [NSFileCoordinatorWritingForDeleting](fordeleting.md)
- [NSFileCoordinatorWritingForMerging](formerging.md)
- [NSFileCoordinatorWritingForReplacing](forreplacing.md)
- [NSFileCoordinatorWritingContentIndependentMetadataOnly](contentindependentmetadataonly.md) — Select this option when writing to change the file’s metadata only and not its contents.
