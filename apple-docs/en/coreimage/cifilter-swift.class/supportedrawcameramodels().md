---
title: supportedRawCameraModels()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coreimage/cifilter-swift.class/supportedrawcameramodels()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/supportedrawcameramodels()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/supportedrawcameramodels%28%29.json'
content_hash: 'sha256:1d029a4e7959c0b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# supportedRawCameraModels()

<sub>Type Method</sub>

> [!warning] Deprecated
> Use new CIRAWFilter class instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func supportedRawCameraModels() -> [String]!
```

## See Also

### Deprecated

- [init(CVPixelBuffer:properties:options:)](<init(cvpixelbuffer_properties_options_)-7qpsv.md>) — Creates a filter from a Core Video pixel buffer. _(deprecated)_
- [+ filterWithImageData:options:](<init(imagedata_options_).md>) — Creates a filter that allows the processing of RAW images. _(deprecated)_
- [+ filterWithImageURL:options:](<init(imageurl_options_).md>) — Creates a filter that allows the processing of RAW images. _(deprecated)_
- [CIRAWFilterOption](../cirawfilteroption.md) _(deprecated)_
- [+ serializedXMPFromFilters:inputImageExtent:](<serializedxmp(from_inputimageextent_).md>) — Serializes filter parameters into XMP form that is suitable for embedding in an image. _(deprecated)_
- [+ filterArrayFromSerializedXMP:inputImageExtent:error:](<filterarray(fromserializedxmp_inputimageextent_error_).md>) — Returns an array of filter objects de-serialized from XMP data. _(deprecated)_
