---
title: FinderDragPro
apple_id: DTS10000665
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/FinderDragPro/Listings/GetIconSuiteFromFinder_h.html
archived_at: '2026-07-18T03:08:42.460077Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FinderDragPro](FinderDragPro.md)


[Next](Document%20Revision%20History.md)[Previous](GetIconSuiteFromFinder.c.md)

# GetIconSuiteFromFinder.h

```c
/*
    File:       FinderDragPro.c

    Description:    Sample file illustrating drag and drop techniques for use
                with file system objects.  This file illustrates how applications
                can use drag and drop commands in a way compatible with current
                and past versions of the Finder.

    Author:     Pete Gontier

    Copyright:  Copyright: © 1999 by Apple Computer, Inc.
                all rights reserved.

    Disclaimer: You may incorporate this sample code into your applications without
                restriction, though the sample code has been provided "AS IS" and the
                responsibility for its operation is 100% yours.  However, what you are
                not permitted to do is to redistribute the source as "DSC Sample Code"
                after having made changes. If you're going to re-distribute the source,
                we require that you make it clear in the source that the code was
                descended from Apple Sample Code, but that you've made changes.

    Change History (most recent first):
    06/09/95    NG  last touched
    08/23/96    PG  stolen from Nitin's old FinderDrag project
    04/21/97    PG  pascal programs can be written in any language
*/

#pragma once

#include <Drag.h>
#include <FinderRegistry.h>

//
//  These two should be in FinderRegistry.h, but they ain't
//

#define keyLocalPositionList    'mvpl'
#define keyGlobalPositionList   'mvpg'

OSErr GetIconSuiteFromFinder(FSSpecPtr, Handle *);
```

[Next](Document%20Revision%20History.md)[Previous](GetIconSuiteFromFinder.c.md)

