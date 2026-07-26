---
title: 'serializedXMP(from:inputImageExtent:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+（17.0 起废弃）, iPadOS 6.0+（17.0 起废弃）, Mac Catalyst 13.1+（17.0 起废弃）, macOS 10.9+（14.0 起废弃）, tvOS（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cifilter-swift.class/serializedxmp(from:inputimageextent:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/serializedxmp(from:inputimageextent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/serializedxmp%28from%3Ainputimageextent%3A%29.json'
content_hash: 'sha256:540ca241bead58a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# serializedXMP(from:inputImageExtent:)

<sub>Type Method</sub>

Serializes filter parameters into XMP form that is suitable for embedding in an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func serializedXMP(from filters: [CIFilter], inputImageExtent extent: CGRect) -> Data?
```

## Parameters

- `filters` — The array of filters to serialize. See Discussion for the filters that can be serialized.

- `extent` — The extent of the input image to the filter.

## Discussion

At this time the only filters classes that can be serialized using this method are, CIAffineTransform, CICrop, and the filters returned by the [CIImage](../ciimage.md) methods [- autoAdjustmentFilters](<../ciimage/autoadjustmentfilters().md>) and [- autoAdjustmentFiltersWithOptions:](<../ciimage/autoadjustmentfilters(options_).md>). The parameters of other filter classes will not be serialized.

## See Also

### Deprecated

- [init(CVPixelBuffer:properties:options:)](<init(cvpixelbuffer_properties_options_)-7qpsv.md>) — Creates a filter from a Core Video pixel buffer. _(deprecated)_
- [+ filterWithImageData:options:](<init(imagedata_options_).md>) — Creates a filter that allows the processing of RAW images. _(deprecated)_
- [+ filterWithImageURL:options:](<init(imageurl_options_).md>) — Creates a filter that allows the processing of RAW images. _(deprecated)_
- [CIRAWFilterOption](../cirawfilteroption.md) _(deprecated)_
- [+ filterArrayFromSerializedXMP:inputImageExtent:error:](<filterarray(fromserializedxmp_inputimageextent_error_).md>) — Returns an array of filter objects de-serialized from XMP data. _(deprecated)_
- [+ supportedRawCameraModels](<supportedrawcameramodels().md>) _(deprecated)_
