---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_Mac_Classes_TMacException_h.html
archived_at: '2026-07-18T03:11:58.539066Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2MacClasses-TThread.cp.md)[Previous](%E2%80%A2MacClasses-TContext.h.md)

# •Mac_Classes/TMacException.h

```
//  TMacException.h - Exception class object
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

#ifndef _H_TMACEXCEPTION
#define _H_TMACEXCEPTION

// ______________________________________________________________________________
// MACROS

// This macro will automatically fill in the __FILE__ and __LINE statements
// when a throw is used.

#define THROWEXCEPTION(name, number) \
    throw TMacException( (name), (number), __FILE__, __LINE__)


// ______________________________________________________________________________
// EXCEPTION CLASSES

class TMacException 
{
public:
    TMacException(const OSErr theError) :
                    fMessage("NO MESSAGE SPECIFIED"), 
                    fError(theError), 
                    fFileName("NO FILE SPECIFIED"), 
                    fLineNumber(0L) 
                    {};

    TMacException(const char *theMessage, const OSErr theError) :
                    fMessage(theMessage), 
                    fError(theError), 
                    fFileName("NO FILE SPECIFIED"), 
                    fLineNumber(0L) 
                    {};

    TMacException(const char *theMessage, const OSErr theError, const char *theFileName, const long theLineNumber) :
                    fMessage(theMessage), 
                    fError(theError), 
                    fFileName(theFileName), 
                    fLineNumber(theLineNumber) 
                    {};

    const char*     GetExceptionMessage(void)   { return fMessage;};
    const OSErr     GetExceptionOSErr(void)     { return fError;};
    const char*     GetExceptionFile(void)      { return fFileName;};
    const long      GetExceptionLine(void)      { return fLineNumber;};

protected:
    const OSErr     fError;
    const char*     fMessage;
    const char*     fFileName;
    const long      fLineNumber;
};


// Utility Macros

#define ThrowIfNil( _val_ )                                     \
        if ( (_val_) == nil )                                       \
            throw TMacException( "UNEXPECTED NIL RETURNED" ,0 , __FILE__, __LINE__)  

#define ThrowIfNotNil( _val_ )                                              \
        if ( (_val_) != nil )                                                   \
            throw TMacException( "EXPECTED NIL" ,0 , __FILE__, __LINE__) 

#define ThrowIfOSErr(_err_)                                     \
        if ((_err_) != noErr)                                           \
            throw TMacException( "NO MESSAGE SPECIFIED", (_err_), __FILE__, __LINE__)    

#define ThrowOSErr(_err_)                                               \
            throw TMacException( "NO MESSAGE SPECIFIED", (_err_), __FILE__, __LINE__)    

#define ThrowMsgIfOSErr(_err_, _Msg_)                                       \
        if ((_err_) != noErr)                                           \
            throw TMacException( (_Msg_), (_err_), __FILE__, __LINE__)   

#define ThrowMsgOSErr(_err_, _Msg_)                                     \
            throw TMacException( (_Msg_), (_err_), __FILE__, __LINE__)   

#define ThrowMsg( _Msg_)                                        \
            throw TMacException( (_Msg_), noErr, __FILE__, __LINE__)     

#endif
```

[Next](%E2%80%A2MacClasses-TThread.cp.md)[Previous](%E2%80%A2MacClasses-TContext.h.md)

