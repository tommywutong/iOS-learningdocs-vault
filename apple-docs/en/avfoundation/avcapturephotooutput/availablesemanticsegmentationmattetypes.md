---
title: availableSemanticSegmentationMatteTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/availablesemanticsegmentationmattetypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/availablesemanticsegmentationmattetypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/availablesemanticsegmentationmattetypes.json'
content_hash: 'sha256:a33be814e30a3c63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# availableSemanticSegmentationMatteTypes

<sub>Instance Property</sub>

An array of semantic segmentation matte types that may be captured and delivered along with the primary photo.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var availableSemanticSegmentationMatteTypes: [AVSemanticSegmentationMatte.MatteType] { get }
```

## Discussion

This property returns the array of semantic segmentation types that’s available given the current session configuration.

This property is key-value observable.

> [!important] Important
> The value of this property may change when switching cameras or formats. When this property changes, [enabledSemanticSegmentationMatteTypes](enabledsemanticsegmentationmattetypes.md) reverts to an empty array. If you’ve previously opted in for delivery of one or more semantic segmentation mattes, you need to set up your [enabledSemanticSegmentationMatteTypes](enabledsemanticsegmentationmattetypes.md) again.

## See Also

### Getting segmentation mattes

- [enabledSemanticSegmentationMatteTypes](enabledsemanticsegmentationmattetypes.md) — The semantic segmentation matte types that the photo render pipeline delivers.
