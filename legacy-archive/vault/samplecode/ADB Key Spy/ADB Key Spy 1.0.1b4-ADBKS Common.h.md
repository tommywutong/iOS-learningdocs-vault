---
title: ADB Key Spy
apple_id: DTS10000004
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ADB_Key_Spy/Listings/ADB_Key_Spy_1_0_1b4_ADBKS_Common_h.html
archived_at: '2026-07-18T02:59:23.719889Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ADB Key Spy](ADB%20Key%20Spy.md)


[Next](ADB%20Key%20Spy%201.0.1b4-ADBKS%20csCodes.h.md)[Previous](ADB%20Key%20Spy.md)

# ADB Key Spy 1.0.1b4/ADBKS Common.h

```
    //
    //  from 'ADB Key Spy' ¥ Pete Gontier
    //  Macintosh Developer Technical Support
    //  ©Ê1995,1996,1998 Apple Computer, Inc.
    //
    //  Changes:
    //
    //      when        who     what
    //      --------------------------------------------------------------
    //      01/11/96    PG      copied from another project,
    //                          merged with various parts of old
    //                          ADB Key Spy
    //

#pragma once

#ifndef __DESKBUS__
#   include <DeskBus.h>
#endif

    //
    //  kMaxKeyCode
    //
    //  GetKeys returns four 32-bit quantities for its key map, and with
    //  each bit corresponding to a key, that 32*4==128 keys. I don't know
    //  if keyboards are capable of supporting more keys, but it's unlikely
    //  anybody cares about key codes that high simply because GetKeys
    //  can't report them. We use 127 because key codes start at 0.
    //

static const unsigned char kMaxKeyCode = 127;

    //
    //  tKeyboardInfo
    //
    //  This structure describes each keyboard discovered during AKS_AcquireKeyboards.
    //  In it we store info from the service routine for the keyboard before we replace it,
    //  plus a key map. We use a byte for each entry in the key map mostly for historical
    //  reasons. (There used to be one key map for all keyboards; each entry was a counter.)
    //  Now it has a byte per entry simply because I am too lazy to write the bit-twiddling
    //  code to make it one bit per entry.
    //
    //  We maintain a simple linked list of these structures. Client code doesn't need to
    //  worry about this structure; it's just here for the benefit of the code resource.
    //

#if PRAGMA_ALIGN_SUPPORTED
#   pragma options align=mac68k
#endif

typedef struct
{
    unsigned char               raw;
    Boolean                     noXor, Xor;
    unsigned char               bits;
    unsigned char               pstring [ ];
}
tKeyMapResourceException;

typedef struct // for corroboration, see "SysTypes.r"
{
    unsigned short              id;
    unsigned short              vers;
    unsigned char               map [kMaxKeyCode + 1];
    unsigned short              exceptionCount;
    tKeyMapResourceException    exceptions [ ];
}
tKeyMapResource, *tKeyMapResourceP, **tKeyMapResourceH;

typedef struct tKeyboardInfo
{
    ADBServiceRoutineUPP    dbServiceRtPtr;
    Ptr                     dbDataAreaAddr;
    unsigned char           virtualKeyMap [kMaxKeyCode + 1];
    tKeyMapResourceH        keyMapResH;
    struct tKeyboardInfo    *next;
}
tKeyboardInfo, *tKeyboardInfoP;

#if PRAGMA_ALIGN_SUPPORTED
#   pragma options align=reset
#endif
```

[Next](ADB%20Key%20Spy%201.0.1b4-ADBKS%20csCodes.h.md)[Previous](ADB%20Key%20Spy.md)

