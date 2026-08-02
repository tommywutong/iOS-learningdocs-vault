---
title: DTSCPlusLibrary
apple_id: DTS10000731
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/DTSCPlusLibrary/Listings/Sources_SpinCursor_cp.html
archived_at: '2026-07-18T03:05:59.123875Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DTSCPlusLibrary](DTSCPlusLibrary.md)


[Next](Sources-SpinCursorTest.cp.md)[Previous](Sources-SoundClassTest.cp.md)

# Sources/SpinCursor.cp

```c
/*
    File:       SpinCursor.cp

    Contains:   TSpinCursor is a simple cursor spinning class.
                SpinCursor.cp contains the TSpinCursor member functions.


    Written by: Kent Sandvik    

    Copyright:  Copyright © 1992-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/18/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#ifndef _SPINCURSOR_
#include "SpinCursor.h"
#endif


//  CONSTRUCTORS AND DESTRUCTORS
#pragma segment SpinCursor
TSpinCursor::TSpinCursor(short acurID,
                         short spinDirection,
                         short spinTicks)
// Default constructor, bind 'acur' and class together by specifying used 'acur' resource.
{
    fCursorHandle = NULL;
    fSpinDirection = spinDirection;
    fTickCounter = 0;
    fSpinTicks = spinTicks;                     // how many ticks between spins

    fCursorList = (AnimationCursRec * *)::GetResource('acur', acurID);
    fError = ::ResError();
    VASSERT(fError == noErr, ("Problems with GetResource = %d", fError));

    if (fCursorList != NULL)
    {
        ::HNoPurge((Handle)fCursorList);        // don't purge this resource during use!

        for (fIndex = 0; fIndex < (**fCursorList).information.count; fIndex++)
        {
            fCursorID = HiWord(((**fCursorList).nCursors[fIndex]));
            fCursorHandle = ::GetCursor(fCursorID);
            ASSERT(fCursorHandle != NULL, "\pGetCursor returned NULL handle");

            (**fCursorList).nCursors[fIndex] = fCursorHandle;

            if (fCursorHandle != NULL)
                ::HNoPurge((Handle)fCursorHandle);// make every CURS handle non-purgeable
        }
    }
}


#pragma segment SpinCursor
TSpinCursor::~TSpinCursor()
// Clean up after the spinning, handles and suchÉ
{
    CursHandle tempHandle;
    short index;

    if (fCursorList != NULL)                    // sanity check
    {
        for (index = 0; index < (**fCursorList).information.count; index++)
        {
            tempHandle = (**fCursorList).nCursors[index];
            if (tempHandle != NULL)
                ::HPurge((Handle)tempHandle);
        }
        ::ReleaseResource((Handle)fCursorList); // don't dispose resources
        fError = ResError();
        VASSERT(fError == noErr, ("Problems with ReleaseResource = %d", fError));
    }
}


// MAIN INTERFACE

#pragma segment SpinCursor
void TSpinCursor::Spin()
// Spin the cursor once (next frame) into earlier defined direction.
{
    long ticks;                                 // temp value
    short count;                                // # of animated cursors
    short frameNum;                             // # of frame

    if (fCursorList != NULL)                    // sanity check
    {
        ticks = ::TickCount();                  // get the stamp

        if ((ticks - fTickCounter) > fSpinTicks)// enough ticks between spins?
        // Éthen spin, change new cursor, increase the frame count (next CURS),
        // and save the new tick stamp.
        {
            count = (**fCursorList).information.count;
            frameNum = (**fCursorList).frame % count;
            fCursorHandle = (**fCursorList).nCursors[frameNum];

            if (fCursorHandle != NULL)          // sanity check
            {
                ::HLock((Handle)fCursorHandle); // lock the resource
                ::SetCursor(&(**fCursorHandle));// set the new CURS
                ::HUnlock((Handle)fCursorHandle);// unlock it
            }
            (**fCursorList).frame = (frameNum + count + fSpinDirection) % count;
        }
    }
}

#pragma segment SpinCursor
void TSpinCursor::SetSpinDirection(EDirection direction)
// Set direction of spin, -1 backwards, 1 = forwardsÉ
{
    fSpinDirection = direction;
}


// _________________________________________________________________________________________________________ //


/*  Change History (most recent last):
  No        Init.   Date        Comment
  1         khs     12/14/92    New file
  2         khs     1/3/93      Cleanup
*/
```

[Next](Sources-SpinCursorTest.cp.md)[Previous](Sources-SoundClassTest.cp.md)

