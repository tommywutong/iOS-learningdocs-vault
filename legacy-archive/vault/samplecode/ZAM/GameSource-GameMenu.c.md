---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameSource_GameMenu_c.html
archived_at: '2026-07-18T03:28:33.200441Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameSource-GameSounds.c.md)[Previous](GameSource-GameAEvents.c.md)

# GameSource/GameMenu.c

```c
/*
*/

#include "MenuDispatch.h"

#include "GameMenu.proto.h"


void ChooseGame(short item)
{
    switch(item) {
        case 1: SoundEnable();
            break;
    }
}
```

[Next](GameSource-GameSounds.c.md)[Previous](GameSource-GameAEvents.c.md)

