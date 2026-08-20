---
title: PostScript Output Filters
apple_id: DTS10000297
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/PostScript_Output_Filters/Listings/Headers_and_Stub_Libraries_PSOutputFilters_r.html
archived_at: '2026-07-18T03:19:24.647415Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PostScript Output Filters](PostScript%20Output%20Filters.md)


[Next](Headers%20and%20Stub%20Libraries-PSSectionInfo.h.md)[Previous](Headers%20and%20Stub%20Libraries-PSOutputFilters.h.md)

# Headers and Stub Libraries/PSOutputFilters.r

```c
/**
    @name  PSOutputFilters.r
*/

    /**
        @name Introduction
        This file contains rez types for PostScript output filters for LaserWriter 8.
    */

/*
    File:       PSOutputFilters.r

    Contains:   This file contains types and defines for PSSection and PSSubsection data.


    Version:    Technology: PrintingLib 8.7
                Release:    1.0

    Copyright:  © 1999 by Apple Computer Inc. All Rights Reserved.

    Bugs?:      For bug reports, consult the following page on
                the World Wide Web:

                    http://developer.apple.com/bugreporter/
*/

#ifndef __PSOUTPUTFILTERS_R__
#define __PSOUTPUTFILTERS_R__

#ifndef __TYPES_R__
#include "Types.r"
#endif

#ifndef __PSOUTPUTFILTERS__
#include "PSOutputFilters.h"                    
#endif

type kPanelDescriptionType {
    integer = $$Countof(Checkboxes);            /// numCheckboxes
    wide array Checkboxes {
        integer;                                /// dlgItem
    };
    integer = $$Countof(Rads);                  /// numRadios
    wide array Rads {
        integer;                                /// radsFrom
        integer;                                /// radsTo
    };

};

type kPluginInfoType {
        hex string;             /* Data*/
};


#endif      
```

[Next](Headers%20and%20Stub%20Libraries-PSSectionInfo.h.md)[Previous](Headers%20and%20Stub%20Libraries-PSOutputFilters.h.md)

