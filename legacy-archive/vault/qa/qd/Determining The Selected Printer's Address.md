---
title: Determining The Selected Printer's Address
apple_id: DTS10001794
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-11-22'
source_url: https://developer.apple.com/library/archive/qa/qd/qd35.html
archived_at: '2026-07-18T02:38:37.283540Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A QD35Determining The Selected Printer's Address |

|  |  |
| --- | --- |
| ---   Q: How do I determine the network address of the currently selected printer (assuming that it is a network printer)?  A: Usually, you can get name of the current printer from the '`PAPA`' (-8192) resource in the chosen printer's driver. Unfortunately, it can be difficult to find the chosen printer's driver, and calling `PrOpen` to make the current driver's resource file the current resource file can cause problems when PrintMonitor is printing in the background.  Attached is some [sample code](https://developer.apple.com/library/archive/qa/qd/downloads/CurrentPrinter_68k.hqx) for you to use.  The following is the most reliable way to find the chosen printer's driver:   - If the Alias Manager is present, then load '`alis`' -8192 from the System's   resource fork. Since this alias points to the chosen printer's driver, all you   have to do is call `ResolveAlias` to obtain an `FSSpec`. - If the Alias Manager is not present, load '`STR` ' -8192 from the System's   resource fork. This string contains only the name (not the entire path) of the   chosen printer's driver, so you'll need to look for the file in either the   Extensions folder or the System folder.   Once you've located the chosen printer's driver using one of these methods, open its resource (using `HOpenResFile` or `FSpOpenResFile`) and load the '`PAPA`' resource. Be aware that not all printers (not even all sharable printers) have '`PAPA`' resources.  Prior to the introduction of GrayShare, there were only two basic classes of printers: local printers (a printer connected to and usable only by the computer it is connected to) and network printers (a printer networked to and usable by several computers).  Local printers cannot be named, so they are identified by the port they are connected to. For this reason, the following printer drivers do not allow names to be attached to printers:   - Personal LaserWriter SC - Personal LaserWriter LS - StyleWriter - ImageWriter - LQ ImageWriter   Network printers, by contrast, are nameable. A copy of the selected printer's name is encoded in the driver's '`PAPA`' resource ID -8192. Drivers in this category currently include:   - LaserWriter - AppleTalk ImageWriter - AppleTalk LQ ImageWriter   Since the introduction of GrayShare, there are three classes of printers: local, network, and shared. Shared printers are those that are connected to one machine but can optionally be shared by other machines on a network. Shared printers store a copy of the selected printer's name in the driver's '`PSEL`' resource ID -8192. Drivers in this category currently include:   - LaserWriter Select 300 - StyleWriter II   A GrayShare driver such as StyleWriter II can operate in either of two modes. If the user selects a StyleWriter that is connected to a serial port, the driver behaves like a local printer driver. If the user selects a shared printer, the driver must act as a client to the printer owner's server. In this situation the driver appears to behave as a normal networked printer, even though the actual mechanism used is considerably different.  Although the '`PSEL`' resource type is currently undocumented, most of the information it contains is identified as follows:   |  | | --- | | ``` OFFSET	LENGTH	USAGE 0	2	mode: if shared = 0xFFFF, if local=0x0000 2	34	user's name 36	34	printer's name:  if local, name=type 36	34	printer's type  e.g.  \pStyleWriterII   70	34	printer's zone  e.g.  \p*   104	102	other ``` |   Most applications can rely on finding the name of a LaserWriter being in '`PAPA`' -8192. In the future, however, you may not be able to assume that the name of a shared device will be found in '`PSEL`' -8192. The '`PAPA`' resource has been standardized by historical usage, but GrayShare is nearly new, and it is not as thoroughly documented. Because GrayShare drivers may encode internal information differently in the future, we recommend checking the version of the device's driver before using its '`PSEL`' to make your software more robust and to retain maximum compatibility.  There is an old undocumented technique for bypassing the chooser by manipulating the values stored in the places mentioned above. If you are thinking of doing this, take note of the following question and answer:  Question:  We've been manually writing '`PAPA`', '`STR` ' and '`alis`' resources in the System file and in the LaserWriter driver to change printers without using the Chooser. This method sometimes causes errors with LaserWriter 8.0. What do we need to do?  Answer:  LaserWriter 8.0 needs to know more about the printer than its AppleTalk name -- it also has to have a parsed and ready-to-use PPD file for that printer. Since there's so little memory available in applications such as the Finder during printing, parsing is done at Chooser time, not at print time.  Apple has always said, We can't guarantee that you can change printers behind the Chooser's back, and with LaserWriter 8.0 this is true. If the driver has parsed a PPD file and has it ready, this should work, but you would have to have manually chosen that printer before and set everything up. If you set up a LaserWriter IINTX printer with the correct PPD file, then choose a LaserWriter IIf, and then another printer driver, you can probably switch back to the LaserWriter IINTX programmatically. However, the driver will use the LaserWriter IIf PPD file with it, which may or may not cause PostScript errors. Designing the driver to be switchable by other applications was not a priority of the Adobe/Apple development team.  As long as you try to switch to a printer that uses the same PPD file that the driver last parsed (the PPD associated with the last printer selected in the Chooser), there shouldn't be any more problems than there were before with earlier printer drivers.  With QuickDraw GX, many things have changed, so you may need to re-think your application's objectives in this environment. QuickDraw GX includes an all-new printing manager and API, all-new extendable printer drivers, and an all-new Chooser interface with desktop printer icons. It doesn't even have a '`PAPA`' resource, but fortunately, much of what you are trying to do (pre-processing and redirecting batches of files) can be accomplished much more cleanly and safely with the Message Override or Printing Extensions mechanisms. The following is a list of publications you can use to obtain more information:   - _develop #16: Print Hints - LaserWriter 8 for Fun and Profit_ - _Inside Macintosh: QuickDraw GX Programmers Overview_ - _Inside Macintosh: QuickDraw GX Printing_ - _Inside Macintosh: QuickDraw GX Printing Extensions and Drivers_ |

#### [Nov 22 1995]

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
