---
title: Scriptable Print SimpleText
apple_id: DTS10000305
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/Scriptable_Print_SimpleText/Listings/MovieFile_r.html
archived_at: '2026-07-18T03:23:29.232114Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Scriptable Print SimpleText](Scriptable%20Print%20SimpleText.md)


[Next](PICTFile.c.md)[Previous](MovieFile.h.md)

# MovieFile.r

```c
/*
**  File:       MovieFile.r
**
**  Contains:   Movie file support for simple text application
**
** Copyright 1993-1999 Apple Computer. All rights reserved.
**
**  You may incorporate this sample code into your applications without
**  restriction, though the sample code has been provided "AS IS" and the
**  responsibility for its operation is 100% yours.  However, what you are
**  not permitted to do is to redistribute the source as "DSC Sample Code"
**  after having made changes. If you're going to re-distribute the source,
**  we require that you make it clear in the source that the code was
**  descended from Apple Sample Code, but that you've made changes.

*/


#include "MovieFile.h"

resource 'WIND' (kMovieWindowID) {
    {40, 40, 215, 400}, noGrowDocProc, invisible, goAway, 0, NEWDOCUMENTTITLE, noAutoCenter
};
```

[Next](PICTFile.c.md)[Previous](MovieFile.h.md)

