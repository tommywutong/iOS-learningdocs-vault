---
title: Bitblitz
apple_id: DTS10000066
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/Bitblitz/Listings/LibHeaders_AutoCursor_h.html
archived_at: '2026-07-18T03:01:55.241229Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Bitblitz](Bitblitz.md)


[Next](LibHeaders-ColorTools.h.md)[Previous](LibHeaders-AlrtDlogTools.h.md)

# LibHeaders/AutoCursor.h

```
#ifndef __AUTOCURSOR__
#define __AUTOCURSOR__

/*---------------------------------------------------------------------------------------
//  File:       AutoCursor.h
//  Date:       July 12, 1989
//
//  Mods:       Apr  16, 1990        JMP        Completely revised.
//
//  By Mike Puckett, Macintosh CPU Software Quality, x4-1332.
//  ©Ê1989 - 1990, Apple Computer, Inc.
//---------------------------------------------------------------------------------------
*/

/* Data Structures ----------------------------------------------------------------------
*/
typedef struct ACRecord                         /* ACRecord is NOT public at this time. */
*AutoCursor;

#define kACMinThreshTicks   60L                 /* For some machines, <1 sec looks bad. */
#define kACStdThreshTicks   120L                /* About every 2 seconds.               */
#define kACStdSpinTicks     12L                 /* About every 1/5th second.            */

#define rACStdACURID        (short)256          /* Seemed like a good number to me.     */

/* The WaitNextEvent yield time should be SOMEWHAT less than the threshold value,
// otherwise the timer will go off too soon and the animation will kick in when
// the app is NOT busy.  The following formula seems to work pretty well when
// tt >= 120L (tt is threshold ticks).
*/
#define AC_WNE_YIELD(tt)    ((tt) >> 2)

/* Constants for use with AutoCursorCommand()É
*/
enum
{   acUpdtThreshTicks = 1,
    acUpdtSpinTicks,
    acGetThreshTicks,
    acGetSpinTicks,
    acForceBusy,
    acForceIdle
    };

/* AutoCursorCommand() MacrosÉ
*/
#define AC_GETTHRESTICKS    acGetThreshTicks,   nil
#define AC_GETSPINTICKS     acGetSpinTicks,     nil
#define AC_FORCEBUSY        acForceBusy,        nil
#define AC_FORCEIDLE        acForceIdle,        nil

/* The Routines  ------------------------------------------------------------------------
*/
#ifdef __safe_link
extern "C" {
#endif

extern pascal   AutoCursor      InstAutoCursor(     short           acurRsrcID,
                                                    unsigned long   threshTicks,
                                                    unsigned long   spinTicks);

extern pascal   void            PrmeAutoCursor(     AutoCursor      autoCursor);
extern pascal   void            RmveAutoCursor(     AutoCursor      autoCursor);

extern pascal   void            ImmedAutoCursor(    AutoCursor      autoCursor);

extern pascal   void            SuspendAutoCursor(  AutoCursor      autoCursor);
extern pascal   void            ResumeAutoCursor(   AutoCursor      autoCursor);

extern pascal   long            AutoCursorCommand(  AutoCursor      autoCursor,
                                                    short           acCommand,
                                                    long            acParam);


#ifdef __safe_link
}
#endif
#endif /* __AUTOCURSOR__ */
```

[Next](LibHeaders-ColorTools.h.md)[Previous](LibHeaders-AlrtDlogTools.h.md)

