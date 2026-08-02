---
title: Network Stream
apple_id: DTS10000242
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Network_Stream/Listings/TNetworkStream_h.html
archived_at: '2026-07-18T03:17:00.938949Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Network Stream](Network%20Stream.md)


[Next](Document%20Revision%20History.md)[Previous](TNetworkStream.cp.md)

# TNetworkStream.h

```c
//  TNetworkStream.h - Macintosh OpenTransport Network Stream IO class object
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

#ifndef _H_TNETWORKSTREAM
#define _H_TNETWORKSTREAM

#include <iostream.h>
#include <OpenTransport.h>

//
// TNetworkBuf  - Macintosh OpenTransport Network Stream Buffer class object
//

#define BUFFSIZE 128

class TNetworkBuf :  public streambuf {

//  CONSTRUCTORS AND DESTRUCTORS
public:
        TNetworkBuf() : streambuf(),
                        fEndPoint(kOTInvalidRef),
                        fBuffer(nil),
                        fChunkSize(0) { };
        ~TNetworkBuf();

// HIGH LEVEL FUNCTIONS
public:
    void    attach (EndpointRef ep, TEndpointInfo* info);
    void    close();
    int     is_open() const { return (fEndPoint != (EndpointRef)kOTInvalidRef) ; }

// CLASS MEMBERS
public:
    static  void    Release(void *);

            char*   ReserveBuffer(size_t reqCount, size_t  *actCount);
            void    EnqueueBuffer(char* buf, size_t count);


// PROTECTED FUNCTIONS
protected :
    virtual int     overflow( int = EOF);
    virtual int     sync();
    virtual int     xsputn( const char*, int);

    virtual int     underflow();
    virtual int     uflow();

// PRIVATE FUNCTIONS
private:    
            int     flush_output(OTFlags flags = 0);
        Boolean     doallocate();

// PRIVATE FIELDS
private:
    EndpointRef     fEndPoint;          // network endpoint
    TEndpointInfo*  fInfo;              // pointer to endpoint Info Stucture
    char*           fBuffer;            // begining of buffer area
    size_t          fChunkSize;         // default chunksize

    char            Buffer[BUFFSIZE];
};

//
// TNetworkOStream  - Macintosh OpenTransport Network Stream output class object
//

class TNetworkIOStream :  
                    virtual public TNetworkBuf, 
                    virtual public ostream, 
                    virtual public istream {

//  CONSTRUCTORS AND DESTRUCTORS
    public:
        TNetworkIOStream (): 
                            ostream((TNetworkBuf*) this),
                            istream((TNetworkBuf*) this),
                            ios(0) {};

        TNetworkIOStream (EndpointRef ep, TEndpointInfo* info):
                                 ostream((TNetworkBuf*) this),
                                 istream((TNetworkBuf*) this),
                                 ios(0) 
                                 { attach(ep, info); };
   ~TNetworkIOStream();

};



#endif
```

[Next](Document%20Revision%20History.md)[Previous](TNetworkStream.cp.md)

