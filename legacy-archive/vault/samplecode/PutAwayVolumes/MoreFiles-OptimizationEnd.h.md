---
title: PutAwayVolumes
apple_id: DTS10000043
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PutAwayVolumes/Listings/MoreFiles_OptimizationEnd_h.html
archived_at: '2026-07-18T03:19:40.415891Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PutAwayVolumes](PutAwayVolumes.md)


[Next](PutAwayOneVolume.c.md)[Previous](MoreFiles-Optimization.h.md)

# MoreFiles/OptimizationEnd.h

```
/*
    File:       OptimizationEnd.h

    Description:The Optimization changes to MoreFiles source and header files, along with
                this file and Optimization.h, let you optimize the code produced by MoreFiles
                in several ways.

    Author:     FO

    Copyright:  Copyright: © 1992-1999 by Apple Computer, Inc.
                all rights reserved.

    Disclaimer: You may incorporate this sample code into your applications without
                restriction, though the sample code has been provided "AS IS" and the
                responsibility for its operation is 100% yours.  However, what you are
                not permitted to do is to redistribute the source as "DSC Sample Code"
                after having made changes. If you're going to re-distribute the source,
                we require that you make it clear in the source that the code was
                descended from Apple Sample Code, but that you've made changes.

    Change History (most recent first):
                6/25/99 Updated for Metrowerks Codewarror Pro 2.1(KG)
*/


#if __USEPRAGMAINTERNAL
    #if defined(__MWERKS__)
        #pragma internal reset
    #endif
#endif


#if __WANTPASCALELIMINATION
    #ifndef __COMPILINGMOREFILES
        #undef pascal
    #endif
#endif
```

[Next](PutAwayOneVolume.c.md)[Previous](MoreFiles-Optimization.h.md)

