---
title: downloadDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetricdownloadsummaryevent/downloadduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetricdownloadsummaryevent/downloadduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetricdownloadsummaryevent/downloadduration.json'
content_hash: 'sha256:827f9fc0b2b23c57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetricDownloadSummaryEvent](../avmetricdownloadsummaryevent.md)

# downloadDuration

<sub>Instance Property</sub>

Returns the total duration of the download in seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var downloadDuration: TimeInterval { get }
```

## See Also

### Inspecting the download summary

- [bytesDownloadedCount](bytesdownloadedcount.md) — Returns the total number of bytes downloaded by the download task.
- [mediaResourceRequestCount](mediaresourcerequestcount.md) — Returns the total number of media requests performed by the download task. This includes playlist requests, media segment requests, and content key requests.
- [recoverableErrorCount](recoverableerrorcount.md) — Returns the total count of recoverable errors encountered during the download. If no errors were encountered, returns 0.
- [variants](variants.md) — Returns the variants that were downloaded.
- [errorEvent](errorevent.md) — Returns the error event if any. If no value is available, returns nil.
