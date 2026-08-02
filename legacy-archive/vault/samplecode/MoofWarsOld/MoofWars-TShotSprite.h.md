---
title: MoofWarsOld
apple_id: DTS10000057
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoofWarsOld/Listings/MoofWars_TShotSprite_h.html
archived_at: '2026-07-18T03:15:03.429341Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoofWarsOld](MoofWarsOld.md)


[Next](MoofWars-TSprite.cp.md)[Previous](MoofWars-TShotSprite.cp.md)

# MoofWars/TShotSprite.h

```c
/*
    File:       TShotSprite.h

    Contains:   This class represents any shots in the game, friendly or enemy.

    Written by:  Timothy Carroll    

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

                8/15/96     Timothy Carroll Initial Release


*/

#ifndef _TSHOTSPRITE_
#define _TSHOTSPRITE_

#pragma once

#include "TSprite.h"

#if PRAGMA_STRUCT_ALIGN
#pragma options align=power
#endif


struct TShotSpriteData
{
    TSpriteData spriteData;
    SInt16      duration;
};

class TShotSprite : public TSprite
{
    public:

    enum {
        kSpriteType = 'SHOT'
    };

    TShotSprite (TShotSpriteData *data);
    ~TShotSprite (void);

    virtual void ProcessSprite (void);
    virtual void Collision (TSprite *theSprite);

    protected:

    SInt16 fDuration;

};

#if PRAGMA_STRUCT_ALIGN
#pragma options align=reset
#endif

#endif /* _TSHOTSPRITE_ */
```

[Next](MoofWars-TSprite.cp.md)[Previous](MoofWars-TShotSprite.cp.md)

