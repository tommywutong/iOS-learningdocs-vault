---
title: MoofWarsOld
apple_id: DTS10000057
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoofWarsOld/Listings/MoofEncoder_Color_Search_Procs_h.html
archived_at: '2026-07-18T03:15:01.801890Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoofWarsOld](MoofWarsOld.md)


[Next](MoofEncoder-GridEncode.cp.md)[Previous](MoofEncoder-Color%20Search%20Procs.cp.md)

# MoofEncoder/Color Search Procs.h

```c
/*
    File:       Color Search Procs.h

    Contains:   This file defines a number of commonly used color search procs.  For the encoder,
                we only use one of the procs, which returns white if the color of a pixel is within
                a certain delta of a key color, and returns black for all other cases.  We can use
                this to quickly create masks of an image.


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
                7/1/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1
                2/24/97     Timothy Carroll Now explicitly include Main.h
                8/15/96     Timothy Carroll Initial Release



*/

#ifndef _COLORSEARCHPROC_
#define _COLORSEARCHPROC_

#pragma once

#include "Main.h"
#include <QuickDraw.h>
// We included main to get our black and white color constants.  If you don't have main.h,
// uncomment these two lines and remove the include.

//const RGBColor kWhite = {0xFFFF, 0xFFFF, 0xFFFF};
//const RGBColor kBlack = {0x0000, 0x0000, 0x0000};

extern ColorSearchUPP MaskSearchProcUPP;
extern ColorSearchUPP LightenSearchProcUPP;
extern ColorSearchUPP DarkenSearchProcUPP;

extern RGBColor gMaskColor;
extern SInt32   gSearchDelta;


#endif // _COLORSEARCHPROC_
```

[Next](MoofEncoder-GridEncode.cp.md)[Previous](MoofEncoder-Color%20Search%20Procs.cp.md)

