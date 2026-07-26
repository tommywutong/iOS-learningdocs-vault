---
title: AVPlayerInterstitialEvent.Cue
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/cue-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/cue-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/cue-swift.struct.json'
content_hash: 'sha256:1970aa44efcafdeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# AVPlayerInterstitialEvent.Cue

<sub>Structure</sub>

A structure that defines standard cues to play interstitial content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Cue
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Cues

- [AVPlayerInterstitialEventNoCue](cue-swift.struct/nocue.md) — A cue that indicates that playback starts at the interstitial event time or date.
- [AVPlayerInterstitialEventJoinCue](cue-swift.struct/joincue.md) — A cue that indicates that playback occurs before starting primary playback, regardless of initial primary playback position.
- [AVPlayerInterstitialEventLeaveCue](cue-swift.struct/leavecue.md) — A cue that indicates event playback occurs after primary playback ends without error, either at the end of the primary asset or at the client-specified forward playback end time.

### Initializers

- [init(rawValue:)](<cue-swift.struct/init(rawvalue_).md>) — Creates an interstitial event cue from its raw string value.

## See Also

### Configuring cues

- [cue](cue-swift.property.md) — A cue to schedule interstitial event playback at a predefined position during primary playback.
