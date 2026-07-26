---
title: noCue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/cue-swift.struct/nocue
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/cue-swift.struct/nocue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/cue-swift.struct/nocue.json'
content_hash: 'sha256:1bf84c1d61d26094'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayerInterstitialEvent](../../avplayerinterstitialevent.md) · [Cue](../cue-swift.struct.md)

# noCue

<sub>Type Property</sub>

A cue that indicates that playback starts at the interstitial event time or date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let noCue: AVPlayerInterstitialEvent.Cue
```

## See Also

### Cues

- [AVPlayerInterstitialEventJoinCue](joincue.md) — A cue that indicates that playback occurs before starting primary playback, regardless of initial primary playback position.
- [AVPlayerInterstitialEventLeaveCue](leavecue.md) — A cue that indicates event playback occurs after primary playback ends without error, either at the end of the primary asset or at the client-specified forward playback end time.
