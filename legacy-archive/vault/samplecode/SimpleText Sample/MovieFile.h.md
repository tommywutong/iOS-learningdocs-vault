---
title: SimpleText Sample
apple_id: DTS10000736
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleText_Sample/Listings/MovieFile_h.html
archived_at: '2026-07-18T03:24:18.072127Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleText Sample](SimpleText%20Sample.md)


[Next](MovieFile.r.md)[Previous](MovieFile.c.md)

# MovieFile.h

```c
/*
    File:       MovieFile.h

    Contains:   Movie file support for simple text application

    Version:    GX 1.2 or later

** Copyright 1993-1996 Apple Computer. All rights reserved.
**
**  You may incorporate this sample code into your applications without
**  restriction, though the sample code has been provided "AS IS" and the
**  responsibility for its operation is 100% yours.  However, what you are
**  not permitted to do is to redistribute the source as "DSC Sample Code"
**  after having made changes. If you're going to re-distribute the source,
**  we require that you make it clear in the source that the code was
**  descended from Apple Sample Code, but that you've made changes.

*/

#include "SimpleText.h"

#define kMovieWindowID  kMovieBaseID

#ifndef REZ
    struct MovieDataRecord
        {
        WindowDataRecord        w;

        Movie                   theMovie;
        MovieController         thePlayer;
        long                    searchOffset;
        };
    typedef struct MovieDataRecord MovieDataRecord, *MovieDataPtr;  
#endif
```

[Next](MovieFile.r.md)[Previous](MovieFile.c.md)

