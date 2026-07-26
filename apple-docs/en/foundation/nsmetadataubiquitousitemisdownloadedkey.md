---
title: NSMetadataUbiquitousItemIsDownloadedKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+（7.0 起废弃）, iPadOS 5.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsmetadataubiquitousitemisdownloadedkey
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisdownloadedkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataubiquitousitemisdownloadedkey.json'
content_hash: 'sha256:03280cb076a7e5a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMetadataUbiquitousItemIsDownloadedKey

<sub>Global Variable</sub>

> [!warning] Deprecated
> Use NSMetadataUbiquitousItemDownloadingStatusKey instead

<sub>tvOS, visionOS, watchOS</sub>

```swift
let NSMetadataUbiquitousItemIsDownloadedKey: String
```

## Discussion

The value is an [NSNumber](nsnumber.md) object that contains a Boolean indicating whether the current version of the item has been downloaded and is available locally.

This constant is deprecated in iOS 7 and OS X v10.9; use [NSMetadataUbiquitousItemDownloadingStatusKey](nsmetadataubiquitousitemdownloadingstatuskey.md) instead.

## See Also

### iCloud Keys

- [NSMetadataItemIsUbiquitousKey](nsmetadataitemisubiquitouskey.md)
- [NSMetadataUbiquitousItemContainerDisplayNameKey](nsmetadataubiquitousitemcontainerdisplaynamekey.md) — The display name of the container that stores the ubiquitous item.
- [NSMetadataUbiquitousItemDownloadRequestedKey](nsmetadataubiquitousitemdownloadrequestedkey.md) — A Boolean value indicating whether a download has been requested for the ubiquitous item.
- [NSMetadataUbiquitousItemIsExternalDocumentKey](nsmetadataubiquitousitemisexternaldocumentkey.md) — A Boolean value indicating whether the ubiquitous item is from an external document.
- [NSMetadataUbiquitousItemURLInLocalContainerKey](nsmetadataubiquitousitemurlinlocalcontainerkey.md) — The URL for the ubiquitous item in the local container.
- [NSMetadataUbiquitousItemHasUnresolvedConflictsKey](nsmetadataubiquitousitemhasunresolvedconflictskey.md)
- [NSMetadataUbiquitousItemIsDownloadingKey](nsmetadataubiquitousitemisdownloadingkey.md)
- [NSMetadataUbiquitousItemIsUploadedKey](nsmetadataubiquitousitemisuploadedkey.md)
- [NSMetadataUbiquitousItemIsUploadingKey](nsmetadataubiquitousitemisuploadingkey.md)
- [NSMetadataUbiquitousItemPercentDownloadedKey](nsmetadataubiquitousitempercentdownloadedkey.md)
- [NSMetadataUbiquitousItemPercentUploadedKey](nsmetadataubiquitousitempercentuploadedkey.md)
- [NSMetadataUbiquitousItemDownloadingStatusKey](nsmetadataubiquitousitemdownloadingstatuskey.md)
- [NSMetadataUbiquitousItemDownloadingErrorKey](nsmetadataubiquitousitemdownloadingerrorkey.md)
- [NSMetadataUbiquitousItemUploadingErrorKey](nsmetadataubiquitousitemuploadingerrorkey.md)
- [NSMetadataUbiquitousItemIsSharedKey](nsmetadataubiquitousitemissharedkey.md) — A Boolean value indicating whether the ubiquitous item is shared.
