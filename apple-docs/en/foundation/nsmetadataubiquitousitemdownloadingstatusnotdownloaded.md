---
title: NSMetadataUbiquitousItemDownloadingStatusNotDownloaded
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataubiquitousitemdownloadingstatusnotdownloaded
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemdownloadingstatusnotdownloaded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataubiquitousitemdownloadingstatusnotdownloaded.json'
content_hash: 'sha256:d460e481b2335658'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMetadataUbiquitousItemDownloadingStatusNotDownloaded

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSMetadataUbiquitousItemDownloadingStatusNotDownloaded: String
```

## Discussion

A string used as the value for [NSMetadataUbiquitousItemPercentUploadedKey](nsmetadataubiquitousitempercentuploadedkey.md) to indicate that this item has not been downloaded yet.

You can use [- startDownloadingUbiquitousItemAtURL:error:](<filemanager/startdownloadingubiquitousitem(at_).md>) to download the item.

## See Also

### iCloud Download Status Values

- [NSMetadataUbiquitousItemDownloadingStatusCurrent](nsmetadataubiquitousitemdownloadingstatuscurrent.md)
- [NSMetadataUbiquitousItemDownloadingStatusDownloaded](nsmetadataubiquitousitemdownloadingstatusdownloaded.md)
