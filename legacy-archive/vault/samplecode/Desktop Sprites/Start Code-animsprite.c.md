---
title: Desktop Sprites
apple_id: DTS10001036
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Desktop_Sprites/Listings/Start_Code_animsprite_c.html
archived_at: '2026-07-18T03:06:47.385568Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Desktop Sprites](Desktop%20Sprites.md)


[Next](Start%20Code-createsprites.c.md)[Previous](MacPrefix.h.md)

# Start Code/animsprite.c

```c

#ifndef _MAININCLUDES_
#include "main.h"
#endif

void MyMoveSprites (void)
{
    short               nIndex;
    MatrixRecord                matrix;

    SetIdentityMatrix(&matrix);

    // for each sprite
    for (nIndex = 0; nIndex < kNumSprites; nIndex++) {

        // modify the spriteÕs matrix
        OffsetRect(&gDestRects[nIndex], gDeltas[nIndex].h,
                    gDeltas[nIndex].v);

        if ((gDestRects[nIndex].right >= gBounceBox.right) ||
            (gDestRects[nIndex].left <= gBounceBox.left))
            gDeltas[nIndex].h = -gDeltas[nIndex].h;

        if ((gDestRects[nIndex].bottom >= gBounceBox.bottom) ||
            (gDestRects[nIndex].top <= gBounceBox.top))
            gDeltas[nIndex].v = -gDeltas[nIndex].v;

        matrix.matrix[2][0] = ((long)gDestRects[nIndex].left << 16);
        matrix.matrix[2][1] = ((long)gDestRects[nIndex].top << 16);

// Step 4.
// Insert "SetSpriteMatrix.clp" here


        // change the spriteÕs image
        gCurrentImages[nIndex]++;
        if (gCurrentImages[nIndex] >= (kNumSpaceShipImages *
                                        (nIndex+1)))
        {
            gCurrentImages[nIndex] = 0;
        }

// Step 5.
// Insert "SetSpriteImage.clp" here

    }
}
```

[Next](Start%20Code-createsprites.c.md)[Previous](MacPrefix.h.md)

