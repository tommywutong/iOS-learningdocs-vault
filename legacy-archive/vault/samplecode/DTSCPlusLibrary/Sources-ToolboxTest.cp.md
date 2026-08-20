---
title: DTSCPlusLibrary
apple_id: DTS10000731
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/DTSCPlusLibrary/Listings/Sources_ToolboxTest_cp.html
archived_at: '2026-07-18T03:05:59.515168Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DTSCPlusLibrary](DTSCPlusLibrary.md)


[Next](Sources-Tracer.cp.md)[Previous](Sources-Toolbox.cp.md)

# Sources/ToolboxTest.cp

```c
/*
    File:       ToolboxTest.cp

    Contains:   TToolbox is a Toolbox initialization and testing class.
                TestToolbox.cp contains the testing code for testing TToolbox.

    Written by:  Kent Sandvik   

    Copyright:  Copyright © 1992-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/18/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#ifndef _TOOLBOX_
#include "Toolbox.h"
#endif

// This is a trivial test, all it does is to call the init phase of the TToolbox class,
// and that all it should do anywayÉ

void main(void)
{
    cout << "Start of TToolbox testÉ\n";

    //  Initialize environment.
    TToolbox myToolbox;
    myToolbox.Initialize();

    cout << "End of TToolbox test!\n";
}

// _________________________________________________________________________________________________________ //


/*  Change History (most recent last):
  No        Init.   Date        Comment
  1         khs     6/6/92      New file
  2         khs     1/3/93      Cleanup
*/
```

[Next](Sources-Tracer.cp.md)[Previous](Sources-Toolbox.cp.md)

