---
title: Desktop Sprites
apple_id: DTS10001036
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Desktop_Sprites/Listings/Completed_Lab_main_h.html
archived_at: '2026-07-18T03:06:47.109105Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Desktop Sprites](Desktop%20Sprites.md)


[Next](MacPrefix.h.md)[Previous](Completed%20Lab-main.c.md)

# Completed Lab/main.h

```c
#ifndef _MAININCLUDES_
#define _MAININCLUDES_

//#define TARGET_API_MAC_CARBON 1

#include <ConditionalMacros.h>
#include <MacTypes.h>

#include <MacMemory.h>
#include <Errors.h>
#include <Fonts.h>
#include <QuickDraw.h>
#include <Resources.h>
#include <Gestalt.h>
#include <FixMath.h>
#include <Sound.h>
#include <string.h>
#include <Movies.h>
#include <ImageCompression.h>
#include <Script.h>
#include <TextUtils.h>
#include <Processes.h>

#ifndef _IMAGECOMPRESSIONUTILITIES_
#include "ImageCompressionUtilities.h"
#endif

#include "createsprites.h"
#include "animsprite.h"
#include "dispsprite.h"

// constants
#define kNumSprites             4
#define kNumSpaceShipImages     24
#define kBackgroundPictID       158
#define kFirstSpaceShipPictID   (kBackgroundPictID + 1)
#define kSpaceShipWidth         106
#define kSpaceShipHeight        80

// global variables

extern SpriteWorld                      gSpriteWorld;
extern GWorldPtr                        gSpritePlane;
extern Sprite                           gSprites[kNumSprites];
extern Handle                           gCompressedPictures[kNumSpaceShipImages];
extern ImageDescriptionHandle           gImageDescriptions[kNumSpaceShipImages];
extern Rect                             gBounceBox;
extern Rect                             gDestRects[kNumSprites];
extern Point                            gDeltas[kNumSprites];
extern short                            gCurrentImages[kNumSprites];
extern Handle                           gCompressedPictures[kNumSpaceShipImages];
extern RGBColor                         gBackgroundColor;



#endif
```

[Next](MacPrefix.h.md)[Previous](Completed%20Lab-main.c.md)

