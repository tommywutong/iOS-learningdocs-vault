---
title: GeometryTest
apple_id: DTS10000103
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/GeometryTest/Listings/Geometries_h.html
archived_at: '2026-07-18T03:10:45.268360Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GeometryTest](GeometryTest.md)


[Next](GTFile.c.md)[Previous](Geometries.c.md)

# Geometries.h

```
// Geometries.h

#ifndef _GEOMETRIES_H_
#define _GEOMETRIES_H_

/*===========================================================================*\
 *
 *  Types
 *
\*===========================================================================*/
typedef struct TextureRec {
    char                fileName[32];
    long                size;
    long                dirty;
    TQ3StoragePixmap    pixmap;
    TQ3ShaderObject     shader;
    long                on;
} TextureRec;




TQ3GroupObject BuildGeometry( int type )  ;


#endif
```

[Next](GTFile.c.md)[Previous](Geometries.c.md)

