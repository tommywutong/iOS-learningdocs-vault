---
title: 'replacingSemanticSegmentationMatte(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsemanticsegmentationmatte/replacingsemanticsegmentationmatte(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/replacingsemanticsegmentationmatte(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsemanticsegmentationmatte/replacingsemanticsegmentationmatte%28with%3A%29.json'
content_hash: 'sha256:0528800f6643a7fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSemanticSegmentationMatte](../avsemanticsegmentationmatte.md)

# replacingSemanticSegmentationMatte(with:)

<sub>Instance Method</sub>

Returns a semantic segmentation matte instance that wraps the replacement pixel buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacingSemanticSegmentationMatte(with pixelBuffer: CVPixelBuffer) throws -> Self
```

## Parameters

- `pixelBuffer` — A pixel buffer containing a semantic segmentation matting image, represented as [kCVPixelFormatType_OneComponent8](../../corevideo/kcvpixelformattype_onecomponent8.md) with a [kCVImageBufferTransferFunction_Linear](../../corevideo/kcvimagebuffertransferfunction_linear.md) transfer function.

## Return Value

A new semantic segmentation matte instance, or `nil` if the pixel buffer is malformed.

## Discussion

When applying complex edits to media containing a semantic segmentation matte, you may create a derivative matte with arbitrary transforms applied to it. You can then use this method to create a new semantic segmentation matte instance.

## See Also

### Creating a segmentation matte

- [+ semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:](<init(fromimagesourceauxiliarydatatype_dictionaryrepresentation_).md>) — Returns a new semantic segmentation matte instance from auxiliary image information in an image file.
- [- semanticSegmentationMatteByApplyingExifOrientation:](<applyingexiforientation(__).md>) — Returns a new semantic segmentation matte instance with the specified Exif orientation applied.
- [- dictionaryRepresentationForAuxiliaryDataType:](<dictionaryrepresentation(forauxiliarydatatype_).md>) — Returns a dictionary of primitive map information to use when writing an image file with a semantic segmentation matte.
