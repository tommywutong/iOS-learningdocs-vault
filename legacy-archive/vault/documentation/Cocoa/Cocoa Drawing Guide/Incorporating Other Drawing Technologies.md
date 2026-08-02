---
title: Cocoa Drawing Guide
apple_id: TP40003290
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/QuartzOpenGL/QuartzOpenGL.html
archived_at: '2026-07-15T07:12:35.044072Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Drawing Guide](Introduction%20to%20Cocoa%20Drawing%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Paths.md)

# Incorporating Other Drawing Technologies

Cocoa was designed to integrate well with other technologies in OS X. Many technologies are packaged as Objective-C frameworks, which makes including them in Cocoa easy. You are not limited to the use of Objective-C frameworks, though. Cocoa itself uses Quartz internally to implement most drawing routines. You can use Quartz and other C-based technologies, such as OpenGL and QuickTime, from your code with little extra effort.

The sections that follow provide information about how to incorporate some of the more important drawing technologies available in OS X.

Everything you can draw using Cocoa can also be drawn using Quartz. The Cocoa drawing code itself uses Quartz primitives to render content. Cocoa simply adds an object-oriented interface and in some cases does more of the work for you. Cocoa does not provide classes for all Quartz behavior, however. In situations where a feature is not available in Cocoa, you may want to use Quartz directly.

For general information about Quartz features and how to use them, see _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.

Because Quartz implements some features that Cocoa does not, there may be times when you need to use Quartz function calls from your Cocoa code. Because Cocoa uses Quartz for most drawing operations, mixing the two technologies is not an issue.

Some of the Quartz features that are not supported directly by Cocoa include the following:

- Layers
- Gradients (also called shadings)
- Image data sources
- Blend modes (Cocoa uses compositing modes instead)
- Masking images
- Transparency layers (for grouping content)
- Arbitrary patterns (other than images)

In each case, you are free to use Quartz functions to take advantage of these features. Some features can produce data types that you can then incorporate back into a Cocoa object. (For example, you can use an image data source to obtain a Quartz image ([CGImageRef](https://developer.apple.com/documentation/coregraphics/cgimageref)), which you can then use to create an `NSImage` object.) In some cases, however, you may need to perform the entire operation using Quartz functions.

For information on how to use Quartz features, see _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.

When going back and forth between Cocoa and Quartz code, some conversion of data types may be necessary. Table 9-1 shows the Cocoa equivalents of some basic Quartz types.

__Table 9-1__  Simple data-type conversions

| Cocoa type | Quartz type |
| [NSRect](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSRect) | [CGRect](https://developer.apple.com/documentation/coregraphics/cgrect) |
| [NSPoint](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSPoint) | [CGPoint](https://developer.apple.com/documentation/coregraphics/cgpoint) |
| [NSSize](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSSize) | [CGSize](https://developer.apple.com/documentation/coregraphics/cgsize) |

Although in each case the structure layout is the same, you cannot pass the Quartz data type directly to a method expecting the Cocoa type. To convert, you must cast from one type to another, as shown in the following example:

```
NSRect cocoaRect = *(NSRect*)&myCGRect;
```

Table 9-2 lists the Cocoa classes that approximate the behavior of specific Quartz data types. In some cases, the Cocoa class wraps an instance of its Quartz counterpart, but that is not always true. In the case of shadows, Quartz provides no direct data type for managing the shadow parameters; you must set shadows attributes in Quartz using several different functions. In the case of layers, there are no Cocoa equivalents.

__Table 9-2__  Equivalent Cocoa and Quartz data types

| Cocoa type | Quartz type |
| [NSGraphicsContext](https://developer.apple.com/documentation/appkit/nsgraphicscontext) | [CGContextRef](https://developer.apple.com/documentation/coregraphics/cgcontextref) |
| [NSAffineTransform](https://developer.apple.com/documentation/foundation/nsaffinetransform) | [CGAffineTransform](https://developer.apple.com/documentation/coregraphics/cgaffinetransform) |
| [NSColor](https://developer.apple.com/documentation/appkit/nscolor) | [CGColorRef](https://developer.apple.com/documentation/coregraphics/cgcolor), [CGPatternRef](https://developer.apple.com/documentation/coregraphics/cgpattern) |
| [NSFont](https://developer.apple.com/documentation/appkit/nsfont) | [CGFontRef](https://developer.apple.com/documentation/coregraphics/cgfontref) |
| [NSGlyph](https://developer.apple.com/documentation/appkit/nsglyph) | [CGGlyph](https://developer.apple.com/documentation/coregraphics/cgglyph) |
| [NSImage](https://developer.apple.com/documentation/appkit/nsimage) | [CGImageRef](https://developer.apple.com/documentation/coregraphics/cgimageref) |
| [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) | [CGPathRef](https://developer.apple.com/documentation/coregraphics/cgpath) |
| [NSShadow](https://developer.apple.com/documentation/uikit/nsshadow) | [CGSize](https://developer.apple.com/documentation/coregraphics/cgsize), [CGColorRef](https://developer.apple.com/documentation/coregraphics/cgcolor) |
| [NSGradient](https://developer.apple.com/documentation/appkit/nsgradient) (OS X v10.5 and later) | [CGShadingRef](https://developer.apple.com/documentation/coregraphics/cgshadingref) |
| No equivalent | [CGLayerRef](https://developer.apple.com/documentation/coregraphics/cglayerref) |

Because Cocoa types often wrap equivalent Quartz types, you should look at the Cocoa reference documentation for information about how to get equivalent Quartz objects, if any. In many cases, Cocoa classes do not offer direct access to their Quartz equivalent and you may need to create the Quartz type based on information in the Cocoa object, such as in the following cases:

- To create a `CGPathRef` object from an `NSBezierPath` object, you must redraw the path using Quartz function calls. Use the [elementAtIndex:associatedPoints:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520674-elementatindex) method of `NSBezierPath` to retrieve the path’s point information.
- To convert back and forth between `CGColorRef` and `NSColor` objects, get the color component values from one object and use those values to create the other object. When creating colors, you may also need to specify the color space for that color. For the most part, Quartz and Cocoa support the same color spaces. If a color uses a custom color space, you can use the available ICC profile data to create the appropriate color space object.
- To create an `NSImage` object from a Quartz image, you need to create the image object indirectly. For information on how to do this, see [Using a Quartz Image to Create an NSImage](Images.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqhawueq2jjjeuoskh).
- To create Quartz shadows, you can use the methods of `NSShadow` to retrieve the color, offset, and blur radius values prior to calling [CGContextSetShadow](https://developer.apple.com/documentation/coregraphics/cgcontext/1456082-setshadow) or [CGContextSetShadowWithColor](https://developer.apple.com/documentation/coregraphics/1455205-cgcontextsetshadowwithcolor).

Before using any Quartz features, you need to obtain a Quartz graphics context (`CGContextRef`) for drawing. For view-based drawing, you can get the context by sending a [graphicsPort](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1524914-graphicsport) message to the current Cocoa graphics context (`NSGraphicsContext`). This method returns a pointer that you can cast to a `CGContextRef` data type and use in subsequent Quartz function calls.

In OS X v10.4 and later, if you have an existing Quartz graphics context, you can create a Cocoa graphics context object using the [graphicsContextWithGraphicsPort:flipped:](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1529263-graphicscontextwithgraphicsport) class method of `NSGraphicsContext`. You then use the `setCurrentContext:` class method to make that context the current context.

When mixing calls to Quartz and Cocoa, remember that many Cocoa classes maintain a local copy of some graphics attributes normally associated with the Quartz graphics context. When such a class is ready to draw its content, it modifies the graphics state to match its local settings, draws its content, and restores the graphics state to its original settings. If you use Quartz to change an attribute that is maintained locally by a Cocoa class, your changes may not be used.

If you make changes to the graphics state using the `NSGraphicsContext` class, your changes are immediately conveyed to the Quartz graphics context, and vice versa. If you are not using `NSGraphicsContext` to set an attribute, you should assume that the attribute is local to the object. For example, the `NSBezierPath` class prefers local copies of graphics attributes over the default (or global) attributes stored in the current context.

OpenGL is an open, cross-platform, three-dimensional (3D) graphics standard with broad industry support. OpenGL eases the task of writing real-time 2D or 3D graphics applications by providing a mature, well-documented graphics processing pipeline that supports the abstraction of current and future hardware accelerators.

The sections that follow provide a glimpse into the techniques used to incorporate OpenGL drawing calls into your Cocoa application. For more on OpenGL support in OS X, and for detailed examples of how to integrate OpenGL into your Cocoa application, see _[OpenGL Programming Guide for Mac](../../Graphics%20Imaging/OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_. For general information about OpenGL, see [Reference Library > Graphics & Imaging > OpenGL](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000424-TP30000549).

One way to do OpenGL drawing is to add an OpenGL view (an instance of [NSOpenGLView](https://developer.apple.com/documentation/appkit/nsopenglview)) to your window. An OpenGL view behaves like any other view but also stores a pointer to an OpenGL graphics context object (an instance of [NSOpenGLContext](https://developer.apple.com/documentation/appkit/nsopenglcontext)). Storing the graphics context in the view eliminates the need for your code to recreate the context during each drawing cycle, which can be expensive.

To use an OpenGL view in your program, you create a subclass of `NSOpenGLView` and add that view to your window, either programmatically or using Interface Builder. When creating an OpenGL view programmatically, you specify the pixel format object you want to associate with the view. A pixel format object (an instance of [NSOpenGLPixelFormat](https://developer.apple.com/documentation/appkit/nsopenglpixelformat)) specifies the buffers and other rendering attributes of the OpenGL graphics context. For information on the meaning of different pixel format attributes, see _[OpenGL Programming Guide for Mac](../../Graphics%20Imaging/OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_.

If you use Interface Builder to add your view to a window, you specify the pixel format information using the inspector for your view. Interface Builder lets you specify some pixel attributes, but not all. To support other attributes, you must replace the view’s pixel format object at runtime using the [setPixelFormat:](https://developer.apple.com/documentation/appkit/nsopenglview/1414946-pixelformat) method.

As with other views, you use your OpenGL view’s `drawRect:` method to draw the content of your view. When your `drawRect:` method is invoked, the environment is automatically configured for drawing using the OpenGL graphics context associated with your view.

Unlike with other graphics contexts, you do not need to restore the previous OpenGL graphics context when you are done drawing. OpenGL does not maintain a stack of graphics contexts that need to be popped as they are no longer needed. Instead, it simply uses the most recent context that was made current.

Before creating an OpenGL graphics context object, you first create a pixel format object ([NSOpenGLPixelFormat](https://developer.apple.com/documentation/appkit/nsopenglpixelformat)). The attributes you specify when creating your pixel format object determine the rendering behavior of the graphics context. Once you have a valid pixel format object, you can create and initialize your OpenGL graphics context object.

Listing 9-1 attempts to create an OpenGL graphics context that supports full-screen, double-buffered, 32-bit drawing. If the desired renderer is available, it returns the context; otherwise, it returns `nil`.

__Listing 9-1__  Creating an OpenGL graphics context

```objc
- (NSOpenGLContext*)getMyContext
{
    // Specify the pixel-format attributes.
    NSOpenGLPixelFormatAttribute attrs[] =
    {
        NSOpenGLPFAFullScreen,
        NSOpenGLPFADoubleBuffer,
        NSOpenGLPFADepthSize, 32,
        0
    };

    // Create the pixel-format object.
    NSOpenGLContext* myContext = nil;
    NSOpenGLPixelFormat* pixFmt = [[NSOpenGLPixelFormat alloc]
                                     initWithAttributes:attrs];

    // If the pixel format is valid, create the OpenGL context.
    if (pixFmt != nil)
    {
        myContext = [[NSOpenGLContext alloc] initWithFormat:pixFmt
                                 shareContext:NO];
    }

    [pixFmt release];
    return myContext;
}
```

Because the creation of OpenGL graphics contexts depends on the currently available renderers, your code should always verify that the desired objects were created before trying to use them. If creating an object fails, you can always try to create it again using a different set of attributes.

QuickTime is Apple's cross-platform multimedia technology designed to help you create and deliver video, sound, animation, graphics, text, interactivity, and music. QuickTime supports dozens of file and compression formats for images, video, and audio, including ISO-compliant MPEG-4 video and AAC audio.

You can incorporate QuickTime features into your Cocoa applications in one of two ways. The easiest way is through the QuickTime Kit, which is a full-featured Objective-C based framework for the QuickTime interfaces. If you are already familiar with the C-based QuickTime interfaces, you can use those instead.

The QuickTime Kit framework (`QTKit.framework`) works with QuickTime movies in Cocoa applications in OS X. The QuickTime Kit framework was introduced in OS X v10.4 and was designed as an alternative to and eventual replacement for the existing `NSMovie` and `NSMovieView` classes in Cocoa. This new framework provides more extensive coverage of QuickTime functions and data types than had been offered by the Application Kit classes. More importantly, the framework does not require Cocoa programmers to be conversant with Carbon data types such as handles, aliases, file-system specifications, and so on.

The QuickTime Kit framework is available primarily in OS X v10.4 and later, but it is also supported in OS X v10.3 with QuickTime 7 or later installed. For information on how to use the QuickTime Kit, see _[QuickTime Kit Programming Guide](../../Quick%20Time/QuickTime%20Kit%20Programming%20Guide/Introduction%20to%20QuickTime%20Kit%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenbv)_. For a reference of the classes in the QuickTime Kit, see _[QTKit Framework Reference](https://developer.apple.com/documentation/qtkit)_.

Long before the introduction of the QuickTime Kit framework, QuickTime programs were written using a C-based API. The QuickTime API encompasses thousands of functions and gives you the maximum flexibility in managing QuickTime content. You can use this API in your Cocoa applications like you would any other framework.

For an introduction to QuickTime, see _[QuickTime Overview](../../Quick%20Time/QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs)_. For the complete QuickTime reference, see _QuickTime Framework Reference_.

If your software runs in OS X v10.4 and later, you can use Quartz Composer to render complex graphical content. Quartz Composer uses the latest OS X graphics technologies to create advanced graphical images and animations quickly and easily. You use the Quartz Composer application to create composition files graphically and then load those compositions into your Cocoa application and run them. Changing the behavior of your Cocoa application is then as simple as updating the composition file.

Quartz Composer is especially suited for applications that want to perform complex image manipulations. Through it, you gain easy access to features of Quartz 2D, Core Image, Core Video, OpenGL, QuickTime, MIDI System Services, and Real Simple Syndication (RSS). Your application can render compositions for display or provide the user with controls for manipulating the composition parameters.

For a detailed example showing you how to run a composition from your Cocoa application, see the chapter “Using QCRenderer to Play a Composition” in _[Quartz Composer Programming Guide](../../Graphics%20Imaging/Quartz%20Composer%20Programming%20Guide/Introduction%20to%20Quartz%20Composer%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjx)_.

OS X includes several different technologies for manipulating images. Although the `NSImage` class provide a robust feature set that is sufficient for many developer’s uses, there may be specific times when you need to use other imaging technologies. Table 9-3 lists some of the other imaging technologies available and when you might use each one of them.

__Table 9-3__  Imaging technologies

| Image technology | Description |
| Quartz Images ([CGImageRef](https://developer.apple.com/documentation/coregraphics/cgimageref)) | Quartz images are immutable data types that you use to manipulate bitmap data in Quartz. Although `NSImage` is easier to use and provides automatic support for resolution independence, you might need to create Quartz images if another API you are using expects them. You can create a Quartz image by drawing into a `NSBitmapImageRep` object or Quartz bitmap context and then extracting a `CGImageRef` from there. Quartz images are part of the Application Services framework. |
| Quartz Layers ([CGLayerRef](https://developer.apple.com/documentation/coregraphics/cglayerref)) | Quartz layers are a mutable alternative to Quartz images. You can draw to layers much like you would draw to an `NSImage` object. You do so by creating a context, locking focus on that context, drawing, and retrieving an image object from the results. Because they are implemented in video memory, layers can be very efficient to use, especially if you need to draw the same image repeatedly. Quartz layers are available in OS X v10.4 and later as part of the Application Services framework. |
| Core Image ([CIImage](https://developer.apple.com/documentation/coreimage/ciimage)) | The Core Image framework is geared toward processing image data. You would use this technology to apply visual effects or filters to existing bitmap images. Because it is explicitly designed for manipulating bitmap images, you must convert your images to a `CIImage` object before you do any processing. Core Image is available in OS X v10.4 and later as part of the Quartz Core framework. |
| Image I/O | The Image I/O framework is geared towards developers who need more direct control over reading and writing image data. You might use this framework to convert images from one format to another or you might use it to add metadata to an image created by your program. The features of Image I/O are available in OS X v10.4 and later as part of the Application Services framework. |
| Core Animation | While not explicitly an imaging technology, the Core Animation framework is a smart and efficient way to render images and other data inside a view. The framework provides a cached backing store that makes it possible to do animations with a minimal amount of redrawing. You might use this technology in place of `NSImage` or other imaging technologies to create animation effects or other rapidly changing graphics. It offers respectable animation performance without requiring you to use low-level APIs such as OpenGL. The Core Animation framework is available in OS X v10.5 and later as part of the Quartz Core framework. |

[Next](Document%20Revision%20History.md)[Previous](Paths.md)

