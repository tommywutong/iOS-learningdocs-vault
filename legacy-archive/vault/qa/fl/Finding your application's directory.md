---
title: Finding your application's directory
apple_id: DTS10001200
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreServices
published: '2000-06-19'
source_url: https://developer.apple.com/library/archive/qa/fl/fl14.html
archived_at: '2026-07-18T02:29:29.164132Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > File Management](https://developer.apple.com/referencelibrary/Carbon/idxFileManagement-date.html)

|  |
| --- |
| Technical Q&A FL14Finding your application's directory |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---   Q: How can I find out the directory ID and volume reference number for the folder containing my application?  A: You can ask the Process Manager for this information by calling the `GetProcessInformation` routine from inside of your application. The directory ID and volume reference number can be extracted from the `FSSpec` record filled out by the `GetProcessInformation` call. The `GetApplicationDirectory` routine shown in Listing 1 illustrates how you would do this.   |  |  | | --- | --- | | |  | | --- | | ```     #include <Types.h>     #include <Files.h>     #include <Processes.h>           /* GetApplicationDirectory returns the volume reference number         and directory ID for the current application's directory. */      OSStatus GetApplicationDirectory(short *vRefNum, long *dirID) {         ProcessSerialNumber PSN;         ProcessInfoRec pinfo;         FSSpec pspec;         OSStatus err;             /* valid parameters */         if (vRefNum == NULL || dirID == NULL) return paramErr;             /* set up process serial number */         PSN.highLongOfPSN = 0;         PSN.lowLongOfPSN = kCurrentProcess;             /* set up info block */         pinfo.processInfoLength = sizeof(pinfo);         pinfo.processName = NULL;         pinfo.processAppSpec = &pspec;             /* grab the vrefnum and directory */         err = GetProcessInformation(&PSN, &pinfo);         if (err == noErr) {             *vRefNum = pspec.vRefNum;             *dirID = pspec.parID;         }         return err;     } ``` | |    __Listing 1__. Extracting an application's location in the file system from results returned by `GetProcessInformation`.   Q: Okay, now that I know how to find the directory containing the application, how can I make sure this is the default directory?  A: Here, all you need to do is pass the volume reference number and directory ID extracted from the results returned from `GetProcessInformation` to the `PBHSetVol` routine. An example of how to do this is shown in Listing 2.   |  |  | | --- | --- | | |  | | --- | | ```     #include <Types.h>     #include <Files.h>     #include <Processes.h>           /* SetApplicationDirAsDefault sets the default directory         to the directory containing the current application. */      OSStatus SetApplicationDirAsDefault(void) {         WDPBRec wpb;         OSStatus err;         err = GetApplicationDirectory(&wpb.ioVRefNum, &wpb.ioWDDirID);         if (err == noErr) {             wpb.ioNamePtr = NULL;             err = PBHSetVolSync(&wpb);         }         return err;     } ``` | |    __Listing 2__. Setting the default directory to the directory containing the application.   Q: Great! But what versions of the system software allow me to do this?  A: The techniques shown in Listing 1 and Listing 2 can be used in any version of the system software from System 7 through Carbon. |

#### [Jun 19 2000]

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
