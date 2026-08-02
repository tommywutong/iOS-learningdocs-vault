---
title: BoxMooV
apple_id: DTS10000099
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BoxMooV/Listings/sources_BoxPaint_utility_c.html
archived_at: '2026-07-18T03:02:15.497412Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BoxMooV](BoxMooV.md)


[Next](Document%20Revision%20History.md)[Previous](sources-BoxPaintSupport.c.md)

# sources/BoxPaint_utility.c

```c
/*  utility.c                                                                           

    Nick Thompson
    Michael Bishop - August 21 1996                                                 
    (c)1994-96 Apple computer Inc., All Rights Reserved                             

*/

/* --------------------------------------------------------------------
** INCLUDES
*/
#include    <QuickDraw.h>
#include    <Events.h>

#include    "BoxPaint_utility.h"


/* --------------------------------------------------------------------
** GLOBAL VARIABLES
*/


/* --------------------------------------------------------------------
** LOCAL FUNCTION DEFINITIONS
*/


/*  --------------------------------------------------------------------
**  Utility_HiWrd
**  DESCRIPTION
*/
short Utility_HiWrd(long aLong)
{
    return  (((aLong) >> 16) & 0xFFFF) ;
}

/*  --------------------------------------------------------------------
**  Utility_LoWrd
**  DESCRIPTION
*/
short Utility_LoWrd(long aLong)
{
    return  ((aLong) & 0xFFFF) ;

}


/*  --------------------------------------------------------------------
**  Utility_MyGetMouse
**  Abstract GetMouse Function for Porting
*/
void Utility_MyGetMouse(TQ3Point2D *thePoint)
{
    Point macPoint;

    GetMouse(&macPoint);

/*  GlobalToLocal(&macPoint);
*/  
    thePoint->x = (float)(macPoint.h);
    thePoint->y = (float)(macPoint.v);
}

/*  --------------------------------------------------------------------
**  Utility_MyStillDown
**  Abstract StillDown Function for Porting
*/
int Utility_MyStillDown(void)
{
    return StillDown();
}
```

[Next](Document%20Revision%20History.md)[Previous](sources-BoxPaintSupport.c.md)

