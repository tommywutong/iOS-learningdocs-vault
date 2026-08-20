---
title: QuickTime Import and Export Guide
apple_id: TP40000903
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2006-01-10'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/RM/ImportExport/DataExchange/A-Intro/1Introduction.html
archived_at: '2026-07-18T02:05:04.027824Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/ImportExport/DataExchange/B-Chapter/2AboutGraphicsImport.html)

# Introduction to QuickTime Import and Export Guide

This book describes QuickTime’s technology for importing and exporting graphics and other data into and out of movies.

QuickTime imports and exports data between movies and still images using graphic importer and exporter components and movie data exchange components:

- Graphic importer and exporter components open, display, and save graphic images stored using various file formats and compression algorithms. Apple-provided components read many common compressed image types. Support for cross-platform and web-derived images is provided, including the ability to query for capability by MIME type and by examination (a component can be asked to examine a file of unknown type, to see if it can decompress the file).
- Movie data exchange components allow you to import data from non-movie sources into QuickTime movies, and to export data to non-movie formats. For example, you can import a CD audio track into a QuickTime movie, or save a QuickTime movie’s sound track as an AIFF file, using data exchange components. Applications programmers can use the services of data exchange components indirectly, through high-level calls to the Movie Toolbox. Movie data exchange components can also be controlled directly from applications.

Image importers and exporters manage the import and export of graphic images, such as JPEG, TIFF, Photoshop, and PNG. Movie data exchange components support the import and export of other multimedia formats, such as AIFF, WAVE, AVI, MPEG-1, MIDI, MPEG-4, 3GPP, MP3, MPEG-2, H.263, H.264, and OpenDML. QuickTime can open any format file for which it has an importer and create any for which it has an exporter.

Applications make direct calls to graphic importer components, so this document will be of interest to most QuickTime developers who work with still images or the web. To obtain the services of a graphics importer component, applications normally use the `GetGraphicsImporterForFile` or `GetGraphicsImporterForDataRef` functions of the Image Compression Manager.

If your application needs to import or export data between movies and other data types, you should read the sections [Movie Data Exchange Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/ImportExport/DataExchange/F-Chapter/6MovieDataExchangeCo.html#//apple_ref/doc/uid/TP40000903-MovieDataExchangeComponents-SW1), and [Using Movie Data Exchange Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/ImportExport/DataExchange/H-Chapter/8UsingMovieDataExcha.html#//apple_ref/doc/uid/TP40000903-UsingMovieDataExchangeComponents-SW1). If you plan to control data exchange components directly from within your application, or if you are creating a new movie data exchange component, you will need to read all of the material in this document.

If you need to create a new graphics importer component, refer to this document to implement a component that supports the required interface functions.

This document is divided into seven chapters:

- [About Graphics Importer and Exporter Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/ImportExport/DataExchange/B-Chapter/2AboutGraphicsImport.html#//apple_ref/doc/uid/TP40000903-AboutGraphicsImporterandExporterComponents-SW1) describes what QuickTime graphic importer and exporter components do and shows how to use them from within an application.
- [Graphics Importer Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/ImportExport/DataExchange/C-Chapter/3GraphicsImporterCom.html#//apple_ref/doc/uid/TP40000903-GraphicsImporterComponents-SW1) tells you how applications can use graphics importer components.
- [Graphics Exporter Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/ImportExport/DataExchange/D-Chapter/4GraphicsExporterCom.html#//apple_ref/doc/uid/TP40000903-GraphicsExporterComponents-SW1) describes the general features of graphics exporter components.
- [Graphics Exporter Component Functions By Task](https://developer.apple.com/library/archive/documentation/QuickTime/RM/ImportExport/DataExchange/E-Chapter/5GraphicsExporterCom.html#//apple_ref/doc/uid/TP40000903-GraphicsExporterComponentFunctionsByTask-SW1) describes the graphics exporter functions grouped by task and category.
- [Movie Data Exchange Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/ImportExport/DataExchange/F-Chapter/6MovieDataExchangeCo.html#//apple_ref/doc/uid/TP40000903-MovieDataExchangeComponents-SW1) describes what movie data exchange components are and shows how they work.
- [Creating a Movie Data Exchange Component](https://developer.apple.com/library/archive/documentation/QuickTime/RM/ImportExport/DataExchange/G-Chapter/7CreatingaMovieDataE.html#//apple_ref/doc/uid/TP40000903-CreatingaMovieDataExchangeComponent-SW1) describes how to create a movie data exchange component. Sample import and export components are provided as a programming aid.
- [Using Movie Data Exchange Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/ImportExport/DataExchange/H-Chapter/8UsingMovieDataExcha.html#//apple_ref/doc/uid/TP40000903-UsingMovieDataExchangeComponents-SW1) describes how to use movie exchange components from within your application.

Sample code is available at:

[http://developer.apple.com/samplecode/ImproveYourImage/index.html](https://developer.apple.com/samplecode/ImproveYourImage/index.html)

The sample code demonstrates the usage of QuickTime graphics importers and exporters, and includes twelve separate examples, each of which can be chosen from the Examples menu. These show how to use graphics importers to

- Simply draw a still image.
- Import, draw, scale and rotate a still image.
- Demonstrate compositing with alpha graphics modes and images containing alpha channels.
- Retrieve metadata from image files.
- Display multiple layers stored in a Photoshop file.
- Import an image from a URL data reference.
- Add a filter to an imported image, draw it with the filter, and export a new image with the filter applied.

The following Apple books cover related aspects of QuickTime programming:

- _[QuickTime Overview](QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs)_ gives you the starting information you need to do QuickTime programming.
- _[QuickTime Movie Basics](QuickTime%20Movie%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmby)_ introduces you to some of the basic concepts you need to understand when working with QuickTime movies.
- _[QuickTime Movie Creation Guide](QuickTime%20Movie%20Creation%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmbw)_ describes some of the different ways your application can create a new QuickTime movie.
- _QuickTime Guide for Windows_ provides information specific to programming for QuickTime on the Windows platform.
- _[QuickTime Media Types and Media Handlers Guide](QuickTime%20Media%20Types%20and%20Media%20Handlers%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqojz)_ introduces the idea of QuickTime media handler components and provides details of the video, sound, text, timecode, and tween media handlers.
- _[QuickTime Compression and Decompression Guide](QuickTime%20Compression%20and%20Decompression%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnzy)_ introduces you to the QuickTime Image Compression Manager and its associated components, which provide image-compression and image-decompression services to applications and to other QuickTime components.
[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/ImportExport/DataExchange/B-Chapter/2AboutGraphicsImport.html)

