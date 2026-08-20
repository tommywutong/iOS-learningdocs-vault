---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/CoreSource_ErrMsg_c.html
archived_at: '2026-07-18T03:28:32.095855Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](CoreSource-EventLoop.c.md)[Previous](CoreSource-Document.c.md)

# CoreSource/ErrMsg.c

```
/*
    9-30-92  ¥ Brigham Stevens
    --------------------------

    This contains code for handling an error dialog box.
    This is for debugging only, not for a complete real application type thing.

    If you want to display an error code and string, call ErrMsgCode,
    otherwise, for string only, just call ErrMsg.
*/

#define KEEP_GOING 1
#define DEBUGGER 2
#define EXITTOSHELL 3



void ErrMsgCode(Str255 msg, short code)
/*
    Display the error alert with
    an error code.

    This handy alert will also display 
    memerr and reserr for you.
*/
{ 
    Str31   codeStr;
    Str31   memErrStr;
    Str31   resErrStr;
    short   disposition;

    NumToString(code,codeStr);
    NumToString(MemErr,memErrStr);
    NumToString(ResErr,resErrStr);

    ParamText(msg, codeStr, memErrStr, resErrStr);

    disposition = Alert(128, nil);

    switch(disposition)
    {
        case    KEEP_GOING:     return;
        break;
        case    DEBUGGER:       DebugStr("\p Doing a Stack Crawl;sc6");
        break;
        case    EXITTOSHELL:    ExitToShell();
        break;
    }
}


void ErrMsg(Str255 msg)
/*
    No error code desired.
*/
{
    ErrMsgCode(msg, 0);
}
```

[Next](CoreSource-EventLoop.c.md)[Previous](CoreSource-Document.c.md)

