---
title: 'filterArray(fromSerializedXMP:inputImageExtent:error:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+（17.0 起废弃）, iPadOS 6.0+（17.0 起废弃）, Mac Catalyst 13.1+（17.0 起废弃）, macOS 10.9+（14.0 起废弃）, tvOS（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cifilter-swift.class/filterarray(fromserializedxmp:inputimageextent:error:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/filterarray(fromserializedxmp:inputimageextent:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/filterarray%28fromserializedxmp%3Ainputimageextent%3Aerror%3A%29.json'
content_hash: 'sha256:2457eec33c0e35c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# filterArray(fromSerializedXMP:inputImageExtent:error:)

<sub>Type Method</sub>

Returns an array of filter objects de-serialized from XMP data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func filterArray(fromSerializedXMP xmpData: Data, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [CIFilter]
```

## Parameters

- `xmpData` — The XMP data created previously by calling [+ serializedXMPFromFilters:inputImageExtent:](<serializedxmp(from_inputimageextent_).md>).

- `extent` — The extent of the image from which the XMP data was extracted.

- `outError` — The address of an `NSError` object for receiving errors, otherwise `nil`.

## See Also

### Deprecated

- [init(CVPixelBuffer:properties:options:)](<init(cvpixelbuffer_properties_options_)-7qpsv.md>) — Creates a filter from a Core Video pixel buffer. _(deprecated)_
- [+ filterWithImageData:options:](<init(imagedata_options_).md>) — Creates a filter that allows the processing of RAW images. _(deprecated)_
- [+ filterWithImageURL:options:](<init(imageurl_options_).md>) — Creates a filter that allows the processing of RAW images. _(deprecated)_
- [CIRAWFilterOption](../cirawfilteroption.md) _(deprecated)_
- [+ serializedXMPFromFilters:inputImageExtent:](<serializedxmp(from_inputimageextent_).md>) — Serializes filter parameters into XMP form that is suitable for embedding in an image. _(deprecated)_
- [+ supportedRawCameraModels](<supportedrawcameramodels().md>) _(deprecated)_
