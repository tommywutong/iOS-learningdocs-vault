---
title: Bitblitz
apple_id: DTS10000066
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/Bitblitz/Listings/Resources_AlertDlogUtils_r.html
archived_at: '2026-07-18T03:01:55.648381Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Bitblitz](Bitblitz.md)


[Next](Resources-BitBlitz.r.md)[Previous](LibHeaders-WCenter.h.md)

# Resources/AlertDlogUtils.r

```c

/*======================================================================================*/
/*  File:   AlertDlogUtils.r                                                            */
/*                                                                                      */
/*  By:     George Delaney                                                              */
/*          Mac CPU Software Quality                                                    */
/*  Date:   5/14/90                                                                     */
/*                                                                                      */
/*  Contents:                                                                           */
/*  All resource declarations needed to support the AlertDlogUtils library file.        */
/*======================================================================================*/


#include "Types.r"



/*--------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------*/
/*  Alerts  */


/*--------------------------------------------------------------------------------------*/
/*  Generic text string alert box   */

resource 'ALRT' (5000) {{46, 106, 146, 421},5000,{
        OK, visible, sound1,
        OK, visible, sound1,
        OK, visible, sound1,
        OK, visible, sound1}};

resource 'DITL' (5000) {{
    { 75, 128,  95, 188},   Button      {enabled,"OK"},
    {  5,   4,  71, 311},   StaticText  {disabled,"^0"}
}};
```

[Next](Resources-BitBlitz.r.md)[Previous](LibHeaders-WCenter.h.md)

