---
title: 'init(fromImageSourceAuxiliaryDataType:dictionaryRepresentation:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsemanticsegmentationmatte/init(fromimagesourceauxiliarydatatype:dictionaryrepresentation:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/init(fromimagesourceauxiliarydatatype:dictionaryrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsemanticsegmentationmatte/init%28fromimagesourceauxiliarydatatype%3Adictionaryrepresentation%3A%29.json'
content_hash: 'sha256:e9aa51fe70eb1962'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSemanticSegmentationMatte](../avsemanticsegmentationmatte.md)

# init(fromImageSourceAuxiliaryDataType:dictionaryRepresentation:)

<sub>Initializer</sub>

Returns a new semantic segmentation matte instance from auxiliary image information in an image file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(fromImageSourceAuxiliaryDataType imageSourceAuxiliaryDataType: CFString, dictionaryRepresentation imageSourceAuxiliaryDataInfoDictionary: [AnyHashable : Any]) throws
```

## Parameters

- `imageSourceAuxiliaryDataType` — The `kCGImageAuxiliaryDataType` constants corresponding to the semantic segmentation matte being created (see `CGImageProperties`).

- `imageSourceAuxiliaryDataInfoDictionary` — A dictionary of primitive semantic segmentation matte information obtained from [CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)](<../../imageio/cgimagesourcecopyauxiliarydatainfoatindex(______).md>).

## Return Value

A new semantic segmentation matte instance, or `nil` if the auxiliary data info dictionary is malformed.

## See Also

### Creating a segmentation matte

- [- semanticSegmentationMatteByReplacingSemanticSegmentationMatteWithPixelBuffer:error:](<replacingsemanticsegmentationmatte(with_).md>) — Returns a semantic segmentation matte instance that wraps the replacement pixel buffer.
- [- semanticSegmentationMatteByApplyingExifOrientation:](<applyingexiforientation(__).md>) — Returns a new semantic segmentation matte instance with the specified Exif orientation applied.
- [- dictionaryRepresentationForAuxiliaryDataType:](<dictionaryrepresentation(forauxiliarydatatype_).md>) — Returns a dictionary of primitive map information to use when writing an image file with a semantic segmentation matte.
