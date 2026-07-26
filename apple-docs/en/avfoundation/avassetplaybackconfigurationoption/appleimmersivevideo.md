---
title: appleImmersiveVideo
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetplaybackconfigurationoption/appleimmersivevideo
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetplaybackconfigurationoption/appleimmersivevideo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetplaybackconfigurationoption/appleimmersivevideo.json'
content_hash: 'sha256:84131503f80aed8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetPlaybackConfigurationOption](../avassetplaybackconfigurationoption.md)

# appleImmersiveVideo

<sub>Type Property</sub>

Indicates whether the asset is Apple Immersive Video.

<sub>macOS, visionOS</sub>

```swift
static let appleImmersiveVideo: AVAssetPlaybackConfigurationOption
```

## Discussion

Clients may use this property to switch into specific display and control modes for Apple Immersive Video playback.

## See Also

### Configuration options

- [AVAssetPlaybackConfigurationOptionStereoVideo](stereovideo.md) — An option that indicates whether the asset can render as stereo video.
- [AVAssetPlaybackConfigurationOptionStereoMultiviewVideo](stereomultiviewvideo.md) — An option that indicates whether the asset is in a multiview compression format and can render as stereo video.
- [AVAssetPlaybackConfigurationOptionSpatialVideo](spatialvideo.md) — An option that indicates whether the asset can render as spatial video.
- [AVAssetPlaybackConfigurationOptionNonRectilinearProjection](nonrectilinearprojection.md) — Indicates whether the asset calls for the use of a non-rectilinear projection for rendering video.
