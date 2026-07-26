---
title: ubiquitousItemPercentUploadedKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+（6.0 起废弃）, iPadOS 5.0+（6.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlresourcekey/ubiquitousitempercentuploadedkey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/ubiquitousitempercentuploadedkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/ubiquitousitempercentuploadedkey.json'
content_hash: 'sha256:b415788057b087ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# ubiquitousItemPercentUploadedKey

<sub>Type Property</sub>

The key for a value that indicates the percentage of data that the system uploaded to iCloud storage.

> [!warning] Deprecated
> Use the [NSMetadataQuery](../nsmetadataquery.md) class to search for [NSMetadataItem](../nsmetadataitem.md) objects that have the [NSMetadataUbiquitousItemPercentUploadedKey](../nsmetadataubiquitousitempercentuploadedkey.md) attribute instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
static let ubiquitousItemPercentUploadedKey: URLResourceKey
```

## See Also

### Deprecated

- [NSURLUbiquitousItemIsDownloadedKey](ubiquitousitemisdownloadedkey.md) — The key for a Boolean value that indicates whether the system downloaded this item’s data from iCloud storage. _(deprecated)_
- [NSURLUbiquitousItemPercentDownloadedKey](ubiquitousitempercentdownloadedkey.md) — The key for a value that indicates the percentage of data that the system downloaded from iCloud storage. _(deprecated)_
