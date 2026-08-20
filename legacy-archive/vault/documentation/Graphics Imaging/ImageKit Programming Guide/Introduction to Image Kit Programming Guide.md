---
title: ImageKit Programming Guide
apple_id: TP40004907
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageKitProgrammingGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:36:02.919965Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Basics%20of%20Using%20the%20Image%20Kit.md)

# Introduction to Image Kit Programming Guide

The Image Kit is an Objective-C framework, introduced in OS X v10.5, for browsing, viewing, editing, and processing images in an efficient manner. It also supports browsing Core Image filters, previewing the effects, and providing controls for individual filters. This document describes Image Kit user interface elements and shows, through code examples, how to use Image Kit classes.

Anyone developing a digital media application that supports images will want to read this document to find out how to use the Image Kit to provide the best user experience possible. You don’t need to be a seasoned Cocoa programmer to use the Image Kit or to read this guide, although prior experience with Objective-C is helpful and will make it easier to understand the code examples.

The examples in this document use Xcode version 3.0 and Interface Builder version 3.0.

Image Kit has a variety of image capabilities that your app can adopt. You should first read [Basics of Using the Image Kit](Basics%20of%20Using%20the%20Image%20Kit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmbxfvbuqmznknltc) to can an understanding of the tasks that each Image Kit class supports. You’ll also get an overview of how to use the framework with Apple’s developer tools.

### Image Views Support Viewing, Editing, and Saving Images

Image Kit provides a user interface that displays a single image and supports editing and saving images.

### Use and Image Browser to Support Looking Through Large Image Sets

Image Kit’s browser class (`IKImageBrowserView`) provides a user interface that allows users to view large sets of images.

### Slideshows are Easy to Support

The `IKSlideshow` class provides controls for viewing and advancing through a slideshow. You can also allow users to see index sheets and view slides in fullscreen mode.

### Use the Picture Taker to Support Setting Buddy Photos

The `IKPictureTaker` class is a lightweight panel that you can use to allow users to choose pictures and take snapshots for use as a “buddy” picture or anywhere the user needs an icon-sized image.

### Browse and Set Parameters for Core Image Filters

The `IKFilterBrowserPanel` and `IKFilterBrowserView` classes support browsing built-in Core Image filters by category, previewing a filter’s effect, and applying the filter to an image.

The following documents are helpful guides and references for many of the tasks described in the book:

- _Image Kit Reference Collection_ contains the class and protocol reference documentation.
- _[Core Image Programming Guide](../Core%20Image%20Programming%20Guide/About%20Core%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobv)_ shows how to create Core Image filters ([CIFilter](https://developer.apple.com/documentation/coreimage/cifilter) objects) and apply them to images.
- _[Image I/O Programming Guide](../Image%20I-O%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrs)_ provides information on how to create an image source and extract an image from an image source.
[Next](Basics%20of%20Using%20the%20Image%20Kit.md)

