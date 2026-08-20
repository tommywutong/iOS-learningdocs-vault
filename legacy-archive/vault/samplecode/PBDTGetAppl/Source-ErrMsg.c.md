---
title: PBDTGetAppl
apple_id: DTS10000042
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PBDTGetAppl/Listings/Source_ErrMsg_c.html
archived_at: '2026-07-18T03:18:19.797632Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PBDTGetAppl](PBDTGetAppl.md)


[Next](Source-EventLoop.c.md)[Previous](Source-Drawing.c.md)

# Source/ErrMsg.c

```
/*
    9-30-92  ¥ Brigham Stevens
    --------------------------

    This contains code for handling an error dialog box.

    If you want to display an error code and string, call ErrMsgCode,
    otherwise, for string only, just call ErrMsg.
*/

#define KEEP_GOING 1
#define DEBUGGER 2
#define EXITTOSHELL 3


void Msg(Str255 msg)
/*
    Display an Alert with the string passed.
*/
{
    ParamText(msg,nil,nil,nil);
    Alert(130, nil);
}

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

[Next](Source-EventLoop.c.md)[Previous](Source-Drawing.c.md)

