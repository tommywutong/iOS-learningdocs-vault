---
title: 'dictionaryRepresentation(forAuxiliaryDataType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avdepthdata/dictionaryrepresentation(forauxiliarydatatype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/dictionaryrepresentation(forauxiliarydatatype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/dictionaryrepresentation%28forauxiliarydatatype%3A%29.json'
content_hash: 'sha256:b7743d8b99c94458'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDepthData](../avdepthdata.md)

# dictionaryRepresentation(forAuxiliaryDataType:)

<sub>Instance Method</sub>

Returns a dictionary representation of the depth data suitable for writing into an image file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func dictionaryRepresentation(forAuxiliaryDataType outAuxDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?
```

## Parameters

- `outAuxDataType` — On output, either [kCGImageAuxiliaryDataTypeDisparity](../../imageio/kcgimageauxiliarydatatypedisparity.md) or [kCGImageAuxiliaryDataTypeDepth](../../imageio/kcgimageauxiliarydatatypedepth.md), depending on the depth data’s type.

## Discussion

When using `CGImageDestination` functions to write depth data (along with image data) to a HEIF, JPEG, or DNG file, you can use this method to obtain a dictionary of primitive depth map information, then use the [CGImageDestinationAddAuxiliaryDataInfo(_:_:_:)](<../../imageio/cgimagedestinationaddauxiliarydatainfo(______).md>) function to embed that data into the output file.

## See Also

### Creating depth data

- [+ depthDataFromDictionaryRepresentation:error:](<init(fromdictionaryrepresentation_).md>) — Creates a depth data object from depth information such as that found in an image file.
