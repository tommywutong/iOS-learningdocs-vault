---
title: Embedding Instruments
apple_id: DTS10000321
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Embedding_Instruments/Listings/BigEasy_BigEasyUtils_h.html
archived_at: '2026-07-18T03:07:43.822391Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Embedding Instruments](Embedding%20Instruments.md)


[Next](BigEasy-IconUtilsPriv.h.md)[Previous](BigEasy-BigEasyUtils.c.md)

# BigEasy/BigEasyUtils.h

```
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
```

[Next](BigEasy-IconUtilsPriv.h.md)[Previous](BigEasy-BigEasyUtils.c.md)

