---
title: spatialVideo
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetplaybackconfigurationoption/spatialvideo
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetplaybackconfigurationoption/spatialvideo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetplaybackconfigurationoption/spatialvideo.json'
content_hash: 'sha256:3d49e62f3f76fad5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetPlaybackConfigurationOption](../avassetplaybackconfigurationoption.md)

# spatialVideo

<sub>Type Property</sub>

An option that indicates whether the asset can render as spatial video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let spatialVideo: AVAssetPlaybackConfigurationOption
```

## Discussion

Apps may use this property to determine whether to configure spatial video rendering.

## See Also

### Configuration options

- [AVAssetPlaybackConfigurationOptionStereoVideo](stereovideo.md) — An option that indicates whether the asset can render as stereo video.
- [AVAssetPlaybackConfigurationOptionStereoMultiviewVideo](stereomultiviewvideo.md) — An option that indicates whether the asset is in a multiview compression format and can render as stereo video.
- [AVAssetPlaybackConfigurationOptionAppleImmersiveVideo](appleimmersivevideo.md) — Indicates whether the asset is Apple Immersive Video.
- [AVAssetPlaybackConfigurationOptionNonRectilinearProjection](nonrectilinearprojection.md) — Indicates whether the asset calls for the use of a non-rectilinear projection for rendering video.
