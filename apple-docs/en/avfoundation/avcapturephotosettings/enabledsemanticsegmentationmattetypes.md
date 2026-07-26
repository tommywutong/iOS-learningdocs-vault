---
title: enabledSemanticSegmentationMatteTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/enabledsemanticsegmentationmattetypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/enabledsemanticsegmentationmattetypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/enabledsemanticsegmentationmattetypes.json'
content_hash: 'sha256:8e7b4f96f413b333'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# enabledSemanticSegmentationMatteTypes

<sub>Instance Property</sub>

An array of semantic segmentation matte types that the photo render pipeline can deliver.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var enabledSemanticSegmentationMatteTypes: [AVSemanticSegmentationMatte.MatteType] { get set }
```

## Discussion

You may set this property to the array of matte types you’d like delivered with [AVCapturePhoto](../avcapturephoto.md). The array may only contain values present in [availableSemanticSegmentationMatteTypes](../avcapturephotooutput/availablesemanticsegmentationmattetypes.md).

The default value of this property is an empty array.

## See Also

### Capturing semantic segmentation mattes

- [embedsSemanticSegmentationMattesInPhoto](embedssemanticsegmentationmattesinphoto.md) — A Boolean value that specifies whether to write the enabled semantic segmentation matte types captured with this photo to the photo’s file structure.
