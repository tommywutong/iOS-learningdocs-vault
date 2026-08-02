---
title: PThreadSorts
apple_id: DTS10000753
resource_type: Sample Code
platform: macOS
topic: Performance
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PThreadSorts/Listings/Sorts_QuickSortPicture_h.html
archived_at: '2026-07-18T03:18:38.773057Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PThreadSorts](PThreadSorts.md)


[Next](Sorts-SelectionSortPicture.cp.md)[Previous](Sorts-QuickSortPicture.cp.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html](https://developer.apple.com/library/mac/#documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html)

# Sorts/QuickSortPicture.h

```c
/*
    File:       QuickSortPicture.h

    Contains:   Quick Sort O(N*log(N))

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
#ifndef QUICK_SORT_PICTURE_H
#define QUICK_SORT_PICTURE_H

#include "SortablePicture.h"

class QuickSortPicture : public SortablePicture
{
    public:
        QuickSortPicture(ResID pictID) : SortablePicture(pictID){}
        virtual CFStringRef GetSortName(){return CFSTR("Quick Sort");}
        virtual void Sort();
    protected:
        void qsort(SInt32 lower, SInt32 upper);
};

#endif
```

[Next](Sorts-SelectionSortPicture.cp.md)[Previous](Sorts-QuickSortPicture.cp.md)

