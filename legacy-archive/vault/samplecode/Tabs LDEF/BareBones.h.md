---
title: Tabs LDEF
apple_id: DTS10000621
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/Tabs_LDEF/Listings/BareBones_h.html
archived_at: '2026-07-18T03:26:18.609052Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabs LDEF](Tabs%20LDEF.md)


[Next](Events.c.md)[Previous](BareBones.c.md)

# BareBones.h

```c
/*
    File:       BareBones.h

    Contains:   Common header file included by all source files

    Written by: Chris White 

    Copyright:  Copyright © 1995-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/10/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/



#ifndef __BAREBONES__
#define __BAREBONES__



#ifndef __LISTS__
    #include <Lists.h>
#endif



#define DEBUGGING   1       // Anything that shouldn't normally occur
#define WARNINGS    0       // Something that can occur, but you might like to know about


#define USE_LDEF            // Using the LDEF or including the source code


enum
{
    // Generall application stuff

    kCreatorCode = 'tdem',                  // Tabs Demo
    kSleepTime = 60L

};



enum
{
    // Menu ID numbers

    kMenuBarID = 1000,
    kAppleMenu = 1000,
    kFileMenu = 1001
};



enum
{
    // Apple menu commands

    cAbout = 1
};



enum
{
    // File menu commands

    cQuit = 1
};






enum
{
    // Error strings

    kNeedSystem7 = 1,
    kGenericErrorStr
};



enum
{
    // Windows

    kDisplayWindow = 1000,
    kAboutDialog,
    kErrorDialog
};



enum
{
    // Strings

    kErrorStrings = 1000
};




#define kTabsLDEF       1000

typedef OSErr (*tContentsProcPtr) ( ListRef theList, void* refCon );




// Global Variable Definitions. This allows me to include this file
// in all sources with the extern keyword used in all instances except
// the main source file.

#ifdef __MAIN__
    #define global
#else
    #define global  extern
#endif


global  Boolean                 gQuit;                  /* quit program flag */
global  SInt32                  gSleepTime;



#ifndef USE_LDEF
    #define kLDEFID 0
#else
    #define kLDEFID kTabsLDEF
#endif






#endif  // __BAREBONES__
```

[Next](Events.c.md)[Previous](BareBones.c.md)

