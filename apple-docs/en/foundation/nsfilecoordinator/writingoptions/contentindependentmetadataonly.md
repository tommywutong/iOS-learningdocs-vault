---
title: contentIndependentMetadataOnly
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilecoordinator/writingoptions/contentindependentmetadataonly
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions/contentindependentmetadataonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/writingoptions/contentindependentmetadataonly.json'
content_hash: 'sha256:bc7ebab8301bbac2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSFileCoordinator](../../nsfilecoordinator.md) · [WritingOptions](../writingoptions.md)

# contentIndependentMetadataOnly

<sub>Type Property</sub>

Select this option when writing to change the file’s metadata only and not its contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var contentIndependentMetadataOnly: NSFileCoordinator.WritingOptions { get }
```

## Discussion

Any changes written to the item’s contents during this coordinated write may not be preserved or may fail. Changing metadata that is related to the item’s content is also not supported, and those changes may not be preserved. For example, changing the value of [NSURLTagNamesKey](../../urlresourcekey/tagnameskey.md) is supported, but changing the value of [NSURLContentModificationDateKey](../../urlresourcekey/contentmodificationdatekey.md) is not.

## See Also

### Constants

- [NSFileCoordinatorWritingForDeleting](fordeleting.md)
- [NSFileCoordinatorWritingForMoving](formoving.md)
- [NSFileCoordinatorWritingForMerging](formerging.md)
- [NSFileCoordinatorWritingForReplacing](forreplacing.md)
