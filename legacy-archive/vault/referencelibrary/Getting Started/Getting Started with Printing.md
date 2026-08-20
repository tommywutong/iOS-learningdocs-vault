---
title: Getting Started with Printing
apple_id: TP30001080
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Printing/_index.html
archived_at: '2026-07-18T02:39:26.504929Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Technology Overview

The Mac OS X printing system provides Macintosh developers with a flexible and powerful printing environment that uses Quartz 2D for rendering and conversion services. Quartz 2D supports a resolution-independent PDF drawing model. With this model, applications can print high-quality, color-managed output on all classes of raster and PostScript printers, and save documents as PDFs.

You can use the Mac OS X printing system in your application in numerous ways or extend it with software you create. Application developers can add printing support to their applications and application-specific features to the Page Setup or Print dialog. Printer vendors can write printer drivers to support their printers. They can also provide custom panes for the Print dialog to support printer-specific features.

### Start Here

Before you begin to write any code, it’s a good idea to be familiar with the underlying technology of the printing system. If you haven’t already done so, read about Apple’s [printing features](http://www.apple.com/macosx/features/printing/). Then read Mac OS X Printing System Overview for a look under the hood at how printing is implemented in Mac OS X.

### Choose a Learning Path

If you’re an application developer, you want users to print from your application or from the Finder. If your application is specialized for graphics or publication, you may want to provide users with other customized options. If you are a printer vendor, you want to make sure your printer and its unique features can be accessed from any application.

#### Supporting Printing in Your Application

You can support printing in your application whether you develop in procedural C, Objective-C, or BSD UNIX. You can also support printing of documents created by your application without users opening the application.

- __If you are using procedural C,__ see [Supporting Printing in Your Carbon Application](../../documentation/Carbon/Supporting%20Printing%20in%20Your%20Carbon%20Application/Introduction%20to%20Supporting%20Printing%20in%20Your%20Carbon%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzy). You can find the functions that are discussed there in Carbon Printing Manager Reference. For helpful code, install the Xcode Tools CD and go to the folder `/Developer/Examples/Printing/`.
- __If you are using Objective-C,__ you support printing using Cocoa objects and methods. For an overview of printing in Cocoa, read [Printing Programming Guide for Mac](../../documentation/Cocoa/Printing%20Programming%20Guide%20for%20Mac/About%20Printing%20on%20the%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4dg2i). For helpful sample code, install the Xcode Tools CD and go to the folder `/Developer/Examples/AppKit/TextEdit/`.
- __If you are using BSD UNIX,__ you can write a faceless application using functions and data types defined in the header files `PMCore.h` and `PMDefinitions.h`. To understand the items in the printing header files, refer to Carbon Printing Manager Reference. If you are interested in knowing the details of CUPS, obtain a copy of Michael R. Sweet’s book [CUPS: Common UNIX Printing System](http://www.cups.org/documentation.php).
- __If you want users to print documents created by your application without first opening the application,__ become familiar with Apple events, especially the Print Documents Apple event. To learn about the variety of printing settings that Mac OS X v 10.3 supports, read Technical Note TN2082, [The Enhanced Print Apple Event](https://developer.apple.com/technotes/tn2002/tn2082.html). To understand Apple events and the AppleScript language, read [AppleScript Overview](../../documentation/Apple%20Script/AppleScript%20Overview/Introduction%20to%20AppleScript%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tm2i). You can find functions that are discussed there in [Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager).

#### Customizing Options in Printing Dialogs

You have the option to write a printing dialog extension to support application features that are not supported in the Apple-provided Page Setup and Print dialogs.

- __If you are using procedural C,__ you can find information on printing dialog extensions in Printing Plug-in Interfaces Reference, [Extending Printing Dialogs](../../documentation/Printing/Extending%20Printing%20Dialogs/Introduction%20to%20Extending%20Printing%20Dialogs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzz), and Ticket Services Reference.
- __If you are using Objective-C,__ for information on how to customize a Print or Page Setup dialog see the articles [Using a Print Panel](../../documentation/Cocoa/Printing%20Programming%20Guide%20for%20Mac/Managing%20and%20Extending%20the%20Print%20Panel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3delkciffeershivca) and [Using a Page Setup Panel](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Printing/osxp_printlayoutpanel/osxp_printlayoutpanel.html#//apple_ref/doc/uid/20000863) in [Printing Programming Guide for Mac](../../documentation/Cocoa/Printing%20Programming%20Guide%20for%20Mac/About%20Printing%20on%20the%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4dg2i).

#### Supporting Printer Hardware

If you are a printer vendor, you’ll create a printer driver for each printer or family of printers to ensure the printers support Mac OS X. You’ll also provide a printing dialog extension so that users have access to the special features offered by your hardware, regardless of the application they print from.

Because of the specialized nature of printer driver development, Apple recommends reading Printing Plug-in Interfaces Reference, [Extending Printing Dialogs](../../documentation/Printing/Extending%20Printing%20Dialogs/Introduction%20to%20Extending%20Printing%20Dialogs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzz), and Ticket Services Reference. Then contact Apple Developer Technical Support with your requirements before beginning development. You can contact developer support through developer.apple.com.

### Next Steps

The [Printing Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000432) includes the following high-level Printing resource pages, which you can bookmark for easy access:

- [Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP30000432)

  Conceptual and how-to information for printing.
- [Reference](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000432)

  Focused, detailed descriptions in reference format for printing.
- [Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30000432)

  Samples demonstrating how to use printing routines.
- [Technical Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000924-TP30000432)

  Late-breaking documents on printing issues
- [Technical Q&As](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000926-TP30000432)

  Programming tips, code snippets, & FAQs by Apple’s support engineers.
- Mailing Lists

  You can use the [Printing](http://www.lists.apple.com/mailman/listinfo/printing) mailing list to discuss any issues you encounter writing code.

Here are additional Printing resources that you should be aware of.

- [Common UNIX Printing System page](http://www.cups.org/)

  www.cups.org
- [IPP at the Printing Working Group](http://www.pwg.org/ipp/index.html)

  Home of IPP, the Internet Printing Protocol.
- [Gimp-Print](http://gimp-print.sourceforge.net/)

  Home of Gimp-Print, an open source suite of printer drivers that work with CUPS.

