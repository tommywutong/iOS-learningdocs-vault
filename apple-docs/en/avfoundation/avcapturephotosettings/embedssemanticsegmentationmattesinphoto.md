---
title: embedsSemanticSegmentationMattesInPhoto
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/embedssemanticsegmentationmattesinphoto
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/embedssemanticsegmentationmattesinphoto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/embedssemanticsegmentationmattesinphoto.json'
content_hash: 'sha256:b43c56b66520029c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# embedsSemanticSegmentationMattesInPhoto

<sub>Instance Property</sub>

A Boolean value that specifies whether to write the enabled semantic segmentation matte types captured with this photo to the photo’s file structure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var embedsSemanticSegmentationMattesInPhoto: Bool { get set }
```

## Discussion

Semantic segmentation mattes are only supported in HEIF and JPEG. The photo output ignores this property if you set [enabledSemanticSegmentationMatteTypes](enabledsemanticsegmentationmattetypes.md) to an empty array.

The property’s default value is [true](../../swift/true.md).

> [!important] Important
> Enabling semantic segmentation matte delivery requires a lengthy reconfiguration of the capture render pipeline. If you intend to capture semantic segmentation mattes, set this property to [true](../../swift/true.md) before calling the capture session’s [- startRunning](<../avcapturesession/startrunning().md>) method.

## See Also

### Capturing semantic segmentation mattes

- [enabledSemanticSegmentationMatteTypes](enabledsemanticsegmentationmattetypes.md) — An array of semantic segmentation matte types that the photo render pipeline can deliver.
