---
title: GLUTBasics
apple_id: DTS10003150
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2004-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/GLUTBasics/Listings/SurfaceGeometry_h.html
archived_at: '2026-07-18T03:10:32.548894Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUTBasics](GLUTBasics.md)


[Next](trackball.c.md)[Previous](SurfaceGeometry.c.md)

# SurfaceGeometry.h

```c
#include <OpenGL/gl.h>

#define kSurfaces 6
#define kColorSchemes 21

enum {
    kCube = 0,
    kTranguloidTrefoil,
    kTriaxialTritorus,
    kStilettoSurface,
    kSlippersSurface,
    kMaedersOwl
};

void GetStrings (unsigned int surface, char ** strName, char ** strAuthor, char ** strX, char ** strY, char ** strZ, char ** strRange);

void BuildGeometry (unsigned int surface, unsigned int colorScheme, unsigned int subdivisions, unsigned int xyRatio,
                    GLuint * polyList, GLuint * lineList, GLuint * pointList);
```

[Next](trackball.c.md)[Previous](SurfaceGeometry.c.md)

