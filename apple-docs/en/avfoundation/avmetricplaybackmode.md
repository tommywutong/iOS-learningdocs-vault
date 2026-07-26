---
title: AVMetricPlaybackMode
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetricplaybackmode
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetricplaybackmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetricplaybackmode.json'
content_hash: 'sha256:f8f84eee7867ff91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetricPlaybackMode

<sub>Enumeration</sub>

These constants are the possible playback modes returned by the property “mode” on AVMetricPlaybackModeSwitchEvent

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AVMetricPlaybackMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a playback mode

- [init(rawValue:)](<avmetricplaybackmode/init(rawvalue_).md>)

### Playback modes

- [AVMetricPlaybackModeLocal](avmetricplaybackmode/local.md) — Indicates that playback is local.
- [AVMetricPlaybackModeAirPlayVideo](avmetricplaybackmode/airplayvideo.md) — Indicates that playback is via AirPlay Video.

## See Also

### Playback mode

- [AVMetricPlaybackModeSwitchEvent](avmetricplaybackmodeswitchevent.md) — Represents a change in playback state, entering one of AVMetricPlaybackMode _(beta)_
