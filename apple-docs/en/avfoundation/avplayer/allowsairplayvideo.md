---
title: allowsAirPlayVideo
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 9.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayer/allowsairplayvideo
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/allowsairplayvideo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/allowsairplayvideo.json'
content_hash: 'sha256:1abf9d5a2d5bbd17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# allowsAirPlayVideo

<sub>Instance Property</sub>

A Boolean value that indicates whether the player allows AirPlay video playback.

> [!warning] Deprecated
> Use [allowsExternalPlayback](allowsexternalplayback.md) instead.

<sub>tvOS</sub>

```swift
var allowsAirPlayVideo: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md).

## See Also

### Configuring AirPlay behavior

- [airPlayVideoActive](isairplayvideoactive.md) — A Boolean value that indicates whether the player is playing video through AirPlay. _(deprecated)_
- [usesAirPlayVideoWhileAirPlayScreenIsActive](usesairplayvideowhileairplayscreenisactive.md) — A Boolean value that indicates whether the player automatically switches to AirPlay Video while AirPlay Screen is active. _(deprecated)_
