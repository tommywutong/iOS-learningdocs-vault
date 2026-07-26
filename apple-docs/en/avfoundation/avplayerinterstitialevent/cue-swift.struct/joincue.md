---
title: joinCue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/cue-swift.struct/joincue
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/cue-swift.struct/joincue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/cue-swift.struct/joincue.json'
content_hash: 'sha256:be79a7cb7e63c4e2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayerInterstitialEvent](../../avplayerinterstitialevent.md) · [Cue](../cue-swift.struct.md)

# joinCue

<sub>Type Property</sub>

A cue that indicates that playback occurs before starting primary playback, regardless of initial primary playback position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let joinCue: AVPlayerInterstitialEvent.Cue
```

## See Also

### Cues

- [AVPlayerInterstitialEventNoCue](nocue.md) — A cue that indicates that playback starts at the interstitial event time or date.
- [AVPlayerInterstitialEventLeaveCue](leavecue.md) — A cue that indicates event playback occurs after primary playback ends without error, either at the end of the primary asset or at the client-specified forward playback end time.
