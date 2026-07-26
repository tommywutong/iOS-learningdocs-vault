---
title: AVMetricHLSPlaylistRequestEvent
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetrichlsplaylistrequestevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetrichlsplaylistrequestevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetrichlsplaylistrequestevent.json'
content_hash: 'sha256:984d2d8e5a503249'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetricHLSPlaylistRequestEvent

<sub>Class</sub>

An event that represents a live streaming playlist resource request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMetricHLSPlaylistRequestEvent
```

## Relationships

- **Inherits From**: [AVMetricEvent](avmetricevent.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting the event

- [isMultivariantPlaylist](avmetrichlsplaylistrequestevent/ismultivariantplaylist.md)
- [mediaResourceRequestEvent](avmetrichlsplaylistrequestevent/mediaresourcerequestevent.md)
- [mediaType](avmetrichlsplaylistrequestevent/mediatype.md)
- [url](avmetrichlsplaylistrequestevent/url.md)

## See Also

### HTTP Live Streaming

- [AVMetricMediaResourceRequestEvent](avmetricmediaresourcerequestevent.md) — An event that represents a media resource request.
- [AVMetricContentKeyRequestEvent](avmetriccontentkeyrequestevent.md) — An event that represents a live streaming content key resource request.
- [AVMetricHLSMediaSegmentRequestEvent](avmetrichlsmediasegmentrequestevent.md) — An event that represents a live streaming media segment resource request.
- [AVMetricPlayerItemVariantSwitchStartEvent](avmetricplayeritemvariantswitchstartevent.md) — An event that represents when the player attempts a variant switch.
- [AVMetricPlayerItemVariantSwitchEvent](avmetricplayeritemvariantswitchevent.md) — An event that represents when the player completes a variant switch.
- [AVMetricMediaRendition](avmetricmediarendition.md)
