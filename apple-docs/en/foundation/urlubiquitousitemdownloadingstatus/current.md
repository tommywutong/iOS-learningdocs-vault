---
title: current
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlubiquitousitemdownloadingstatus/current
source_url: 'https://developer.apple.com/documentation/foundation/urlubiquitousitemdownloadingstatus/current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlubiquitousitemdownloadingstatus/current.json'
content_hash: 'sha256:fd103c282430bd9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLUbiquitousItemDownloadingStatus](../urlubiquitousitemdownloadingstatus.md)

# current

<sub>Type Property</sub>

A local copy of this item exists and is the most up-to-date version known to the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let current: URLUbiquitousItemDownloadingStatus
```

## See Also

### Constants

- [NSURLUbiquitousItemDownloadingStatusDownloaded](downloaded.md) — A local copy of this item exists, but it is stale. The most recent version will be downloaded as soon as possible.
- [NSURLUbiquitousItemDownloadingStatusNotDownloaded](notdownloaded.md) — This item has not been downloaded yet. Use [- startDownloadingUbiquitousItemAtURL:error:](<../filemanager/startdownloadingubiquitousitem(at_).md>) to download it.
