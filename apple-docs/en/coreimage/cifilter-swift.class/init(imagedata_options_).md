---
title: 'init(imageData:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+（27.0 起废弃）, iPadOS 10.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.5+（27.0 起废弃）, tvOS 10.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cifilter-swift.class/init(imagedata:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(imagedata:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/init%28imagedata%3Aoptions%3A%29.json'
content_hash: 'sha256:7c17db350b1706ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# init(imageData:options:)

<sub>Initializer</sub>

Creates a filter that allows the processing of RAW images.

> [!warning] Deprecated
> Use [+ filterWithImageData:identifierHint:](<../cirawfilter/init(imagedata_identifierhint_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init!(imageData data: Data!, options: [CIRAWFilterOption : Any]! = [:])
```

## Parameters

- `data` — The RAW image data to initialize the object with.

- `options` — An options dictionary.

## Return Value

A [CIFilter](../cifilter-swift.class.md) object.

## Discussion

You can pass any of the keys defined in [RAW Image Options](../raw-image-options.md) along with the appropriate value in `options`. You should provide a source type identifier hint key ([kCGImageSourceTypeIdentifierHint](../../imageio/kcgimagesourcetypeidentifierhint.md)) and the appropriate source type value to help the decoder determine the file type. Otherwise it’s possible to obtain incorrect results.

The first step when working with RAW images in Core Image is to process the image using either [+ filterWithImageData:options:](<init(imagedata_options_).md>) or [+ filterWithImageURL:options:](<init(imageurl_options_).md>). These initializers create a [CIFilter](../cifilter-swift.class.md) object with an [outputImage](outputimage.md) which is a [CIImage](../ciimage.md) representation of the supplied RAW image. You can process After calling this method, the [CIFilter](../cifilter-swift.class.md) object returns a [CIImage](../ciimage.md) object that’s properly processed similar to images retrieved using the `outputImage` key.

> [!important] Important
> Core Image doesn’t process the supplied RAW image until the filter’s [outputImage](outputimage.md) is rendered. For this reason, if you supply this initializer with a RAW image of an unsupported format, the filter object will be initialized but its [outputImage](outputimage.md) will be `nil`.

## See Also

### Deprecated

- [init(CVPixelBuffer:properties:options:)](<init(cvpixelbuffer_properties_options_)-7qpsv.md>) — Creates a filter from a Core Video pixel buffer. _(deprecated)_
- [+ filterWithImageURL:options:](<init(imageurl_options_).md>) — Creates a filter that allows the processing of RAW images. _(deprecated)_
- [CIRAWFilterOption](../cirawfilteroption.md) _(deprecated)_
- [+ serializedXMPFromFilters:inputImageExtent:](<serializedxmp(from_inputimageextent_).md>) — Serializes filter parameters into XMP form that is suitable for embedding in an image. _(deprecated)_
- [+ filterArrayFromSerializedXMP:inputImageExtent:error:](<filterarray(fromserializedxmp_inputimageextent_error_).md>) — Returns an array of filter objects de-serialized from XMP data. _(deprecated)_
- [+ supportedRawCameraModels](<supportedrawcameramodels().md>) _(deprecated)_
