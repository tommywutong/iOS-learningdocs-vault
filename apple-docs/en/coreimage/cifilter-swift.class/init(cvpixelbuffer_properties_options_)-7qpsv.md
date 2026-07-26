---
title: 'init(CVPixelBuffer:properties:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+（27.0 起废弃）, iPadOS 10.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.12+（27.0 起废弃）, tvOS 10.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cifilter-swift.class/init(cvpixelbuffer:properties:options:)-7qpsv'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(cvpixelbuffer:properties:options:)-7qpsv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/init%28cvpixelbuffer%3Aproperties%3Aoptions%3A%29-7qpsv.json'
content_hash: 'sha256:4ece1d0fdd220711'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# init(CVPixelBuffer:properties:options:)

<sub>Initializer</sub>

Creates a filter from a Core Video pixel buffer.

> [!warning] Deprecated
> Use [+ filterWithCVPixelBuffer:properties:](<../cirawfilter/init(cvpixelbuffer_properties_)-6209q.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init!(CVPixelBuffer pixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]! = [:])
```

## Parameters

- `pixelBuffer` — CVPixelBufferRef with one of the following RAW pixel format types: [kCVPixelFormatType_14Bayer_GRBG](../../corevideo/kcvpixelformattype_14bayer_grbg.md) [kCVPixelFormatType_14Bayer_RGGB](../../corevideo/kcvpixelformattype_14bayer_rggb.md) [kCVPixelFormatType_14Bayer_BGGR](../../corevideo/kcvpixelformattype_14bayer_bggr.md) [kCVPixelFormatType_14Bayer_GBRG](../../corevideo/kcvpixelformattype_14bayer_gbrg.md)

- `properties` — A properties dictionary. Defines the properties of the pixel buffer.

- `options` — An options dictionary.  You can pass any of the keys defined in [RAW Image Options](../raw-image-options.md).

## Return Value

A [CIFilter](../cifilter-swift.class.md) object.

## Discussion

The first step when working with RAW images in Core Image is to process the image using either [+ filterWithImageData:options:](<init(imagedata_options_).md>) or [+ filterWithImageURL:options:](<init(imageurl_options_).md>). These initializers create a [CIFilter](../cifilter-swift.class.md) object with an [outputImage](outputimage.md) which is a [CIImage](../ciimage.md) representation of the supplied RAW image.

> [!important] Important
> Core Image doesn’t process the supplied RAW image until the filter’s [outputImage](outputimage.md) is rendered. For this reason, if you supply this initializer with a RAW image of an unsupported format, the filter object will be initialized but its [outputImage](outputimage.md) will be nil.

## See Also

### Deprecated

- [+ filterWithImageData:options:](<init(imagedata_options_).md>) — Creates a filter that allows the processing of RAW images. _(deprecated)_
- [+ filterWithImageURL:options:](<init(imageurl_options_).md>) — Creates a filter that allows the processing of RAW images. _(deprecated)_
- [CIRAWFilterOption](../cirawfilteroption.md) _(deprecated)_
- [+ serializedXMPFromFilters:inputImageExtent:](<serializedxmp(from_inputimageextent_).md>) — Serializes filter parameters into XMP form that is suitable for embedding in an image. _(deprecated)_
- [+ filterArrayFromSerializedXMP:inputImageExtent:error:](<filterarray(fromserializedxmp_inputimageextent_error_).md>) — Returns an array of filter objects de-serialized from XMP data. _(deprecated)_
- [+ supportedRawCameraModels](<supportedrawcameramodels().md>) _(deprecated)_
