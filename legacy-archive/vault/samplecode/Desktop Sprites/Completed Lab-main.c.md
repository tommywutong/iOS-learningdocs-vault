---
title: Desktop Sprites
apple_id: DTS10001036
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Desktop_Sprites/Listings/Completed_Lab_main_c.html
archived_at: '2026-07-18T03:06:47.077169Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Desktop Sprites](Desktop%20Sprites.md)


[Next](Completed%20Lab-main.h.md)[Previous](Completed%20Lab-ImageCompressionUtilities.h.md)

# Completed Lab/main.c

```c
#include <MacWindows.h>
#include <ImageCompression.h>
#include <QuickTimeComponents.h>

#ifndef _MAININCLUDES_
#include "main.h"
#endif


SpriteWorld                     gSpriteWorld = NULL;
GWorldPtr                       gSpritePlane = NULL;
Sprite                          gSprites[kNumSprites];
Handle                          gCompressedPictures[kNumSpaceShipImages];
ImageDescriptionHandle          gImageDescriptions[kNumSpaceShipImages];
Rect                            gBounceBox;
Rect                            gDestRects[kNumSprites];
Point                           gDeltas[kNumSprites];
short                           gCurrentImages[kNumSprites];
Handle                          gCompressedPictures[kNumSpaceShipImages];
RGBColor                        gBackgroundColor;

#define kWNEDefaultSleep            0               // WaitNextEvent sleep time


int main( void );

int main( void )
{
    OSErr err = noErr;
    Rect bounds = {50,50,400,400};
    WindowPtr window = nil;

    InitCursor();

    err = EnterMovies();

    // Create a window to display our sprites
    window = NewCWindow( nil, &bounds, "\pDesktop Sprites", true, documentProc, 
                        (WindowPtr)-1, true, 0);
    if (window != nil)
    {
        SetPortWindowPort(window);
    }

    // Create our sprite world & sprites
    CreateSpriteStuff (&bounds, GetWindowPort(window));

    while (!Button())
    {
        // Animate the sprites
        MyMoveSprites();

        SpriteWorldIdle(gSpriteWorld,   /* the sprite world for this operation */
                        0,              /* Contains flags describing actions that may take place during the idle. */
                        0);             /* On return, contains a pointer to flags describing actions that
                                        took place during the idle. */
    }

    MyDisposeEverything();

    return (0);
}
```

[Next](Completed%20Lab-main.h.md)[Previous](Completed%20Lab-ImageCompressionUtilities.h.md)

