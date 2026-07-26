---
title: notDownloaded
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlubiquitousitemdownloadingstatus/notdownloaded
source_url: 'https://developer.apple.com/documentation/foundation/urlubiquitousitemdownloadingstatus/notdownloaded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlubiquitousitemdownloadingstatus/notdownloaded.json'
content_hash: 'sha256:d9814d72924ade07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLUbiquitousItemDownloadingStatus](../urlubiquitousitemdownloadingstatus.md)

# notDownloaded

<sub>Type Property</sub>

This item has not been downloaded yet. Use [- startDownloadingUbiquitousItemAtURL:error:](<../filemanager/startdownloadingubiquitousitem(at_).md>) to download it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let notDownloaded: URLUbiquitousItemDownloadingStatus
```

## See Also

### Constants

- [NSURLUbiquitousItemDownloadingStatusCurrent](current.md) — A local copy of this item exists and is the most up-to-date version known to the device.
- [NSURLUbiquitousItemDownloadingStatusDownloaded](downloaded.md) — A local copy of this item exists, but it is stale. The most recent version will be downloaded as soon as possible.
