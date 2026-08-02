---
title: PThreadSorts
apple_id: DTS10000753
resource_type: Sample Code
platform: macOS
topic: Performance
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PThreadSorts/Listings/Sorts_BubbleSortPicture_cp.html
archived_at: '2026-07-18T03:18:38.520754Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PThreadSorts](PThreadSorts.md)


[Next](Sorts-BubbleSortPicture.h.md)[Previous](SortablePicture.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html](https://developer.apple.com/library/mac/#documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html)

# Sorts/BubbleSortPicture.cp

```c
/*
    File:       BubbleSortPicture.cp

    Contains:   BubbleSort Sorts

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
#include "BubbleSortPicture.h"

void BubbleSortPicture::Sort()
{
    /*------------------------------------------------------
       Standard bubble sort
    --------------------------------------------------------*/
    for(UInt32 i=0;i<linearPictSize-1;i++)
        for(UInt32 j=0; j<linearPictSize-1-i;j++)
            if(!InOrder(j,j+1))
                SwapPixels(j,j+1);
}

void RBubbleSortPicture::Sort()
{
    /*------------------------------------------------------
       Bubble sort in reverse order
    --------------------------------------------------------*/

    for(SInt32 i=linearPictSize-1;i>0;i--)
        for(SInt32 j=linearPictSize-1;j>(SInt32)linearPictSize-1-i;j--)
            if(!InOrder(j-1,j))
                SwapPixels(j-1,j);
}

void BiDirBubbleSortPicture::Sort()
{
    /*------------------------------------------------------
       Bubble sort in alternating directions
    --------------------------------------------------------*/
    for(UInt32 i=0,j=linearPictSize-1;i<j;i++,j--){
        for(UInt32 k=i;k<j;k++)
            if(!InOrder(k,k+1))
                SwapPixels(k,k+1);
        for(UInt32 k=j;k>i;k--)
            if(!InOrder(k-1,k))
                SwapPixels(k-1,k);
    }
}
```

[Next](Sorts-BubbleSortPicture.h.md)[Previous](SortablePicture.h.md)

