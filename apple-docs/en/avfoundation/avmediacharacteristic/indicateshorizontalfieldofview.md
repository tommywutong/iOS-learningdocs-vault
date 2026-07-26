---
title: indicatesHorizontalFieldOfView
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/indicateshorizontalfieldofview
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/indicateshorizontalfieldofview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/indicateshorizontalfieldofview.json'
content_hash: 'sha256:75fceedaab7d7950'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# indicatesHorizontalFieldOfView

<sub>Type Property</sub>

A media characteristic that indicates the video track carries information related to the horizontal field of view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let indicatesHorizontalFieldOfView: AVMediaCharacteristic
```

## Discussion

This media characteristic is present when the [CMVideoFormatDescription](../../coremedia/cmvideoformatdescription.md) includes a [kCMFormatDescriptionExtension_HorizontalFieldOfView](../../coremedia/kcmformatdescriptionextension_horizontalfieldofview.md) extension. This is not an indication that the field of view is expanded beyond or more narrow than typical horizontal fields of view.

The value of this characteristic is `public.indicates-horizontal-field-of-view`.

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
- [AVMediaCharacteristicCarriesVideoStereoMetadata](carriesvideostereometadata.md) — A media characteristic that indicates that the stereoscopic video track carries additional information related to the stereoscopic video.
- [AVMediaCharacteristicIndicatesNonRectilinearProjection](indicatesnonrectilinearprojection.md) — A media characteristic that indicates the video track carries information related to how it should be projected for display.
