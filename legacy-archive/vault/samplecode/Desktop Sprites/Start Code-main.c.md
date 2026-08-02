---
title: Desktop Sprites
apple_id: DTS10001036
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Desktop_Sprites/Listings/Start_Code_main_c.html
archived_at: '2026-07-18T03:06:47.501122Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Desktop Sprites](Desktop%20Sprites.md)


[Next](Document%20Revision%20History.md)[Previous](Start%20Code-ImageCompressionUtilities.c.md)

# Start Code/main.c

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

// Step 6.
// Insert "SpriteWorldIdle.clp" here

    }

    MyDisposeEverything();

    return (0);
}
```

[Next](Document%20Revision%20History.md)[Previous](Start%20Code-ImageCompressionUtilities.c.md)

