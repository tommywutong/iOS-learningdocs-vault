---
title: Locating the Selected Printer
apple_id: DTS10001251
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd36.html
archived_at: '2026-07-18T02:29:33.922583Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A GXPD36Locating the Selected Printer |

|  |  |  |
| --- | --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: How do I find out which printer is selected in the Chooser?  A: Under the old print architecture, you can locate the driver for the currently selected printer by accessing the `'STR '` -8192 or `'alis'` -8192 resources in the System file. The `'STR '` -8192 resource contains the name of the current driver and the `'alis'` resource contains an alias record that will take you right to the driver. Either can be used to locate the driver. Note that with older system software the `'alis'` resource does not appear in the System. If the `'alis'` resource is present, resolve it. If not, look in the Extensions folder and in the System folder for a file with the same name as `'STR '` -8192.  With GX installed, the `'STR '` -8192 resource is supported for backward compatibility in applications that are not GX-printing savvy. In this case the `'STR '` -8192 resource gives the name of the default DTP file on the desktop. For applications that are GX-printing savvy, the concept of a default printer is not important because the user can pick any printer from the GX Print dialog.  Once you've located the `'STR '` -8192, and you have the name of the current printer, you can then determine the printer's zone and type using the `'PAPA'` resource id -8192 in the driver (if the traditional printing architecture is in use) or by accessing the printer's 'comm' resource (if the GX printing architecture is in use).  Here is some sample code which demonstrates how to do this.   |  | | --- | | ``` // Current Printer info sample code // // Dave Polaschek and David Hayward // Developer Technical Support // AppleLink: DEVSUPPORT // // Copyright 1995, Apple Computer,Inc // // Check the default printer under GX or old printing architecture. // Print out the name, entityType, and zone. // // davep    8/16/95    initial cut  #include <stdio.h> #define gestaltGXVersion            'qdgx'   // in PrintingManager.h (old) or GXPrinting.h (new)  #define gestaltGXPrintingMgrVersion 'pmgr'  // in PrintingManager.h (old) or GXPrinting.h (new)  #define gestaltAliasMgrAttr         'alis'  // in Aliases.h #define printingResourceID            0xE000            // 0xE000 = -8192  OSErr        GetCurrentPrinter(Str255 printer); OSErr        test(void); Boolean        gxInstalled(void); Boolean        validPrinter(void);  /*---------------------------------------------------------------------------*\         This function returns true if QuickDraw GX printing is available \*---------------------------------------------------------------------------*/ Boolean gxInstalled(void) {     long version;     if (Gestalt(gestaltGXVersion, &version) == noErr)         if (Gestalt(gestaltGXPrintingMgrVersion, &version) == noErr)             return(true);     return(false); }  /*---------------------------------------------------------------------------*\         This function returns the network entity of the currently         selected printer, and as an added bonus, you get an error code, too! \*---------------------------------------------------------------------------*/ OSErr GetCurrentPrinter(Str255 printer) {     StringHandle    theDriver;     Handle            thePrinter;     OSErr            theErr;     short            resFileRefnum;     theDriver = GetString(printingResourceID);     if (!theDriver) goto BADDriver;     if (gxInstalled()) {         short    vRefNum;         long    dirID;         FSSpec    theFile;         long    resSize;         theErr=FindFolder(kOnSystemDisk,kDesktopFolderType,kDontCreateFolder,         &vRefNum,&dirID);         if (theErr != noErr) goto BADDriver;         theErr=FSMakeFSSpec(vRefNum,dirID,*theDriver,&theFile);         if (theErr != noErr) goto BADDriver;         resFileRefnum = FSpOpenResFile(&theFile,fsRdPerm);         if (resFileRefnum == -1) goto BADResFile;         thePrinter = Get1Resource('comm', 0);         if (!thePrinter) goto BADPrinter;         if (*((long *)*thePrinter) != 'PPTL') goto BADPrinter;         resSize = GetHandleSize(thePrinter)-6;         BlockMoveData((*thePrinter)+6,printer,resSize);     } else {         Boolean     aliasCallsPresent;         Boolean     aliasResourcePresent;         long        resSize,response;         AliasHandle    theAlias;          aliasCallsPresent = ((Gestalt(gestaltAliasMgrAttr,&response) == noErr)             &&             (response & 1));         theAlias = (AliasHandle) GetResource('alis',printingResourceID);         aliasResourcePresent = !!(theAlias);          if (aliasCallsPresent && aliasResourcePresent) {             FSSpec    fileSpec;             Boolean    wasChanged;             theErr = ResolveAlias(NULL, theAlias,&fileSpec,&wasChanged);             if (theErr != noErr) goto BADDriver;             resFileRefnum = FSpOpenResFile(&fileSpec,fsRdPerm);             if (resFileRefnum == -1) goto BADResFile;         } else {             resFileRefnum = OpenResFile(*theDriver);             if (resFileRefnum == -1) goto BADResFile;         }         thePrinter = Get1Resource('PAPA', printingResourceID);         if (!thePrinter) goto BADPrinter;         resSize = GetHandleSize(thePrinter);         BlockMoveData(*thePrinter,printer,resSize);     }     ReleaseResource(thePrinter);     CloseResFile(resFileRefnum);     return(noErr); // Error returns BADPrinter:     CloseResFile(resFileRefnum); BADResFile:     theErr = ResError(); BADDriver:     return(theErr); }  /*---------------------------------------------------------------------------*\         This function is called by the test harness. Doesn't do much         except prove that things work without crashing. \*---------------------------------------------------------------------------*/ OSErr test(void) {     OSErr    testValue;     Str255    printerEntity;     testValue = GetCurrentPrinter(printerEntity);     if (testValue)         return testValue;     else {         Str31            printer,type,zone;         unsigned char    *currentString;         currentString = printerEntity;         BlockMove(currentString,printer,Length(currentString)+1);         p2cstr(printer);          currentString += Length(currentString) + 1;         BlockMove(currentString,type,Length(currentString) + 1);         p2cstr(type);          currentString += Length(currentString) + 1;         BlockMove(currentString,zone,Length(currentString) + 1);         p2cstr(zone);         printf("Current Printer name = %s\n"                 "EntityType = %s\n"                 "Zone = %s\n",printer,type,zone);         return noErr;     } }  /*---------------------------------------------------------------------------*\         This function tells if there's a valid printer selected (i.e. not         aimed at a driver that's since been deleted or no printer selected         since last System sw install) in the chooser \*---------------------------------------------------------------------------*/ Boolean validPrinter(void) {     Str255    printerEntity;      if (GetCurrentPrinter(printerEntity) != noErr)         return false;     else if (Length(printerEntity) == 0)         return false;     else         return true; }  // Simple testbed for Macintosh sample code // // Dave Polaschek // Developer Technical Support // AppleLink: DEVSUPPORT // // Copyright 1995, Apple Computer,Inc // // This file contains main, and nothing else. // dave    8/15/95    initial cut #include <stdio.h> extern OSErr test(void);        // in CurrentPrinter.c  void main(void) {     OSErr    testResult;      testResult = test();     printf("Return value from test() = %d\n",testResult); } ``` | |

#### [Sep 15 1995]

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
