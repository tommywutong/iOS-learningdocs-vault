---
title: Quartz Programming Guide for QuickDraw Developers
apple_id: TP40001098
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/QuickDrawToQuartz2D/tq_strategies/tq_strategies.html
archived_at: '2026-07-15T05:24:41.682273Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Programming Guide for QuickDraw Developers](Introduction%20to%20Quartz%20Programming%20Guide%20for%20QuickDraw%20Developers.md)


[Next](Basic%20Drawing.md)[Previous](Introduction%20to%20Quartz%20Programming%20Guide%20for%20QuickDraw%20Developers.md)

# Strategies

The QuickDraw to Quartz imaging models are different enough that rewriting your application so that is uses only Quartz is not trivial. Your hard work will be worthwhile. Making the transition opens a world of possibilities for tasks that you can perform with Quartz but could not dream of accomplishing with QuickDraw. Just as QuickDraw was revolutionary in its time, Quartz is today. In Mac OS X v10.4, Quartz introduces a wealth of new features that makes the switchover even more compelling. Quartz has many more convenience functions, improved performance, and a lot of new documentation. What’s more, Quartz is fully integrated with other Mac OS X v10.4 technologies, such as Core Image, which makes image processing a snap. There is no better time than now to roll up your sleeves and get to work removing that old QuickDraw code!

This chapter provides overall strategies for revising your code to use only Quartz, while the remaining chapters in the book show how to accomplish specific tasks using Quartz. Where appropriate, the strategies in this chapter cross-reference specific tasks so you can get ideas (and perhaps some code) for how to modify your own application.

Make sure you are using a development environment that supports Quartz, such as Xcode.

Gather up the latest Quartz documentation so that it is readily accessible to you.

- _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_. If you haven’t read this document yet, at least read the overview and the table of contents so that you know what’s covered in the book. Take a quick scan through the book.
- _Quartz 2D Reference Collection_. You’ll need to look up function definitions as you start rewriting your code.

Locate the Carbon Sketch application and familiarize yourself with the code and what the application does. By looking at the code, you can get ideas on how to rearchitect your application to use only Quartz for drawing. You can find Carbon Sketch on the ADC Reference Library site:

[http://developer.apple.com/samplecode/GraphicsImaging/idxQuartz-title.html#doclist](https://developer.apple.com/samplecode/GraphicsImaging/idxQuartz-title.html)

The application performs many tasks needed in a drawing application. For example, it:

- Draws all artwork using Quartz
- Uses an overlay window to handle selection, dragging, and resizing objects
- Performs hit testing using a 1-pixel bitmap context
- Copy and pastes PDF data using the PasteBoard API
- Uses Quartz Generic color spaces

Analyze your QuickDraw code so that you can understand what needs to change. Then develop a plan before you start reworking your code. Keep in mind that many things have changed in Mac OS X, and especially in Mac OS X v10.4. Technologies other than QuickDraw are deprecated in Mac OS X v10.4, including QuickDraw Text, Display Manager, and Draw Sprockets.

If, after analyzing your code, you plan to stick with the C APIs in the Carbon framework, you may want to use HIView along with Quartz. The HIToolbox offers many technologies that are complementary to Quartz (such as HIShape) and that will ensure that your application is updated for the 21st century.

If you decide to completely rewrite your application in all respects, you might want to think about moving to Cocoa. You can use the Quartz API in any framework outside of the kernel. When you use Cocoa, you can call Quartz directly and you can also use Cocoa drawing methods, which are built on top of Quartz.

As you analyze your code, take a careful look at how you use QuickDraw. Sometimes you’ll find that Quartz provides functional equivalents for your QuickDraw code, but more often than not you’ll need to think differently. Your application will benefit most if you can think beyond QuickDraw. That is, don’t just look for ways to accomplish the same task in Quartz. Take some time to think about how your application currently works and how you might be able to leverage the new capabilities that Mac OS X provides to improve the user experience of your application, not just maintain parity with your QuickDraw version.

The following strategies are useful for revising QuickDraw applications to use Quartz:

1. Think differently, especially for those items that don’t have equivalent functionality in Quartz—such as arithmetic transfer modes, `SeedCFill`, `SearchProcs`—but that you still need to find a substitute for.
2. Focus on functionality, not functions. The approach of translating QuickDraw idioms into Quartz won’t work in most cases, especially for calls to `CopyBits` and the regions functions.
3. Analyze your use of regions to see what functionality each use provides. Then revise the code accordingly. You may have used regions for a variety of purposes; you’ll find alternative strategies throughout this guide. See [Regions Replacement Strategies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrqgiwueqsdiveuoqki).
4. Analyze your `CopyBits` calls to see what functionality each call provides. Then revise the code accordingly. You probably used `CopyBits` and related functions to achieve a number of tasks in QuickDraw; you’ll find alternative strategies throughout this guide. See [CopyBits Replacement Strategies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrqgiwueqsdinbemscd).
5. Account for differences between the QuickDraw and Quartz coordinate systems. If you use HIView along with Quartz, make sure you are familiar with how HIView handles coordinates. See [Coordinate Space](Basic%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgawugsscjbcucq2j).
6. Use alpha. It’s fully supported in Quartz. See [The Alpha Value](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Color%20and%20Color%20Spaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqguwviucykjcummjrhe) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.
7. Convert PICT data to PDF and provide conversion support in your application to handle legacy PICT files that your users may need to open. See [Converting PICT Data](Converting%20PICT%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgewviucykjcummjqge).
8. Support PDF data for Copy and Paste actions. Only PDF content fully captures Quartz drawing, and you’ll want to ensure fidelity of content. See [Converting PICT Data](Converting%20PICT%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgewviucykjcummjqge).
9. Save and restore graphics states appropriately. See [Graphics State and Global Effects](Basic%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgawugsscjjeecrsf).
10. Revise your hit testing code. See [Hit Testing](Hit%20Testing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrshewviucykjcummjqge).
11. Think device independence and resolution independence. See [Drawing Destinations](Basic%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgawugsscizdemrkd).
12. Identify the shortcomings of your QuickDraw application to see where you can use new features of Quartz to improve your application.
13. Remove code that compensates for QuickDraw shortcomings. For example, XOR drawing isn’t needed by most applications that use Quartz. The `GrafProcs` bottleneck tricks simply don’t apply in Quartz.
14. Optimize your code to ensure that your application performs at its best. See [Performance](Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrtgawviucykjcummjqge).

Regions served many purposes in QuickDraw. You’ll want to analyze your code to see what purpose each use of regions serves.

If you use QuickDraw regions for:

- Drawing shapes, then instead use paths to construct arbitrary shapes and use Quartz convenience functions to draw rectangles, circles, ovals, ellipses, and lines. See [Alternatives to QuickDraw Drawing Functions](Basic%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgawugsscjfbuissk) and [Constructing and Drawing Shapes](Basic%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgawugsscizcemr2b). In Quartz, you can draw directly to a destination, or you can use the [CGPathRef](https://developer.apple.com/documentation/coregraphics/cgpath) data type to build up a complex shape that you draw later and reuse anytime you’d like.
- Clipping regions, consider one of the Quartz context clipping functions, such as [CGContextClip](https://developer.apple.com/documentation/coregraphics/1455262-cgcontextclip) or [CGContextClipToMask](https://developer.apple.com/documentation/coregraphics/1456497-cgcontextcliptomask). See[Clipping](Basic%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgawugsscindeeske).
- Hit test, then use paths or a 1x1 bitmap graphics context. See [Hit Testing](Hit%20Testing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrshewviucykjcummjqge).
- Masking, then there are a number of approaches you can take, depending on what you want to accomplish. Consider the Quartz function [CGContextClipToMask](https://developer.apple.com/documentation/coregraphics/1456497-cgcontextcliptomask), take a look at what you can accomplish with blend modes, and for images, consider [CGImageMaskCreate](https://developer.apple.com/documentation/coregraphics/1455089-cgimagemaskcreate), [CGImageCreateWithMask](https://developer.apple.com/documentation/coregraphics/1456337-cgimagecreatewithmask), and [CGImageCreateWithMaskingColors](https://developer.apple.com/documentation/coregraphics/cgimage/1454358-copy). See [Masking](Masking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrshawviucykjcummjqge) and [Color Blend Modes](Basic%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgawugssci5dukrke).

If you want to:

- Create a `RgnHandle`, consider using an HIShape object, which is an abstract shape object that replaces the old QuickDraw region handle. HIShape objects are the preferred way to describe regions in HIView views that use Quartz. See _HIShape Reference_. If you are not using HIView, take a look at CGPath objects ([CGPathRef](https://developer.apple.com/documentation/coregraphics/cgpath) data type), which you can use to draw reusable shapes. See [Constructing and Drawing Shapes](Basic%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgawugsscizcemr2b).
- Update a region shape, see [Updating Regions](Updating%20Regions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgiwviucykjcummjqge).

Many years of development and optimization made the QuickDraw function `CopyBits` an exceptionally fast, general-purpose blitter. QuickDraw is based on bitmap graphics, and `CopyBits` makes perfect sense in that environment. The Quartz imaging model does not provide for pixel drawing operations or bit copying functionality. The fact that Quartz is not based on bits gives rise to its many cool features, including its ability to maintain device and resolution independence. Quartz does have the capability for you to draw bits, should you need to do so, but most of the time you’ll want to adopt strategies for replacing `CopyBits`, `CopyMask`, and `CopyDeepMask`—strategies that leverage Quartz rather than seek parity with QuickDraw.

The functions `CopyBits`, `CopyMask`, and `CopyDeepMask` were used to achieve so many results in QuickDraw that you’ll want to read all the replacement strategies before you decide which course of action to take. If you use the QuickDraw functions `CopyBits`, `CopyMask`, or `CopyDeepMask` for:

- Moving bits from a GWorld to the screen. See [Working With Bitmap Image Data](Working%20With%20Bitmap%20Image%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsg4wviucykjcummjqge) and [Offscreen Drawing](Offscreen%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgmwviucykjcummjqge).
- Offscreen drawing, check out the [CGLayerRef](https://developer.apple.com/documentation/coregraphics/cglayerref) data type and how to use it with the function [CGLayerCreateWithContext](https://developer.apple.com/documentation/coregraphics/1450892-cglayercreatewithcontext). You might also investigate `HIViewCreateOffscreenImage`. See [Using a CGLayer Object for Offscreen Drawing](Offscreen%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgmwueqsdinauqqkd).
- Fast scrolling, consider using HIView to create a scrolling view (see the function `HIScrollViewCreate`). See _[HIView Programming Guide](../HIView%20Programming%20Guide/Introduction%20to%20HIView%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrt)_ and _HIView Reference_ for more information.
- Image animation, use overlay windows. See [Using Overlay Windows](Updating%20Regions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgiwugsscireekrse).
- Highlighting portions of an image, use overlay windows. See [Updating Regions](Updating%20Regions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgiwviucykjcummjqge).
- Converting from one pixel depth to another, then eliminate code that changes pixel depth. Modern hardware has plenty of memory and rendering horsepower, and there is no longer any motivation to reduce image depth.
- Scaling or resizing an image, you can instead use the Quartz function [CGContextDrawImage](https://developer.apple.com/documentation/coregraphics/1454845-cgcontextdrawimage) and then adjust the destination rectangle to get the desired scaling.
- Clipping or cropping an image, consider the Quartz functions [CGImageCreateWithImageInRect](https://developer.apple.com/documentation/coregraphics/cgimage/1454683-cropping), [CGImageCreateWithMask](https://developer.apple.com/documentation/coregraphics/1456337-cgimagecreatewithmask), and [CGContextClipToMask](https://developer.apple.com/documentation/coregraphics/1456497-cgcontextcliptomask). You can create thumbnail images in Quartz using the function [CGImageSourceCreateThumbnailAtIndex](https://developer.apple.com/documentation/imageio/1465099-cgimagesourcecreatethumbnailatin). All four functions are introduced in Mac OS X v10.4. See [Creating Images](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Bitmap%20Images%20and%20Image%20Masks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgiwugsscijdugskj) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.
- Color blending using transfer modes, consider using blend modes in Quartz. See [Color Blend Modes](Basic%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgawugssci5dukrke), which allows blending shapes using translucent color. In _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_, see [Setting Blend Modes](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Paths.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgewueq2ji5eugrkg) and [Using Blend Modes With Images](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Bitmap%20Images%20and%20Image%20Masks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgiwugsscjffekrsh).

  Quartz doesn’t have an functions that operate on a per-pixel basis, but Core Image does. If you want to perform image processing on a per pixel basis, you can convert a Quartz image to a Core Image image, perform the operation, and pass the processed image back to Quartz. See _[Core Image Programming Guide](../../Graphics%20Imaging/Core%20Image%20Programming%20Guide/About%20Core%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobv)_ and [Moving Data Between Quartz 2D and Core Image](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Data%20Management%20in%20Quartz%202D.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgywueqkkjbcuescf) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.
- Creating transparency effects, then use the alpha channel to specify the translucency of a color. See [The Alpha Value](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Color%20and%20Color%20Spaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqguwviucykjcummjrhe) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.
- Creating image masks, consider using [CGImageMaskCreate](https://developer.apple.com/documentation/coregraphics/1455089-cgimagemaskcreate). See [Masking](Masking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrshawviucykjcummjqge).
- Storing and retrieving images, then use the Quartz image-source and image-destination functions. These handle the common image file formats in use today, including JPEG, PNG, TIFF, JPEG2000. See _[CGImageSource Reference](https://developer.apple.com/documentation/imageio/cgimagesource-r84)_, _[CGImageDestination Reference](https://developer.apple.com/documentation/imageio/cgimagedestination)_, and Data Management in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.
- Inverting colors, consider using the exclusion or difference blend modes. In _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_, see [Setting Blend Modes](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Paths.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgewueq2ji5eugrkg) and [Using Blend Modes With Images](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Bitmap%20Images%20and%20Image%20Masks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgiwugsscjffekrsh).
- Colorizing an image, consider using blend modes. See [Colorizing an Image](Basic%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgawugsscinbukrcd).

[Next](Basic%20Drawing.md)[Previous](Introduction%20to%20Quartz%20Programming%20Guide%20for%20QuickDraw%20Developers.md)

