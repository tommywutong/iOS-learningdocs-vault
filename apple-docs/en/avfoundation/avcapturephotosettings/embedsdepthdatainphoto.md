---
title: embedsDepthDataInPhoto
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/embedsdepthdatainphoto
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/embedsdepthdatainphoto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/embedsdepthdatainphoto.json'
content_hash: 'sha256:a52b4e3bcb96e387'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# embedsDepthDataInPhoto

<sub>Instance Property</sub>

A Boolean value that determines whether any depth data captured with the photo is included when generating output file data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var embedsDepthDataInPhoto: Bool { get set }
```

## Discussion

When this property is [true](../../swift/true.md) (the default), and depth data capture is enabled with the [depthDataDeliveryEnabled](isdepthdatadeliveryenabled.md) property, the [AVCapturePhoto](../avcapturephoto.md) class includes the depth map as an embedded attachment when you flatten the photo data for output in compatible file formats.

Set this property to [false](../../swift/false.md) if you wish to capture depth data with a photo but not include depth data in  output.

## See Also

### Capturing depth data

- [depthDataDeliveryEnabled](isdepthdatadeliveryenabled.md) — A Boolean value that determines whether the photo output captures depth data along with the photo.
- [depthDataFiltered](isdepthdatafiltered.md) — A Boolean value that determines whether to smooth noise and fill in missing values in depth data output.
