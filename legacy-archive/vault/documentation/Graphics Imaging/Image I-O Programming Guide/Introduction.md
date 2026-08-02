---
title: Image I/O Programming Guide
apple_id: TP40005462
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageIOGuide/imageio_intro/ikpg_intro.html
archived_at: '2026-07-15T07:35:42.416233Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Basics%20of%20Using%20Image%20I-O.md)

# Introduction

The Image I/O programming interface allows applications to read and write most image file formats. Originally part of the Core Graphics framework, Image I/O resides in its own framework to allow developers to use it independently of Core Graphics (Quartz 2D). Image I/O provides the definitive way to access image data because it is highly efficient, allows easy access to metadata, and provides color management.

The Image I/O interface is available in OS X v10.4 and later and in iOS 4 and later.

This document is intended for developers who read or write image data in an application. Any developer currently using image importers or other image handling libraries should read this document to see how to use the Image I/O framework instead.

This document is organized into the following chapters:

- [Basics of Using Image I/O](Basics%20of%20Using%20Image%20I-O.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrsfvbuqmrrgywviucykjcummjqge) discusses supported image formats and shows how to include the framework in an Xcode project.
- [Creating and Using Image Sources](Creating%20and%20Using%20Image%20Sources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrsfvbuqmrrhawvgvzt) shows how to create an image source, create an image from it, and extract properties for display in the user interface.
- [Working with Image Destinations](Working%20with%20Image%20Destinations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrsfvbuqmrrhewvgvzt) provides information on creating an image destination, setting up its properties, and adding an image to it.

The _[Image I/O Reference Collection](https://developer.apple.com/documentation/imageio)_ provides detailed descriptions of the functions, data types, and constants in the Image I/O framework.

[Next](Basics%20of%20Using%20Image%20I-O.md)

