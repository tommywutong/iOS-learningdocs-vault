---
title: Quick Look Programming Guide
apple_id: TP40005020
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickLook
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Quicklook_Programming_Guide/Introduction/Introduction.html
archived_at: '2026-07-18T02:12:41.386279Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Quick%20Look%20and%20the%20User%20Experience.md)

# Introduction to Quick Look Programming Guide

Quick Look is a technology introduced in OS X version 10.5 that enables client applications, such as Spotlight and the Finder, to display thumbnail images and full-size previews of documents. For documents of common content types—notably HTML, RTF, plain text, TIFF, PNG, JPEG, PDF, DAE, and QuickTime movies—this support is automatic. However, applications with documents that are of less common or even private content types can still take advantage of the Quick Look feature. Those applications can include Quick Look generators: plug-ins that convert a given document from its native format into a format that Quick Look can display to users.

This document describes the Quick Look technology and explains how you, as an application developer, can create a generator so Quick Look can display thumbnail and preview images of your documents. Although Quick Look generators are designed as CFPlugIn-style bundles, all the gritty details of plug-in implementation are handled for you. And although the programmatic interface for Quick Look generators is an ANSI C interface, you can write generators using Objective-C code that calls methods of the Cocoa frameworks.

The _Quick Look Programming Guide_ has the following chapters:

- [Quick Look and the User Experience](Quick%20Look%20and%20the%20User%20Experience.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqmznknltg) describes what the Quick Look technology does and points out the advantages for applications that make use of the technology. it also defines terms that have special meaning in Quick Look.
- [Quick Look Architecture](Quick%20Look%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqnbnknltc) describes the various components of Quick Look, including their roles and how they communicate with each other.
- [Creating and Configuring a Quick Look Project](Creating%20and%20Configuring%20a%20Quick%20Look%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqnjnknltk) explains how to create a Quick Look generator project and how to specify the properties of a generator.
- [Overview of Generator Implementation](Overview%20of%20Generator%20Implementation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqnrnknltk) summarizes the approaches for generating thumbnails and previews and identifies the best contexts for each approach.
- [Drawing Thumbnails and Previews In a Graphics Context](Drawing%20Thumbnails%20and%20Previews%20In%20a%20Graphics%20Context.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqobnknlti) shows how to draw thumbnails and previews in graphics context optimized for bitmap, single-page vector, and multipage vector graphics.
- [Dynamically Generating Previews](Dynamically%20Generating%20Previews.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqmjvfvjvoni) discusses how you can dynamically generate text-based previews in a supported content type such as RTF or HTML; for HTML previews it also shows how you can include attachments such as images.
- [Saving Previews and Thumbnails in the Document](Saving%20Previews%20and%20Thumbnails%20in%20the%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqmjqfvjvona) describes the approach where the application saves the thumbnail or preview image in the document and the generator simply retrieves the image for Quick Look. It also describes the function to use when the image data returned to Quick Look is in a format supported by the Image I/O framework.
- [Assigning Core Graphics Images to Thumbnails](Assigning%20Core%20Graphics%20Images%20to%20Thumbnails.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqmjsfvjvomq) shows how you can return an image (as a CGImage object) when that image is not in a format supported by the Image I/O framework.
- [Canceling Previews and Thumbnails](Canceling%20Previews%20and%20Thumbnails.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqmjtfvjvomi) explains how you can, when requested by Quick Look, cancel the generation of previews and thumbnails.
- [Debugging and Testing a Generator](Debugging%20and%20Testing%20a%20Generator.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqmjufvjvona) describes the tools and techniques you can use to debug and test a Quick Look generator.

Consult the following documents for descriptions of Quick Look generator functions and constants:

- _QLPreviewRequest Reference_
- _QLThumbnailRequest Reference_

Because generating a thumbnail or preview image often requires drawing or the creation of an image, the following documents might be of help:

- _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_
- _[Image I/O Reference Collection](https://developer.apple.com/documentation/imageio)_
- _[Cocoa Drawing Guide](../../Cocoa/Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_
- _[Core Image Programming Guide](../../Graphics%20Imaging/Core%20Image%20Programming%20Guide/About%20Core%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobv)_
[Next](Quick%20Look%20and%20the%20User%20Experience.md)

