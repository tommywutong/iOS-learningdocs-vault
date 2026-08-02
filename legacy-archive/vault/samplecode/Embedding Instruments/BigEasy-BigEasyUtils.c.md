---
title: Embedding Instruments
apple_id: DTS10000321
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Embedding_Instruments/Listings/BigEasy_BigEasyUtils_c.html
archived_at: '2026-07-18T03:07:43.759616Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Embedding Instruments](Embedding%20Instruments.md)


[Next](BigEasy-BigEasyUtils.h.md)[Previous](BigEasy-BigEasyTextish.h.md)

# BigEasy/BigEasyUtils.c

```c
/* file: BigEasyUtils.c
  *
  * Started 25 January 1992, more or less.
  *
  * Little Extras that go
  * well with BigEasy.
  *
  */


/*----------------
    Inclusions
----------------*/


#include "BigEasy2.h"
#include "BigEasyUtils.h"


/*----------------
    Dofu
----------------*/


void SetMenuItemRange(short loRef,short hiRef,short active,short bulletRef)
/*
 * Set the range of menu-refs passed to either
 * active or inactive (±1) and bullet the
 * one that matches 'bulletref'
 */
    {
    short i;

    for(i = loRef; i<= hiRef; i++)
        SetMenuItem(i,active,SignIt(bulletRef == i),'¥',nil);
    }



#ifdef THINK_C
    long RememberThis(long what,short which)
    /*
     * To store something, pass what, and a negative "which".
     * To retrieve it, pass the positive which.
     */
        {
        asm {
            LEA     @them,A0
            MOVE    which,D0
            ADD     D0,D0
            ADD     D0,D0
            BMI.S   @stash
            ADDA    D0,A0
            MOVE.L  (A0),D0
            BRA.S   @done
    @stash:
            SUBA    D0,A0
            MOVE.L  what,(A0)
            MOVE.L  what,D0
            BRA.S   @done

    @them   DC.L    0,0,0,0,0,0,0,0,0,0,0

    @done:
            }
        }
#endif


void CenterRect(Rect *centerThis,Rect *insideThis)
    {
    OffsetRect(centerThis,
            (insideThis->left + insideThis->right - centerThis->left - centerThis->right)>>1,
            (insideThis->top + insideThis->bottom - centerThis->top - centerThis->bottom)>>1);
    }
```

[Next](BigEasy-BigEasyUtils.h.md)[Previous](BigEasy-BigEasyTextish.h.md)

