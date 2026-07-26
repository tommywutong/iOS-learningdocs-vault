---
title: usesWideGamutColorSpace
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/useswidegamutcolorspace
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/useswidegamutcolorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/useswidegamutcolorspace.json'
content_hash: 'sha256:676cf3c6162396af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# usesWideGamutColorSpace

<sub>Type Property</sub>

A media characteristic that indicates that a track uses a wide-gamut color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let usesWideGamutColorSpace: AVMediaCharacteristic
```

## Discussion

Tracks that use a wide-gamut color space may use colors that can’t be accurately represented in standard RGB mode.

## See Also

### Visual

- [AVMediaCharacteristicVisual](visual.md) — A media characteristic that indicates that a track or media selection option includes visual content.
- [AVMediaCharacteristicContainsAlphaChannel](containsalphachannel.md) — A media characteristic that indicates that a track contains an alpha channel.
- [AVMediaCharacteristicContainsHDRVideo](containshdrvideo.md) — A media characteristic that indicates that a track contains HDR video.
- [AVMediaCharacteristicFrameBased](framebased.md) — A media characteristic that indicates that a track or media selection option includes frame-based content.
- [AVMediaCharacteristicContainsStereoMultiviewVideo](containsstereomultiviewvideo.md) — A media characteristic that indicates that a track contains stereoscopic video captured in a multiview compression format.
- [AVMediaCharacteristicCarriesVideoStereoMetadata](carriesvideostereometadata.md) — A media characteristic that indicates that the stereoscopic video track carries additional information related to the stereoscopic video.
- [AVMediaCharacteristicIndicatesHorizontalFieldOfView](indicateshorizontalfieldofview.md) — A media characteristic that indicates the video track carries information related to the horizontal field of view.
- [AVMediaCharacteristicIndicatesNonRectilinearProjection](indicatesnonrectilinearprojection.md) — A media characteristic that indicates the video track carries information related to how it should be projected for display.
