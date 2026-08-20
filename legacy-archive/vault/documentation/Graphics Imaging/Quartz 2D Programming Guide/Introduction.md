---
title: Quartz 2D Programming Guide
apple_id: TP30001066
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Graphics & Animation
technology: Quartz
published: '2017-03-21'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html
archived_at: '2026-07-15T07:38:07.635953Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20Quartz%202D.md)

# Introduction

Core Graphics, also known as Quartz 2D, is an advanced, two-dimensional drawing engine available for iOS, tvOS and macOS application development. Quartz 2D provides low-level, lightweight 2D rendering with unmatched output fidelity regardless of display or printing device. Quartz 2D is resolution- and device-independent.

The Quartz 2D API is easy to use and provides access to powerful features such as transparency layers, path-based drawing, offscreen rendering, advanced color management, anti-aliased rendering, and PDF document creation, display, and parsing.

This document is intended for developers who need to perform any of the following tasks:

- Draw graphics
- Provide graphics editing capabilities in an application
- Create or display bitmap images
- Work with PDF documents

This document is organized into the following chapters:

- [Overview of Quartz 2D](Overview%20of%20Quartz%202D.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgiwviucykjcummjqge) describes the page, drawing destinations, Quartz opaque data types, graphics states, coordinates, and memory management, and it takes a look at how Quartz works “under the hood.”
- [Graphics Contexts](Graphics%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgmwviucykjcummjqge) describes the kinds of drawing destinations and provides step-by-step instructions for creating all flavors of graphics contexts.
- [Paths](Paths.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgewviucykjcummjqge) discusses the basic elements that make up paths, shows how to create and paint them, shows how to set up a clipping area, and explains how blend modes affect painting.
- [Color and Color Spaces](Color%20and%20Color%20Spaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqguwviucykjcummjqge) discusses color values and using alpha values for transparency, and it describes how to create a color space, set colors, create color objects, and set rendering intent.
- [Transforms](Transforms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgqwviucykjcummjqge) describes the current transformation matrix and explains how to modify it, shows how to set up affine transforms, shows how to convert between user and device space, and provides background information on the mathematical operations that Quartz performs.
- [Patterns](Patterns.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgywviucykjcummjqge) defines what a pattern and its parts are, tells how Quartz renders them, and shows how to create colored and stenciled patterns.
- [Shadows](Shadows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqhawviucykjcummjqge) describes what shadows are, explains how they work, and shows how to paint with them.
- [Gradients](Gradients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqg4wviucykjcummjqge) discusses axial and radial gradients and shows how to create and use CGShading and CGGradient objects.
- [Transparency Layers](Transparency%20Layers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgawviucykjcummjqge) gives examples of what transparency layers look like, discusses how they work, and provides step-by-step instructions for implementing them.
- [Data Management in Quartz 2D](Data%20Management%20in%20Quartz%202D.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgywviucykjcummjqge) discusses how to move data into and out of Quartz.
- [Bitmap Images and Image Masks](Bitmap%20Images%20and%20Image%20Masks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgiwviucykjcummjqge) describes what makes up a bitmap image definition and shows how to use a bitmap image as a Quartz drawing primitive. It also describes masking techniques you can use on images and shows the various effects you can achieve by using blend modes when drawing images.
- [Core Graphics Layer Drawing](Core%20Graphics%20Layer%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrhewviucykjcummjqge) describes how to create and use drawing layers to achieve high-performance patterned drawing or to draw offscreen.
- [PDF Document Creation, Viewing, and Transforming](PDF%20Document%20Creation%2C%20Viewing%2C%20and%20Transforming.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgqwviucykjcummjqge) shows how to open and view PDF documents, apply transforms to them, create a PDF file, access PDF metadata, add links, and add security features (such as password protection).
- [PDF Document Parsing](PDF%20Document%20Parsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrsgawviucykjcummjqge) describes how to use CGPDFScanner and CGPDFContentStream objects to parse and inspect PDF documents.
- [PostScript Conversion](PostScript%20Conversion.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrguwviucykjcummjqge) gives an overview of the functions you can use in Mac OS X to convert a PostScript file to a PDF document. These functions are not available in iOS.
- [Text](Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrrgmwviucykjcummjqge) describes Quartz 2D low-level support for text and glyphs, and alternatives that provide higher-level and Unicode text support. It also discusses how to copy font variations.
- [Glossary](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrsgewvgvzx) defines the terms used in this guide.

These items are essential reading for anyone using Quartz 2D:

- [Core Graphics Framework Reference](https://developer.apple.com/reference/coregraphics) provides a complete reference for the Quartz 2D application programming interface.
- _[Color Management Overview](../Color%20Management%20Overview/Introduction%20to%20Color%20Management%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnby)_ is a brief introduction to the principles of color perception, color spaces, and color management systems.
- Mailing lists. Join the [quartz-dev](http://lists.apple.com/mailman/listinfo/quartz-dev) mailing list to discuss problems using Quartz 2D.
[Next](Overview%20of%20Quartz%202D.md)

