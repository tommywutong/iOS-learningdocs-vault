---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_ASIPChallenge_h.html
archived_at: '2026-07-18T03:18:29.804567Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-clientUAMGlue.c.md)[Previous](sources-ASIPChallenge.cp.md)

# sources/ASIPChallenge.h

```c
//  ASIPChallenge.h - base class for Appleshare IP Challenge Object
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

#ifndef _H_TASIPCHALLENGE
#define _H_TASIPCHALLENGE

#include "TPGPkey.h"

void    MakeChallenge(TPGPkey *, StringPtr outBuf);

void    ReplyToChallenge(TPGPkey *serverKey, const char *passPhrase, TPGPkey *clientKey, StringPtr inBuf, StringPtr outBuf);

Boolean VerifyChallenge(TPGPkey *, StringPtr origChallenge, StringPtr inBuf);

PGPError ReplyToCounterChallenge(StringPtr promptString, StringPtr fpBuf, StringPtr inBuf, StringPtr outBuf);

Boolean VerifyCounterChallenge(TPGPkey *theKey, StringPtr origCounterChallenge, StringPtr inBuf);


#endif
```

[Next](sources-clientUAMGlue.c.md)[Previous](sources-ASIPChallenge.cp.md)

