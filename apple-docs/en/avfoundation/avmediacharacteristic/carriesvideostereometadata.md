---
title: carriesVideoStereoMetadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/carriesvideostereometadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/carriesvideostereometadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/carriesvideostereometadata.json'
content_hash: 'sha256:d1590badfb4be6f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# carriesVideoStereoMetadata

<sub>Type Property</sub>

A media characteristic that indicates that the stereoscopic video track carries additional information related to the stereoscopic video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let carriesVideoStereoMetadata: AVMediaCharacteristic
```

## Discussion

This characteristic doesnindicate whether the encoded video contains stereoscopic views. It instead indicates that it contains additional information that may influence the interpretation of those views and contribute to a better experience.

The value of this characteristic is `com.apple.quicktime.video.stereo-metadata`.

> [!note] Note
> The presence of this characteristic is strictly inferred from the format description of the associated track.

## See Also

### Visual

- [AVMediaCharacteristicVisual](visual.md) — A media characteristic that indicates that a track or media selection option includes visual content.
- [AVMediaCharacteristicContainsAlphaChannel](containsalphachannel.md) — A media characteristic that indicates that a track contains an alpha channel.
- [AVMediaCharacteristicContainsHDRVideo](containshdrvideo.md) — A media characteristic that indicates that a track contains HDR video.
- [AVMediaCharacteristicFrameBased](framebased.md) — A media characteristic that indicates that a track or media selection option includes frame-based content.
- [AVMediaCharacteristicUsesWideGamutColorSpace](useswidegamutcolorspace.md) — A media characteristic that indicates that a track uses a wide-gamut color space.
- [AVMediaCharacteristicContainsStereoMultiviewVideo](containsstereomultiviewvideo.md) — A media characteristic that indicates that a track contains stereoscopic video captured in a multiview compression format.
- [AVMediaCharacteristicIndicatesHorizontalFieldOfView](indicateshorizontalfieldofview.md) — A media characteristic that indicates the video track carries information related to the horizontal field of view.
- [AVMediaCharacteristicIndicatesNonRectilinearProjection](indicatesnonrectilinearprojection.md) — A media characteristic that indicates the video track carries information related to how it should be projected for display.
