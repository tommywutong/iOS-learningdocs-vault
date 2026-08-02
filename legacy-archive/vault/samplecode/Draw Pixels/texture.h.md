---
title: Draw Pixels
apple_id: DTS10000524
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2003-07-16'
source_url: https://developer.apple.com/library/archive/samplecode/Draw_Pixels/Listings/texture_h.html
archived_at: '2026-07-18T03:07:14.417085Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Draw Pixels](Draw%20Pixels.md)


[Next](Document%20Revision%20History.md)[Previous](texture.c.md)

# texture.h

```

/* texture.h - by David Blythe, SGI */

/* Simple SGI .rgb image file loader routine. */
unsigned *
read_texture(char *name, int *width, int *height, int *components);

extern void imgLoad(char *filenameIn, 
  int borderIn, GLfloat borderColorIn[4],
  int *wOut, int *hOut, GLubyte ** imgOut);
```

[Next](Document%20Revision%20History.md)[Previous](texture.c.md)

