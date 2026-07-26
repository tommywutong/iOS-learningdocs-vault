---
title: nonRectilinearProjection
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetplaybackconfigurationoption/nonrectilinearprojection
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetplaybackconfigurationoption/nonrectilinearprojection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetplaybackconfigurationoption/nonrectilinearprojection.json'
content_hash: 'sha256:ba267cef51cad029'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetPlaybackConfigurationOption](../avassetplaybackconfigurationoption.md)

# nonRectilinearProjection

<sub>Type Property</sub>

Indicates whether the asset calls for the use of a non-rectilinear projection for rendering video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let nonRectilinearProjection: AVAssetPlaybackConfigurationOption
```

## Discussion

Clients may use this property to determine whether to configure a non-rectilinear projection when displaying video.

## See Also

### Configuration options

- [AVAssetPlaybackConfigurationOptionStereoVideo](stereovideo.md) — An option that indicates whether the asset can render as stereo video.
- [AVAssetPlaybackConfigurationOptionStereoMultiviewVideo](stereomultiviewvideo.md) — An option that indicates whether the asset is in a multiview compression format and can render as stereo video.
- [AVAssetPlaybackConfigurationOptionSpatialVideo](spatialvideo.md) — An option that indicates whether the asset can render as spatial video.
- [AVAssetPlaybackConfigurationOptionAppleImmersiveVideo](appleimmersivevideo.md) — Indicates whether the asset is Apple Immersive Video.
