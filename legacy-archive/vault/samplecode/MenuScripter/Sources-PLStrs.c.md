---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_PLStrs_c.html
archived_at: '2026-07-18T03:14:43.853509Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-PLStrs.h.md)[Previous](Sources-Offscreen.h.md)

# Sources/PLStrs.c

```c
/*
    PLStrs.c

    Version 3.1

    Copyright © 1995 Apple Computer, Inc., all rights reserved.

    MenuScripter by Nigel Humphreys and Jon Lansdell
    AppleEvent to script extensions by Greg Sutton
*/

#include "PLStrs.h"

#include <memory.h>

pascal StringPtr    PLstrcpy(StringPtr str1, StringPtr str2)
    {
      BlockMove(str2, str1, str2[0] + 1);
      return(str1);
    }

pascal StringPtr    PLstrcat(StringPtr str1, StringPtr str2)
    {
        long copyLen;

      if (str1[0] + 1 + str2[0]>255)
        copyLen = 255 - str1[0];
      else
        copyLen = str2[0];

      BlockMove(&str2[1], str1 + 1 + str1[0], copyLen);
      str1[0] += copyLen;

      return(str1);
    }
```

[Next](Sources-PLStrs.h.md)[Previous](Sources-Offscreen.h.md)

