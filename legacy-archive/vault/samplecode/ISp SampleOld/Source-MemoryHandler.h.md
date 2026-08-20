---
title: ISp SampleOld
apple_id: DTS10000056
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/ISp_SampleOld/Listings/Source_MemoryHandler_h.html
archived_at: '2026-07-18T03:12:10.087855Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ISp SampleOld](ISp%20SampleOld.md)


[Next](Source-MenuHandler.cp.md)[Previous](Source-MemoryHandler.c.md)

# Source/MemoryHandler.h

```c
/*
    File:       MemoryHandler.h

    Contains:   xxx put contents here xxx

    Version:    xxx put version here xxx

    Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                xxx put dri here xxx

        Other Contact:      xxx put other contact here xxx

        Technology:         xxx put technology here xxx

    Writers:

        (BWS)   Brent Schorsch

    Change History (most recent first):

       <SP1>      7/1/99    BWS     first checked in
*/

#ifndef __MEMHANDLER__
#define __MEMHANDLER__

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Includes

#ifndef __CONTROLS__
#include <Controls.h>
#endif

#ifndef __LISTS__
#include <Lists.h>
#endif

#ifndef __PALETTES__
#include <Palettes.h>
#endif

#ifndef __QDOFFSCREEN__
#include <QDOffscreen.h>
#endif

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Definitions
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Types
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Variables
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Functions

#ifdef __cplusplus
extern "C" {
#endif

extern Boolean IsResourceHandle(Handle theHandle);
extern Boolean IsLockedHandle(Handle theHandle);

extern void DisposeControlZ(ControlHandle *theControl);
extern void DisposeWindowZ(WindowPtr *theWindow);
extern void DisposeDialogZ(DialogPtr *theDialog);
extern void DisposeGWorldZ(GWorldPtr *theGWorld);
extern void DisposePaletteZ(PaletteHandle *thePal);

extern void KillPictureZ(PicHandle *thePicture);

extern void DisposePtrZ(Ptr *thePtr);
extern void DisposeHandleZ(Handle *theHandle);

extern void TEDisposeZ(TEHandle *theHandle);
extern void LDisposeZ(ListHandle *theHandle);

extern void PurgeAndCompactMem(void);

extern Ptr NewTaggedPtr(Size size, OSType tag, UInt32 refCon);
extern Ptr NewTaggedPtrClear(Size size, OSType tag, UInt32 refCon);
extern void DisposeTaggedPtr(Ptr thePtr);
extern void DisposeTaggedPtrZ(Ptr *thePtr);

extern UInt32 GetAllocatedRam(void);

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Source-MenuHandler.cp.md)[Previous](Source-MemoryHandler.c.md)

