---
title: AVMetricPlayerItemSeekDidCompleteEvent
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetricplayeritemseekdidcompleteevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetricplayeritemseekdidcompleteevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetricplayeritemseekdidcompleteevent.json'
content_hash: 'sha256:73a41353e2505088'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetricPlayerItemSeekDidCompleteEvent

<sub>Class</sub>

An event that represents when the playback seek completes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMetricPlayerItemSeekDidCompleteEvent
```

## Relationships

- **Inherits From**: [AVMetricPlayerItemRateChangeEvent](avmetricplayeritemratechangeevent.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting the event

- [didSeekInBuffer](avmetricplayeritemseekdidcompleteevent/didseekinbuffer.md)

## See Also

### Transport control

- [AVMetricPlayerItemPlaybackSummaryEvent](avmetricplayeritemplaybacksummaryevent.md) — An event that represents the combined metrics for the entire playback session.
- [AVMetricPlayerItemRateChangeEvent](avmetricplayeritemratechangeevent.md) — An event that represents when the playback rate changes.
- [AVMetricPlayerItemSeekEvent](avmetricplayeritemseekevent.md) — An event that represents when a playback seek occurs.
