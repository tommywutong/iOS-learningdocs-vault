---
title: kCFURLUbiquitousItemIsDownloadedKey
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+（7.0 起废弃）, iPadOS 5.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/kcfurlubiquitousitemisdownloadedkey
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemisdownloadedkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfurlubiquitousitemisdownloadedkey.json'
content_hash: 'sha256:329d4938b5e734b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFURLUbiquitousItemIsDownloadedKey

<sub>Global Variable</sub>

A `CFBoolean` value that tells whether there is local data present for the item. (read-only)

> [!warning] Deprecated
> Use kCFURLUbiquitousItemDownloadingStatusKey instead

<sub>tvOS, visionOS, watchOS</sub>

```swift
let kCFURLUbiquitousItemIsDownloadedKey: CFString!
```

## See Also

### Constants

- [kCFURLIsUbiquitousItemKey](kcfurlisubiquitousitemkey.md) — A `CFBoolean` value that tells whether the item is synced to the cloud. (read-only)
- [kCFURLUbiquitousItemHasUnresolvedConflictsKey](kcfurlubiquitousitemhasunresolvedconflictskey.md) — A `CFBoolean` value that tells whether the item has conflicts outstanding. (read-only)
- [kCFURLUbiquitousItemIsDownloadingKey](kcfurlubiquitousitemisdownloadingkey.md) — A `CFBoolean` value that tells whether data for the item is being downloaded. (read-only)
- [kCFURLUbiquitousItemIsUploadedKey](kcfurlubiquitousitemisuploadedkey.md) — A `CFBoolean` value that tells whether there is data present in the cloud for this item. (read-only)
- [kCFURLUbiquitousItemIsUploadingKey](kcfurlubiquitousitemisuploadingkey.md) — A `CFBoolean` value that tells whether data for the item is being uploaded. (read-only)
- [kCFURLUbiquitousItemPercentDownloadedKey](kcfurlubiquitousitempercentdownloadedkey.md) _(deprecated)_
- [kCFURLUbiquitousItemPercentUploadedKey](kcfurlubiquitousitempercentuploadedkey.md) _(deprecated)_
