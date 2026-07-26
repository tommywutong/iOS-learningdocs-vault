---
title: CIContext
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontext
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext.json'
content_hash: 'sha256:a1d8e7a64be654fc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIContext

<sub>Class</sub>

The Core Image context class provides an evaluation context for Core Image processing with Metal, OpenGL, or OpenCL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIContext
```

## Overview

You use a `CIContext` instance to render a [CIImage](ciimage.md) instance which represents a graph of image processing operations which are built using other Core Image classes, such as [CIFilter](cifilter-swift.class.md), [CIKernel](cikernel.md), [CIColor](cicolor.md) and [CIImage](ciimage.md). You can also use a `CIContext` with the [CIDetector](cidetector.md) class to analyze images — for example, to detect faces or barcodes.

Contexts support automatic color management by performing all processing operations in a working color space. This means that unless told otherwise:

- All input images are color matched from the input’s color space to the working space.
- All renders are color matched from the working space to the destination space. (For more information on `CGColorSpace` see [CGColorSpace](../coregraphics/cgcolorspace.md))

`CIContext` and [CIImage](ciimage.md) instances are immutable, so multiple threads can use the same [CIContext](cicontext.md) instance to render [CIImage](ciimage.md) instances. However, [CIFilter](cifilter-swift.class.md) instances are mutable and thus cannot be shared safely among threads. Each thread must take case not to access or modify a [CIFilter](cifilter-swift.class.md) instance while it is being used by another thread.

The `CIContext` manages various internal state such as `MTLCommandQueue` and caches for compiled kernels and intermediate buffers.  For this reason it is not recommended to create many `CIContext` instances.  As a rule, it recommended that you create one `CIContext` instance for each view that renders [CIImage](ciimage.md) or each background task.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Context Without Specifying a Destination

- [- init](<cicontext/init().md>) — Initializes a context without a specific rendering destination, using default options.

### Creating a Context for CPU-Based Rendering

- [+ contextWithCGContext:options:](<cicontext/init(cgcontext_options_)-6p78w.md>) — Creates a Core Image context from a Quartz context, using the specified options.

### Creating a Context for GPU-Based Rendering

- [+ contextWithMTLDevice:](<cicontext/init(mtldevice_)-swey.md>) — Creates a Core Image context using the specified Metal device.
- [+ contextWithMTLDevice:options:](<cicontext/init(mtldevice_options_)-26usb.md>) — Creates a Core Image context using the specified Metal device and options.
- [+ contextWithMTLCommandQueue:](<cicontext/init(mtlcommandqueue_)-7dtqk.md>)
- [+ contextWithMTLCommandQueue:options:](<cicontext/init(mtlcommandqueue_options_)-6i3me.md>)

### Rendering Images

- [- createCGImage:fromRect:](<cicontext/createcgimage(__from_).md>) — Creates a Core Graphics image from a region of a Core Image image instance.
- [- createCGImage:fromRect:format:colorSpace:](<cicontext/createcgimage(__from_format_colorspace_).md>) — Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling the pixel format and color space of the `CGImage`.
- [- createCGImage:fromRect:format:colorSpace:deferred:](<cicontext/createcgimage(__from_format_colorspace_deferred_).md>) — Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling when the image is rendered.
- [- render:toBitmap:rowBytes:bounds:format:colorSpace:](<cicontext/render(__tobitmap_rowbytes_bounds_format_colorspace_).md>) — Renders to the given bitmap.
- [- render:toCVPixelBuffer:](<cicontext/render(__to_).md>) — Renders an image into a pixel buffer.
- [- render:toCVPixelBuffer:bounds:colorSpace:](<cicontext/render(__to_bounds_colorspace_)-2k8l2.md>) — Renders a region of an image into a pixel buffer.
- [- render:toIOSurface:bounds:colorSpace:](<cicontext/render(__to_bounds_colorspace_)-54b9l.md>) — Renders a region of an image into an IOSurface object.
- [- render:toMTLTexture:commandBuffer:bounds:colorSpace:](<cicontext/render(__to_commandbuffer_bounds_colorspace_).md>) — Renders a region of an image to a Metal texture.

### Drawing Images

- [- drawImage:inRect:fromRect:](<cicontext/draw(__in_from_).md>) — Renders a region of an image to a rectangle in the context destination.

### Determining the Allowed Extents for Images Used by a Context

- [- inputImageMaximumSize](<cicontext/inputimagemaximumsize().md>) — Returns the maximum size allowed for any image rendered into the context.
- [- outputImageMaximumSize](<cicontext/outputimagemaximumsize().md>) — Returns the maximum size allowed for any image created by the context.

### Managing Resources

- [- clearCaches](<cicontext/clearcaches().md>) — Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [- reclaimResources](<cicontext/reclaimresources().md>) — Runs the garbage collector to reclaim any resources that the context no longer requires.
- [+ offlineGPUCount](<cicontext/offlinegpucount().md>) — Returns the number of GPUs not currently driving a display.
- [workingColorSpace](cicontext/workingcolorspace.md) — The working color space of the Core Image context.
- [workingFormat](cicontext/workingformat.md) — The working pixel format of the Core Image context.

### Rendering Images for Data or File Export

- [- TIFFRepresentationOfImage:format:colorSpace:options:](<cicontext/tiffrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in TIFF format.
- [- JPEGRepresentationOfImage:colorSpace:options:](<cicontext/jpegrepresentation(of_colorspace_options_).md>) — Renders the image and exports the resulting image data in JPEG format.
- [- PNGRepresentationOfImage:format:colorSpace:options:](<cicontext/pngrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in PNG format.
- [- HEIFRepresentationOfImage:format:colorSpace:options:](<cicontext/heifrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in HEIF format.
- [- HEIF10RepresentationOfImage:colorSpace:options:error:](<cicontext/heif10representation(of_colorspace_options_).md>) — Renders the image and exports the resulting image data in HEIF10 format.
- [- OpenEXRRepresentationOfImage:options:error:](<cicontext/openexrrepresentation(of_options_).md>) — Renders the image and exports the resulting image data in open EXR format.
- [- writeTIFFRepresentationOfImage:toURL:format:colorSpace:options:error:](<cicontext/writetiffrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in TIFF format.
- [- writeJPEGRepresentationOfImage:toURL:colorSpace:options:error:](<cicontext/writejpegrepresentation(of_to_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in JPEG format.
- [- writePNGRepresentationOfImage:toURL:format:colorSpace:options:error:](<cicontext/writepngrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in PNG format.
- [- writeHEIFRepresentationOfImage:toURL:format:colorSpace:options:error:](<cicontext/writeheifrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in HEIF format.
- [- writeHEIF10RepresentationOfImage:toURL:colorSpace:options:error:](<cicontext/writeheif10representation(of_to_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in HEIF10 format.
- [- writeOpenEXRRepresentationOfImage:toURL:options:error:](<cicontext/writeopenexrrepresentation(of_to_options_).md>) — Renders the image and exports the resulting image data as a file in open EXR format.
- [CIImageRepresentationOption](ciimagerepresentationoption.md)

### Creating Depth Blur Filters

- [- depthBlurEffectFilterForImage:disparityImage:portraitEffectsMatte:hairSemanticSegmentation:glassesMatte:gainMap:orientation:options:](<cicontext/depthblureffectfilter(for_disparityimage_portraiteffectsmatte_hairsemanticsegmentation_glassesmatte_gainmap_orientation_options_).md>) — Create a [CIFilter](cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [- depthBlurEffectFilterForImage:disparityImage:portraitEffectsMatte:hairSemanticSegmentation:orientation:options:](<cicontext/depthblureffectfilter(for_disparityimage_portraiteffectsmatte_hairsemanticsegmentation_orientation_options_).md>) — Create a [CIFilter](cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [- depthBlurEffectFilterForImage:disparityImage:portraitEffectsMatte:orientation:options:](<cicontext/depthblureffectfilter(for_disparityimage_portraiteffectsmatte_orientation_options_).md>) — Create a [CIFilter](cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [- depthBlurEffectFilterForImageData:options:](<cicontext/depthblureffectfilter(forimagedata_options_).md>) — Create a [CIFilter](cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect.
- [- depthBlurEffectFilterForImageURL:options:](<cicontext/depthblureffectfilter(forimageurl_options_).md>) — Create a [CIFilter](cifilter-swift.class.md) instance for the supplied image URL that can be used to apply a depth blur effect.

### Constants

- [CIContextOption](cicontextoption.md) — An enum string type that your code can use to select different options when creating a Core Image context.

### Customizing Render Destination

- [- prepareRender:fromRect:toDestination:atPoint:error:](<cicontext/preparerender(__from_to_at_).md>) — An optional call to warm up a [CIContext](cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.
- [- startTaskToClear:error:](<cicontext/starttask(toclear_).md>) — Fills the entire destination with black or clear depending on its [alphaMode](cirenderdestination/alphamode.md).
- [- startTaskToRender:fromRect:toDestination:atPoint:error:](<cicontext/starttask(torender_from_to_at_).md>) — Renders a portion of an image to a point in the destination.
- [- startTaskToRender:toDestination:error:](<cicontext/starttask(torender_to_).md>) — Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.

### Deprecated

- [+ contextWithCGLContext:pixelFormat:colorSpace:options:](<cicontext/init(cglcontext_pixelformat_colorspace_options_)-6rp6d.md>) — Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object. _(deprecated)_
- [+ contextWithEAGLContext:](<cicontext/init(eaglcontext_)-8ajef.md>) — Creates a Core Image context from an EAGL context. _(deprecated)_
- [+ contextWithEAGLContext:options:](<cicontext/init(eaglcontext_options_)-6uyqj.md>) — Creates a Core Image context from an EAGL context using the specified options. _(deprecated)_
- [init(forOfflineGPUAtIndex:)](<cicontext/init(forofflinegpuatindex_).md>) — Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display. _(deprecated)_
- [init(forOfflineGPUAtIndex:colorSpace:options:sharedContext:)](<cicontext/init(forofflinegpuatindex_colorspace_options_sharedcontext_).md>) — Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options. _(deprecated)_
- [- createCGLayerWithSize:info:](<cicontext/createcglayer(with_info_).md>) — Creates a CGLayer object from the provided parameters. _(deprecated)_
- [- drawImage:atPoint:fromRect:](<cicontext/draw(__at_from_).md>) — Renders a region of an image to a point in the context destination. _(deprecated)_

### Initializers

- [init(CGContext:options:)](<cicontext/init(cgcontext_options_)-1yzwi.md>)
- [init(CGLContext:pixelFormat:colorSpace:options:)](<cicontext/init(cglcontext_pixelformat_colorspace_options_)-3t25h.md>) _(deprecated)_
- [init(EAGLContext:)](<cicontext/init(eaglcontext_)-293h1.md>) _(deprecated)_
- [init(EAGLContext:options:)](<cicontext/init(eaglcontext_options_)-2853a.md>) _(deprecated)_
- [init(MTLCommandQueue:)](<cicontext/init(mtlcommandqueue_)-2pgxu.md>)
- [init(MTLCommandQueue:options:)](<cicontext/init(mtlcommandqueue_options_)-q929.md>)
- [init(MTLDevice:)](<cicontext/init(mtldevice_)-8ksdj.md>)
- [init(MTLDevice:options:)](<cicontext/init(mtldevice_options_)-15xqo.md>)
- [+ contextForOfflineGPUAtIndex:](<cicontext/init(forofflinegpuat_).md>) _(deprecated)_
- [+ contextForOfflineGPUAtIndex:colorSpace:options:sharedContext:](<cicontext/init(forofflinegpuat_colorspace_options_sharedcontext_).md>) _(deprecated)_
- [- initWithOptions:](<cicontext/init(options_).md>) — Initializes a context without a specific rendering destination, using the specified options.

### Instance Methods

- [- calculateHDRStatsForCGImage:](<cicontext/calculatehdrstats(for_)-3ia7r.md>) — Given a Core Graphics image, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then return a new Core Graphics image that has the calculated values.
- [- calculateHDRStatsForIOSurface:](<cicontext/calculatehdrstats(for_)-6lwmz.md>) — Given an IOSurface, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then update the surface’s attachments to store the values.
- [- calculateHDRStatsForCVPixelBuffer:](<cicontext/calculatehdrstats(for_)-7bcki.md>) — Given a CVPixelBuffer, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then update the buffer’s attachments to store the values.
- [- calculateHDRStatsForImage:](<cicontext/calculatehdrstats(for_)-l1rj.md>) — Given a Core Image image, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then return a new Core Image image that has the calculated values.
- [- createCGImage:fromRect:format:colorSpace:deferred:calculateHDRStats:](<cicontext/createcgimage(__from_format_colorspace_deferred_calculatehdrstats_).md>) — Creates a Core Graphics image from a region of a Core Image image instance with an option for calculating HDR statistics.
- [- estimateRender:fromRect:toDestination:atPoint:error:](<cicontext/estimaterender(__from_to_at_).md>) — Returns a task with estimated resource statistics for a render, without executing the render. _(beta)_

### Default Implementations

- [CIContext Implementations](cicontext/cicontext-implementations.md)

## See Also

### Essentials

- [Processing an Image Using Built-in Filters](processing-an-image-using-built-in-filters.md) — Apply effects such as sepia tint, highlight strengthening, and scaling to images.
- [CIImage](ciimage.md) — A representation of an image to be processed or produced by Core Image filters.
