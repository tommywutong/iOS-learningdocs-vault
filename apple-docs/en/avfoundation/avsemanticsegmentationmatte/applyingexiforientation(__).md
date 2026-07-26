---
title: 'applyingExifOrientation(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsemanticsegmentationmatte/applyingexiforientation(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/applyingexiforientation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsemanticsegmentationmatte/applyingexiforientation%28_%3A%29.json'
content_hash: 'sha256:d2a3f556f47c37a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSemanticSegmentationMatte](../avsemanticsegmentationmatte.md)

# applyingExifOrientation(_:)

<sub>Instance Method</sub>

Returns a new semantic segmentation matte instance with the specified Exif orientation applied.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func applyingExifOrientation(_ exifOrientation: CGImagePropertyOrientation) -> Self
```

## Parameters

- `exifOrientation` — A [CGImagePropertyOrientation](../../imageio/cgimagepropertyorientation.md) value expressing how the matte should be rotated or mirrored.

## Return Value

A new semantic segmentation matte instance.

## Discussion

This method throws an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) if you pass an unrecognized `exifOrientation`.

## See Also

### Creating a segmentation matte

- [+ semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:](<init(fromimagesourceauxiliarydatatype_dictionaryrepresentation_).md>) — Returns a new semantic segmentation matte instance from auxiliary image information in an image file.
- [- semanticSegmentationMatteByReplacingSemanticSegmentationMatteWithPixelBuffer:error:](<replacingsemanticsegmentationmatte(with_).md>) — Returns a semantic segmentation matte instance that wraps the replacement pixel buffer.
- [- dictionaryRepresentationForAuxiliaryDataType:](<dictionaryrepresentation(forauxiliarydatatype_).md>) — Returns a dictionary of primitive map information to use when writing an image file with a semantic segmentation matte.
