---
title: FinderLaunch
apple_id: DTS10000666
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ApplicationServices
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/FinderLaunch/Listings/CodeWarrior____OS_9__MPWTool_FinderLaunchTool_c.html
archived_at: '2026-07-18T03:08:42.729225Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FinderLaunch](FinderLaunch.md)


[Next](CodeWarrior%20%28OS%209%29-MPWTool-FinderLaunchTool.r.md)[Previous](CodeWarrior%20%28OS%209%29-MPWTool-FinderLaunch.h.md)

# CodeWarrior (OS 9)/MPWTool/FinderLaunchTool.c

```c
/*  File:       FinderLaunchTool.c

    Description: 
            A test application for sending an open documents Apple event to the
            Finder.  A sample mpw tool that asks the finder to launch any of the
            objects provided on the command line.


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

#include <Types.h>
#include <QuickDraw.h>
#include <string.h>
#include <strings.h>
#include <StdIO.h>
#include "FinderLaunch.h"



QDGlobals   qd; /* QuickDraw globals */


int main(long argc, char** argv) {
    Str255 name;
    OSErr err;
    long i;
    FSSpec spec;
    InitGraf(&qd.thePort);
    for ( i=1; i<argc; i++) {
        c2pstr(strcpy((char*)name, argv[i]));
        err = FSMakeFSSpec(0, 0, name, &spec);
        if (err != noErr) goto bail;
        err = FinderLaunch(1, &spec);
        if (err != noErr) goto bail;
    }
    return 0;
bail:
    fprintf(stderr, "\n# %s error = %d\n", argv[0], err);
    return 1;
}
```

[Next](CodeWarrior%20%28OS%209%29-MPWTool-FinderLaunchTool.r.md)[Previous](CodeWarrior%20%28OS%209%29-MPWTool-FinderLaunch.h.md)

