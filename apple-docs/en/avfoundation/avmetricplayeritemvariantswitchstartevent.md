---
title: AVMetricPlayerItemVariantSwitchStartEvent
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetricplayeritemvariantswitchstartevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetricplayeritemvariantswitchstartevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetricplayeritemvariantswitchstartevent.json'
content_hash: 'sha256:62ea785df5c75212'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetricPlayerItemVariantSwitchStartEvent

<sub>Class</sub>

An event that represents when the player attempts a variant switch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMetricPlayerItemVariantSwitchStartEvent
```

## Relationships

- **Inherits From**: [AVMetricEvent](avmetricevent.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting the event

- [fromVariant](avmetricplayeritemvariantswitchstartevent/fromvariant.md)
- [loadedTimeRanges](avmetricplayeritemvariantswitchstartevent/loadedtimeranges-2mbm7.md)
- [toVariant](avmetricplayeritemvariantswitchstartevent/tovariant.md)
- [audioRendition](avmetricplayeritemvariantswitchstartevent/audiorendition.md)
- [videoRendition](avmetricplayeritemvariantswitchstartevent/videorendition.md)
- [subtitleRendition](avmetricplayeritemvariantswitchstartevent/subtitlerendition.md)

## See Also

### HTTP Live Streaming

- [AVMetricMediaResourceRequestEvent](avmetricmediaresourcerequestevent.md) — An event that represents a media resource request.
- [AVMetricContentKeyRequestEvent](avmetriccontentkeyrequestevent.md) — An event that represents a live streaming content key resource request.
- [AVMetricHLSMediaSegmentRequestEvent](avmetrichlsmediasegmentrequestevent.md) — An event that represents a live streaming media segment resource request.
- [AVMetricHLSPlaylistRequestEvent](avmetrichlsplaylistrequestevent.md) — An event that represents a live streaming playlist resource request.
- [AVMetricPlayerItemVariantSwitchEvent](avmetricplayeritemvariantswitchevent.md) — An event that represents when the player completes a variant switch.
- [AVMetricMediaRendition](avmetricmediarendition.md)
