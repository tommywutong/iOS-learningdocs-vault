---
title: QTMusicToo
apple_id: DTS10000915
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-19'
source_url: https://developer.apple.com/library/archive/samplecode/QTMusicToo/Listings/BigEasy_BigEasyGestalt_h.html
archived_at: '2026-07-18T03:21:04.358867Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTMusicToo](QTMusicToo.md)


[Next](BigEasy-BigEasyGrafish.c.md)[Previous](BigEasy-BigEasyGestalt.c.md)

# BigEasy/BigEasyGestalt.h

```c
/*
    File:       BigEasyGestalt.h

    Contains:   xxx put contents here xxx

    Written by: xxx put writers here xxx

    Copyright:  © 1992 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

         <2>      1/7/93    dvb     More selectors.
         <1>     1/20/92    dvb     first checked in

*/

/* file: BigEasyGestalt.h
 *
 * Started 28 December 1991, more or less.
 *
 */



/*--------------------------
    Inclusions
--------------------------*/

#include <GestaltEqu.h>

/*--------------------------
    Constants
--------------------------*/

#define kEasyGestaltPPC 0L
#define kEasyGestaltColor 1L
#define kEasyGestaltQuickTime 2L
#define kEasyGestaltImageCompression 3L
#define kEasyGestaltComponents 4L
#define kEasyGestaltFSSpecs 5L
#define kEasyGestaltFPU 6L
#define kEasyGestaltSoundInputDevice 7L
#define kLastEasyGestaltKnownFeature 8L


/*--------------------------
    Types
--------------------------*/

typedef struct
    {
    long type;                          /* Gestalt selector */
    long mask;                          /* Mask, result must be nonzero */
    Boolean canRunWithout;              /* Just warn the user, but run anyway? */
    unsigned char *unpresentWarning;    /* Message for the user if this feature absent */
    } EasyGestaltItem;



/*--------------------------
    Routines
--------------------------*/

Boolean CheckEasyGestaltItem(EasyGestaltItem *egi);
Boolean CheckEasyGestaltItemList(long count, EasyGestaltItem egiList[]);

Boolean CheckEasyGestaltKnownFeature(Boolean canRunWithout,long feature);   /* uses enum above */
Boolean CheckEasyGestaltKnownFeatures(Boolean canRunWithout,
        short count,long feature1,...); /* uses enum above */
```

[Next](BigEasy-BigEasyGrafish.c.md)[Previous](BigEasy-BigEasyGestalt.c.md)

