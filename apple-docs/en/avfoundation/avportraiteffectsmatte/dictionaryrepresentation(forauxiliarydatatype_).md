---
title: 'dictionaryRepresentation(forAuxiliaryDataType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avportraiteffectsmatte/dictionaryrepresentation(forauxiliarydatatype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/dictionaryrepresentation(forauxiliarydatatype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avportraiteffectsmatte/dictionaryrepresentation%28forauxiliarydatatype%3A%29.json'
content_hash: 'sha256:8406a964ec9e9eb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPortraitEffectsMatte](../avportraiteffectsmatte.md)

# dictionaryRepresentation(forAuxiliaryDataType:)

<sub>Instance Method</sub>

A dictionary of primitive map information used for writing an image file with a portrait effects matte.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dictionaryRepresentation(forAuxiliaryDataType outAuxDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?
```

## Parameters

- `outAuxDataType` — Must be [kCGImageAuxiliaryDataTypePortraitEffectsMatte](../../imageio/kcgimageauxiliarydatatypeportraiteffectsmatte.md).

## Return Value

A dictionary of primitive map information for [CGImageDestinationAddAuxiliaryDataInfo(_:_:_:)](<../../imageio/cgimagedestinationaddauxiliarydatainfo(______).md>).

## See Also

### Examining a Portrait Effects matte

- [Extracting Portrait Effects matte image data from a photo](../extracting-portrait-effects-matte-image-data-from-a-photo.md) — Check for portrait effects matte metadata in existing images.
- [mattingImage](mattingimage.md) — The portrait effects matte’s internal image, formatted as a pixel buffer.
- [pixelFormatType](pixelformattype.md) — The pixel format type of this portrait effects matte’s internal image.
