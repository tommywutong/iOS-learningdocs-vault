---
title: Color Animated Cursors
apple_id: DTS10002189
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tb/tb03.html
archived_at: '2026-07-18T02:38:55.031505Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB03Color Animated Cursors |

|  |
| --- |
| Q Is there any way the routines in "CursorCtl.h" (Universal Headers) can be made to work with color cursors rather than black and white ones? If not, why not?   A The routines in "CursorCtl.h" can be made to work with color cursors. The routines in "CursorCtl.h" use an interrupt handler to animate the cursor. One advantage of this technique is that it allows the cursor to animate smoothly while some time-consuming routine does its thing.  There are, however, two key problems with this approach. One is that the cursor will continue to animate even if the time-consuming routine has crashed. This means the user won't get any feedback that something has gone wrong, which is the main motivation for animating the cursor to begin with.  The other problem is that the interrupt handler must not do anything which will move memory. Because setting a color cursor can move memory, there is no safe way to animate color cursors with this technique.  So if you want to animate color cursors, then you'll need to do it in a subroutine instead of an interrupt handler. This means that your time-consuming routine may need to be reorganized a bit, so that it can call a cursor animation routine periodically.  Here is a snippet of code your routine can call.   ``` #include <QuickDraw.h> #include <Resources.h> #include <Memory.h> #include <Events.h> #include <ToolUtils.h> #include <Desk.h> #include <DiskInit.h>  static Boolean          gUseColorCursors;       // If true, spinning cursors are                                                 // crsrs, not CURSs. static ACurHdl          gACur;                  // Spinning cursors' 'acur' resource. static Handle           gCursor[kMaxNumCursors];// Handles of cursors to spin. static short            gFinalCursorID;         // Cursor ID to use when done spinning. static unsigned long    gTicksLastCursor;       // TickCount when we last spun cursors.  //----------------------------------------------------------------------- //  SetUpCursors - This routine does initialization for the //  animated cursor routines BumpCursor and TearDownCursors. // //  The caller passes in the resource ID of an 'acur' reource, //  and this routine loads the related cursors.  Finally, //  it calls BumpCursor to start using the first cursor. // //  We attempt to load 'crsr' resources if they're available. //  If not, we use 'CURS' ones.  That's so we can use color //  cursors if they're around. // //  finalCursorID is the ID of the cursor to use when we're //  all done (in TearDownCursors).  It may be: // //  * kArrowCursor - for the arrow cursor. // //    * or a valid ID of a 'crsr' or 'CURS' resource. //      (TearDownCursors tries for a 'crsr' first.) // //  void SetUpCursors(short acurID, short finalCursorID) {     short    oldRes, cu;      // Save the current resource file, then switch to our     // application's, get the requested 'acur' resource and store     // the resource ID of the cursor we should use in     // TearDownCursors.      oldRes = CurResFile();     UseResFile(gAppResRefNum);      gACur = (ACurHdl) GetResource('acur', acurID);     gFinalCursorID = finalCursorID;       // If we loaded the resource, detach it and get, load and     // detach each cursor it points to.  We store the cursors     // in global handles so that we can easily access them.  If     // the acur resource references more cursors than we've     // allocated space for, then we just use as many as we can     // handle.  Note that we try to load 'crsr' resources first,     // and if that fails we try 'CURS' resoruces.  That's so we     // can use color cursors if they're available.      if (gACur != nil)     {         gUseColorCursors = true;          DetachResource((Handle) gACur);         (*gACur)->numCursors = (*gACur)->numCursors ;         if( kMaxNumCursors < (*gACur)->numCursors)             (*gACur)->numCursors = kMaxNumCursors ;          for (cu = 0; cu < (*gACur)->numCursors; cu++)         {             if (gUseColorCursors)             {                 gCursor[cu] = (Handle) GetCCursor((*gACur)->cursID[cu] >>16);                 if ((cu == 0) && (gCursor[cu] == nil))                     gUseColorCursors = false;             }              if (!gUseColorCursors)             {                 gCursor[cu] = (Handle) GetCursor((*gACur)->cursID[cu] >>16);                  // We need to lock the non-color cursors because we have to                 // dereference their handle for SetCursor.                  if (gCursor[cu])                 {                     MoveHHi(gCursor[cu]);                     HLock(gCursor[cu]);                 }             }              if (gCursor[cu] != nil)                 DetachResource((Handle) gCursor[cu]);         }          // Set the "next frame" counter and the "tick count when         // we last changed cursors" to 0.  That's so that we'll         // immediately display the first cursor, which we do by         // calling BumpCursor.  Finally, restore the old         // resource file.          (*gACur)->nextFrame = gTicksLastCursor = 0;         BumpCursor();     }     UseResFile(oldRes); }   //---------------------------------------------------------------- //  BumpCursor - This routine displays the next cursor in our //  animated cursor list (from the 'acur' resource whose ID //  we passed to SetUpCursors.  void BumpCursor() {     register short          curFrame;     register unsigned long  numTicks;      // If there's an 'acur' resource loaded and we're in the foreground,     // see if we should change cursors.  If so, (if the time that's passed     // since the last change is at least kMinCursorTicks) store the new tick     // count, grab the next cursor to use and bump the frame counter.      if (gACur != nil && !gInBackground)     {         numTicks = TickCount();         if ((numTicks - gTicksLastCursor) < kMinCursorTicks)             return;          gTicksLastCursor = numTicks;         curFrame = (*gACur)->nextFrame;         (*gACur)->nextFrame = ++(*gACur)->nextFrame % (*gACur)->numCursors;          // Call the appropriate SetCursor" call, based on whether we have color         // or black and white cursors loaded.  Non-color cursors will be locked.          if (gCursor[curFrame] != nil)         {             if (gUseColorCursors)                 SetCCursor((CCrsrHandle) gCursor[curFrame]);             else                 SetCursor(*(CursHandle) gCursor[curFrame]);         }     } }   //--------------------------------------------------------------- //  TearDownCursors - This routine undoes what SetUpCursors //  did.  It disposes of any loaded handles and sets the //  cursor to the cursor having the ID stored in //  gFinalCursorID, which is where SetUpCursors stores the //  final cursor's resource ID.   void TearDownCursors() {     short        numCursors, cu;     Handle        newCursor;      // If we have cursors loaded, go through and dispose of them all, and     // their accompanying 'acur' resource.  Note that these aren't really     // resources, since we called DetachResource on them earlier.      if (gACur != nil)     {         numCursors = (*gACur)->numCursors;          for (cu = 0; cu < numCursors; cu++)         {             if (gCursor[cu]) DisposHandle((Handle) gCursor[cu]);             gCursor[cu] = nil;         }          DisposHandle((Handle) gACur);         gACur = nil;     }      // If we didn't get switched into the background, set the cursor to     // whatever is in gFinalCursor.  If it's kArrowCursor, we use the     // global arrow cursor (which doesn't have an ID).  We look for a     // 'crsr' first, and if that's not found, try to load a 'CURS'.      if (gFinalCursorID == kArrowCursor && !gInBackground)         SetCursor(&qd.arrow);     else     {         newCursor = (Handle) GetCCursor(gFinalCursorID);          if (newCursor != nil && !gInBackground)             SetCCursor((CCrsrHandle) newCursor);         else         {             newCursor = (Handle) GetCursor(gFinalCursorID);              if (newCursor != nil && !gInBackground)                 SetCursor(*(CursHandle) newCursor);         }     } } ```  [May 01 1995] |

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
