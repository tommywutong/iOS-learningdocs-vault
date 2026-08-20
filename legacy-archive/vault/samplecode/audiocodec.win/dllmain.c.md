---
title: audiocodec.win
apple_id: DTS10000813
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/audiocodec.win/Listings/dllmain_c.html
archived_at: '2026-07-18T03:28:49.779388Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [audiocodec.win](audiocodec.win.md)


[Next](uLawCodec.h.md)[Previous](README.txt.md)

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

[Next](uLawCodec.h.md)[Previous](README.txt.md)

