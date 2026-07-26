---
title: isPortraitEffectsMatteDeliveryEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/isportraiteffectsmattedeliveryenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isportraiteffectsmattedeliveryenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/isportraiteffectsmattedeliveryenabled.json'
content_hash: 'sha256:44dc72ec2bf09f68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# isPortraitEffectsMatteDeliveryEnabled

<sub>Instance Property</sub>

Specifies whether a portrait effects matte should be captured along with the photo.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isPortraitEffectsMatteDeliveryEnabled: Bool { get set }
```

## Discussion

The default is `NO`.  Set to `YES` if you wish to receive a portrait effects matte with your photo. AVFoundation throws an exception if [portraitEffectsMatteDeliveryEnabled](../avcapturephotooutput/isportraiteffectsmattedeliveryenabled.md) is not set to `YES`, or if your delegate doesn’t respond to the [- captureOutput:didFinishProcessingPhoto:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) selector.

> [!important] Important
> Portrait effects matte generation requires depth data to be present, so you must also set [depthDataDeliveryEnabled](../avcapturephotooutput/isdepthdatadeliveryenabled.md) to `YES`.

Setting this property to `YES` doen’t guarantee that a portrait effects matte will be present in the resulting [AVCapturePhoto](../avcapturephoto.md). The matte is primarily used to improve the rendering quality of portrait effects on the image. If the photo’s content lacks a clear foreground subject, no portrait effects matte is generated, and the property returns `nil`. Setting this property to `YES` may add significant processing time to the delivery of your [- captureOutput:didFinishProcessingPhoto:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) callback.

## See Also

### Capturing Portrait Effects matte

- [embedsPortraitEffectsMatteInPhoto](embedsportraiteffectsmatteinphoto.md) — Specifies whether the portrait effects matte captured with ths photo should be written to the photo’s file structure.
