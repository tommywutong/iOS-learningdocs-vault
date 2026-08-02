---
title: GeometryTest
apple_id: DTS10000103
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/GeometryTest/Listings/Textures_h.html
archived_at: '2026-07-18T03:10:45.611978Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GeometryTest](GeometryTest.md)


[Next](Document%20Revision%20History.md)[Previous](Textures.c.md)

# Textures.h

```c
// routines to allow us to put texture maps on a parameterized group
#ifndef _TEXTURES_H_
#define _TEXTURES_H_

#include "PictRead.h"       // this is a library file from QD3D applications folder

TQ3Status AddTextureToGroup( TQ3GroupObject theGroup, TQ3StoragePixmap *textureImage) ;
TQ3Status PictureFileToPixmap( TQ3StoragePixmap *bMap ) ;
TQ3Status TextureGroup( TQ3GroupObject  theGroup) ;

#endif
```

[Next](Document%20Revision%20History.md)[Previous](Textures.c.md)

