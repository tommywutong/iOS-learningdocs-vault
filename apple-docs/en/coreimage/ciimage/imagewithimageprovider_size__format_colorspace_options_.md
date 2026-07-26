---
title: 'imageWithImageProvider:size::format:colorSpace:options:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/imagewithimageprovider:size::format:colorspace:options:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/imagewithimageprovider:size::format:colorspace:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/imagewithimageprovider%3Asize%3A%3Aformat%3Acolorspace%3Aoptions%3A.json'
content_hash: 'sha256:2243bda7906c4368'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# imageWithImageProvider:size::format:colorSpace:options:

<sub>Type Method</sub>

Create an image object based on pixels from an image provider object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIImage *) imageWithImageProvider:(id) provider size:(size_t) width :(size_t) height format:(CIFormat) format colorSpace:(CGColorSpaceRef) colorSpace options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `provider` — An object that implements the `CIImageProvider` protocol.

- `width` — The width of the image.

- `height` — The height of the image.

- `format` — The [CIFormat](../ciformat.md) of the provided pixels.

- `colorSpace` — The color space that the image is defined in. If `nil`, then the pixels will not be is not color matched to the Core Image working color space.

- `options` — A dictionary that contains various [CIImageOption](../ciimageoption.md) keys that affect the resulting [CIImage](../ciimage.md). The option [kCIImageProviderTileSize](../ciimageoption/providertilesize.md) controls if and how the provider object is called in tiles. The option [kCIImageProviderUserInfo](../ciimageoption/provideruserinfo.md) allows additional state to be passed to the provider object.

## Return Value

An autoreleased [CIImage](../ciimage.md) object based on the data provider.

## Discussion

Core Image retains the provider object until the image is deallocated. The image provider object will not be called until the image is rendered.

## See Also

### Creating an Image

- [+ emptyImage](<empty().md>) — Creates and returns an empty image object.
- [- initWithImage:](<init(image_).md>) — Initializes an image object with the specified UIKit image object.
- [- initWithImage:options:](<init(image_options_).md>) — Initializes an image object with the specified UIKit image object, using the specified options.
- [- initWithContentsOfURL:](<init(contentsof_).md>) — Initializes an image object by reading an image from a URL.
- [imageWithContentsOfURL:](imagewithcontentsofurl_.md) — Creates and returns an image object from the contents of a file.
- [- initWithContentsOfURL:options:](<init(contentsof_options_).md>) — Initializes an image object by reading an image from a URL, using the specified options.
- [imageWithContentsOfURL:options:](imagewithcontentsofurl_options_.md) — Creates and returns an image object from the contents of a file, using the specified options.
- [imageWithCGImage:](imagewithcgimage_.md) — Creates and returns an image object from a Quartz 2D image.
- [- initWithCGImage:](<init(cgimage_)-2kvvb.md>) — Initializes an image object with a Quartz 2D image.
- [imageWithCGImage:options:](imagewithcgimage_options_.md) — Creates and returns an image object from a Quartz 2D image using the specified options.
- [- initWithCGImage:options:](<init(cgimage_options_)-8663h.md>) — Initializes an image object with a Quartz 2D image, using the specified options.
- [imageWithCGImageSource:index:options:](imagewithcgimagesource_index_options_.md)
- [- initWithCGImageSource:index:options:](<init(cgimagesource_index_options_)-e2bz.md>)
- [imageWithData:](imagewithdata_.md) — Creates and returns an image object initialized with the supplied image data.
- [- initWithData:](<init(data_).md>) — Initializes an image object with the supplied image data.
