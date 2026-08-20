---
title: Color Management in Safari
apple_id: DTS40009339
resource_type: Technical Note
platform: Safari|macOS
topic: null
technology: null
published: '2009-10-22'
source_url: https://developer.apple.com/library/archive/technotes/tn2220/_index.html
archived_at: '2026-07-26T19:54:09.703181Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2220

# Color Management in Safari

This Technote discusses how to take advantage of the built-in color management in Safari to make sure your image colors look great.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmzthewugsbrfvjukq2ujfhu4mi)[The Challenge of Color Reproduction in the Browser](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmzthewugsbrfvjukq2ujfhu4mq)[Safari Color Management](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmzthewugsbrfvjukq2ujfhu4my)[ICC Profiles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmzthewugsbrfvjvkqstivbviskpjyzq)[How to take advantage of Safari's Color Management](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmzthewugsbrfvjukq2ujfhu4ni)[When you should tag your Images](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmzthewugsbrfvjvkqstivbviskpjy2q)[When you shouldn't tag your Images](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmzthewugsbrfvjvkqstivbviskpjy3a)[Software Developers - How to Tag your Content](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmzthewugsbrfvjvkqstivbviskpjy3q)[Content Creators - How to Tag your Content](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmzthewugsbrfvjvkqstivbviskpjy4a)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmzthewugsbrfvjukq2ujfhu4mjq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmzthewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

By following the guidelines discussed in this technote you can make sure your images are appropriately color managed in Safari on the Macintosh and on Windows. Additionally, these guidelines cover content that is not color managed alongside content that is color managed on the same web page.

[Back to Top](#)

## The Challenge of Color Reproduction in the Browser

Often, colors in your images will look different when displayed on the Web. Consider for example a JPEG image in an HTML document on the Web. The pixel colors in the image are directly related to the device on which it was created (for example, a digital camera). The image colors will look different if the image is displayed on a different device.

Safari for Mac OS X and Windows offers a solution to the color issues on the web by providing consistent color management.  Safari's built-in color management will correctly display images you've specifically designated to be color managed.

[Back to Top](#)

## Safari Color Management

Safari uses support for ICC profiles and provides color managed graphics on the Web.

### ICC Profiles

Color Management with Safari begins with the ICC profile, a cross-platform profile format that defines the color data required for calculating a color match between devices or between color spaces. Profiles provide the information necessary to understand how a particular device reproduces color, and can be embedded in images to communicate this color information for when the image is displayed.

When creating an image (either with a tool, or programmatically in your application) you should save--along with the document or picture--the profile for the device on which the image was created or modified. These embedded profiles allow for the automatic interpretation of color information as the color image is transferred from one device to another. Embedding a profile in an image (also referred to as "tagging") guarantees that the image can be rendered correctly on a different system.

__Important:__ For images that are __not__ tagged with a color profile, their color values will be displayed on the screen by Safari with no optimization or adjustment for differences between devices in how they render colors. This may result in the colors not being displayed as originally intended.

[Back to Top](#)

## How to take advantage of Safari's Color Management

Review your web content and determine which images should be tagged, and which should remain untagged.

### When you should tag your Images

Generally, you should add a color profile to an image where color fidelity is important. Examples of this include a photograph or a piece of artwork, such as a company logo that needs to appear with the correct colors.

If you do attach a color profile, then the image will have the following characteristics:

- It will be color corrected by Safari, and it will have the best possible color rendition of the image data on the user's display

By attaching a color profile to your image, you will ensure the best possible color rendition of the image. In general, this means that your images will look more consistent on both the system that created the content, and on all systems that display it.

__Important:__ There are tradeoffs involved with tagging images. Embedded profiles take up additional space and bandwidth. Therefore, you should really only tag large images where the image data is much bigger than the profile data. For example, it is not a good idea to have a small 100 x 100 image with a 20k ICC profile attached.

### When you shouldn't tag your Images

You don't need to embed a color profile for an image that you want to use as an integral part of a web page design, where it needs to match the color of text, colored backgrounds, plug-in content, and so on. This includes image-based widgets, banners, and other colored HTML elements designed to blend in with the page around it.

If you do not attach a color profile to the image, the image will have the following characteristics:

- It will be smaller
- It can match the corresponding colors in the surrounding web page

__Important:__ When designing content for publication to the Web that won't include color profiles, we recommend you work in the sRGB color space. sRGB is a standard [RGB color space](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/csintro/csintro_colorspace/chapter_3_section_3.html), and has been endorsed by The World Wide Web Consortium (W3C), the main international standards organization for the World Wide Web, as the recommended color space for use on the Internet.

### Software Developers - How to Tag your Content

Software developers working with the Quartz 2D APIs should read [Technical Q&A QA1396 : Creating color spaces that ensure color matching](https://developer.apple.com/qa/qa2004/qa1396.html) when creating image data that is going to show up on the web.

Cocoa software developers should read the [Cocoa Drawing Guide](https://developer.apple.com/documentation/Cocoa/Conceptual/CocoaDrawingGuide/index.html), and look for the sections [Associating a ColorSync Profile With an Image](https://developer.apple.com/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Images/chapter_7_section_6.html#//apple_ref/doc/uid/TP40003290-CH208-DontLinkElementID_63) and [Converting Between Color Spaces](https://developer.apple.com/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Images/chapter_7_section_6.html#//apple_ref/doc/uid/TP40003290-CH208-SW5) to learn how to properly create image data for the Web.

### Content Creators - How to Tag your Content

Many image editors (such as Photoshop, Preview, Graphics Converter and so on) can save images with embedded profiles. See the instructions that came with your application to determine how to correctly set up your application for color management.

You can also use an image editor to add or replace a color profile to your image.  For example, follow these steps to add or replace a color profile to your image using Preview.

Make sure you have the proper color profile selected.  If you are not sure, duplicate the images or have a backup copy of the images.

- Open your image in Preview.
- From the Tools menu, choose Assign Profile...
- From the "ColorSync Profile:" pop-up menu select the appropriate color profile.
- From the File menu, choose Save (or Save As to save a different copy).

For batch processing of images, Automator provides an Apply ColorSync Profile to Images action.

It's very easy to set up a workflow using Automator. For information on using the Automator application, choose Help in Automator or Help > Mac Help in the Finder and search for “Automator”. For information on creating actions, see [Automator Programming Guide](https://developer.apple.com/documentation/AppleApplications/Conceptual/AutomatorConcepts/index.html#//apple_ref/doc/uid/TP40001450) and [Automator Framework Reference](https://developer.apple.com/documentation/AppleApplications/Reference/AutomatorReference/index.html#//apple_ref/doc/uid/TP40001452).

Similarly, the Mac OS X Scriptable Image Processing System (SIPS) tool can be used for batch processing of images and contains commands to both add and remove profiles.

For more information about SIPS, see [TN2035 ColorSync on Mac OS X](https://developer.apple.com/technotes/tn/tn2035.html).

[Back to Top](#)

## References

- [Safari](http://www.apple.com/safari/)
- [Color management](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/csintro/csintro_intro/chapter_1_section_1.html#//apple_ref/doc/uid/TP30001148-CH204-DontLinkElementID_14)
- [ColorSync On Mac OS X](https://developer.apple.com/technotes/tn/tn2035.html)
- [ICC Web site](http://www.color.org/)
- [TN 2115 Image Color Management](https://developer.apple.com/technotes/tn2006/tn2115.html)
- [Apple RGB and Generic RGB Profiles Explained](https://developer.apple.com/qa/qa2005/qa1430.html)
- [Technical Q&A QA1396 : Creating color spaces that ensure color matching](https://developer.apple.com/qa/qa2004/qa1396.html)
- [Cocoa Drawing Guide](https://developer.apple.com/documentation/Cocoa/Conceptual/CocoaDrawingGuide/index.html)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-10-22 | New document that discusses how to take advantage of the built-in color management in Safari to make sure your image colors look great. |

