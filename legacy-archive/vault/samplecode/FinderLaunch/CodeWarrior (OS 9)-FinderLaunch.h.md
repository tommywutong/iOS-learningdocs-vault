---
title: FinderLaunch
apple_id: DTS10000666
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ApplicationServices
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/FinderLaunch/Listings/CodeWarrior____OS_9__FinderLaunch_h.html
archived_at: '2026-07-18T03:08:42.658479Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FinderLaunch](FinderLaunch.md)


[Next](CodeWarrior%20%28OS%209%29-MPWTool-FinderLaunch.c.md)[Previous](CodeWarrior%20%28OS%209%29-FinderLaunch.c.md)

# CodeWarrior (OS 9)/FinderLaunch.h

```c
/*  File:       FinderLaunch.h

    Description: 
            A routine for sending an open documents Apple event to the
            finder.  This routine provides functionality equivalent to
            selecting a document/file/application and choosing the
            open command in the Finder's file menu.  

    Author: John Montbriand

    Copyright: 
            Copyright © 1999 by Apple Computer, Inc.
            All rights reserved worldwide.

    Disclaimer:
            You may incorporate this sample code into your applications without
            restriction, though the sample code has been provided "AS IS" and the
            responsibility for its operation is 100% yours.  However, what you are
            not permitted to do is to redistribute the source as "DSC Sample Code"
            after having made changes. If you're going to re-distribute the source,
            we require that you make it clear in the source that the code was
            descended from Apple Sample Code, but that you've made changes.

    Change History (most recent first):
            9/13/99 created by John Montbriand
*/

#ifndef __FINDERLAUNCH__
#define __FINDERLAUNCH__

#include <Types.h>
#include <Files.h>

/* FinderLaunch converts a list of nTargets FSSpec records pointed to by the
    targetList parameter and converts the list to an apple event.  It then
    sends that event to the Finder.  The array of FSSpec records pointed
    to by the targetList parameter may contain references to files, folders,
    or applications.  The net effect of this command is equivalent to the
    user selecting an icon in one of the Finder's windows and then choosing
    the open command from the Finder's file menu. */
OSErr FinderLaunch(long nTargets, FSSpec *targetList);


#endif
```

[Next](CodeWarrior%20%28OS%209%29-MPWTool-FinderLaunch.c.md)[Previous](CodeWarrior%20%28OS%209%29-FinderLaunch.c.md)

