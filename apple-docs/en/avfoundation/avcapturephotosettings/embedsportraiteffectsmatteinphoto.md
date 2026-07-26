---
title: embedsPortraitEffectsMatteInPhoto
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/embedsportraiteffectsmatteinphoto
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/embedsportraiteffectsmatteinphoto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/embedsportraiteffectsmatteinphoto.json'
content_hash: 'sha256:578063bc93fb59e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# embedsPortraitEffectsMatteInPhoto

<sub>Instance Property</sub>

Specifies whether the portrait effects matte captured with ths photo should be written to the photo’s file structure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var embedsPortraitEffectsMatteInPhoto: Bool { get set }
```

## Discussion

The default is [true](../../swift/true.md), which tells AV Foundation to embed the portrait effects matte images as HEIF and JPEG in the photo.

This property is ignored if [portraitEffectsMatteDeliveryEnabled](isportraiteffectsmattedeliveryenabled.md) is set to [false](../../swift/false.md). AV Foundation includes the portrait effects matte only if both this property and [portraitEffectsMatteDeliveryEnabled](isportraiteffectsmattedeliveryenabled.md) are set to [true](../../swift/true.md).

## See Also

### Capturing Portrait Effects matte

- [portraitEffectsMatteDeliveryEnabled](isportraiteffectsmattedeliveryenabled.md) — Specifies whether a portrait effects matte should be captured along with the photo.
