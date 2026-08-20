---
title: QTMusicToo
apple_id: DTS10000915
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-19'
source_url: https://developer.apple.com/library/archive/samplecode/QTMusicToo/Listings/_Instrument_Editor_IE_PrintUtilities_c.html
archived_at: '2026-07-18T03:21:05.916379Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTMusicToo](QTMusicToo.md)


[Next](%E2%80%A2Instrument%20Editor-IE%20PrintUtilities.h.md)[Previous](%E2%80%A2Instrument%20Editor-IE%20KeyboardDiagram.h.md)

# •Instrument Editor/IE PrintUtilities.c

```c


#include <QuickDraw.h>
#include "BigEasyTextish.h"
#include "IE PrintUtilities.h"



void PrintPlural(long x, StringPtr zero,StringPtr s1,StringPtr pluralizer, StringPtr s2)
    {
    if(x)
        DrawNum(x);
    else
        {
        if(zero)
            DrawString(zero);
        else
            DrawString("\pNo");
        }
    DrawChar(' ');
    DrawString(s1);
    if(x != 1 && x != -1)
        {
        if(pluralizer)
            DrawString(pluralizer);
        else
            DrawChar('s');
        }
    if(s2)
        DrawString(s2);
    }
```

[Next](%E2%80%A2Instrument%20Editor-IE%20PrintUtilities.h.md)[Previous](%E2%80%A2Instrument%20Editor-IE%20KeyboardDiagram.h.md)

