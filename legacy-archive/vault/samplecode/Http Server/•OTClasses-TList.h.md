---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TList_h.html
archived_at: '2026-07-18T03:11:59.125577Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TNetworkAcceptor.cp.md)[Previous](%E2%80%A2OTClasses-TList.cp.md)

# •OT_Classes/TList.h

```c
//  TList.h - Macintosh Queues and Lists class object
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

#ifndef _H_TLIST
#define _H_TLIST

#include <OpenTransport.h>

class TLink
    {
public:
        TLink()  : fNext(NULL) {};

        TLink*  Next() { return  fNext;  };

        TLink*  fNext;
    };

//
// TLIFO  - Atomic LIFO list
//
class TLifo
    {
    public:
        TLifo()  : fHead(NULL) {};

         void   Enqueue(TLink* link)
                    { OTLIFOEnqueue((OTLIFO*)this, (OTLink*) link); }

        TLink*  Dequeue()
                    { return (TLink*)OTLIFODequeue((OTLIFO*)this); }

        TLink*  StealList()
                    { return (TLink*)OTLIFOStealList((OTLIFO*)this); }

        void    Reverse()
                    {  fHead = (TLink*) OTReverseList( (OTLink*) fHead); }

        Boolean IsEmpty()
                    { return fHead == NULL; }

        TLink*  fHead;      
    };


//
// TList  - Non- Atomic list management
//
class TList
    {
    public:
        TList()  : fHead(NULL) {};

         void   Add (TLink* link)
                    { OTAddFirst((OTList*)this, (OTLink*) link); }

         void   Append (TLink* link)
                    { OTAddLast((OTList*)this, (OTLink*) link); }

        TLink*  RemoveFirst ()
                    { return (TLink*) OTRemoveFirst( (OTList*) this); }

        Boolean Remove (TLink* link)
                    { return OTRemoveLink((OTList*) this, (OTLink*) link); }

        TLink*  GetFirst ()
                    { return (TLink*) OTGetFirst( (OTList*) this); }

        Boolean IsEmpty()
                    { return fHead == NULL; }

        size_t  Count();

    private:
        TLink*  fHead;      
    };




#endif
```

[Next](%E2%80%A2OTClasses-TNetworkAcceptor.cp.md)[Previous](%E2%80%A2OTClasses-TList.cp.md)

