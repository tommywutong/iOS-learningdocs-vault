---
title: isDepthDataFiltered
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/isdepthdatafiltered
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isdepthdatafiltered'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/isdepthdatafiltered.json'
content_hash: 'sha256:604baedde214870c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# isDepthDataFiltered

<sub>Instance Property</sub>

A Boolean value that determines whether to smooth noise and fill in missing values in depth data output.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isDepthDataFiltered: Bool { get set }
```

## Discussion

When this property is [true](../../swift/true.md) (the default), and depth data capture is enabled with the [depthDataDeliveryEnabled](isdepthdatadeliveryenabled.md) property, the capture system smooths noise and fills in missing values (caused by low light or lens occlusion) in depth data maps by temporally interpolating between previous and subsequent frames of captured depth data.

Filtering depth data makes it more useful for applying visual effects to a companion image, but alters the data such that it may no longer be suitable for computer vision tasks. (In an unfiltered depth map, missing values are represented as `NaN`.) Set this property to [false](../../swift/false.md) to disable filtering and receive unfiltered depth data.

## See Also

### Capturing depth data

- [depthDataDeliveryEnabled](isdepthdatadeliveryenabled.md) — A Boolean value that determines whether the photo output captures depth data along with the photo.
- [embedsDepthDataInPhoto](embedsdepthdatainphoto.md) — A Boolean value that determines whether any depth data captured with the photo is included when generating output file data.
