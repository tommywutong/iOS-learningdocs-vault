---
title: isAirPlayVideoActive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 9.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayer/isairplayvideoactive
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/isairplayvideoactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/isairplayvideoactive.json'
content_hash: 'sha256:44bad450778f0883'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# isAirPlayVideoActive

<sub>Instance Property</sub>

A Boolean value that indicates whether the player is playing video through AirPlay.

> [!warning] Deprecated
> Use [externalPlaybackActive](isexternalplaybackactive.md) instead.

<sub>tvOS</sub>

```swift
var isAirPlayVideoActive: Bool { get }
```

## See Also

### Configuring AirPlay behavior

- [allowsAirPlayVideo](allowsairplayvideo.md) — A Boolean value that indicates whether the player allows AirPlay video playback. _(deprecated)_
- [usesAirPlayVideoWhileAirPlayScreenIsActive](usesairplayvideowhileairplayscreenisactive.md) — A Boolean value that indicates whether the player automatically switches to AirPlay Video while AirPlay Screen is active. _(deprecated)_
