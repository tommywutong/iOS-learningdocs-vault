---
title: QTMusicToo
apple_id: DTS10000915
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-19'
source_url: https://developer.apple.com/library/archive/samplecode/QTMusicToo/Listings/BigEasy_BigEasyUtils_h.html
archived_at: '2026-07-18T03:21:05.421981Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTMusicToo](QTMusicToo.md)


[Next](BigEasy-IconUtilsPriv.h.md)[Previous](BigEasy-BigEasyUtils.c.md)

# BigEasy/BigEasyUtils.h

```
/*
    File:       BigEasyUtils.h

    Contains:   xxx put contents here xxx

    Written by: xxx put writers here xxx

    Copyright:  

    Change History (most recent first):

         <2>    11-10-94    dvb     GetModKeys

*/

/* file: BigEasyUtils.h
  *
  * Started 25 January 1992, more or less.
  *
  * Little Extras that go
  * well with BigEasy.
  *
  */

/*--------------------------
    Types and globals
--------------------------*/


#define SignIt(x) ( (x)?1:-1)


/*--------------------------
    Routines
--------------------------*/

void SetMenuItemRange(short loRef,short hiRef,short active,short bulletRef);
long RememberThis(long what,short which);
void CenterRect(Rect *centerThis,Rect *insideThis);
short GetModKeys(void);
```

[Next](BigEasy-IconUtilsPriv.h.md)[Previous](BigEasy-BigEasyUtils.c.md)

