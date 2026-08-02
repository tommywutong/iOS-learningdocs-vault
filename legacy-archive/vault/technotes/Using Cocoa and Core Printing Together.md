---
title: Using Cocoa and Core Printing Together
apple_id: DTS40008838
resource_type: Technical Note
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2009-05-27'
source_url: https://developer.apple.com/library/archive/technotes/tn2248/_index.html
archived_at: '2026-07-26T19:54:09.626420Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2248

# Using Cocoa and Core Printing Together

Illustrates how to use core printing objects together with Cocoa.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobthawugsbrfvke4vcbi4yq)[Modifying Print Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobthawugsbrfvke4vcbi4za)[Programmatic Paper Selection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobthawugsbrfvke4vcbi43a)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobthawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Cocoa provides a solid default implementation of printing that meets most needs. When you want to customize things that can't be directly accessed from Cocoa printing objects, you can call through to the Core Printing functionality as needed. This note illustrates how to use the Core Printing APIs together with Cocoa. As examples, it demonstrates how to access and modify general print settings, and how to programmatically change paper size while keeping the Cocoa printInfo object synchronized with your changes.

[Back to Top](#)

## Modifying Print Settings

This code snippet illustrates how to obtain print settings from a printInfo object, change them, and then notify Cocoa that the settings have been changed. The code shows changing the number of copies and turning on collation, but the same technique works for other print settings.

__Listing 1__  Modifying print settings with Core Printing.

```
/*         This is a short code snippet to demonstrate how to modify          print settings information that is stored in an NSPrintInfo.          This code performs no error handling for simplicity of presentation in a sample.          The Cocoa methods used here are available only on Mac OS X 10.5 and later. */          // Obtain the printInfo you want to modify.         // This code assumes the variable myPrintInfo holds         // an object of class NSPrintInfo.         // Where myPrintInfo comes from is up to your application.          // Get the PMPrintSettings object from the printInfo.         PMPrintSettings settings = [myPrintInfo PMPrintSettings];          // Modify/Set the settings of interest.         // This code sets the number of copies requested to 10.         (void)PMSetCopies(settings, 10, false);          // Turn on collation so that the copies are collated.         (void)PMSetCollate(settings, true);          // Tell Cocoa that the print settings have been changed. This allows         // Cocoa to perform necessary housekeeping.         [myPrintInfo updateFromPMPrintSettings];
```

[Back to Top](#)

## Programmatic Paper Selection

This code snippet illustrates how to replace one of the low level Core Printing objects stored in an NSPrintInfo with a custom object you obtain or create, in this case an object that customizes the page format.

__Listing 2__  Replacing the PageFormat object.

```
/*         This is a short code snippet to demonstrate how to replace         the PMPageFormat stored in an NSPrintInfo with one you obtain         or create.           The purpose of this code is to demonstrate how to completely replace         one of the low level CorePrinting objects stored in an NSPrintInfo         with one you obtain or create. Programmatic paper selection as         demonstrated here may be appropriate for an application that is performing         automated printing of data.         This code performs no error handling for simplicity of presentation in a sample.          The Cocoa methods used here are available only on Mac OS X 10.5 and later.          Here are the steps this code takes:          1) Obtain a PMPaper object from those available for the currently selected printer. To do this:                 1a) Obtain the currently selected printer.                 1b) Get an array of the pre-defined papers for that printer.                 1c) Choose a paper from that list that meets your criteria.         2) Make that paper the current paper for your Cocoa print job. To do this:                 2a) Create a PMPageFormat from the chosen paper.                 2b) Copy that page format into the page format stored in the NSPrintInfo you want to modify.                 2c) Tell Cocoa you have made a change to the PageFormat in the NSPrintInfo.  */          // Obtain the printInfo you want to modify.         // This code assumes the variable myPrintInfo holds         // an object of class NSPrintInfo.         // Where myPrintInfo comes from is up to your application.          // Get the PMPrintSession from the printInfo.         PMPrintSession session = [myPrintInfo PMPrintSession];          PMPrinter currentPrinter = NULL;         // Get the current printer from the session.         (void)PMSessionGetCurrentPrinter(session, &currentPrinter);          // Get the array of pre-defined PMPapers this printer supports.         CFArrayRef paperList = NULL;         (void)PMPrinterGetPaperList(currentPrinter, &paperList);          // Pick a paper from the list, using the appropriate criteria for your application.         // This code simply chooses the first paper in the list. More likely you would use         // information from your data (perhaps obtained from a database) to determine         // which paper in the paperList best meets the current need.         // Of course randomly choosing from the list is NOT appropriate criteria but         // is done for purposes of simplifying this sample.         PMPaper theChosenPaper = (PMPaper)[(NSArray *)paperList objectAtIndex: 0];          // Create a PMPageFormat from that paper.         PMPageFormat theChosenPageFormat = NULL;         (void)PMCreatePageFormatWithPMPaper(&theChosenPageFormat, theChosenPaper);          // Get the PMPageFormat contained in the printInfo.         PMPageFormat originalFormat = [myPrintInfo PMPageFormat];          // Copy over the original format with the new format you want to use.         (void)PMCopyPageFormat(theChosenPageFormat, originalFormat);          // Tell Cocoa you that changed the page format. This allows Cocoa         // to perform the necessary housekeeping.         [myPrintInfo updateFromPMPageFormat];          // Release the PMPageFormat this code created.         PMRelease(theChosenPageFormat);
```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-05-27 | New document that describes how to modify print settings and allow programmatic paper selection. |

