---
title: AIFFWriter
apple_id: DTS10000904
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AIFFWriter/Listings/dllmain_c.html
archived_at: '2026-07-18T02:59:39.258589Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AIFFWriter](AIFFWriter.md)


[Next](MacDebugPrefix.h.md)[Previous](AIFFWriter.r.md)

# dllmain.c

```c
//////////
//
//  File:       dllmain.c
//
//  Contains:   Code for creating a sound output component.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      03/05/99    rtm     first file
//
//////////

#include <QTML.h>
#include <windows.h>


static HINSTANCE    ghInst = 0;

BOOL WINAPI dllMain (HANDLE hInst, ULONG ul_reason_for_call, LPVOID lpReserved)
{
    ghInst = hInst;

    switch (ul_reason_for_call) {
        case DLL_PROCESS_ATTACH:
            break;

        case DLL_THREAD_ATTACH:
            break;

        case DLL_THREAD_DETACH:
            break;

        case DLL_PROCESS_DETACH:
            break;
    }

    return(true);
}
```

[Next](MacDebugPrefix.h.md)[Previous](AIFFWriter.r.md)

