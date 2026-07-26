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
doc_path: /documentation/avfoundation/avcapturephotooutput/enabledsemanticsegmentationmattetypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/enabledsemanticsegmentationmattetypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/enabledsemanticsegmentationmattetypes.json'
content_hash: 'sha256:d1879a77c8fa62ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# enabledSemanticSegmentationMatteTypes

<sub>Instance Property</sub>

The semantic segmentation matte types that the photo render pipeline delivers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var enabledSemanticSegmentationMatteTypes: [AVSemanticSegmentationMatte.MatteType] { get set }
```

## Discussion

Set this property value to the array of matte types you’d like delivered with your primary photos. The array may only contain values present in [availableSemanticSegmentationMatteTypes](availablesemanticsegmentationmattetypes.md).

The default value of this property is an empty array.

> [!important] Important
> Enabling semantic segmentation matte delivery requires a lengthy reconfiguration of the capture render pipeline. If you intend to capture semantic segmentation mattes, set this property to your desired types before calling the capture session’s [- startRunning](<../avcapturesession/startrunning().md>) method.

## See Also

### Getting segmentation mattes

- [availableSemanticSegmentationMatteTypes](availablesemanticsegmentationmattetypes.md) — An array of semantic segmentation matte types that may be captured and delivered along with the primary photo.
