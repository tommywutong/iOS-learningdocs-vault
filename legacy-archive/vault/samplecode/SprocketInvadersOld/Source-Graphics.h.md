---
title: SprocketInvadersOld
apple_id: DTS10000061
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SprocketInvadersOld/Listings/Source_Graphics_h.html
archived_at: '2026-07-18T03:25:26.730125Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SprocketInvadersOld](SprocketInvadersOld.md)


[Next](Source-main.c.md)[Previous](Source-Graphics.c.md)

# Source/Graphics.h

```c
//¥ ------------------------------------------------------------------------------------------  ¥
//¥
//¥ Copyright © 1996 Apple Computer, Inc., All Rights Reserved
//¥
//¥
//¥     You may incorporate this sample code into your applications without
//¥     restriction, though the sample code has been provided "AS IS" and the
//¥     responsibility for its operation is 100% yours.  However, what you are
//¥     not permitted to do is to redistribute the source as "DSC Sample Code"
//¥     after having made changes. If you're going to re-distribute the source,
//¥     we require that you make it clear in the source that the code was
//¥     descended from Apple Sample Code, but that you've made changes.
//¥
//¥     Authors:
//¥         Chris De Salvo
//¥
//¥ ------------------------------------------------------------------------------------------  ¥

#ifndef __GRAPHICS__
#define __GRAPHICS__

//¥ ------------------------------  Includes

#include <DrawSprocket.h>

//¥ ------------------------------  Public Definitions
//¥ ------------------------------  Public Types
//¥ ------------------------------  Public Variables

extern DSpContextReference  gDisplayContext;
extern DSpContextAttributes gDisplayAttributes;
extern GDHandle gGameGDH;

extern const RGBColor   rgbBlack;
extern const RGBColor   rgbWhite;
extern const RGBColor   rgbRed;
extern const RGBColor   rgbBlue;
extern const RGBColor   rgbYellow;
extern const RGBColor   rgbGreen;

//¥ ------------------------------  Public Functions

#ifdef __cplusplus
extern "C" {
#endif

extern void GraphicsInit(SInt16 modifiers);
extern void GraphicsUpdateScreen(void);
extern void GraphicsLoadBackground(SInt16 whichBG);
extern void GraphicsRepairBackground(void);
extern void GraphicsMergeCLUT(SInt16 clutID, UInt16 firstColor, UInt16 lastColor);
extern void GraphicsOptimizeGWorld(GWorldPtr gw);
extern void GraphicsSetRectDirty(RectPtr r);
extern void GraphicsSetUnderlayRectDirty(RectPtr r);
extern void GraphicsRepairScreenRect(RectPtr r);
extern void GraphicsReset(void);
extern void GraphicsGetUnderlayGrafPort(CGrafPtr *underlay, GDHandle *device);
extern void GraphicsActive(void);
extern void GraphicsPaused(void);
extern void GraphicsInactive(void);
extern void GraphicsDoUpdateEvent(void);

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Source-main.c.md)[Previous](Source-Graphics.c.md)

