---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/CoreSource_Document_c.html
archived_at: '2026-07-18T03:28:32.019880Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](CoreSource-ErrMsg.c.md)[Previous](CoreSource-AEventCoreDisp.c.md)

# CoreSource/Document.c

```c
#include "CoreGlobals.h"
#include "ZAM.h"
#include "MenuDispatch.h"


//#define NETWORK_HELL 1

void UpdateGameWindow(WindowPtr graf, gamePtr game)
{
    SpriteUpdateEvent();
}

void OpenGameWindow(WindowPtr   wp, gamePtr game)
{
}

void CloseGameWindow(WindowPtr wp, gamePtr game)
{
}

void SaveGameWindow(WindowPtr   wp, gamePtr game)
{
}

void ClickGameWindow(WindowPtr wp, gamePtr game)
{

#if 0
    Point       click;
    short       dir;
    GrafPtr     savePort;
    fixPt       vel;
    Fixed       velH,velV;

    GetPort(&savePort);
    SetPort(wp);

    click = gEvent.where;
    GlobalToLocal(&click);

    dir = Random() % kNumShotFrames;
    if(dir < 0) dir = -dir;

    //StartExplosionHere(game, ff(click.h), ff(click.v));


    FireMissile( dir, ff(click.h), ff(click.v), false);

    {
        short   i;
        for(i = 0; i < 10; i++) {
            dir += i;
            if(dir >= kNumShotFrames) dir = 0;
            FireMissile( dir, ff(click.h), ff(click.v), false);

        }

        for(i = 0; i < 5; i++) {
            dir += i;
            if(dir >= kNumShotFrames) dir = 0;
            FireMissile( dir, ff(click.h), ff(click.v), false);
        }


    }

    SetPort(savePort);

#endif

#ifdef NETWORK_HELL
    FireNetworkMissile(game, dir, click);
#endif
}

void KeyGameWindow(WindowPtr wp, gamePtr game)
{
}

void AdjustMenuGameWindow(WindowPtr wp, gamePtr game)
{
}

void IdleGameWindow(void)
{

    ProcessXThingTask(10);
    CheckMissileColissions(gGame);
    AnimateSprites();
    SoundKeeper();
    CheckTankDead();
}

void NewGameWindow(void)
{
    NewGame();
}


void ForceRefreshGameWindow(WindowPtr wp, gamePtr game)
{
    GrafPtr     savePort;

    GetPort(&savePort);
    SetPort(wp);

    ValidRect(&wp->portRect);
    UpdateGameWindow(wp, game);

    SetPort(savePort);


}
```

[Next](CoreSource-ErrMsg.c.md)[Previous](CoreSource-AEventCoreDisp.c.md)

