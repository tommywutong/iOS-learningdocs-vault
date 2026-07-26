---
title: containsHDRVideo
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/containshdrvideo
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/containshdrvideo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/containshdrvideo.json'
content_hash: 'sha256:ac21f418d7d96cc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# containsHDRVideo

<sub>Type Property</sub>

A media characteristic that indicates that a track contains HDR video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let containsHDRVideo: AVMediaCharacteristic
```

## Discussion

HDR video contains extended dynamic range that requires explicit support when compositing. The system infers this characteristic from the format description of the associated track.

The value of this characteristic is `public.contains-hdr-video`.

## See Also

### Visual

- [AVMediaCharacteristicVisual](visual.md) — A media characteristic that indicates that a track or media selection option includes visual content.
- [AVMediaCharacteristicContainsAlphaChannel](containsalphachannel.md) — A media characteristic that indicates that a track contains an alpha channel.
- [AVMediaCharacteristicFrameBased](framebased.md) — A media characteristic that indicates that a track or media selection option includes frame-based content.
- [AVMediaCharacteristicUsesWideGamutColorSpace](useswidegamutcolorspace.md) — A media characteristic that indicates that a track uses a wide-gamut color space.
- [AVMediaCharacteristicContainsStereoMultiviewVideo](containsstereomultiviewvideo.md) — A media characteristic that indicates that a track contains stereoscopic video captured in a multiview compression format.
- [AVMediaCharacteristicCarriesVideoStereoMetadata](carriesvideostereometadata.md) — A media characteristic that indicates that the stereoscopic video track carries additional information related to the stereoscopic video.
- [AVMediaCharacteristicIndicatesHorizontalFieldOfView](indicateshorizontalfieldofview.md) — A media characteristic that indicates the video track carries information related to the horizontal field of view.
- [AVMediaCharacteristicIndicatesNonRectilinearProjection](indicatesnonrectilinearprojection.md) — A media characteristic that indicates the video track carries information related to how it should be projected for display.
