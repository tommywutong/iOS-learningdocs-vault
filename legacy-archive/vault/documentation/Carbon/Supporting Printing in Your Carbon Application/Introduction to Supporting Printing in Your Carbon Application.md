---
title: Supporting Printing in Your Carbon Application
apple_id: TP30000978
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2004-08-31'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/CPM_Concepts/cpm_chap1/cpm_intro.html
archived_at: '2026-07-15T05:22:29.039887Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Printing%20Concepts%20for%20Carbon%20Developers.md)

# Introduction to Supporting Printing in Your Carbon Application

This document shows you how to set up a Carbon application to print in Mac OS X using the Carbon Printing Manager. The _Carbon Printing Manager_ defines a programming interface that Carbon applications use for printing their documents. For Carbon applications, this programming interface replaces that of the original Printing Manager. The original Printing Manager—referred to as the old Printing Manager in this document—was introduced with the very first release of Macintosh system software. The Carbon Printing Manager allows applications to print both in Mac OS 8 and 9 with existing printer drivers and in Mac OS X with new printer drivers.

You should read this document if you are a developer who wants to support printing from your Carbon application. This document:

- describes the Carbon Printing Manager concepts you need to know to start coding your application
- provides examples of how to set up printing in a new application
- discusses how to revise an existing application

To get the most from this document, you should first read _About the Mac OS X Printing System_, which describes the various portions of the printing system, including the user interface and the printing architecture.

This document describes how to write only the application portion of generating a print job. It does not describe how to write printer modules, converters, I/O modules, or printing dialog extensions. See the [Printing Carbon Documentation](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000432-TP30000494) for information on these other topics.

The document is divided into the following chapters:

- [Chapter 2](Printing%20Concepts%20for%20Carbon%20Developers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambuguwviubz) contains details on how the Carbon Printing Manager works and describes the concepts you need to use the Carbon Printing Manager in your application.
- [Chapter 3](Printing%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviubz) shows you how to use the Carbon Printing Manager to support printing in a Carbon application. The chapter contains sample code you can customize for your application.
- [Chapter 4](Adopting%20the%20Carbon%20Printing%20Manager.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambug4wviubz) explains what you need to do to revise an existing non-Carbon Mac OS 9 application so that it can print in either Mac OS 9 or Mac OS X.

See also _Carbon Printing Manager Reference_.

[Next](Printing%20Concepts%20for%20Carbon%20Developers.md)

