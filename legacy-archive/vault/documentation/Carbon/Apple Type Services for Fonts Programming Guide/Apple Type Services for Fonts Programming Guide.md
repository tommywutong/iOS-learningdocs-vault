---
title: Apple Type Services for Fonts Programming Guide
apple_id: TP30000981
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-09-29'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ATS_Concepts/atsfonts_intro/atsfonts_intro.html
archived_at: '2026-07-15T05:22:26.862158Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Managing%20Fonts-%20ATS%20Concepts.md)

# Apple Type Services for Fonts Programming Guide

_Apple Type Services for Fonts Programming Guide_ provides an overview of font management in Mac OS X, describes the concepts needed to understand font management, and shows you how to perform the most common font management tasks. The Apple Type Services for Fonts programming interface is a collection of functions and data types that you can use to access and manage font data. It is designed to handle all the font formats and associated data models supported in Mac OS X. The programming interface is designed with performance, scalability, and consistency in mind, and is available to Cocoa and Carbon applications through the Apple Type Services (ATS) framework in Mac OS X.

Apple Type Services for Fonts offers better stability and enhanced performance than previous versions, and features the following improvements:

- Error checking and exception handling are improved.
- More information is cached to disk, speeding up login and logout times.
- Font data is retrieved faster.
- Memory allocation is more efficient.
- Corrupt or invalid font files are disabled automatically.
- Better font streaming supports PDF embedding and downloading fonts to a printer.

You should read this document if you plan to write a Mac OS X application that

- activates or deactivates fonts
- needs to keep track of fonts available in the ATS font database
- provides font utility services to other applications
- supports the Fonts panel user interface
- plans to store persistent font information in a document
- uses basic font metrics

This document is organized into the following chapters:

- [Managing Fonts: ATS Concepts](Managing%20Fonts-%20ATS%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbzfvjvomi), details the fonts services available in Mac OS X, defines font terminology, provides information on where fonts are installed, gives an overview of the ATS server, and describes the user interface for fonts.
- [Managing Fonts: ATS Tasks](Managing%20Fonts-%20ATS%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmjqfvjvomq), shows how to accomplish the most common programming tasks using ATS for Fonts and provides guidelines for increasing performance and making efficient use of memory in your application.

In addition to this document, you may find the following documents useful:

- _[ATSUI Programming Guide](../ATSUI%20Programming%20Guide/Introduction%20to%20ATSUI%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobu)_ in Carbon Text Manipulation Documentation provides an overview on how text is laid out and displayed, defines typographical concepts, and discusses the style and text layout objects and attributes used by the Apple Type Services for Unicode Imaging (ATSUI) programming interface.
- _[Managing Fonts: QuickDraw](../Managing%20Fonts-%20QuickDraw/Introduction%20to%20Managing%20Fonts-%20QuickDraw.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobs)_ in Carbon Typography Documentation defines font terminology, provides an overview of QuickDraw-based font management and discusses how to use the Font Manager to manage fonts in both Mac OS 9 and Mac OS X. If your application runs only in Mac OS X, you may not need to read this document. However, the discussion of font terminology may be useful if you are new to font management.

The following website provides font-related information, including the _TrueType Reference Manual_ and links to other typography and font websites:

[http://developer.apple.com/fonts](https://developer.apple.com/fonts)

[Next](Managing%20Fonts-%20ATS%20Concepts.md)

