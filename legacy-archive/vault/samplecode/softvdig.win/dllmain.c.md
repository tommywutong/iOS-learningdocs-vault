---
title: softvdig.win
apple_id: DTS10000335
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-08-29'
source_url: https://developer.apple.com/library/archive/samplecode/softvdig.win/Listings/dllmain_c.html
archived_at: '2026-07-26T19:52:28.154030Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [softvdig.win](softvdig.win.md)


[Next](softVdig.c.md)[Previous](README.txt.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# dllmain.c

```c
#include "windows.h"

static HINSTANCE    ghInst=0;

/* ----------------------------------------------------------- */

BOOL WINAPI DllMain(HANDLE hInst, ULONG ul_reason_for_call, LPVOID lpReserved)
{
    ghInst = hInst;

    switch( ul_reason_for_call ) {
        case DLL_PROCESS_ATTACH:
            break;

        case DLL_THREAD_ATTACH:
            break;

        case DLL_THREAD_DETACH:
            break;

        case DLL_PROCESS_DETACH:
            break;
    }
    return TRUE;
}

/* ----------------------------------------------------------- */
```

[Next](softVdig.c.md)[Previous](README.txt.md)

