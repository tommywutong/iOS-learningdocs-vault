---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TList_cp.html
archived_at: '2026-07-18T03:11:59.086665Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TList.h.md)[Previous](%E2%80%A2OTClasses-TCachedStorage.h.md)

# •OT_Classes/TList.cp

```c
//  TList.cp - Macintosh Queues and Lists class object
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

#include "TList.h"

// ---------------------------------------------------------------------------
//   TList::Count( )
// ---------------------------------------------------------------------------
// count items on list

size_t  TList::Count()
{
    size_t index;
    TLink* p;

    for(p = GetFirst(),  index = 0;  p;  p = p->Next(), index++);
    return index;
}
```

[Next](%E2%80%A2OTClasses-TList.h.md)[Previous](%E2%80%A2OTClasses-TCachedStorage.h.md)

