---
title: SoundSprocketTest
apple_id: DTS10000060
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SoundSprocketTest/Listings/TS3Message_h.html
archived_at: '2026-07-18T03:25:09.562884Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SoundSprocketTest](SoundSprocketTest.md)


[Next](TS3Resource.h.md)[Previous](TS3Message.c.md)

# TS3Message.h

```
/*
 *  File:       TS3Message.h
 *
 *  Copyright © 1996 Apple Computer, Inc.
 */

#ifndef __TS3Message__
#define __TS3Message__

void Message_Init(
    void);

void Message_Exit(
    void);

#define Message_CheckError(inErr,inInRoutine,inFromRoutine) \
       _Message_CheckError(inErr,inInRoutine,inFromRoutine,__FILE__,__LINE__)

void _Message_CheckError(
    OSStatus            inErr,
    const char*         inInRoutine,
    const char*         inFromRoutine,
    const char*         inFile,
    unsigned long       inLine);

#endif /* __TS3Message__ */
```

[Next](TS3Resource.h.md)[Previous](TS3Message.c.md)

