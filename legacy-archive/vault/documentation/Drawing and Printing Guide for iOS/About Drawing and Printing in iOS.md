---
title: Drawing and Printing Guide for iOS
apple_id: TP40010156
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Graphics & Animation
technology: UIKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/Introduction/Introduction.html
archived_at: '2026-07-15T03:48:38.361156Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](iOS%20Drawing%20Concepts.md)

# About Drawing and Printing in iOS

This document covers three related subjects:

- Drawing custom UI views. Custom UI views allow you to draw content that cannot easily be drawn with standard UI elements. For example, a drawing program might use a custom view for the user’s drawing, or an arcade game might use a custom view into which it draws sprites.
- Drawing into offscreen bitmap and PDF content. Whether you plan to display the images later, export them to a file, or print the images to an AirPrint-enabled printer, offscreen drawing lets you do so without interrupting the user’s workflow.
- Adding AirPrint support to your app. The iOS printing system lets you draw your content differently to fit on the page.

__Figure I-1__  You can combine custom views with standard views, and even draw things offscreen.

!!

The iOS native graphics system combines three major technologies: UIKit, Core Graphics, and Core Animation. UIKit provides views and some high-level drawing functionality within those views, Core Graphics provides additional (lower-level) drawing support within UIKit views, and Core Animation provides the ability to apply transformations and animation to UIKit views. Core Animation is also responsible for view compositing.

### Custom UI Views Allow Greater Drawing Flexibility

This document describes how to draw into custom UI views using native drawing technologies. These technologies, which include the Core Graphics and UIKit frameworks, support 2D drawing.

Before you consider using a custom UI view, you should make certain that you really need to do so. Native drawing is suitable for handling more complex 2D layout needs. However, because custom views are processor-intensive, you should limit the amount of drawing you do using native drawing technologies.

As an alternative to custom drawing, an iOS app can draw things onscreen in several other ways.

- __Using standard (built-in) views.__ Standard views let you draw common user-interface primitives, including lists, collections, alerts, images, progress bars, tables, and so on without the need to explicitly draw anything yourself. Using built-in views not only ensures a consistent user experience between iOS apps, but also saves you programming effort. If built-in views meet your needs, you should read _[View Programming Guide for iOS](../Windows%20Views/View%20Programming%20Guide%20for%20iOS/About%20Windows%20and%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbt)_.
- __Using Core Animation layers.__ Core Animation lets you create complex, layered 2D views with animation and transformations. Core Animation is a good choice for animating standard views, or for combining views in complex ways to present the illusion of depth, and can be combined with custom-drawn views as described in this document. To learn more about Core Animation, read _Core Animation Overview_.
- __Using OpenGL ES in a GLKit view or a custom view.__ The OpenGL ES [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) provides a set of open-standard graphics libraries geared primarily toward game development or apps that require high frame rates, such as virtual prototyping apps and mechanical and architectural design apps. It conforms to the OpenGL ES 2.0 and OpenGL ES v1.1 specifications. To learn more about OpenGL drawing, read _[OpenGL ES Programming Guide](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/About%20OpenGL%20ES.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojt)_.
- __Using web content.__ The [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) class lets you display web-based user interfaces in an iOS app. To learn more about displaying web content in a web view, read _[Using UIWebView to display select document types](https://developer.apple.com/library/archive/qa/qa1630/_index.html#//apple_ref/doc/uid/DTS40008749)_ and _[UIWebView Class Reference](https://developer.apple.com/documentation/uikit/uiwebview)_.

Depending on the type of app you are creating, it may be possible to use little or no custom drawing code. Although immersive apps typically make extensive use of custom drawing code, utility and productivity apps can often use standard views and controls to display their content.

The use of custom drawing code should be limited to situations where the content you display needs to change dynamically. For example, a drawing app typically needs to use custom drawing code to track the user’s drawing commands, and an arcade-style game may need to update the screen constantly to reflect the changing game environment. In those situations, you should choose an appropriate drawing technology and create a custom view class to handle events and update the display appropriately.

On the other hand, if the bulk of your app’s interface is fixed, you can render the interface in advance to one or more image files and display those images at runtime using the [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) class. You can layer image views with other content as needed to build your interface. You can also use the [UILabel](https://developer.apple.com/documentation/uikit/uilabel) class to display configurable text and include buttons or other controls to provide interactivity. For example, an electronic version of a board game can often be created with little or no custom drawing code.

Because custom views are generally more processor-intensive (with less help from the GPU), if you can do what you need to do using standard views, you should always do so. Also, you should make your custom views as small as possible, containing only content that you cannot draw in any other way, use use standard views for everything else. If you need to combine standard UI elements with custom drawing, consider using a Core Animation layer to superimpose a custom view with a standard view so that you draw as little as possible.

#### A Few Key Concepts Underpin Drawing With the Native Technologies

When you draw content with UIKit and Core Graphics, you should be familiar with a few concepts in addition to the view drawing cycle.

- For the [drawRect:](https://developer.apple.com/documentation/uikit/uiview/1622529-draw) method, UIKit creates a __graphics context__ for rendering to the display. This graphics context contains the information the drawing system needs to perform drawing commands, including attributes such as fill and stroke color, the font, the clipping area, and line width. You can also create and draw into custom graphics context for bitmap images and PDF content.
- UIKit has a __default coordinate system__ where the origin of drawing is at the top-left of a view; positive values extend downward and to the right of that origin. You can change the size, orientation, and position of the default coordinate system relative to the underlying view or window by modifying the current transformation matrix, which maps a view’s coordinate space to the device screen.
- In iOS, the __logical coordinate space__, which measures distances in points, is not equal to the device coordinate space, which measures in pixels. For greater precision, points are expressed in floating-point values.

#### UIKit, Core Graphics, and Core Animation Give Your App Many Tools For Drawing

The UIKit and Core Graphics have many complementary graphics capabilities that encompass graphics contexts, Bézier paths, images, bitmaps, transparency layers, colors, fonts, PDF content, and drawing rectangles and clipping areas. In addition, Core Graphics has functions related to line attributes, color spaces, pattern colors, gradients, shadings, and image masks. The Core Animation framework enables you to create fluid animations by manipulating and displaying content created with other technologies.

### Apps Can Draw Into Offscreen Bitmaps or PDFs

It is often useful for an app to draw content offscreen:

- Offscreen bitmap contexts are often used when scaling down photographs for upload, rendering content into an image file for storage purposes, or using Core Graphics to generate complex images for display.
- Offscreen PDF contexts are often used when drawing user-generated content for printing purposes.

After you create an offscreen context, you can draw into it just as you would draw within the [drawRect:](https://developer.apple.com/documentation/uikit/uiview/1622529-draw) method of a custom view.

### Apps Have a Range of Options for Printing Content

As of iOS 4.2, apps can print content wirelessly to supported printers using AirPrint. When assembling a print job, they have three ways to give UIKit the content to print:

- They can give the framework one or more objects that are directly printable; such objects require minimal app involvement. These are instances of the [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData), [NSURL](https://developer.apple.com/documentation/foundation/nsurl), [UIImage](https://developer.apple.com/documentation/uikit/uiimage), or [ALAsset](https://developer.apple.com/documentation/assetslibrary/alasset) classes containing or referencing image data or PDF content.
- They can assign a print formatter to the print job. A print formatter is an object that can lay out content of a certain type (such as plain text or HTML) over multiple pages.
- They can assign a page renderer to the print job. A page renderer is usually an instance of a custom subclass of [UIPrintPageRenderer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer) that draws the content to be printed in part or in full. A page renderer can use one or more print formatters to help it draw and format its printable content.

### It’s Easy to Update Your App for High-Resolution Screens

Some iOS devices feature high-resolution screens, so your app must be prepared to run on these devices and on devices with lower-resolution screens. iOS handles much of the work required to handle the different resolutions, but your app must do the rest. Your tasks include providing specially named high-resolution images and modifying your layer- and image-related code to take the current scale factor into account.

For complete examples of printing, see the _[PrintPhoto: Using the Printing API with Photos](../../samplecode/PrintPhoto-%20Using%20the%20Printing%20API%20with%20Photos/PrintPhoto.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamzwgy)_, _[Sample Print Page Renderer](../../samplecode/Sample%20Print%20Page%20Renderer/Sample%20Print%20Page%20Renderer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmbzha)_, and _[UIKit Printing with UIPrintInteractionController and UIViewPrintFormatter](../../samplecode/UIKit%20Printing%20with%20UIPrintInteractionController%20and%20UIViewPrintFormatter/UIKit%20Printing%20with%20UIPrintInteractionController%20and%20UIViewPrintFormatter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamzrge)_ sample code projects.

[Next](iOS%20Drawing%20Concepts.md)

