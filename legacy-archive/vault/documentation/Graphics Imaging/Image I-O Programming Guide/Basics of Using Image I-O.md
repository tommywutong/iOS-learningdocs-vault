---
title: Image I/O Programming Guide
apple_id: TP40005462
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageIOGuide/imageio_basics/ikpg_basics.html
archived_at: '2026-07-15T07:35:42.401734Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Image I/O Programming Guide](Introduction.md)


[Next](Creating%20and%20Using%20Image%20Sources.md)[Previous](Introduction.md)

# Basics of Using Image I/O

The Image I/O framework provides opaque data types for reading image data from a source ([CGImageSourceRef](https://developer.apple.com/documentation/imageio/cgimagesource)) and writing image data to a destination ([CGImageDestinationRef](https://developer.apple.com/documentation/imageio/cgimagedestinationref)). It supports a wide range of image formats, including the standard web formats, high dynamic range images, and raw camera data. Image I/O has many other features such as:

- The fastest image decoders and encoders for the Mac platform
- The ability to load images incrementally
- Support for image metadata
- Effective caching

You can create image source and image destination objects from:

- URLs. Images whose location can be specified as a URL can act as a supplier or receiver of image data. In Image I/O, a URL is represented as the Core Foundation data type [CFURLRef](https://developer.apple.com/documentation/corefoundation/cfurl).
- The Core Foundation objects [CFDataRef](https://developer.apple.com/documentation/corefoundation/cfdata) and [CFMutableDataRef](https://developer.apple.com/documentation/corefoundation/cfmutabledataref).
- Quartz data consumer ([CGDataConsumerRef](https://developer.apple.com/documentation/coregraphics/cgdataconsumer)) and data provider ([CGDataProviderRef](https://developer.apple.com/documentation/coregraphics/cgdataprovider)) objects.

Image I/O resides in the Application Services framework in OS X, and in the Image I/O framework in iOS. After adding the framework to your application, import the header file by including this statement:

`#import <ImageIO/ImageIO.h>`

The Image I/O framework understands most of the common image file formats, such as JPEG, JPEG2000, RAW, TIFF, BMP, and PNG. Not all formats are supported on each platform. For the most up-to-date list of what Image I/O supports, you can call the these functions:

- [CGImageSourceCopyTypeIdentifiers](https://developer.apple.com/documentation/imageio/1465383-cgimagesourcecopytypeidentifiers) returns an array of the [Uniform Type Identifiers](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/UniformTypeIdentifier.html#//apple_ref/doc/uid/TP40008195-CH60) (UTIs) that Image I/O supports as image sources.
- [CGImageDestinationCopyTypeIdentifiers](https://developer.apple.com/documentation/imageio/1465316-cgimagedestinationcopytypeidenti) returns an array of the uniform type identifiers (UTIs) that Image I/O supports as image destinations.

You can then use the [CFShow](https://developer.apple.com/documentation/corefoundation/1541433-cfshow) function to print the array to the debugger console in Xcode, as shown in Listing 1-1. The strings in the array returned by these functions take the form of `com.apple.pict`, `public.jpeg`, `public.tiff`, and so on. [Table 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrsfvbuqmrrgywvgvzt) lists the UTIs for many common image file formats. OS X and iOS define constants for most common image file formats; The full set of constants are declared in the `UTCoreTypes.h` header file. You can use these constants when you need to specify an image type, either as a hint for an image source (`kCGImageSourceTypeIdentifierHint`) or as an image type for an image destination.

__Listing 1-1__  Getting and printing supported UTIs

```
CFArrayRef mySourceTypes = CGImageSourceCopyTypeIdentifiers();
CFShow(mySourceTypes);
CFArrayRef myDestinationTypes = CGImageDestinationCopyTypeIdentifiers();
CFShow(myDestinationTypes);
```


__Table 1-1__  Common uniform type identifiers (UTIs) and image content type constants

| Uniform type identifier | Image content type constant |
| public.image | `kUTTypeImage` |
| public.png | `kUTTypePNG` |
| public.jpeg | `kUTTypeJPEG` |
| public.jpeg-2000 (OS X only) | `kUTTypeJPEG2000` |
| public.tiff | `kUTTypeTIFF` |
| com.apple.pict (OS X only) | `kUTTypePICT` |
| com.compuserve.gif | `kUTTypeGIF` |

[Next](Creating%20and%20Using%20Image%20Sources.md)[Previous](Introduction.md)

