---
title: Core Image Programming Guide
apple_id: TP30001185
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: CoreImage
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_revhistory/ci_revhistory.html
archived_at: '2026-07-15T07:35:37.551738Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Image Programming Guide](About%20Core%20Image.md)


[Previous](Packaging%20and%20Loading%20Image%20Units.md)

# Document Revision History

This table describes the changes to _Core Image Programming Guide_.

| __Date__ | __Notes__ |
| 2016-09-13 | Updated for iOS 10.0, tvOS 10.0, and OS X v10.12. |
|  | Rewrote the [Processing Images](Processing%20Images.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqmznkrifqusfiyytami) chapter to reflect modern Core Image best practices. |
| 2016-03-21 | Corrected typos and references to features that were formerly for OS X only and are now available in iOS. |
| 2015-10-21 | Corrected errors in example code listings. |
| 2015-09-16 | Fixed errors in code examples. |
| 2014-11-18 | Fixed errors in code examples. |
| 2013-10-22 | Corrected several minor errors. |
|  | Updated code examples to use number, array, and dictionary literals. |
|  | Updated code examples to use standard key constants where available (for example, [kCIInputImageKey](https://developer.apple.com/documentation/coreimage/kciinputimagekey) instead of `@"inputImage"`). |
| 2013-01-28 | Corrected code listing in "The color cube in code". |
|  | Corrected code line `c[3] = rgb[3] * alpha` in [Listing 5-3](Subclassing%20CIFilter-%20Recipes%20for%20Custom%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnbnknltq) to read simply `c[3] = alpha`. |
| 2012-09-19 | Updated for iOS 6.0 and OS X v10.7. |
|  | Updated the introduction chapter. |
|  | Added chapters on face detection and auto enhancement filters. |
|  | Added information on performance best practices. |
|  | Added recipes for subclassing CIFilter to get custom effects. |
|  | Moved information on using the `CIImageAccumulator` class to its own chapter and revised the content to bring it up to date. |
|  | Added clarification on naming input parameters for custom filters. |
|  | Added information on thread safety. |
|  | Fixed broken link to external article. |
| 2011-10-12 | Included for Core Image on iOS 5. |
| 2008-06-09 | Added details on coordinate spaces. |
|  | Added information to [Building a Dictionary of Filters](Querying%20the%20System%20for%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqmrnknltc). |
| 2007-10-31 | Updated for OS X v10.5. |
|  | Added a note to [Building a Dictionary of Filters](Querying%20the%20System%20for%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqmrnknltc). |
|  | Add information about CIFilter Image Kit Additions. |
|  | Added information about support for RAW images. |
|  | Updated links to references and added links in several places to _[Image Unit Tutorial](../Image%20Unit%20Tutorial/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmzr)_. |
|  | Revised [Executable and Nonexecutable Filters](What%20You%20Need%20to%20Know%20Before%20Writing%20a%20Custom%20Filter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqojnknltcmy). |
|  | Revised [Write an Output Image Method](Creating%20Custom%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnrnijbusrkeijdeg). |
| 2007-05-29 | Added link to Cocoa memory management. |
|  | Removed section on memory management. Instead, see _[Advanced Memory Management Programming Guide](../../Cocoa/Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_. |
|  | Added a note to [Building a Dictionary of Filters](Querying%20the%20System%20for%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqmrnknltc). |
|  | Fixed a typographical error. |
| 2007-01-08 | Fixed minor technical and typographical errors. |
| 2006-09-05 | Fixed minor technical problem. |
|  | Corrected the angular values for colors in [Creating a CIFilter Object and Setting Values](Processing%20Images.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqmznknltg). |
| 2006-06-28 | Reorganized content and added task information. |
|  | Removed the appendix “Core Image Filters” and created a new document named _[Core Image Filter Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346)_. |
|  | Removed the appendix “Core Image Kernel Language” and created a new document named _[Core Image Kernel Language Reference](../Core%20Image%20Kernel%20Language%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojx)_. |
|  | Added [Kernel Routine Examples](Creating%20Custom%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnrnknltk) to [Creating Custom Filters](Creating%20Custom%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnrnkrifqusfiyytami) and changed some of the short variable names to long ones in the code listings. Added information to [Computing a Hole Distortion](Creating%20Custom%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnrnknlti) to clarify the purpose of the example. |
|  | Moved information about packaging filters as image units into its own chapter. Added additional information about the files needed in the project and where to install the image unit. See [Before You Get Started](Packaging%20and%20Loading%20Image%20Units.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnznknltcna), [Build and Test the Image Unit](Packaging%20and%20Loading%20Image%20Units.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnznknltcmy), and [See Also](Packaging%20and%20Loading%20Image%20Units.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnznknltcni). |
|  | Updated the book introduction and some of the chapter introductions to reflect the chapter and appendix changes. |
|  | Revised [Creating Custom Filters](Creating%20Custom%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnrnkrifqusfiyytami). In particular, see [Write a Custom Attributes Method](Creating%20Custom%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnrnknltc) and [Register the Filter](Creating%20Custom%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnrnijbusqshinduu). |
|  | Added additional information on how to create nonexecutable filters. See [Writing Nonexecutable Filters](Creating%20Custom%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnrninfeersii5dug). |
|  | Revised information on creating a CIContext object from an OpenGL graphics context. |
|  | Fixed formatting and, in online versions of this document, provided hyperlinks to the image creation functions in “Methods used to create a CIImage object from existing image sources.” |
|  | Added hyperlinks to most symbols and to sample code available in the ADC Reference Library. |
|  | Numerous small formatting and grammatical changes throughout. |
| 2005-12-06 | Made minor corrections to a few filter parameters. Added information on the CIFilterBrowser widget. |
| 2005-11-09 | Fixed several typographical errors and a broken hyperlink. |
| 2005-08-11 | Updated a figure in the PDF version of this document. |
| 2005-07-07 | Corrected typographical errors. |
| 2005-04-29 | Updated for public release of OS X v10.4. First public version. |
|  | Changed the title from _Image Processing With Core Image_ to make it more consistent with the titles of similar documentation. |
|  | Completely revised [Querying the System for Filters](Querying%20the%20System%20for%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqmrnkrifqusfiyytami) to provide more in-depth information about how Core Image works. |
|  | Split the chapter titled Core Image Tasks into two chapters: [Processing Images](Processing%20Images.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqmznkrifqusfiyytami) and [Creating Custom Filters](Creating%20Custom%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnrnkrifqusfiyytami). Completely updated the content in each to reflect additions to the API and to provide more in-depth information. |
|  | Added Using Transition Effects. |
|  | Added [Using Feedback to Process Images](Using%20Feedback%20to%20Process%20Images.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnjnknltk). |
|  | Added Applying a Filter to Video. |
|  | Added [Expressing Image Processing Operations in Core Image](Creating%20Custom%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnrnijbusscfjjfes). |
|  | Added [Use Quartz Composer to Test the Kernel Routine](Creating%20Custom%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnrnijbusq2hinfem). |
|  | Provided more information on the region of interest and ROI functions. See [The Region of Interest](What%20You%20Need%20to%20Know%20Before%20Writing%20a%20Custom%20Filter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqojnknltcmq) and [Supplying an ROI Function](Creating%20Custom%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnrninfeerkdifcug). |
|  | Provided more information on executable and nonexecutable filters. See [Executable and Nonexecutable Filters](What%20You%20Need%20to%20Know%20Before%20Writing%20a%20Custom%20Filter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqojnknltcmy) and [Writing Nonexecutable Filters](Creating%20Custom%20Filters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqnrninfeersii5dug). |
|  | Updated the appendix “Core Image Filters to include recently-added built-in Core Image filters. Also replaced many of the figures to provide a better idea of the result produced by a filter. |
|  | Updated the appendix “Core Image Kernel Language” to reflect changes in the kernel language. Added explanations for the kernel routine examples. |
| 2004-06-29 | New seed draft that describes an image processing technology, built into OS X v10.4, that provides access to built-in image filters for both video and still images and support for custom filters and real-time processing. |

[Previous](Packaging%20and%20Loading%20Image%20Units.md)

