---
title: AVMetricEvent
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetricevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetricevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetricevent.json'
content_hash: 'sha256:568137bbbf59d4f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetricEvent

<sub>Class</sub>

A base class that represents a metric event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMetricEvent
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVMetricContentKeyRequestEvent](avmetriccontentkeyrequestevent.md), [AVMetricDownloadSummaryEvent](avmetricdownloadsummaryevent.md), [AVMetricErrorEvent](avmetricerrorevent.md), [AVMetricHLSMediaSegmentRequestEvent](avmetrichlsmediasegmentrequestevent.md), [AVMetricHLSPlaylistRequestEvent](avmetrichlsplaylistrequestevent.md), [AVMetricMediaResourceRequestEvent](avmetricmediaresourcerequestevent.md), [AVMetricPlaybackModeSwitchEvent](avmetricplaybackmodeswitchevent.md), [AVMetricPlayerItemLikelyToKeepUpEvent](avmetricplayeritemlikelytokeepupevent.md), [AVMetricPlayerItemPlaybackSummaryEvent](avmetricplayeritemplaybacksummaryevent.md), [AVMetricPlayerItemRateChangeEvent](avmetricplayeritemratechangeevent.md), [AVMetricPlayerItemVariantSwitchEvent](avmetricplayeritemvariantswitchevent.md), [AVMetricPlayerItemVariantSwitchStartEvent](avmetricplayeritemvariantswitchstartevent.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting an event

- [date](avmetricevent/date.md)
- [mediaTime](avmetricevent/mediatime.md)
- [sessionID](avmetricevent/sessionid.md)

### Initializers

- [init(coder:)](<avmetricevent/init(coder_).md>)

## See Also

### Metrics

- [AVMetrics](avmetrics.md) — An asynchronous stream of metric information.
- [AVMergedMetrics](avmergedmetrics.md) — An asynchronous stream of metric information from different publishers.
- [AVVideoPerformanceMetrics](avvideoperformancemetrics.md) — An object that provides metrics related to video playback quality.
- [AVMetricEventStreamPublisher](avmetriceventstreampublisher.md) — A type for objects that publish metric events to the event stream.
- [AVMetricErrorEvent](avmetricerrorevent.md) — An object that represents a metric event when an error occurs.
- [Metric event types](metric-event-types.md)
