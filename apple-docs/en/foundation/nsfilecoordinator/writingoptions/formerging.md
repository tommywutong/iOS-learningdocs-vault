---
title: forMerging
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilecoordinator/writingoptions/formerging
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions/formerging'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/writingoptions/formerging.json'
content_hash: 'sha256:09ea82a8ee1a6c88'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSFileCoordinator](../../nsfilecoordinator.md) · [WritingOptions](../writingoptions.md)

# forMerging

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var forMerging: NSFileCoordinator.WritingOptions { get }
```

## Discussion

When this constant is specified, the file coordinator calls the [- savePresentedItemChangesWithCompletionHandler:](<../../nsfilepresenter/savepresenteditemchanges(completionhandler_).md>) method of relevant file presenters to give them a chance to save their changes before your code makes its changes.

## See Also

### Constants

- [NSFileCoordinatorWritingForDeleting](fordeleting.md)
- [NSFileCoordinatorWritingForMoving](formoving.md)
- [NSFileCoordinatorWritingForReplacing](forreplacing.md)
- [NSFileCoordinatorWritingContentIndependentMetadataOnly](contentindependentmetadataonly.md) — Select this option when writing to change the file’s metadata only and not its contents.
