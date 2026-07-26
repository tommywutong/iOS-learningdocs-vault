---
title: kCFURLUbiquitousItemPercentDownloadedKey
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+（6.0 起废弃）, iPadOS 5.0+（6.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/kcfurlubiquitousitempercentdownloadedkey
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitempercentdownloadedkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfurlubiquitousitempercentdownloadedkey.json'
content_hash: 'sha256:5751dea1277631e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFURLUbiquitousItemPercentDownloadedKey

<sub>Global Variable</sub>

> [!warning] Deprecated
> Use NSMetadataQuery and NSMetadataUbiquitousItemPercentDownloadedKey on NSMetadataItem instead

<sub>tvOS, visionOS, watchOS</sub>

```swift
let kCFURLUbiquitousItemPercentDownloadedKey: CFString!
```

## Discussion

A `CFNumber` value that provides the status of the download in progress.

Deprecated. Use [NSMetadataQuery](../foundation/nsmetadataquery.md) and [NSMetadataUbiquitousItemPercentDownloadedKey](../foundation/nsmetadataubiquitousitempercentdownloadedkey.md) on [NSMetadataItem](../foundation/nsmetadataitem.md) instead.

## See Also

### Constants

- [kCFURLIsUbiquitousItemKey](kcfurlisubiquitousitemkey.md) — A `CFBoolean` value that tells whether the item is synced to the cloud. (read-only)
- [kCFURLUbiquitousItemHasUnresolvedConflictsKey](kcfurlubiquitousitemhasunresolvedconflictskey.md) — A `CFBoolean` value that tells whether the item has conflicts outstanding. (read-only)
- [kCFURLUbiquitousItemIsDownloadedKey](kcfurlubiquitousitemisdownloadedkey.md) — A `CFBoolean` value that tells whether there is local data present for the item. (read-only) _(deprecated)_
- [kCFURLUbiquitousItemIsDownloadingKey](kcfurlubiquitousitemisdownloadingkey.md) — A `CFBoolean` value that tells whether data for the item is being downloaded. (read-only)
- [kCFURLUbiquitousItemIsUploadedKey](kcfurlubiquitousitemisuploadedkey.md) — A `CFBoolean` value that tells whether there is data present in the cloud for this item. (read-only)
- [kCFURLUbiquitousItemIsUploadingKey](kcfurlubiquitousitemisuploadingkey.md) — A `CFBoolean` value that tells whether data for the item is being uploaded. (read-only)
- [kCFURLUbiquitousItemPercentUploadedKey](kcfurlubiquitousitempercentuploadedkey.md) _(deprecated)_
