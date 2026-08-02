---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TNetworkException_h.html
archived_at: '2026-07-18T03:11:59.732726Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TNetworkServerApp.cp.md)[Previous](%E2%80%A2OTClasses-TNetworkEventHandler.h.md)

# •OT_Classes/TNetworkException.h

```c
//  TNetworkException.h - Macintosh OpenTransport Exception class object
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

#ifndef _H_TNETWORKEXCEPTION
#define _H_TNETWORKEXCEPTION

#include "TMacException.h"


//
// TNetworkException  - OpenTransport Network Exception 
//
class TNetworkException : public TMacException
{
public:
//  CONSTRUCTORS AND DESTRUCTORS
    TNetworkException(const char *theMessage, const OSStatus theStatus) :
                    fStatus( theStatus),
                    TMacException(theMessage, -1, "NO FILE SPECIFIED", 0L)
                    {};

    TNetworkException(const char *theMessage, const OSStatus theStatus, const char *theFileName, const long theLineNumber) :
                    fStatus( theStatus),
                    TMacException(theMessage, -1, theFileName, theLineNumber)
                    {};

// ACCESSORS and MUTATORS   
    const OSStatus  GetOSStatus(void)       { return fStatus;};

// PROTECTED FIELDS
protected:
    const OSStatus fStatus;

};

// Utility Macros

#define ThrowIfOTErr(_err_)                                     \
        if (_err_ != noErr)                                         \
            throw TNetworkException( "NO MESSAGE SPECIFIED", (_err_), __FILE__, __LINE__)    

#define ThrowIfOTInvalidRef( _val_ )                                        \
        if ( (_val_) == (EndpointRef) kOTInvalidRef )                                       \
            throw TMacException( "INVALID PROVIDER REF RETURNED" ,0 , __FILE__, __LINE__)    

#define ThrowIfOTInvalidConfig( _val_ )                                     \
        if ( (_val_) == kOTInvalidConfigurationPtr )                                        \
            throw TMacException( "INVALID CONFIG RETURNED" ,0 , __FILE__, __LINE__)  

#define ThrowOTErr(_err_)                                       \
            throw TNetworkException( "NO MESSAGE SPECIFIED", (_err_), __FILE__, __LINE__)    

#endif
```

[Next](%E2%80%A2OTClasses-TNetworkServerApp.cp.md)[Previous](%E2%80%A2OTClasses-TNetworkEventHandler.h.md)

