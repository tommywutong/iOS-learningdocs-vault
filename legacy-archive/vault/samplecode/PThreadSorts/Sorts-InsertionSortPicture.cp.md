---
title: PThreadSorts
apple_id: DTS10000753
resource_type: Sample Code
platform: macOS
topic: Performance
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PThreadSorts/Listings/Sorts_InsertionSortPicture_cp.html
archived_at: '2026-07-18T03:18:38.655246Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PThreadSorts](PThreadSorts.md)


[Next](Sorts-InsertionSortPicture.h.md)[Previous](Sorts-HeapSortPicture.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html](https://developer.apple.com/library/mac/#documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html)

# Sorts/InsertionSortPicture.cp

```c
/*
    File:       InsertionSortPicture.cp

    Contains:   Insertion Sort

    Written by:     Karl Groethe

    Copyright:  Copyright © 2000 by Apple Computer, Inc., All Rights Reserved.

            You may incorporate this Apple sample source code into your program(s) without
            restriction. This Apple sample source code has been provided "AS IS" and the
            responsibility for its operation is yours. You are not permitted to redistribute
            this Apple sample source code as "Apple sample source code" after having made
            changes. If you're going to re-distribute the source, we require that you make
            it clear in the source that the code was descended from Apple sample source
            code, but that you've made changes.

    Change History (most recent first):
                        7/00    Created
*/
#include "InsertionSortPicture.h"

void InsertionSortPicture::Sort()
{
    /*------------------------------------------------------
       Insertion Sort
    --------------------------------------------------------*/
    for(UInt32 i=0;i<linearPictSize;i++)
    {
        Boolean inserted=FALSE;
        UInt32 j=i;
        while((j>0) && !inserted){
            if(!InOrder(j-1,j))
                SwapPixels(j-1,j);
            else
                inserted=TRUE;
            j--;
        }
    }
}
```

[Next](Sorts-InsertionSortPicture.h.md)[Previous](Sorts-HeapSortPicture.h.md)

