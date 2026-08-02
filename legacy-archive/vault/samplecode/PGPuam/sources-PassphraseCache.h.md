---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_PassphraseCache_h.html
archived_at: '2026-07-18T03:18:33.089556Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-PGPServerMemory.cp.md)[Previous](sources-PassphraseCache.c.md)

# sources/PassphraseCache.h

```c
//  PassphraseCache.h -  Passphrase Cache Interface Object  
// 
// Apple Macintosh Developer Technical Support
// Written by:  Vinnie Moscaritolo
//
//  Copyright (work in progress)  Apple Computer, Inc All rights reserved.
//
// You may incorporate this sample code into your applications without
// restriction, though the sample code has been provided "AS IS" and the
// responsibility for its operation is 100% yours.  However, what you are
// not permitted to do is to redistribute the source as "DSC Sample Code"
// after having made changes. If you're going to re-distribute the source,
// we require that you make it clear in the source that the code was
// descended from Apple Sample Code, but that you've made changes.
// 

#pragma once

#define PGP_MACINTOSH 1
#include "pgpkeys.h"


#ifdef __cplusplus
extern "C" {
#endif

    void     FlushPassphraseCache();

    void     SetPassphraseCacheTimeLimit( SInt16 mins);

    void     EnablePassphraseCaching( Boolean );

    void     RememberPassphrase (PGPKeyRef  keyRef, const char* passphrase);        

    Boolean  GetPassphrase      (PGPContextRef, PGPKeyRef, char** passphrase);      

#ifdef __cplusplus
}
#endif
```

[Next](sources-PGPServerMemory.cp.md)[Previous](sources-PassphraseCache.c.md)

