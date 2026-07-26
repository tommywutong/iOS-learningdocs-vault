---
title: forReplacing
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilecoordinator/writingoptions/forreplacing
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions/forreplacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/writingoptions/forreplacing.json'
content_hash: 'sha256:42ee3fe827c151f4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSFileCoordinator](../../nsfilecoordinator.md) · [WritingOptions](../writingoptions.md)

# forReplacing

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var forReplacing: NSFileCoordinator.WritingOptions { get }
```

## Discussion

Specifies whether the act of writing to the file involves actually replacing the file with a different file (or directory). If the current file coordinator is waiting for another object to move or rename the file, this option treats the operation as the creation of a new file (instead of as the replacement of the old file); otherwise, this constant causes the same behavior as the [NSFileCoordinatorWritingForDeleting](fordeleting.md) constant. Use this method when the moving or creating an item should replace any item currently stored at that location. To avoid a race condition, use it regardless of whether an item is actually in the way before the writing begins. Do not use this method when simply updating the contents of the existing file.

## See Also

### Constants

- [NSFileCoordinatorWritingForDeleting](fordeleting.md)
- [NSFileCoordinatorWritingForMoving](formoving.md)
- [NSFileCoordinatorWritingForMerging](formerging.md)
- [NSFileCoordinatorWritingContentIndependentMetadataOnly](contentindependentmetadataonly.md) — Select this option when writing to change the file’s metadata only and not its contents.
