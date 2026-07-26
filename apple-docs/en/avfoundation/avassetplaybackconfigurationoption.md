---
title: AVAssetPlaybackConfigurationOption
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetplaybackconfigurationoption
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetplaybackconfigurationoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetplaybackconfigurationoption.json'
content_hash: 'sha256:9b333ee212858110'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetPlaybackConfigurationOption

<sub>Structure</sub>

A structure that defines playback configuration options for an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVAssetPlaybackConfigurationOption
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuration options

- [AVAssetPlaybackConfigurationOptionStereoVideo](avassetplaybackconfigurationoption/stereovideo.md) — An option that indicates whether the asset can render as stereo video.
- [AVAssetPlaybackConfigurationOptionStereoMultiviewVideo](avassetplaybackconfigurationoption/stereomultiviewvideo.md) — An option that indicates whether the asset is in a multiview compression format and can render as stereo video.
- [AVAssetPlaybackConfigurationOptionSpatialVideo](avassetplaybackconfigurationoption/spatialvideo.md) — An option that indicates whether the asset can render as spatial video.
- [AVAssetPlaybackConfigurationOptionAppleImmersiveVideo](avassetplaybackconfigurationoption/appleimmersivevideo.md) — Indicates whether the asset is Apple Immersive Video.
- [AVAssetPlaybackConfigurationOptionNonRectilinearProjection](avassetplaybackconfigurationoption/nonrectilinearprojection.md) — Indicates whether the asset calls for the use of a non-rectilinear projection for rendering video.

### Initializers

- [init(rawValue:)](<avassetplaybackconfigurationoption/init(rawvalue_).md>) — Creates a configuration option from its raw string value.

## See Also

### Utilities

- [AVAssetPlaybackAssistant](avassetplaybackassistant.md) — An object that provides playback information for an asset.
