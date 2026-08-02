---
title: PostScript Output Filters
apple_id: DTS10000297
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/PostScript_Output_Filters/Listings/SectionReport_SectionReport_r.html
archived_at: '2026-07-18T03:19:29.224001Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PostScript Output Filters](PostScript%20Output%20Filters.md)


[Next](SectionReport-Version.h.md)[Previous](SectionReport-SectionReport.c.md)

# SectionReport/SectionReport.r

```c
/*
**  File:           SectionReport.r
**
**  Description:    Resources for the SectionReport filter.
**
**  Version:        1.0
**
**  Copyright 1999 Apple Computer. All rights reserved.
**
**  You may incorporate this sample code into your applications without
**  restriction, though the sample code has been provided "AS IS" and the
**  responsibility for its operation is 100% yours.  However, what you are
**  not permitted to do is to redistribute the source as "ABC Sample Code"
**  after having made changes. If you're going to re-distribute the source,
**  we require that you make it clear in the source that the code was
**  descended from Apple Sample Code, but that you've made changes.
**
*/

#include "SysTypes.r"
#include "Types.r"

#include "Version.h"
#include "PrintingPlugins.r"
#include "PSOutputFilters.r"

#if qDebug
#define filterCFMName   "SectionReport.debug"
#else
#define filterCFMName   "SectionReport"
#endif

resource kPluginResourceInfoType (kPluginResourceInfoID,
#if qNames
    "Plug-In Info",
#endif
    purgeable) {
    {
        // There needs to be an entry here for each plug-in which is built into our file.

        kPSOutputFilterPlugInType, kPSOutputFilterSubtype, filterCFMName,       
    }   
};


//Put correct verion into string.
resource 'vers' (1, purgeable) {
    kMajorRev,
    kMinorRev,
    kReleaseStage,
    kNonRelease,
    verUS,
    kShortVersStr
        #if qDebug              // lets see how we built it.
            kqDebug
        #endif
        #if qSym
            kqSym
        #endif
        #if qNames
            kqNames
        #endif
        ,
    kShortVersStr 
    ", © 1999 Apple Computer Incorporated "

        #if qDebug              // lets see how we built it.
            kqDebug
        #endif
        #if qSym
            kqSym
        #endif
        #if qNames
            kqNames
        #endif
};

resource kPluginInfoType (kPluginInfoID,
#if qNames
    "Plugin Info String",
#endif
    purgeable) {
    "This filter generates a log file with all the subsection information that passes through this filter. The log file has a .dsc suffix and is written to your Job Documentation Folder."
};
```

[Next](SectionReport-Version.h.md)[Previous](SectionReport-SectionReport.c.md)

