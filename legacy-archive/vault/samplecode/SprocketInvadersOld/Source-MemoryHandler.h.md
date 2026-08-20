---
title: SprocketInvadersOld
apple_id: DTS10000061
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SprocketInvadersOld/Listings/Source_MemoryHandler_h.html
archived_at: '2026-07-18T03:25:26.889138Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SprocketInvadersOld](SprocketInvadersOld.md)


[Next](Source-MenuHandler.c.md)[Previous](Source-MemoryHandler.c.md)

# Source/MemoryHandler.h

```c
//¥ ------------------------------------------------------------------------------------------  ¥
//¥
//¥ Copyright © 1996 Apple Computer, Inc., All Rights Reserved
//¥
//¥
//¥     You may incorporate this sample code into your applications without
//¥     restriction, though the sample code has been provided "AS IS" and the
//¥     responsibility for its operation is 100% yours.  However, what you are
//¥     not permitted to do is to redistribute the source as "DSC Sample Code"
//¥     after having made changes. If you're going to re-distribute the source,
//¥     we require that you make it clear in the source that the code was
//¥     descended from Apple Sample Code, but that you've made changes.
//¥
//¥     Authors:
//¥         Chris De Salvo
//¥
//¥ ------------------------------------------------------------------------------------------  ¥

#ifndef __MEMHANDLER__
#define __MEMHANDLER__

//¥ ------------------------------  Includes

#include <Controls.h>
#include <Dialogs.h>
#include <Lists.h>
#include <Palettes.h>
#include <QDOffscreen.h>

//¥ ------------------------------  Public Definitions
//¥ ------------------------------  Public Types
//¥ ------------------------------  Public Variables
//¥ ------------------------------  Public Functions

#ifdef __cplusplus
extern "C" {
#endif

extern Boolean IsResourceHandle(Handle theHandle);
extern Boolean IsLockedHandle(Handle theHandle);

extern void DisposeControlZ(ControlHandle *theControl);
extern void DisposeWindowZ(WindowRef *theWindow);
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

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Source-MenuHandler.c.md)[Previous](Source-MemoryHandler.c.md)

