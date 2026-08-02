---
title: STD File Saver
apple_id: DTS10000307
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/STD_File_Saver/Listings/Source_StringUtils_c.html
archived_at: '2026-07-18T03:22:49.216218Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [STD File Saver](STD%20File%20Saver.md)


[Next](Source-StringUtils.h.md)[Previous](Source-StdFileSaver.r.md)

# Source/StringUtils.c

```c
/*
** Copyright 1991-1996 Apple Computer. All rights reserved.
**
**  You may incorporate this sample code into your applications without
**  restriction, though the sample code has been provided "AS IS" and the
**  responsibility for its operation is 100% yours.  However, what you are
**  not permitted to do is to redistribute the source as "DSC Sample Code"
**  after having made changes. If you're going to re-distribute the source,
**  we require that you make it clear in the source that the code was
**  descended from Apple Sample Code, but that you've made changes.
*/

#include <Types.h>
#include <Memory.h>
#include <TextUtils.h>

#define PStrlen(s) (*s)

void PStrcpy(unsigned char *dest, unsigned char *src)
{
    BlockMoveData(src, dest, PStrlen(src) + 1);
}

void PStr_InsertChar(unsigned char *s, unsigned char c)
{
    unsigned char theLength = PStrlen(s);

    if (theLength >= 255) return;
    BlockMoveData(s+1,s+2,theLength);
    *(s+1) = c;
    PStrlen(s) = theLength + 1;
}

unsigned char *PStrcat(unsigned char *dst, unsigned char *src)
{
    unsigned char srcLength = PStrlen(src);
    unsigned char dstLength = PStrlen(dst);

    if ((srcLength + dstLength) > 255) {
        return dst;
    }
    BlockMoveData(src+1,dst+dstLength+1,srcLength);
    *dst = (unsigned char)(srcLength + dstLength);

    return dst;
}
```

[Next](Source-StringUtils.h.md)[Previous](Source-StdFileSaver.r.md)

