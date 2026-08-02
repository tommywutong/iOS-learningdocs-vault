---
title: OTPAPSampleServer
apple_id: DTS10000252
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/OTPAPSampleServer/Listings/OTDebug_h.html
archived_at: '2026-07-18T03:17:17.538187Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OTPAPSampleServer](OTPAPSampleServer.md)


[Next](PAPPostScriptStuff.c.md)[Previous](EnableSelfSendSample.c.md)

# OTDebug.h

```
/*
    File:       OTDebug.h

    Contains:   Macros for debugging stuff

    Copyright:  © 1994-1998 by Apple Computer, Inc., all rights reserved.

*/

#ifndef __OTDEBUG__
#define __OTDEBUG__


#define kOTFatalErr             "FB "
#define kOTNonfatalErr          "NB "
#define kOTExtFatalErr          "FX "
#define kOTExtNonfatalErr       "NX "
#define kOTUserFatalErr         "UF "
#define kOTUserErr              "UE "
#define kOTUserNonfatalErr      "UE "
#define kOTInfoErr              "IE "
#define kOTInfoBreak            "IN "

pascal  void OTDebugStr(const char* str);

#if qDebug || qDebug2

    #define OTDebugBreak(str)           OTDebugStr(str)
    #define OTDebugTest(val, str)       { if ( val ) OTDebugStr(str); }
    #define OTAssert(name, cond)                                \
        if ( !(cond) )                                          \
        {                                                       \
            OTDebugStr(#name " - Failed assertion:" #cond);     \
        }

#else

    #define OTDebugBreak(str)
    #define OTDebugTest(val, str)
    #define OTAssert(name, cond)

#endif  // qDebug || qDebug2

#if qDebug > 1 || qDebug2 > 1
    #define OTDebugBreak2(str)          OTDebugStr(str)
    #define OTDebugTest2(val, str)      { if ( val) OTDebugStr(str); }
#else
    #define OTDebugBreak2(str)
    #define OTDebugTest2(val, str)
#endif  // qDebug > 1 || qDebug2 > 1

#endif  // __OTDEBUG__
```

[Next](PAPPostScriptStuff.c.md)[Previous](EnableSelfSendSample.c.md)

