---
title: CIImage
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage.json'
content_hash: 'sha256:8a20fb7bfb95a6bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIImage

<sub>Class</sub>

A representation of an image to be processed or produced by Core Image filters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIImage
```

## Overview

You use `CIImage` objects in conjunction with other Core Image classes—such as [CIFilter](cifilter-swift.class.md), [CIContext](cicontext.md), [CIVector](civector.md), and [CIColor](cicolor.md)—to take advantage of the built-in Core Image filters when processing images. You can create `CIImage` objects with data supplied from a variety of sources, including Quartz 2D images, Core Video image buffers ([CVImageBuffer](../corevideo/cvimagebuffer.md)), URL-based objects, and `NSData` objects.

Although a `CIImage` object has image data associated with it, it is not an image. You can think of a `CIImage` object as an image “recipe.” A `CIImage` object has all the information necessary to produce an image, but Core Image doesn’t actually render an image until it is told to do so. This lazy evaluation allows Core Image to operate as efficiently as possible. To show a `CIImage` object as an on-screen image, you can display it as a [UIImage](../uikit/uiimage.md) in [UIImageView](../uikit/uiimageview.md):

**Swift**

```swift
guard let imageURL = Bundle.main.url(forResource: "YourJPEGName", withExtension: "JPG") else {
    print("Could not find image")
    return
}
guard let let ciImage = CIImage(contentsOf: imageURL) else {
    print("Could not create CIImage")
    return
}
let uiImage = UIImage(ciImage: ciImage)
let imageView = UIImageView(image: uiImage)    
self.view.addSubview(imageView)
```

**Objective-C**

```objc
NSURL* imageURL = [[NSBundle mainBundle] URLForResource:@"YourJPEGName" withExtension:@"JPG"];
CIImage* ciImage = [CIImage imageWithContentsOfURL:imageURL];
UIImage* uiImage = [UIImage imageWithCIImage:ciImage];
UIImageView* imageView = [[UIImageView alloc] initWithImage:uiImage];
[self.view addSubview:imageView];
```

`CIContext`  and `CIImage` objects are immutable, which means each can be shared safely among threads. Multiple threads can use the same GPU or CPU `CIContext` object to render `CIImage` objects.  However, this is not the case for `CIFilter` objects, which are mutable. A `CIFilter` object cannot be shared safely among threads.  If you app is multithreaded, each thread must create its own `CIFilter` objects. Otherwise, your app could behave unexpectedly.

Core Image also provides auto-adjustment methods. These methods analyze an image for common deficiencies and return a set of filters to correct those deficiencies. The filters are preset with values for improving image quality by altering values for skin tones, saturation, contrast, and shadows and for removing red-eye or other artifacts caused by flash. (See Getting Autoadjustment Filters.)

For a discussion of all the methods you can use to create `CIImage` objects on iOS and macOS, see [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [AttachableAsImage](../testing/attachableasimage.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an Image

- [+ emptyImage](<ciimage/empty().md>) — Creates and returns an empty image object.
- [- initWithImage:](<ciimage/init(image_).md>) — Initializes an image object with the specified UIKit image object.
- [- initWithImage:options:](<ciimage/init(image_options_).md>) — Initializes an image object with the specified UIKit image object, using the specified options.
- [- initWithContentsOfURL:](<ciimage/init(contentsof_).md>) — Initializes an image object by reading an image from a URL.
- [- initWithContentsOfURL:options:](<ciimage/init(contentsof_options_).md>) — Initializes an image object by reading an image from a URL, using the specified options.
- [- initWithCGImage:](<ciimage/init(cgimage_)-2kvvb.md>) — Initializes an image object with a Quartz 2D image.
- [- initWithCGImage:options:](<ciimage/init(cgimage_options_)-8663h.md>) — Initializes an image object with a Quartz 2D image, using the specified options.
- [- initWithCGImageSource:index:options:](<ciimage/init(cgimagesource_index_options_)-e2bz.md>)
- [- initWithData:](<ciimage/init(data_).md>) — Initializes an image object with the supplied image data.
- [- initWithData:options:](<ciimage/init(data_options_).md>) — Initializes an image object with the supplied image data, using the specified options.
- [- initWithBitmapData:bytesPerRow:size:format:colorSpace:](<ciimage/init(bitmapdata_bytesperrow_size_format_colorspace_).md>) — Initializes an image object with bitmap data.
- [- initWithBitmapImageRep:](<ciimage/init(bitmapimagerep_).md>) — Initializes an image object with the specified bitmap image representation.
- [- initWithImageProvider:size::format:colorSpace:options:](<ciimage/init(imageprovider_size___format_colorspace_options_).md>) — Initializes an image object based on pixels from an image provider object.
- [- initWithDepthData:](<ciimage/init(depthdata_).md>)
- [- initWithDepthData:options:](<ciimage/init(depthdata_options_).md>)
- [- initWithPortaitEffectsMatte:](<ciimage/init(portaiteffectsmatte_).md>)
- [- initWithPortaitEffectsMatte:options:](<ciimage/init(portaiteffectsmatte_options_).md>)
- [- initWithSemanticSegmentationMatte:](<ciimage/init(semanticsegmentationmatte_).md>)
- [- initWithSemanticSegmentationMatte:options:](<ciimage/init(semanticsegmentationmatte_options_).md>)
- [- initWithCVImageBuffer:](<ciimage/init(cvimagebuffer_)-7wmzq.md>) — Initializes an image object from the contents of a Core Video image buffer.
- [- initWithCVImageBuffer:options:](<ciimage/init(cvimagebuffer_options_)-8upim.md>) — Initializes an image object from the contents of a Core Video image buffer, using the specified options.
- [- initWithCVPixelBuffer:](<ciimage/init(cvpixelbuffer_)-3wng7.md>) — Initializes an image object from the contents of a Core Video pixel buffer.
- [- initWithCVPixelBuffer:options:](<ciimage/init(cvpixelbuffer_options_)-9x2pz.md>) — Initializes an image object from the contents of a Core Video pixel buffer using the specified options.
- [- initWithMTLTexture:options:](<ciimage/init(mtltexture_options_)-67uvj.md>) — Initializes an image object with data supplied by a Metal texture.
- [- initWithIOSurface:](<ciimage/init(iosurface_)-5e9yc.md>) — Initializes an image with the contents of an IOSurface.
- [- initWithIOSurface:options:](<ciimage/init(iosurface_options_)-48cta.md>) — Initializes, using the specified options, an image with the contents of an IOSurface.

### Creating an Image by Modifying an Existing Image

- [- imageByApplyingFilter:withInputParameters:](<ciimage/applyingfilter(__parameters_).md>) — Returns a new image created by applying a filter to the original image with the specified name and parameters.
- [- imageByApplyingFilter:](<ciimage/applyingfilter(__).md>) — Applies the filter to an image and returns the output.
- [- imageByApplyingTransform:](<ciimage/transformed(by_).md>) — Returns a new image that represents the original image after applying an affine transform.
- [- imageByApplyingTransform:highQualityDownsample:](<ciimage/transformed(by_highqualitydownsample_).md>)
- [- imageByCroppingToRect:](<ciimage/cropped(to_).md>) — Returns a new image with a cropped portion of the original image.
- [- imageByApplyingOrientation:](<ciimage/oriented(forexiforientation_).md>) — Returns a new image created by transforming the original image to the specified EXIF orientation.
- [- imageByClampingToExtent](<ciimage/clampedtoextent().md>) — Returns a new image created by making the pixel colors along its edges extend infinitely in all directions.
- [- imageByClampingToRect:](<ciimage/clamped(to_).md>) — Returns a new image created by cropping to a specified area, then making the pixel colors along the edges of the cropped image extend infinitely in all directions.
- [- imageByCompositingOverImage:](<ciimage/composited(over_).md>) — Returns a new image created by compositing the original image over the specified destination image.
- [- imageByConvertingWorkingSpaceToLab](<ciimage/convertingworkingspacetolab().md>)
- [- imageByConvertingLabToWorkingSpace](<ciimage/convertinglabtoworkingspace().md>)
- [- imageByColorMatchingColorSpaceToWorkingSpace:](<ciimage/matchedtoworkingspace(from_).md>) — Returns a new image created by color matching from the specified color space to the context’s working color space.
- [- imageByColorMatchingWorkingSpaceToColorSpace:](<ciimage/matchedfromworkingspace(to_).md>) — Returns a new image created by color matching from the context’s working color space to the specified color space.
- [- imageByPremultiplyingAlpha](<ciimage/premultiplyingalpha().md>) — Returns a new image created by multiplying the image’s RGB values by its alpha values.
- [- imageByUnpremultiplyingAlpha](<ciimage/unpremultiplyingalpha().md>) — Returns a new image created by dividing the image’s RGB values by its alpha values.
- [- imageBySettingAlphaOneInExtent:](<ciimage/settingalphaone(in_).md>) — Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.
- [- imageByApplyingGaussianBlurWithSigma:](<ciimage/applyinggaussianblur(sigma_).md>) — Create an image by applying a gaussian blur to the receiver.
- [- imageBySettingProperties:](<ciimage/settingproperties(__).md>) — Return a new image by changing the receiver’s metadata properties.
- [- imageByInsertingIntermediate](<ciimage/insertingintermediate().md>) — Create an image that inserts a intermediate that is cacheable
- [- imageByInsertingIntermediate:](<ciimage/insertingintermediate(cache_).md>) — Create an image that inserts a intermediate that is cacheable.

### Creating Solid Colors

- [- initWithColor:](<ciimage/init(color_).md>) — Initializes an image of infinite extent whose entire content is the specified color.
- [blackImage](ciimage/black.md)
- [blueImage](ciimage/blue.md)
- [clearImage](ciimage/clear.md)
- [cyanImage](ciimage/cyan.md)
- [grayImage](ciimage/gray.md)
- [greenImage](ciimage/green.md)
- [magentaImage](ciimage/magenta.md)
- [redImage](ciimage/red.md)
- [whiteImage](ciimage/white.md)
- [yellowImage](ciimage/yellow.md)

### Getting Image Information

- [definition](ciimage/definition.md) — Returns a filter shape object that represents the domain of definition of the image.
- [extent](ciimage/extent.md) — A rectangle that specifies the extent of the image.
- [properties](ciimage/properties.md) — Returns the metadata properties dictionary of the image.
- [url](ciimage/url.md) — The URL from which the image was loaded.
- [colorSpace](ciimage/colorspace.md) — The color space of the image.
- [- imageTransformForOrientation:](<ciimage/orientationtransform(forexiforientation_).md>) — Returns the transformation needed to reorient the image to the specified orientation.

### Drawing Images

- [- drawAtPoint:fromRect:operation:fraction:](<ciimage/draw(at_from_operation_fraction_).md>) — Draws all or part of the image at the specified point in the current coordinate system.
- [- drawInRect:fromRect:operation:fraction:](<ciimage/draw(in_from_operation_fraction_).md>) — Draws all or part of the image in the specified rectangle in the current coordinate system

### Getting Autoadjustment Filters

- [- autoAdjustmentFilters](<ciimage/autoadjustmentfilters().md>) — Returns all possible automatically selected and configured filters for adjusting the image.
- [- autoAdjustmentFiltersWithOptions:](<ciimage/autoadjustmentfilters(options_).md>) — Returns a subset of automatically selected and configured filters for adjusting the image.
- [Autoadjustment Keys](autoadjustment-keys.md) — Constants used as keys in the options dictionary for the [- autoAdjustmentFiltersWithOptions:](<ciimage/autoadjustmentfilters(options_).md>) method.

### Working with Filter Regions of Interest

- [- regionOfInterestForImage:inRect:](<ciimage/regionofinterest(for_in_).md>) — Returns the region of interest for the filter chain that generates the image.

### Working with Orientation

- [- imageByApplyingCGOrientation:](<ciimage/oriented(__).md>) — Transforms the original image by a given orientation.
- [- imageTransformForCGOrientation:](<ciimage/orientationtransform(for_).md>) — The affine transform for changing the image to the given orientation.

### Sampling the Image

- [- imageBySamplingNearest](<ciimage/samplingnearest().md>) — Create an image by changing the receiver’s sample mode to nearest neighbor.
- [- imageBySamplingLinear](<ciimage/samplinglinear().md>) — Create an image by changing the receiver’s sample mode to bilinear interpolation.

### Accessing Original Image Content

- [CGImage](ciimage/cgimage.md) — The CoreGraphics image object this image was created from, if applicable.
- [pixelBuffer](ciimage/pixelbuffer.md) — The CoreVideo pixel buffer this image was created from, if applicable.
- [depthData](ciimage/depthdata.md) — Depth data associated with the image.
- [portraitEffectsMatte](ciimage/portraiteffectsmatte.md) — The portrait effects matte associated with the image.
- [semanticSegmentationMatte](ciimage/semanticsegmentationmatte.md)

### Image Dictionary Keys

- [CIImageOption](ciimageoption.md)

### AutoAdjustment Keys

- [CIImageAutoAdjustmentOption](ciimageautoadjustmentoption.md)

### Deprecated

- [- initWithCGLayer:](<ciimage/init(cglayer_)-2lgo6.md>) — Initializes an image object  from the contents supplied by a CGLayer object. _(deprecated)_
- [- initWithCGLayer:options:](<ciimage/init(cglayer_options_)-3p3l3.md>) — Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options. _(deprecated)_
- [- initWithTexture:size:flipped:colorSpace:](<ciimage/init(texture_size_flipped_colorspace_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithTexture:size:flipped:options:](<ciimage/init(texture_size_flipped_options_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithIOSurface:plane:format:options:](<ciimage/init(iosurface_plane_format_options_)-93isn.md>) — Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface. _(deprecated)_
- [kCIImageTextureTarget](ciimageoption/texturetarget.md) — The key for an OpenGL texture target. _(deprecated)_
- [kCIImageTextureFormat](ciimageoption/textureformat.md) — The key for an OpenGL texture format. _(deprecated)_

### Instance Properties

- [contentHeadroom](ciimage/contentheadroom.md) — Returns the content headroom of the image.
- [opaque](ciimage/isopaque.md) — Returns YES if the image is known to have and alpha value of `1.0` over the entire image extent.
- [metalTexture](ciimage/metaltexture.md)
- [contentAverageLightLevel](ciimage/contentaveragelightlevel.md) — Returns the content average light level of the image.

### Instance Methods

- [- imageByApplyingGainMap:](<ciimage/applyinggainmap(__).md>) — Create an image that applies a gain map Core Image image to the received Core Image image.
- [- imageByApplyingGainMap:headroom:](<ciimage/applyinggainmap(__headroom_).md>) — Create an image that applies a gain map Core Image image with a specified headroom to the received Core Image image.
- [- imageByInsertingTiledIntermediate](<ciimage/insertingtiledintermediate().md>) — Create an image that inserts a intermediate that is cached in tiles
- [- imageBySettingContentAverageLightLevel:](<ciimage/settingcontentaveragelightlevel(__).md>) — Create an image by changing the receiver’s contentAverageLightLevel property.
- [- imageBySettingContentHeadroom:](<ciimage/settingcontentheadroom(__).md>) — Create an image by changing the receiver’s contentHeadroom property.

### Initializers

- [init(CGImage:)](<ciimage/init(cgimage_)-5vlch.md>)
- [init(CGImage:)](<ciimage/init(cgimage_)-8cm8a.md>)
- [init(CGImage:options:)](<ciimage/init(cgimage_options_)-1ksqh.md>)
- [init(CGImage:options:)](<ciimage/init(cgimage_options_)-28wtj.md>)
- [init(CGImageSource:index:options:)](<ciimage/init(cgimagesource_index_options_)-2dium.md>)
- [init(CGImageSource:index:options:)](<ciimage/init(cgimagesource_index_options_)-4b3fz.md>)
- [init(CGLayer:)](<ciimage/init(cglayer_)-3wseb.md>) _(deprecated)_
- [init(CGLayer:)](<ciimage/init(cglayer_)-8o853.md>) _(deprecated)_
- [init(CGLayer:options:)](<ciimage/init(cglayer_options_)-34jjk.md>) _(deprecated)_
- [init(CGLayer:options:)](<ciimage/init(cglayer_options_)-8su8t.md>) _(deprecated)_
- [init(CVImageBuffer:)](<ciimage/init(cvimagebuffer_)-6k44w.md>)
- [init(CVImageBuffer:)](<ciimage/init(cvimagebuffer_)-9fq4l.md>)
- [init(CVImageBuffer:options:)](<ciimage/init(cvimagebuffer_options_)-79c2d.md>)
- [init(CVImageBuffer:options:)](<ciimage/init(cvimagebuffer_options_)-7g0yo.md>)
- [init(CVPixelBuffer:)](<ciimage/init(cvpixelbuffer_)-1z0mw.md>)
- [init(CVPixelBuffer:)](<ciimage/init(cvpixelbuffer_)-5p2mz.md>)
- [init(CVPixelBuffer:options:)](<ciimage/init(cvpixelbuffer_options_)-6rkzb.md>)
- [init(CVPixelBuffer:options:)](<ciimage/init(cvpixelbuffer_options_)-8i44g.md>)
- [init(IOSurface:)](<ciimage/init(iosurface_)-72me3.md>)
- [init(IOSurface:)](<ciimage/init(iosurface_)-7dwj8.md>)
- [init(IOSurface:options:)](<ciimage/init(iosurface_options_)-4dwl5.md>)
- [init(IOSurface:options:)](<ciimage/init(iosurface_options_)-7qdsg.md>)
- [init(IOSurface:plane:format:options:)](<ciimage/init(iosurface_plane_format_options_)-7k35r.md>) _(deprecated)_
- [init(MTLTexture:options:)](<ciimage/init(mtltexture_options_)-510vm.md>)
- [init(MTLTexture:options:)](<ciimage/init(mtltexture_options_)-5ou1j.md>)
- [init(coder:)](<ciimage/init(coder_).md>)
- [init(contentsOfURL:)](<ciimage/init(contentsofurl_)-1e9r3.md>)
- [init(contentsOfURL:)](<ciimage/init(contentsofurl_)-9vlbb.md>)
- [init(contentsOfURL:options:)](<ciimage/init(contentsofurl_options_)-7g3lx.md>)
- [init(contentsOfURL:options:)](<ciimage/init(contentsofurl_options_)-93guu.md>)

## See Also

### Essentials

- [Processing an Image Using Built-in Filters](processing-an-image-using-built-in-filters.md) — Apply effects such as sepia tint, highlight strengthening, and scaling to images.
- [CIContext](cicontext.md) — The Core Image context class provides an evaluation context for Core Image processing with Metal, OpenGL, or OpenCL.
