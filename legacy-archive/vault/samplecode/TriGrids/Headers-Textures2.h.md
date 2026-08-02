---
title: TriGrids
apple_id: DTS10000105
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TriGrids/Listings/Headers_Textures2_h.html
archived_at: '2026-07-18T03:27:19.531489Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TriGrids](TriGrids.md)


[Next](Headers-TriGrid3DSupport.h.md)[Previous](Headers-MathUtilities.h.md)

# Headers/Textures2.h

```c
// routines to allow us to put texture maps on a parameterized group
#ifndef _TEXTURES_H_
#define _TEXTURES_H_

#include "PictRead.h"       // this is a library file from QD3D applications folder

TQ3Status AddTextureToGroup( TQ3GroupObject theGroup, TQ3StoragePixmap *textureImage) ;
void PictureFileToPixmap( TQ3StoragePixmap *bMap ) ;
void TextureGroup( TQ3GroupObject   theGroup) ;
void AddResourceTextureToGroup( short pictResID, TQ3GroupObject theGroup ) ;

#endif
```

[Next](Headers-TriGrid3DSupport.h.md)[Previous](Headers-MathUtilities.h.md)

