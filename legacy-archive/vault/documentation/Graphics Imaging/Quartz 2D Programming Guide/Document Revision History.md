---
title: Quartz 2D Programming Guide
apple_id: TP30001066
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Graphics & Animation
technology: Quartz
published: '2017-03-21'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/RevisionHistory.html
archived_at: '2026-07-15T07:38:07.648505Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz 2D Programming Guide](Introduction.md)


[Previous](Glossary.md)

# Document Revision History

This table describes the changes to _Quartz 2D Programming Guide_.

| __Date__ | __Notes__ |
| 2018-06-07 | Fixed errors in code listings. |
| 2014-09-17 | Added info about using vImage to work with raw pixel data. |
| 2013-12-16 | Removed text chapter; use Core Text instead. |
| 2012-09-19 | Corrected typos and minor technical issues. |
| 2010-11-19 | Updated for OS X v10.6 and iOS 4.2. |
| 2010-06-25 | Minor clarifications and editing. |
| 2009-05-18 | Updated the font names in text examples to reflect fonts available on both iOS and OS X. |
| 2008-06-04 | Updated for iOS SDK. |
|  | Added information about image formats to [Bitmap Image Information](Bitmap%20Images%20and%20Image%20Masks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgiwueqsdjjbesq2g). |
|  | Corrected typos. |
| 2007-12-11 | Revised text chapter and added a glossary. |
|  | Added code that creates a dictionary and adds metadata to it. See [Listing 13-4](PDF%20Document%20Creation%2C%20Viewing%2C%20and%20Transforming.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgqwugsscjfduqqsi). |
| 2007-07-02 | Updated for OS X v10.5. |
|  | Renamed the Shadings chapter to Gradients and revised it to include information on the use of the `CGGradientRef` opaque data type. |
|  | In [Data Management in Quartz 2D](Data%20Management%20in%20Quartz%202D.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgywviucykjcummjqge) and a link and information about _[Image I/O Programming Guide](../Image%20I-O%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrs)_. |
|  | Updated the introduction with recent, relevant related documentation and added a description of the revised [Gradients](Gradients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqg4wviucykjcummjqge) chapter. |
|  | Revised [Quartz 2D Opaque Data Types](Overview%20of%20Quartz%202D.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgiwueqsdi5buoqsb) to include `CGGradientRef` and provided links to information on `CGImageSourceRef` and `CGImageDestinationRef` opaque data types which are part of the Image I/O framework. |
|  | Updated [Table 2-1](Graphics%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgmwugsscivauosci) with additional pixel formats. |
| 2007-01-08 | Fixed a number of minor technical issues. |
|  | Improved the wording in the first paragraph of [Gradients](Gradients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqg4wviucykjcummjqge). |
|  | Made a correction to the floating-point gray information in [Table 2-1](Graphics%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgmwugsscivauosci). |
|  | Corrected the declarations in [Listing 14-5](PDF%20Document%20Parsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrsgawueqkkizcesrcb) |
| 2006-10-03 | Made minor technical improvements. |
|  | Added cross references to the reference documentation for the constants listed in [Table 2-1](Graphics%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgmwugsscivauosci). |
|  | Removed information on using a `CGGLContextRef` object because the use of a graphics context for OpenGL rendering is not reliable and is not recommended. |
|  | Added thread safety information to [Creating a PostScript Converter Object](PostScript%20Conversion.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrguwvgvzr). |
| 2006-07-24 | Made minor technical improvements. |
|  | Changed [Listing 2-6](Graphics%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgmwueq2jinfeer2h) so that is correctly frees the bitmap data. |
|  | Added cross references to [Creating an Image From Part of a Larger Image](Bitmap%20Images%20and%20Image%20Masks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgiwvgvzr) and [Creating an Image from a Bitmap Graphics Context](Bitmap%20Images%20and%20Image%20Masks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgiwvgvzs) that link to examples of creating graphics contexts. |
| 2006-06-28 | Made minor changes to clarify a few concepts. |
|  | Revised [Figure 12-2](Core%20Graphics%20Layer%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrhewvgvzs) and the text that describes it. |
|  | Revised [Figure 1-2](Overview%20of%20Quartz%202D.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgiwueqsdjjdemrkk) and the text that describes it. |
|  | Revised information in “Python Bindings for Quartz 2D”. |
|  | Provided hyperlinks to the functions and methods discussed in [Data Management in Quartz 2D](Data%20Management%20in%20Quartz%202D.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgywviucykjcummjqge). |
|  | Corrected a typographical error in [Listing 2-2](Graphics%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgmwugssci5dugq2d). |
| 2006-02-07 | Corrected typographical error. |
| 2006-01-10 | Made minor typographical and technical corrections. |
| 2005-11-09 | Corrected several technical, typographical, and formatting errors. |
|  | Made changes to code in [Listing 12-1](Core%20Graphics%20Layer%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrhewvgvzr). |
|  | Revised introductory paragraphs in [Transforms](Transforms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgqwvgvzr). |
|  | Revised several sentences in How Quartz 2D Draws Text. |
| 2005-07-07 | Corrected typos and added clarification about Quartz OpenGL graphics context. |
| 2005-06-04 | Fixed typos and added a Python script name. |
| 2005-04-29 | Updated for OS X v10.4. |
|  | Changed the title from _Drawing With Quartz 2D_ to make it more consistent with the titles of similar documentation. |
|  | Revised the Introduction to reflect the new content. |
|  | Simplified the code in [Figure 3-1](Paths.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgewugssci5decqsi). |
|  | Revised the introductions for [Color and Color Spaces](Color%20and%20Color%20Spaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqguwviucykjcummjqge), [Transforms](Transforms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgqwviucykjcummjqge), [Bitmap Images and Image Masks](Bitmap%20Images%20and%20Image%20Masks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgiwviucykjcummjqge), and [PDF Document Parsing](PDF%20Document%20Parsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrsgawviucykjcummjqge). |
|  | Made changes to code in [Code that uses layers to draw a flag](Core%20Graphics%20Layer%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrhewueqkkineuerkf) so that more appropriately-sized layers are used; substituted the function `CGContextDrawLayerAtPoint` for `CGContextDrawLayerInRect`. |
|  | Revised the section [Setting Blend Modes](Paths.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgewueq2ji5eugrkg); added figures that show actual output produced using blend modes. |
|  | Revised the section [Using Blend Modes with Images](Bitmap%20Images%20and%20Image%20Masks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgiwugsscjffekrsh) and replaced the figures with better examples of drawing an image using different blend modes. |
|  | Added information about Core Image and Core Video in the opening paragraphs of [Overview of Quartz 2D](Overview%20of%20Quartz%202D.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgiwviucykjcummjqge). |
|  | Introduced the notion of CGLayer objects in the section [Drawing Destinations: The Graphics Context](Overview%20of%20Quartz%202D.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgiwviucykjcummjtge). |
|  | Added the new Tiger opaque objects to [Quartz 2D Opaque Data Types](Overview%20of%20Quartz%202D.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgiwueqsdi5buoqsb). |
|  | Added blend mode to [Graphics States](Overview%20of%20Quartz%202D.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgiwviucykjcummjtgi). Added information about using blend modes to [Paths](Paths.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgewviucykjcummjqge) and [Bitmap Images and Image Masks](Bitmap%20Images%20and%20Image%20Masks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgiwviucykjcummjqge). |
|  | Revised [Graphics Contexts](Graphics%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgmwviucykjcummjqge) to show how to use HIView. Also added new figures to many sections and provided information on HIView coordinates as compared to Quartz coordinates. |
|  | Added [Table 2-1](Graphics%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgmwugsscivauosci) to show the supported color spaces and pixel formats. |
|  | Replaced [Figure 2-4](Graphics%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgmwueqsdizfeiqsg) to show an enlargement of aliased and antialiasing drawing and text. |
|  | Added [Ellipses](Paths.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgewueq2jjbfeqrkb) and revised discussions on [Painting a Path](Paths.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgewugssciveuqsck) and [Clipping to a Path](Paths.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgewviucykjcummjsgy) to reflect new Tiger content. |
|  | Changed “clipping region” to “clipping area” throughout the entire book. |
|  | Revised information on [Creating Color Spaces](Color%20and%20Color%20Spaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqguwviucykjcummjsha) to reflect Tiger content. |
|  | Added [Evaluating Affine Transforms](Transforms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgqwugsscjjdugr2j) and [Getting the User to Device Space Transform](Transforms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgqwugsscjfduirsc). |
|  | Revised the chapter formerly titled _Data Providers and Data Consumers_ to contain information on image sources and image destinations, and how to move data between Quartz 2D and Core Image. Retitled the chapter [Data Management in Quartz 2D](Data%20Management%20in%20Quartz%202D.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgywviucykjcummjqge) to reflect the revised content. |
|  | Renamed the Bitmap Image chapter to [Bitmap Images and Image Masks](Bitmap%20Images%20and%20Image%20Masks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgiwviucykjcummjqge) and substantially revised the content to reflect information about image sources, the new image creation functions, image masking function, and using blend modes to composite images. |
|  | Added the chapter [Core Graphics Layer Drawing](Core%20Graphics%20Layer%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrhewviucykjcummjqge). |
|  | Added the chapter [PDF Document Parsing](PDF%20Document%20Parsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrsgawviucykjcummjqge), which contains some material from the old PDF Document chapter along with new material on scanners and content streams. |
|  | Added Copying Font Variations and PostScript Fonts to the Text chapter. |
| 2004-06-28 | Revised for Mac OS X v10.3. |
| 2001-07-01 | First version. |

[Previous](Glossary.md)

