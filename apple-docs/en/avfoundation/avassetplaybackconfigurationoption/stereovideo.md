---
title: stereoVideo
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetplaybackconfigurationoption/stereovideo
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetplaybackconfigurationoption/stereovideo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetplaybackconfigurationoption/stereovideo.json'
content_hash: 'sha256:3887742bbb968ad3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetPlaybackConfigurationOption](../avassetplaybackconfigurationoption.md)

# stereoVideo

<sub>Type Property</sub>

An option that indicates whether the asset can render as stereo video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let stereoVideo: AVAssetPlaybackConfigurationOption
```

## Discussion

Apps may use this property to determine whether to configure stereo video rendering.

## See Also

### Configuration options

- [AVAssetPlaybackConfigurationOptionStereoMultiviewVideo](stereomultiviewvideo.md) — An option that indicates whether the asset is in a multiview compression format and can render as stereo video.
- [AVAssetPlaybackConfigurationOptionSpatialVideo](spatialvideo.md) — An option that indicates whether the asset can render as spatial video.
- [AVAssetPlaybackConfigurationOptionAppleImmersiveVideo](appleimmersivevideo.md) — Indicates whether the asset is Apple Immersive Video.
- [AVAssetPlaybackConfigurationOptionNonRectilinearProjection](nonrectilinearprojection.md) — Indicates whether the asset calls for the use of a non-rectilinear projection for rendering video.
