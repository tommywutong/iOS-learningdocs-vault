---
title: recoverableErrorCount
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetricdownloadsummaryevent/recoverableerrorcount
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetricdownloadsummaryevent/recoverableerrorcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetricdownloadsummaryevent/recoverableerrorcount.json'
content_hash: 'sha256:c0186b6da5338a08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetricDownloadSummaryEvent](../avmetricdownloadsummaryevent.md)

# recoverableErrorCount

<sub>Instance Property</sub>

Returns the total count of recoverable errors encountered during the download. If no errors were encountered, returns 0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var recoverableErrorCount: Int { get }
```

## Discussion

Error counts may not be consistent across OS versions. Comparisons should be made within a given OS version, as error reporting is subject to change with OS updates.

## See Also

### Inspecting the download summary

- [downloadDuration](downloadduration.md) — Returns the total duration of the download in seconds.
- [bytesDownloadedCount](bytesdownloadedcount.md) — Returns the total number of bytes downloaded by the download task.
- [mediaResourceRequestCount](mediaresourcerequestcount.md) — Returns the total number of media requests performed by the download task. This includes playlist requests, media segment requests, and content key requests.
- [variants](variants.md) — Returns the variants that were downloaded.
- [errorEvent](errorevent.md) — Returns the error event if any. If no value is available, returns nil.
