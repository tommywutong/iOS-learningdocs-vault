---
title: DigitizerShell
apple_id: DTS10000799
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/DigitizerShell/Listings/AppConfiguration_h.html
archived_at: '2026-07-18T03:06:53.087530Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DigitizerShell](DigitizerShell.md)


[Next](DTSQTUtilities.c.md)[Previous](DigitizerShell.md)

# AppConfiguration.h

```c
/*
    File:       AppConfiguration.h

    Contains:   Values for configuration purposes inside the actual application.

    Written by:     

    Copyright:  Copyright © 1994-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/28/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/


#pragma once


#include <Movies.h>


// TOOLBOX CONSTANTS
enum eBasicConstants {
    kWNEDefaultSleep = 0,                                                               // WNE Sleep time value
    kDefaultSysBeep = 10
};

enum eWindowConstants {
    kDefaultX = 100,
    kDefaultY = 100
};
```

[Next](DTSQTUtilities.c.md)[Previous](DigitizerShell.md)

