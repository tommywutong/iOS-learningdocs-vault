---
title: MoofWarsOld
apple_id: DTS10000057
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoofWarsOld/Listings/MoofWars_TShotSprite_cp.html
archived_at: '2026-07-18T03:15:03.378379Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoofWarsOld](MoofWarsOld.md)


[Next](MoofWars-TShotSprite.h.md)[Previous](MoofWars-TShipSprite.h.md)

# MoofWars/TShotSprite.cp

```c
/*
    File:       TShotSprite.cp

    Contains:   This class represents any shots in the game, friendly or enemy.

    Written by: Timothy Carroll 

    Copyright:  Copyright © 1996-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/2/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1

                1/23/97     Timothy Carroll Added include for Moofwars.h so that MrC will
                            compile


*/

#include "Moofwars.h"
#include "TShotSprite.h"


TShotSprite::TShotSprite (TShotSpriteData *data):
TSprite((TSpriteData *) data)
{
    fDuration = data->duration;
    gShotsOnBoard +=1;
}


TShotSprite::~TShotSprite (void)
{
    gShotsOnBoard -=1;
}

void
TShotSprite::ProcessSprite (void)
{
// Because of changes in the current implementation, the following code won't compile.
// It implements a primitive seeking algorithm.
//
// We basically look 3 frames ahead and try to move our sprite so that we'll hit the ship.

#if 0
    long deltaX, deltaY;
    deltaX = (gEnemyShipToSeek->fCurrentX+3*gEnemyShipToSeek->fCurVelocityX+(12<<16)
                 - this->fCurrentX-3*this->fCurVelocityX);
    deltaY = (gEnemyShipToSeek->fCurrentY+3*gEnemyShipToSeek->fCurVelocityY+(12<<16)
                 - this->fCurrentY-3*this->fCurVelocityY);

    if (deltaX < 0)
    {
        fCurVelocityX -= (2 << 15);
    }
    else if (deltaX > 0)
    {
        fCurVelocityX += (2 << 15);
    }

    if (deltaY < 0)
    {
        fCurVelocityY -= (2 << 15);
    }
    else if (deltaY > 0)
    {
        fCurVelocityY += (2 << 15);
    }

#endif

    // If the sprite is invisible, we should delete it, otherwise we should make it invisible
    // if its duration is up.
#if qShotsHaveRange
    if (fVisibility == kInvisible)
    {
        delete this;
    }
    else
    {
        fDuration -= 1;
        if (fDuration == 0)
            SetVisibility(kInvisible);
    }
#endif

    TSprite::ProcessSprite();
    TSprite::Bounce (&gWorldBounds);
}

void
TShotSprite::Collision (TSprite *theSprite)
{
#pragma unused (theSprite)

    // Change our sprite to the "hit" shape.
    fFace = 2;

    if (fDuration > 3)
        fDuration = 3;
    // This will delete the sprite.
    //SetVisibility(kInvisible);

}
```

[Next](MoofWars-TShotSprite.h.md)[Previous](MoofWars-TShipSprite.h.md)

