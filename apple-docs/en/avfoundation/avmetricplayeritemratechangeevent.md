---
title: AVMetricPlayerItemRateChangeEvent
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetricplayeritemratechangeevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetricplayeritemratechangeevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetricplayeritemratechangeevent.json'
content_hash: 'sha256:5e3cc157569eb666'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetricPlayerItemRateChangeEvent

<sub>Class</sub>

An event that represents when the playback rate changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMetricPlayerItemRateChangeEvent
```

## Relationships

- **Inherits From**: [AVMetricEvent](avmetricevent.md)

- **Inherited By**: [AVMetricPlayerItemSeekDidCompleteEvent](avmetricplayeritemseekdidcompleteevent.md), [AVMetricPlayerItemSeekEvent](avmetricplayeritemseekevent.md), [AVMetricPlayerItemStallEvent](avmetricplayeritemstallevent.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting the event

- [previousRate](avmetricplayeritemratechangeevent/previousrate.md)
- [rate](avmetricplayeritemratechangeevent/rate.md)
- [variant](avmetricplayeritemratechangeevent/variant.md)

## See Also

### Transport control

- [AVMetricPlayerItemPlaybackSummaryEvent](avmetricplayeritemplaybacksummaryevent.md) — An event that represents the combined metrics for the entire playback session.
- [AVMetricPlayerItemSeekDidCompleteEvent](avmetricplayeritemseekdidcompleteevent.md) — An event that represents when the playback seek completes.
- [AVMetricPlayerItemSeekEvent](avmetricplayeritemseekevent.md) — An event that represents when a playback seek occurs.
