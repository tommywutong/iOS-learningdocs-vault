---
title: 'init(imageProvider:size:_:format:colorSpace:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/init(imageprovider:size:_:format:colorspace:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/init(imageprovider:size:_:format:colorspace:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/init%28imageprovider%3Asize%3A_%3Aformat%3Acolorspace%3Aoptions%3A%29.json'
content_hash: 'sha256:a4aa01811d0c8078'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# init(imageProvider:size:_:format:colorSpace:options:)

<sub>Initializer</sub>

Initializes an image object based on pixels from an image provider object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(imageProvider provider: Any, size width: Int, _ height: Int, format: CIFormat, colorSpace: CGColorSpace?, options: [CIImageOption : Any]? = nil)
```

## Parameters

- `provider` — An object that implements the `CIImageProvider` protocol.

- `width` — The width of the image.

- `height` — The height of the image.

- `format` — The [CIFormat](../ciformat.md) of the provided pixels.

- `colorSpace` — The color space that the image is defined in. If `nil`, then the pixels will not be is not color matched to the Core Image working color space.

- `options` — A dictionary that contains various [CIImageOption](../ciimageoption.md) keys that affect the resulting [CIImage](../ciimage.md). The option [kCIImageProviderTileSize](../ciimageoption/providertilesize.md) controls if and how the provider object is called in tiles. The option [kCIImageProviderUserInfo](../ciimageoption/provideruserinfo.md) allows additional state to be passed to the provider object.

## Return Value

An initialized [CIImage](../ciimage.md) object based on the data provider.

## Discussion

Core Image retains the provider object until the image is deallocated. The image provider object will not be called until the image is rendered.

## See Also

### Creating an Image

- [+ emptyImage](<empty().md>) — Creates and returns an empty image object.
- [- initWithImage:](<init(image_).md>) — Initializes an image object with the specified UIKit image object.
- [- initWithImage:options:](<init(image_options_).md>) — Initializes an image object with the specified UIKit image object, using the specified options.
- [- initWithContentsOfURL:](<init(contentsof_).md>) — Initializes an image object by reading an image from a URL.
- [- initWithContentsOfURL:options:](<init(contentsof_options_).md>) — Initializes an image object by reading an image from a URL, using the specified options.
- [- initWithCGImage:](<init(cgimage_)-2kvvb.md>) — Initializes an image object with a Quartz 2D image.
- [- initWithCGImage:options:](<init(cgimage_options_)-8663h.md>) — Initializes an image object with a Quartz 2D image, using the specified options.
- [- initWithCGImageSource:index:options:](<init(cgimagesource_index_options_)-e2bz.md>)
- [- initWithData:](<init(data_).md>) — Initializes an image object with the supplied image data.
- [- initWithData:options:](<init(data_options_).md>) — Initializes an image object with the supplied image data, using the specified options.
- [- initWithBitmapData:bytesPerRow:size:format:colorSpace:](<init(bitmapdata_bytesperrow_size_format_colorspace_).md>) — Initializes an image object with bitmap data.
- [- initWithBitmapImageRep:](<init(bitmapimagerep_).md>) — Initializes an image object with the specified bitmap image representation.
- [- initWithDepthData:](<init(depthdata_).md>)
- [- initWithDepthData:options:](<init(depthdata_options_).md>)
- [- initWithPortaitEffectsMatte:](<init(portaiteffectsmatte_).md>)
