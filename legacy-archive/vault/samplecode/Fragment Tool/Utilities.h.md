---
title: Fragment Tool
apple_id: DTS10000572
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/Fragment_Tool/Listings/Utilities_h.html
archived_at: '2026-07-18T03:08:56.609550Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fragment Tool](Fragment%20Tool.md)


[Next](Windows.c.md)[Previous](Utilities.c.md)

# Utilities.h

```c
/*
    File:       Utilities.h

    Contains:   General utility routines

    Written by: Chris White 

    Copyright:  Copyright © 1995-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/5/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#ifndef __UTILITIES__
#define __UTILITIES__



#ifndef __FRAGMENTTOOL__
    #include "FragmentTool.h"
#endif






void AlertUser ( short messageCode, short errorNum, StringPtr theString );

StringPtr CopyPStr ( Str255 inSourceStr, StringPtr outDestStr, int16 inDestSize );
StringPtr ConcatPStr ( Str255 ioFirstStr, Str255 inSecondStr, int16 inDestSize );
StringPtr OSTypeToPStr ( OSType inOSType, StringPtr outString );

void BlockClear ( Ptr ptr, char value, Size size );

pascal void OutlineUserItem ( DialogRef theDialog, short theItem );

Boolean IsAResource ( Handle theHan );

OSErr CreateTemporaryFile ( FSSpecPtr theSpec );





#endif
```

[Next](Windows.c.md)[Previous](Utilities.c.md)

