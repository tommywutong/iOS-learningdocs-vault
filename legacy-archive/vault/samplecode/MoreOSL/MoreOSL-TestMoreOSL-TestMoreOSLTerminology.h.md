---
title: MoreOSL
apple_id: DTS10000670
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ApplicationServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoreOSL/Listings/MoreOSL_TestMoreOSL_TestMoreOSLTerminology_h.html
archived_at: '2026-07-18T03:15:53.777612Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoreOSL](MoreOSL.md)


[Next](MoreOSL-TestMoreOSL-TestMoreOSLTerminology.r.md)[Previous](MoreOSL-TestMoreOSL-TestMoreOSL.c.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html%23//apple_ref/doc/uid/TP40002164](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

# MoreOSL/TestMoreOSL/TestMoreOSLTerminology.h

```
/*
    File:       TestMoreOSLTerminology.h

    Contains:   Constants shared between C and Rez

    Written by: Quinn

    Copyright:  Copyright © 2000 by Apple Computer, Inc., all rights reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):

         <2>     20/3/00    Quinn   Comments and various fixes.
         <1>      6/3/00    Quinn   First checked in.
*/

#pragma once

/////////////////////////////////////////////////////////////////

// The creator 'MOSL' has been registered with DTS for this sample.
// I use it in two key places.  Firstly, the test application uses it
// as its creator code.  Secondly, MOSLStringCompare uses it (in the non-Carbon
// implementation) as the class ID of events that it sends to the comparison
// script.  The second use is hardwired to 'MOSL' (because the script
// is compiled that way).  The first use you can change by changing the
// constant below.

#define kMyCreator          'MOSL'
#define kMyAESuite          kMyCreator

// application properties

#define pMyDebug            'MDBG'
#define pMyNextUniqueID     'MNUI'
#define pMyFileValid        'MFLV'
    // All of these properties have explanator comments in
    // the file "TestMoreOSLTerminology.r".

// custom classes

#define cNodeWindow             'NWIN'
#define cAboutWindow            'AWIN'
    // Both of these are subclasses of window.

#define cNode                   'CNDE'
    // Elements of a node window.

// properties of cDocument

#define pMyNodeDisplay          'NDSP'
#define pMyLocationOnDisk       'MLOC'

// properties of cAboutWindow

#define pMyCredits              'CRD'
```

[Next](MoreOSL-TestMoreOSL-TestMoreOSLTerminology.r.md)[Previous](MoreOSL-TestMoreOSL-TestMoreOSL.c.md)

