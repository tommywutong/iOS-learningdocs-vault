---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_Mac_Classes_TThread_h.html
archived_at: '2026-07-18T03:11:58.662939Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TAddr.cp.md)[Previous](%E2%80%A2MacClasses-TThread.cp.md)

# •Mac_Classes/TThread.h

```c
//  TThread.h - Macintosh Thread class object
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

#ifndef _H_TTHREAD
#define _H_TTHREAD

#include <Threads.h>        // Thread manager
#include "TContext.h"

class TThread
{

//  CONSTRUCTORS AND DESTRUCTORS
public:
                    TThread();
    virtual         ~TThread();

// HIGH LEVEL FUNCTIONS
public:
    void    Start();                
    void    Stop(void* theResult = nil);
    void    Sleep();
    void    WakeUp();

// CALLBACK METHODS
protected:
    virtual void*   Run();
    virtual void    Done();

// THREAD MANAGER CALLBACKS
private:
    static pascal void* DoEntry         (void *);
    static pascal void  DoTermination   (ThreadID , void*);
    static pascal void  DoSwapIn        (ThreadID, void*);
    static pascal void  DoSwapOut       (ThreadID, void*);

// PRIVATE METHODS
private:
    void    Initialize();

// PRIVATE FIELDS
private:
    TContext            fContext;
    ThreadID            fTID;   
    void*               fResult;

// CLASS FUNCTIONS
public:
    static  void    Allocate(short numToCreate, long MinStack);
    static  void    Yield();

// CLASS VARIABLES
private:
    static Boolean              fgInited;           // is the thread class initialised?
    static ProcessSerialNumber  fgPSN;              // ptr to application's PSN
    static ThreadTaskRef        fgThreadTaskRef;    // thread task ref
};



#endif
```

[Next](%E2%80%A2OTClasses-TAddr.cp.md)[Previous](%E2%80%A2MacClasses-TThread.cp.md)

