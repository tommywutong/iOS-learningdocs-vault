---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_TMemPGPkey_cp.html
archived_at: '2026-07-18T03:18:33.600777Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-TMemPGPkey.h.md)[Previous](sources-TMacException.h.md)

# sources/TMemPGPkey.cp

```c
//  TMemPGPkey.cp - In Memory PGP Key Object  
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

#include "TMemPGPkey.h"
#include "TPGPException.h"

// ---------------------------------------------------------------------------
TMemPGPkey::~TMemPGPkey()
// ---------------------------------------------------------------------------
// 
{
    if(PGPKeySetRefIsValid (fKeySet)) PGPFreeKeySet(fKeySet);
}

// ---------------------------------------------------------------------------
void    TMemPGPkey::Initialize(void* buf, PGPSize bufSize )
// ---------------------------------------------------------------------------
// 
{
    PGPKeySetRef    newKeySet       = NULL;
    PGPUInt32       numKeys;
    PGPKeyListRef   theKeyListRef   = kInvalidPGPKeyListRef;
    PGPKeyIterRef   theIterator     = kInvalidPGPKeyIterRef;
    PGPKeyRef       aKey            = kInvalidPGPKeyRef;
    PGPError        err;

//DebugStr("\pTMemPGPkey::Initialize");

    if(PGPKeySetRefIsValid (fKeySet)) PGPFreeKeySet(fKeySet);

    ThrowIfPGPErr ( PGPImportKeySet(fgContext, &newKeySet, 
                        PGPOInputBuffer( fgContext, buf, bufSize ),
                        PGPOLastOption( fgContext) ));

    ThrowIfPGPErr( PGPCountKeys(newKeySet, &numKeys));
    if(numKeys > 0) 
    {
        Boolean canSign;

        ThrowIfPGPErr( PGPOrderKeySet(newKeySet,kPGPAnyOrdering, &theKeyListRef));
        ThrowIfPGPErr( PGPNewKeyIter( theKeyListRef, &theIterator ));

        while(IsntPGPError (PGPKeyIterNext( theIterator, &aKey )))
        {
//          ThrowIfPGPErr( PGPGetKeyBoolean (aKey, kPGPKeyPropCanSign,  &canSign));
//          if(canSign)
                {
                    fKeySet = newKeySet;
                    TPGPkey::Initialize(aKey);
                    newKeySet = kInvalidPGPKeySetRef;
                    break;
                }
        }

    }
    PGPFreeKeyIter(theIterator );
    PGPFreeKeyList(theKeyListRef );
    if(PGPKeySetRefIsValid (newKeySet)) PGPFreeKeySet(newKeySet);
 }
```

[Next](sources-TMemPGPkey.h.md)[Previous](sources-TMacException.h.md)

