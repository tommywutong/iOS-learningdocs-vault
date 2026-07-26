---
title: indicatesNonRectilinearProjection
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/indicatesnonrectilinearprojection
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/indicatesnonrectilinearprojection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/indicatesnonrectilinearprojection.json'
content_hash: 'sha256:9145a99c39139423'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# indicatesNonRectilinearProjection

<sub>Type Property</sub>

A media characteristic that indicates the video track carries information related to how it should be projected for display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let indicatesNonRectilinearProjection: AVMediaCharacteristic
```

## Discussion

This media characteristic is currently synthesized if the CMVideoFormatDescription specifies a non-rectilinear projection. To determine which kind of projection is indicated, look for the format description extension with key kCMFormatDescriptionExtension_ProjectionKind. The value of this characteristic is @“public.indicates-non-rectilinear-projection”. Note for content authors: the presence of this characteristic is strictly inferred from the format description of the associated track.

## See Also

### Visual

- [AVMediaCharacteristicVisual](visual.md) — A media characteristic that indicates that a track or media selection option includes visual content.
- [AVMediaCharacteristicContainsAlphaChannel](containsalphachannel.md) — A media characteristic that indicates that a track contains an alpha channel.
- [AVMediaCharacteristicContainsHDRVideo](containshdrvideo.md) — A media characteristic that indicates that a track contains HDR video.
- [AVMediaCharacteristicFrameBased](framebased.md) — A media characteristic that indicates that a track or media selection option includes frame-based content.
- [AVMediaCharacteristicUsesWideGamutColorSpace](useswidegamutcolorspace.md) — A media characteristic that indicates that a track uses a wide-gamut color space.
- [AVMediaCharacteristicContainsStereoMultiviewVideo](containsstereomultiviewvideo.md) — A media characteristic that indicates that a track contains stereoscopic video captured in a multiview compression format.
- [AVMediaCharacteristicCarriesVideoStereoMetadata](carriesvideostereometadata.md) — A media characteristic that indicates that the stereoscopic video track carries additional information related to the stereoscopic video.
- [AVMediaCharacteristicIndicatesHorizontalFieldOfView](indicateshorizontalfieldofview.md) — A media characteristic that indicates the video track carries information related to the horizontal field of view.
