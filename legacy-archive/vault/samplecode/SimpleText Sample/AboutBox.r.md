---
title: SimpleText Sample
apple_id: DTS10000736
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleText_Sample/Listings/AboutBox_r.html
archived_at: '2026-07-18T03:24:16.515707Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleText Sample](SimpleText%20Sample.md)


[Next](AGFile.h.md)[Previous](AboutBox.h.md)

# AboutBox.r

```c
/*
    File:       AboutBox.r

    Contains:   About box for simple text application

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


#include "AboutBox.h"

resource 'WIND' (kAboutWindowID, purgeable) {
    {100, 100, 215, 400}, noGrowDocProc, invisible, goAway, 0, ABOUTBOXTITLE, alertPositionMainScreen
};

resource 'STR#' (kAboutStrings, purgeable) {
    {
    ABOUTSTRING1;
    ABOUTSTRING2;
    ABOUTSTRING3;
    ABOUTSTRING4;
    ABOUTSTRING5;
    ABOUTSTRING6;
    };
};
```

[Next](AGFile.h.md)[Previous](AboutBox.h.md)

