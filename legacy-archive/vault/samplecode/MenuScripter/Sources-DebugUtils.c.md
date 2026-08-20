---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_DebugUtils_c.html
archived_at: '2026-07-18T03:14:36.355134Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-DebugUtils.h.md)[Previous](Resources-MenuScripterAETE.r.md)

# Sources/DebugUtils.c

```c
// DebugUtils.c
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#include "DebugUtils.h"


#include <Memory.h>
#include <TextUtils.h>




void DebugNum ( long err )
{
    Str255 str;

    NumToString ( (long) err , (StringPtr) &str );
    DebugStr(str);

}



void DebugStrNum ( Str255 str, long num )
{
    Str255 debug_str, tmp_str;

    BlockMove ( &str[0], &debug_str[0], str[0] + 1 );

    NumToString ( ( long ) num , &tmp_str[0] );
    debug_str[ debug_str[0] + 1 ] = ' ';
    BlockMove ( &tmp_str[1], &debug_str[ debug_str[0] + 2 ], tmp_str[0] );
    debug_str[0] = debug_str[0] + tmp_str[0] + 1;
    DebugStr ( debug_str );
}
```

[Next](Sources-DebugUtils.h.md)[Previous](Resources-MenuScripterAETE.r.md)

