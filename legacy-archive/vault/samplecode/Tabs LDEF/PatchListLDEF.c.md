---
title: Tabs LDEF
apple_id: DTS10000621
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/Tabs_LDEF/Listings/PatchListLDEF_c.html
archived_at: '2026-07-18T03:26:18.958981Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabs LDEF](Tabs%20LDEF.md)


[Next](Prototypes.h.md)[Previous](Menus.c.md)

# PatchListLDEF.c

```c
/*
    File:       PatchListLDEF.c

    Contains:   

    Written by:     

    Copyright:  Copyright © 1995-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/10/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
// System includes

#ifndef __TYPES__
    #include <Types.h>
#endif

#ifndef __LISTS__
    #include <Lists.h>
#endif

#ifndef __OSUTILS__
    #include <OSUtils.h>
#endif


// Application includes

#ifndef __BAREBONES__
    #include "BareBones.h"
#endif


#ifndef USE_LDEF


pascal void tabsLDEF ( short theMessage, short selFlags, Rect* theRect, Cell theCell,
                            short theOffset, short theLen, ListRef theHandle );





#if GENERATINGPOWERPC
#pragma options align=mac68k
#endif


#if GENERATINGCFM
typedef struct
{
    RoutineDescriptor   routineDescriptor;

} LDEFPatch, *LDEFPatchPtr, **LDEFPatchHndl;
#else
typedef struct
{
    short   jmpInst;
    ProcPtr patchAddr;

} LDEFPatch, *LDEFPatchPtr, **LDEFPatchHndl;
#endif

#if GENERATINGPOWERPC
#pragma options align=reset
#endif






OSErr PatchListLDEF ( ListRef theList );


OSErr PatchListLDEF ( ListRef theList )
{
    OSErr               theErr;
    LDEFPatchHndl       ldefHndl;
    LDEFPatchPtr        ldefPatch;
    RoutineDescriptor   initializedRD = BUILD_ROUTINE_DESCRIPTOR ( uppListDefProcInfo,
                                                                    tabsLDEF );

    ldefHndl = (LDEFPatchHndl) NewHandle ( sizeof ( LDEFPatch ) );
    theErr = MemError ( );
    if ( theErr )
        return theErr;

    HLock ( (Handle) ldefHndl );
    ldefPatch = *ldefHndl;

#if GENERATINGCFM
    ldefPatch->routineDescriptor = initializedRD;
#else
    ldefPatch->jmpInst = 0x4EF9;                    // a 68K JMP instruction
    ldefPatch->patchAddr = (ProcPtr) tabsLDEF;      // where we want to jmp
#endif

    HUnlock ( (Handle) ldefHndl );
    (*theList)->listDefProc = (Handle) ldefHndl;

    return noErr;
}


#endif
```

[Next](Prototypes.h.md)[Previous](Menus.c.md)

