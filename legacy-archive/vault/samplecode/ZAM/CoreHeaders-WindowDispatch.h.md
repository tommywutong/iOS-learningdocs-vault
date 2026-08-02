---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/CoreHeaders_WindowDispatch_h.html
archived_at: '2026-07-18T03:28:31.907836Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](CoreSource-AdjustMenus.c.md)[Previous](CoreHeaders-MenuDispatch.h.md)

# CoreHeaders/WindowDispatch.h

```
#pragma once

typedef Boolean (*wProcPtr)(WindowPeek wp, Handle data);

typedef struct {
    wProcPtr    updateProc;
    wProcPtr    clickProc;
    wProcPtr    closeProc;
    wProcPtr    keyProc;
    wProcPtr    saveProc;
    wProcPtr    adjustMenuProc;
    wProcPtr    idleProc;
    long        wFlags;
    Handle      data;
}  wDispRec, **wDispHandle;

#define GetWDisp(wp)    (wDispHandle)GetWRefCon(wp)

#define kDispWindowKind 128

Handle  GetWData(WindowPtr  wp);
void SetWData(WindowPtr wp, Handle data);
WindowPtr NewDispatchWindow(short ID);
```

[Next](CoreSource-AdjustMenus.c.md)[Previous](CoreHeaders-MenuDispatch.h.md)

