---
title: 'init(imageURL:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+（27.0 起废弃）, iPadOS 10.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.5+（27.0 起废弃）, tvOS 10.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cifilter-swift.class/init(imageurl:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(imageurl:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/init%28imageurl%3Aoptions%3A%29.json'
content_hash: 'sha256:3ecab9b74e829a7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# init(imageURL:options:)

<sub>Initializer</sub>

Creates a filter that allows the processing of RAW images.

> [!warning] Deprecated
> Use [+ filterWithImageURL:](<../cirawfilter/init(imageurl_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init!(imageURL url: URL!, options: [CIRAWFilterOption : Any]! = [:])
```

## Parameters

- `url` — The location of a RAW image file.

- `options` — An options dictionary.  You can pass any of the keys defined in [RAW Image Options](../raw-image-options.md).

## Return Value

A [CIFilter](../cifilter-swift.class.md) object.

## Discussion

The first step when working with RAW images in Core Image is to process the image using either [+ filterWithImageData:options:](<init(imagedata_options_).md>) or [+ filterWithImageURL:options:](<init(imageurl_options_).md>). These initializers create a [CIFilter](../cifilter-swift.class.md) object with an [outputImage](outputimage.md) which is a [CIImage](../ciimage.md) representation of the supplied RAW image.

The newly created filter object allows you fine control over the image processing that isn’t available when working with processed images such a JPEG. The following listing shows how to create a Core Image filter based on a URL named `imageURL`. The image is processed so that its neutral temperature is set to 2,000 Kelvin (giving a blue tint) and its baseline exposure doubled. Finally, a Core Image vignette filter is applied to the processed image in the same way it would be with any other source image:

```objc
let rawFilter = CIFilter(imageURL: imageURL, options: nil)
rawFilter?.setValue(2000,    
                    forKey: kCIInputNeutralTemperatureKey)
if let baselineExposure = rawFilter?.value(forKey: kCIInputBaselineExposureKey) as? NSNumber {    
    rawFilter?.setValue(baselineExposure.doubleValue * 2.5,                        forKey: kCIInputBaselineExposureKey)
}
let vignettedImage = rawFilter?.outputImage?.applyingFilter(    
    "CIVignette",    
    withInputParameters: [kCIInputIntensityKey: 5])
if let outputImage = vignettedImage {    
    imageView.image = UIImage(ciImage: outputImage)
}
```

> [!important] Important
> Core Image doesn’t process the supplied RAW image until the filter’s [outputImage](outputimage.md) is rendered. For this reason, if you supply this initializer with a RAW image of an unsupported format, the filter object will be initialized but its [outputImage](outputimage.md) will be `nil`.

## See Also

### Deprecated

- [init(CVPixelBuffer:properties:options:)](<init(cvpixelbuffer_properties_options_)-7qpsv.md>) — Creates a filter from a Core Video pixel buffer. _(deprecated)_
- [+ filterWithImageData:options:](<init(imagedata_options_).md>) — Creates a filter that allows the processing of RAW images. _(deprecated)_
- [CIRAWFilterOption](../cirawfilteroption.md) _(deprecated)_
- [+ serializedXMPFromFilters:inputImageExtent:](<serializedxmp(from_inputimageextent_).md>) — Serializes filter parameters into XMP form that is suitable for embedding in an image. _(deprecated)_
- [+ filterArrayFromSerializedXMP:inputImageExtent:error:](<filterarray(fromserializedxmp_inputimageextent_error_).md>) — Returns an array of filter objects de-serialized from XMP data. _(deprecated)_
- [+ supportedRawCameraModels](<supportedrawcameramodels().md>) _(deprecated)_
