---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TCachedStorage_cp.html
archived_at: '2026-07-18T03:11:58.951047Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TCachedStorage.h.md)[Previous](%E2%80%A2OTClasses-TAddrInet.h.md)

# •OT_Classes/TCachedStorage.cp

```c
//  TCachedStorage.cp - custom memory  managemnent
// 
// Apple Macintosh Developer Technical Support
// Written by:  Vinne Moscaritolo
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

#include "TCachedStorage.h"


// ===========================================================================
//  Static member variables
// ===========================================================================
TList                   TStorageManager::fgPurgeList;   // List of stacks
TStorageManager::Init   TStorageManager::fgInit;        // Storage manager Init object


struct TPurgeHandler : public TLink
{
    TPurgeHandler(TLifo* theCache) : fCacheList(theCache) {};
    TLifo* fCacheList;
};

// ---------------------------------------------------------------------------
//   TStorageManager::Init::~Init
// ---------------------------------------------------------------------------
//  Destructor.   cleans up after storage manager was used

TStorageManager::Init::~Init(void)
{
    TPurgeHandler *purgeObject;

// Free up all Stacks
    TStorageManager::Purge();

// dispose of any Handlers..
// BUG ****
//  while( purgeObject = (TPurgeHandler*) fgPurgeList.RemoveFirst() ) 
//          delete purgeObject;
}


// ---------------------------------------------------------------------------
//   TStorageManager::Register( theCache )
// ---------------------------------------------------------------------------
//  Register cache Purge Object 
//

void TStorageManager::Register( TLifo* theCache )
 {
   fgPurgeList.Add((TLink*) new TPurgeHandler(theCache) );
 }

// ---------------------------------------------------------------------------
//  UnRegister( theCache )
// ---------------------------------------------------------------------------
//  UnRegister cache Purge Object 
//

void TStorageManager::UnRegister( TLifo* theCache )
 {
   fgPurgeList.Remove((TLink*)theCache); 
 }

// ---------------------------------------------------------------------------
//   TStorageManager::Purge()
// ---------------------------------------------------------------------------
//  Purge all cache registered areas
//

void TStorageManager::Purge()
{
    TPurgeHandler *purgeObject;
             void *deadObject;

    for(purgeObject = (TPurgeHandler*) fgPurgeList.GetFirst();  
        purgeObject;     
        purgeObject = (TPurgeHandler*) purgeObject->Next())
            while(deadObject = purgeObject->fCacheList->Dequeue())
                TStorageManager::Free (deadObject); 
}; 
```

[Next](%E2%80%A2OTClasses-TCachedStorage.h.md)[Previous](%E2%80%A2OTClasses-TAddrInet.h.md)

