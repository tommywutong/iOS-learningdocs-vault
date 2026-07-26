---
title: 'dictionaryRepresentation(forAuxiliaryDataType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsemanticsegmentationmatte/dictionaryrepresentation(forauxiliarydatatype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/dictionaryrepresentation(forauxiliarydatatype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsemanticsegmentationmatte/dictionaryrepresentation%28forauxiliarydatatype%3A%29.json'
content_hash: 'sha256:d66eb62cf7923f2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSemanticSegmentationMatte](../avsemanticsegmentationmatte.md)

# dictionaryRepresentation(forAuxiliaryDataType:)

<sub>Instance Method</sub>

Returns a dictionary of primitive map information to use when writing an image file with a semantic segmentation matte.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dictionaryRepresentation(forAuxiliaryDataType outAuxDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?
```

## Parameters

- `outAuxDataType` — On output, the auxiliary data type to be used when calling the ImageIO framework’s [CGImageDestinationAddAuxiliaryDataInfo(_:_:_:)](<../../imageio/cgimagedestinationaddauxiliarydatainfo(______).md>) function. Currently supported auxiliary data types are enumerated in `CGImageProperties`.

## Return Value

A dictionary of `CGImageDestination`-compatible semantic segmentation matte information, or `nil` if the auxiliary data type is unsupported.

## See Also

### Creating a segmentation matte

- [+ semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:](<init(fromimagesourceauxiliarydatatype_dictionaryrepresentation_).md>) — Returns a new semantic segmentation matte instance from auxiliary image information in an image file.
- [- semanticSegmentationMatteByReplacingSemanticSegmentationMatteWithPixelBuffer:error:](<replacingsemanticsegmentationmatte(with_).md>) — Returns a semantic segmentation matte instance that wraps the replacement pixel buffer.
- [- semanticSegmentationMatteByApplyingExifOrientation:](<applyingexiforientation(__).md>) — Returns a new semantic segmentation matte instance with the specified Exif orientation applied.
