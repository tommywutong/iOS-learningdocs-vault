---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_TMacException_h.html
archived_at: '2026-07-18T03:18:33.555682Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-TMemPGPkey.cp.md)[Previous](sources-TASIPPGPkey.h.md)

# sources/TMacException.h

```
//  TMacException.h - Exception class object
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

#ifndef _H_TMACEXCEPTION
#define _H_TMACEXCEPTION



// ______________________________________________________________________________
// EXCEPTION CLASSES

class TMacException 
{
public:
    TMacException(const OSStatus theError) :
                    fMessage("NO MESSAGE SPECIFIED"), 
                    fError(theError), 
                    fFileName("NO FILE SPECIFIED"), 
                    fLineNumber(0L) 
                    {};

    TMacException(const  char *theMessage, const OSStatus theError) :
                    fMessage(theMessage), 
                    fError(theError), 
                    fFileName("NO FILE SPECIFIED"), 
                    fLineNumber(0L) 
                    {};

    TMacException(const  char *theMessage, const OSStatus theError, const char *theFileName, const long theLineNumber) :
                    fMessage(theMessage), 
                    fError(theError), 
                    fFileName(theFileName), 
                    fLineNumber(theLineNumber) 
                    {};

    const char*             GetExceptionMessage(void)   { return fMessage;};
    const OSStatus      GetExceptionErr(void)           { return fError;};
    const char*             GetExceptionFile(void)      { return fFileName;};
    const long              GetExceptionLine(void)      { return fLineNumber;};

protected:
    const OSStatus  fError;
    const  char*        fMessage;
    const char*         fFileName;
    const long          fLineNumber;
};


// Utility Macros

#define ThrowIfNil( _val_ )                                     \
        if ( (_val_) == nil )                                       \
            throw TMacException( "UNEXPECTED NIL RETURNED" ,0 , __FILE__, __LINE__)  

#define ThrowIfNotNil( _val_ )                                              \
        if ( (_val_) != nil )                                                   \
            throw TMacException( "EXPECTED NIL" ,0 , __FILE__, __LINE__) 

#define ThrowIfMacErr(_err_)                                        \
        { OSErr _temp_ = (_err_);   \
        if ( _temp_ != noErr)                                           \
            throw TMacException( "NO MESSAGE SPECIFIED",  _temp_ , __FILE__, __LINE__);     }  

#define ThrowMacErr(_err_)                                              \
            throw TMacException( "NO MESSAGE SPECIFIED", (_err_), __FILE__, __LINE__)    

#define ThrowMacErrIfNil( _val_, _err_  )                                       \
        if ( (_val_) == nil )                                       \
            throw TMacException( "NO MESSAGE SPECIFIED" , (_err_) , __FILE__, __LINE__)  

#define ThrowMsgIfMacErr(_err_, _Msg_)                                      \
        if ((_err_) != noErr)                                           \
            throw TMacException( (_Msg_), (_err_), __FILE__, __LINE__)   

#define ThrowMsgMacErr(_err_, _Msg_)                                        \
            throw TMacException( (_Msg_), (_err_), __FILE__, __LINE__)   

#define ThrowMsg( _Msg_)                                        \
            throw TMacException( (_Msg_), noErr, __FILE__, __LINE__)     

#define ThrowMsgIfNot( _cond_, _Msg_)           \
            if( ! (_cond_) )                                                    \
            throw TMacException( (_Msg_), noErr, __FILE__, __LINE__)     

#define ThrowMsgIf( _cond_, _Msg_)          \
            if( _cond_ )                                                    \
            throw TMacException( (_Msg_), noErr, __FILE__, __LINE__)     

#endif
```

[Next](sources-TMemPGPkey.cp.md)[Previous](sources-TASIPPGPkey.h.md)

