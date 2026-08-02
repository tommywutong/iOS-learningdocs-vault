---
title: PostScript Output Filters
apple_id: DTS10000297
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/PostScript_Output_Filters/Listings/SampleFilter_LibraryStuff_PrintingPlugins_r.html
archived_at: '2026-07-18T03:19:26.739565Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PostScript Output Filters](PostScript%20Output%20Filters.md)


[Next](SampleFilter-LibraryStuff-PSOutputFilters.h.md)[Previous](SampleFilter-LibraryStuff-PrintingPlugins.h.md)

# SampleFilter/LibraryStuff/PrintingPlugins.r

```c
/**
    @name PrintingPlugins.r
*/

    /**
        @name Introduction
        This documentation lists the Rez types required for creating Printing Plug-ins.
    */

/*
    File:       PrintingPlugins.r

    Contains:   Rez types needed for creating Printing Plug-ins.

    Version:    Technology: PrintingLib 8.6.5
                Release:    1.0

    Copyright:  © 1999 by Apple Computer Inc. All Rights Reserved.

    Bugs?:      For bug reports, consult the following page on
                the World Wide Web:
                    http://developer.apple.com/bugreporter/
*/

#ifndef __PRINTINGPLUGINS_R__
#define __PRINTINGPLUGINS_R__

#ifndef __TYPES_R__
#include "Types.r"
#endif

#ifndef __PrintingPlugins__
#include "PrintingPlugins.h"                    
#endif

/**
    @name #kPluginResourceInfoType#

    The kPluginResourceInfoType resource describes all the printing plug-ins contained within
    a given file. Since a given file can contain multiple plug-ins, the resource contains a count
    of the number of plug-ins within the file containing this resource and a 'LibInfo' for each
    of those plug-ins.
*/

    /** kPluginResourceInfoType */
    type kPluginResourceInfoType{
        /// number of plug-ins this file contains 
        integer = $$Countof(LibInfo);
        /// LibInfo arraqy
        wide array LibInfo {
            /// 'Type' of plug-in described by this LibInfo 
            unsigned longint;
            /// 'SubType' of plug-in described by this LibInfo 
            unsigned longint;                       
            ///  Fragment name of plug-in described by this LibInfo         
            pstring;
            /// word
            align word;
        };
    };



#endif      /* __PRINTINGPLUGINS_R__ */
```

[Next](SampleFilter-LibraryStuff-PSOutputFilters.h.md)[Previous](SampleFilter-LibraryStuff-PrintingPlugins.h.md)

