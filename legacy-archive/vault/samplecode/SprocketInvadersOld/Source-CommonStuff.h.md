---
title: SprocketInvadersOld
apple_id: DTS10000061
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SprocketInvadersOld/Listings/Source_CommonStuff_h.html
archived_at: '2026-07-18T03:25:25.929207Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SprocketInvadersOld](SprocketInvadersOld.md)


[Next](Source-ErrorHandler.c.md)[Previous](Source-CommonStuff.c.md)

# Source/CommonStuff.h

```
//¥ ------------------------------------------------------------------------------------------  ¥
//¥
//¥ Copyright © 1996 Apple Computer, Inc., All Rights Reserved
//¥
//¥
//¥     You may incorporate this sample code into your applications without
//¥     restriction, though the sample code has been provided "AS IS" and the
//¥     responsibility for its operation is 100% yours.  However, what you are
//¥     not permitted to do is to redistribute the source as "DSC Sample Code"
//¥     after having made changes. If you're going to re-distribute the source,
//¥     we require that you make it clear in the source that the code was
//¥     descended from Apple Sample Code, but that you've made changes.
//¥
//¥ ------------------------------------------------------------------------------------------  ¥

// Common Stuff.h is a simple include file that holds a number of standard functions,
// constants, and debugging macros.  Anything that isn't likely to change from program
// to program.

#ifndef _COMMONSTUFF_
#define _COMMONSTUFF_

#pragma once

/*********************************************************************************
    DEBUGGING and ERROR HANDLING MACROS

    These macros should be used to create code with proper error handling.  In
    the debugging version of the macros, they dump a string to the debugger before
    dropping into the error handler.

    To turn debugging off, set the macro qDebugging to 0 before including Common Stuff.

    If an application wants to include special debugging code, the proper way to do this
    is with something like:

    #if qDebugging
        // do additional sanity checking here.
    #endif

    Note that this should only be additional sanity checking code and not eliminate all error
    checking code.

*********************************************************************************/
#define qDebugging 0
#ifndef qDebugging
    #define qDebugging 0
#endif

void DebugPrint(char *message, long error);
void dprintf(char *format, ...);

#if qDebugging
    #define SIGNAL_ERROR(msg, y)        {DebugPrint(msg, y); goto error;}
#else
    #define SIGNAL_ERROR(msg, y)        {goto error;}
#endif

#define FAIL_NIL(y,msg)         if (y == NULL) SIGNAL_ERROR(msg, y)
#define FAIL_OSERR(y,msg)       if (y != noErr) SIGNAL_ERROR(msg, y)
#define FAIL_OSSTATUS(y,msg)    if (y != (OSStatus) 0) SIGNAL_ERROR(msg, y)
#define FAIL_FALSE(y,msg)       if (!y) SIGNAL_ERROR(msg, y)

extern short gMySeed;
extern UInt32 gMyRandomCount;   
extern UInt32 gGameLoopIterations;

int Game_Random(int x);

StringPtr
CopyPStr(
    ConstStr255Param    inSourceStr,
    StringPtr           outDestStr);

#endif /* _COMMONSTUFF_ */
```

[Next](Source-ErrorHandler.c.md)[Previous](Source-CommonStuff.c.md)

