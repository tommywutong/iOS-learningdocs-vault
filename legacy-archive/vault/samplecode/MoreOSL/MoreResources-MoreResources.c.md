---
title: MoreOSL
apple_id: DTS10000670
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ApplicationServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoreOSL/Listings/MoreResources_MoreResources_c.html
archived_at: '2026-07-18T03:15:55.206614Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoreOSL](MoreOSL.md)


[Next](MoreResources-MoreResources.h.md)[Previous](MoreQuickDraw-MoreQuickDraw.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html%23//apple_ref/doc/uid/TP40002164](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

# MoreResources/MoreResources.c

```c
/*
    File:       MoreResources.c

    Contains:   Resource Manager utilities

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

         <2>      3/9/00    gaw     API changes for MoreAppleEvents
         <1>      6/3/00    Quinn   First checked in.
*/

/////////////////////////////////////////////////////////////////

// MoreIsBetter Setup

#include "MoreSetup.h"

// Mac OS Interfaces

#include <Resources.h>

// MIB Prototypes

// Our Prototypes

#include "MoreResources.h"

/////////////////////////////////////////////////////////////////
/*

    Returns ResError() or, if itÕs noErr and p is nil,
    returns resNotFound.  The rationale for this routine
    is that, under some documented circumstances, GetResource
    can return nil but not set ResErr.

    pResHdl     input:  a resource handle

    RESULT CODES
    ____________
    Same as results for ResError
    ____________
*/

pascal OSErr MoreResError(const void *pResHdl)
    // See comment in interface part.
{
    OSErr err;

    err = ResError();
    if ((err == noErr) && (pResHdl == nil)) {
        err = resNotFound;
    }
    return err;
}// end MoreResError
/******************************************************************************
    Given an FSSpec to a file, open it with write permission.
    Check to make sure that the file reference returned actually has write
    permission and return an error if it doesn't.

    pFSSpec     input:  The file to be opened.
    pRefNum     output: File reference for the newly opened file.

    RESULT CODES
    ____________
        Same as results for FSpOpenResFile()
    ____________
*/
pascal OSErr MoreResOpenResFileForWrite(const FSSpec *pFSSpec, SInt16 *pRefNum)
{
    OSErr       anErr = noErr;

    *pRefNum = FSpOpenResFile( pFSSpec, fsRdWrPerm );
    if ( *pRefNum == -1 )
    {
        anErr = ResError();
    }
    else    //  Got it open, but can it be written to?
    {
        if ( ! MoreResIsResFileRefNumWritable( *pRefNum ) )
        {
            anErr = permErr;
            CloseResFile( *pRefNum );
            *pRefNum = -1;
        }
    }

    return anErr;
}//end MoreResOpenResFileForWrite
/******************************************************************************
    Utility routine to check that a file opened with read/write permission
    does in fact have read/write permission.

    It is possible to get a read-only file reference for a resource file that has
    been opened with read/write permission.  This routine verify that a file open
    with read/write permission does in fact have write permission.

    pRefNum     input:  File reference number for file to be checked.

    RESULT CODES
    ____________
        true        The resource file was really opened with write permission
        false       It wasn't
    ____________
*/
pascal Boolean MoreResIsResFileRefNumWritable(const SInt16 pRefNum)
{
    FCBPBRec    fcbPB;
    Boolean     result = false;

    fcbPB.ioNamePtr = nil;
    fcbPB.ioVRefNum = 0;
    fcbPB.ioRefNum = pRefNum;
    fcbPB.ioFCBIndx = 0;
    if ( PBGetFCBInfoSync( &fcbPB ) == noErr )
    {
        result = ( (fcbPB.ioFCBFlags & kioFCBWriteMask) != 0 );
    }

    return result;
}//end MoreResIsResFileRefNumWritable
//******************************************************************************
```

[Next](MoreResources-MoreResources.h.md)[Previous](MoreQuickDraw-MoreQuickDraw.h.md)

