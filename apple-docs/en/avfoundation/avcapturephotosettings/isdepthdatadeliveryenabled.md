---
title: isDepthDataDeliveryEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/isdepthdatadeliveryenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isdepthdatadeliveryenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/isdepthdatadeliveryenabled.json'
content_hash: 'sha256:804adec102650de5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# isDepthDataDeliveryEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether the photo output captures depth data along with the photo.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isDepthDataDeliveryEnabled: Bool { get set }
```

## Discussion

When this property is  [false](../../swift/false.md) (the default), the capture output produces only photo data and metadata.

If you change this property to [true](../../swift/true.md), the capture output records per-pixel scene depth information and delivers an [AVDepthData](../avdepthdata.md) object in the photo capture results. Enabling depth capture for a photo capture request requires that the photo output first be configured for depth capture using its own [depthDataDeliveryEnabled](../avcapturephotooutput/isdepthdatadeliveryenabled.md) property (and raises an exception otherwise).

> [!note] Note
> Enabling depth capture along with photo capture adds significant processing time before delivery of results to your delegate’s [- captureOutput:didFinishProcessingPhoto:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) method.

## See Also

### Capturing depth data

- [embedsDepthDataInPhoto](embedsdepthdatainphoto.md) — A Boolean value that determines whether any depth data captured with the photo is included when generating output file data.
- [depthDataFiltered](isdepthdatafiltered.md) — A Boolean value that determines whether to smooth noise and fill in missing values in depth data output.
