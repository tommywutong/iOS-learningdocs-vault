---
title: Using PostScript Printer Description Files
apple_id: TP40000960
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Printing/Conceptual/UsingPPDFiles/ppd_intro/ppd_intro.html
archived_at: '2026-07-18T01:52:36.498463Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](PPD%20Concepts.md)

# Introduction to Using PostScript Printer Description Files

_PostScript printer description_ (PPD) files are created by printer vendors to describe the set of printer features available for their PostScript printers. On the Macintosh, PPD files provide all the information necessary to describe a PostScript printer’s features, including options and default settings. They also contain the PostScript code used to invoke those features.

This document is important for printer vendors who are providing PPD files in OS X because it

- describes where PPD files need to be installed
- provides information about localizing PPD files
- details the differences between PPD support in OS X and earlier versions of the Mac OS
- tells what you need to do if you provide a printing dialog extension for your PostScript printer
- shows how to specify that certain features should be grouped in the interface
- discusses how OS X searches for PPD files

Application developers might also find this document useful because it

- provides an overview of PPD files and how OS X handles the files
- describes the Printer Features pane in the Print dialog

For detailed information on PPD files, see _PostScript Printer Description File Format Specification_, available from Adobe Developer Support:

[http://partners.adobe.com/](http://partners.adobe.com/)

The LaserWriter 8 driver is Apple’s general purpose PostScript printer driver for Mac OS 9 and earlier. It was designed to work with any PostScript or PostScript-compatible printer connected to a Macintosh computer. The LaserWriter 8 driver (specifically version 8.4.1 and later) allows developers to define a custom user interface using `'ppdt'`, `'PPDA'`, `'DITL'`, and `'ALRT'` resources in the PPD file. (See Apple TechNote 1068 for more information.) In the absence of these resources the LaserWriter 8 driver provides a generic user interface for the features in the PPD file that are defined by the `*OpenUI/*CloseUI` keywords. (See [PostScript Printer Description Files](PPD%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcobzfvkfawcsivddcmjr) for more information on PPD keywords.)

The OS X printing system also parses PPD files and provides an interface for PostScript printer features, but OS X does not use the resource fork data in a PPD file. Apple supports a set of standard features for all printers while allowing developers to add features either through a custom user interface or by letting OS X automatically create the user interface for nonstandard features. Developers who want to create a custom user interface must write a printing dialog extension (PDE).

The differences between the OS X printing system and the LaserWriter 8 bring up a number of issues for developers who support PostScript printing in OS X and earlier versions of the Mac OS, including from the Classic environment. Applications that print from the Classic environment use an unmodified version of the LaserWriter 8 driver as their primary PostScript printer driver.

Here’s a summary of the differences and the issues you may need to consider:

- OS X does not use the resource fork data in a PPD file; earlier versions of the Mac OS do. If a PPD file that’s needed by OS X exists only in the Classic System Folder, OS X uses that PPD file. However, OS X only uses the information in the data fork, not the resource fork.
- OS X uses printing dialog extensions to add or replace panes in the Print dialog while earlier versions of the Mac OS use data in the resource fork of the PPD file to control the layout of features in a custom pane.

  This means if you take advantage of the resource-based PPD file to do custom panels for earlier versions of the Mac OS, the corresponding printer features appear in the Printer Features pane of the Print dialog as generic features in OS X (unless you provide printing dialog extensions to handle these features.)

  Conversely, if you provide a printing dialog extension for a PostScript printer, and use the data-fork-only PPD file in OS X and for the LaserWriter 8 driver, LaserWriter 8 uses its generic user interface.
- The location of some of the features in the Print dialog provided by the LaserWriter 8 driver and that are provided by OS X are slightly different. For example, the duplex option appears in the Layout pane provided by LaserWriter 8, but in the Duplex pane in OS X.
- OS X printing and the LaserWriter 8 driver support a similar, but slightly different set of features. If you use the same PPD file in the Classic environment as you do for OS X, the user interface might not reflect all the printer features in the PPD file.
- Desktop printing is not supported in OS X and it is not available when printing from an application in the Classic environment.

[Next](PPD%20Concepts.md)

