---
title: RAVE Starter Samples
apple_id: DTS10000155
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/RAVE_Starter_Samples/Listings/RAVE_CommonCode_RAVE_Utilities_h.html
archived_at: '2026-07-18T03:21:48.256010Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RAVE Starter Samples](RAVE%20Starter%20Samples.md)


[Next](Texture%20Sample-Texture%20Triangle.cp.md)[Previous](RAVE%20CommonCode-RAVE%20Utilities.cp.md)

# RAVE CommonCode/RAVE Utilities.h

```c
/*
    File:       RAVE Utilities.h

    Contains:   RAVE Utilities defines a number of useful functions for working with RAVE,
                including functions to find the deepest GDevice, loading textures from a PICT
                resource, and so on. Essentially, it defines a number of pieces of common code
                that were useful to many of my projects.

    Written by: Timothy Carroll 

    Copyright:  Copyright © 1998-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/15/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/

#ifndef _RAVEUTILITIES_
#define _RAVEUTILITIES_

#pragma once

#include <RAVE.h>
#include "Common Stuff.h"


/*****************************************************************************
LOOKUP TABLES

I use SIN and COS in a number of places, and we don't need perfect precision,
so we generate a set of lookup tables on 0.5 degree increments.  Most of the
3D math routines use these lookups to generate matrices.
*****************************************************************************/

extern float gSinArray[721]; // [720] = [0]
extern float gCosArray[721]; // [720] = [0]

OSStatus InitializeLookups(void);


/*****************************************************************************
RAVE ENGINE FUNCTIONS

FindTextureMappingEngine walks the list of available engines and returns
the first engine capable of Texture Mapping.

GetListOfEngines creates a handle filled with references to all engines
available to the application.   
*****************************************************************************/

TQAEngine   *FindTextureMappingEngine (TQADevice *device);
OSStatus    GetListOfEngines (GDHandle screen, Handle *list, long *number);


/*****************************************************************************
TEXTURES

LoadTextureFromPictResource loads a PICT resource, draws it into an offscreen
GWorld, creates a RAVE texture, and then detaches it so that the engine is
responsible for managing it.  Complete texture management code would probably
want to make sure that the textures are also available as a GWorld, so that
they can be quickly loaded and unloaded from the card.
*****************************************************************************/

TQATexture  *LoadTextureFromPictResource (TQAEngine *engine, short pictID);


#endif _RAVEUTILITIES_
```

[Next](Texture%20Sample-Texture%20Triangle.cp.md)[Previous](RAVE%20CommonCode-RAVE%20Utilities.cp.md)

