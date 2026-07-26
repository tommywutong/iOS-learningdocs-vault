---
title: AVMetricDownloadSummaryEvent
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetricdownloadsummaryevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetricdownloadsummaryevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetricdownloadsummaryevent.json'
content_hash: 'sha256:04b0ad643b5a8ec3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetricDownloadSummaryEvent

<sub>Class</sub>

Represents a summary metric event with aggregated metrics for the entire download task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMetricDownloadSummaryEvent
```

## Overview

Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Relationships

- **Inherits From**: [AVMetricEvent](avmetricevent.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting the download summary

- [downloadDuration](avmetricdownloadsummaryevent/downloadduration.md) — Returns the total duration of the download in seconds.
- [bytesDownloadedCount](avmetricdownloadsummaryevent/bytesdownloadedcount.md) — Returns the total number of bytes downloaded by the download task.
- [mediaResourceRequestCount](avmetricdownloadsummaryevent/mediaresourcerequestcount.md) — Returns the total number of media requests performed by the download task. This includes playlist requests, media segment requests, and content key requests.
- [recoverableErrorCount](avmetricdownloadsummaryevent/recoverableerrorcount.md) — Returns the total count of recoverable errors encountered during the download. If no errors were encountered, returns 0.
- [variants](avmetricdownloadsummaryevent/variants.md) — Returns the variants that were downloaded.
- [errorEvent](avmetricdownloadsummaryevent/errorevent.md) — Returns the error event if any. If no value is available, returns nil.

## See Also

### Summary

- [AVMetricPlayerItemPlaybackSummaryEvent](avmetricplayeritemplaybacksummaryevent.md) — An event that represents the combined metrics for the entire playback session.
