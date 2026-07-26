---
title: stereoMultiviewVideo
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetplaybackconfigurationoption/stereomultiviewvideo
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetplaybackconfigurationoption/stereomultiviewvideo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetplaybackconfigurationoption/stereomultiviewvideo.json'
content_hash: 'sha256:b7f7cf60d5c2c870'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetPlaybackConfigurationOption](../avassetplaybackconfigurationoption.md)

# stereoMultiviewVideo

<sub>Type Property</sub>

An option that indicates whether the asset is in a multiview compression format and can render as stereo video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let stereoMultiviewVideo: AVAssetPlaybackConfigurationOption
```

## Discussion

Apps may use this property to determine whether to configure stereo video rendering.

## See Also

### Configuration options

- [AVAssetPlaybackConfigurationOptionStereoVideo](stereovideo.md) — An option that indicates whether the asset can render as stereo video.
- [AVAssetPlaybackConfigurationOptionSpatialVideo](spatialvideo.md) — An option that indicates whether the asset can render as spatial video.
- [AVAssetPlaybackConfigurationOptionAppleImmersiveVideo](appleimmersivevideo.md) — Indicates whether the asset is Apple Immersive Video.
- [AVAssetPlaybackConfigurationOptionNonRectilinearProjection](nonrectilinearprojection.md) — Indicates whether the asset calls for the use of a non-rectilinear projection for rendering video.
