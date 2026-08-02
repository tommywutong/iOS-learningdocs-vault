---
title: GLUTBasics
apple_id: DTS10003150
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2004-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/GLUTBasics/Listings/trackball_h.html
archived_at: '2026-07-18T03:10:32.838399Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUTBasics](GLUTBasics.md)


[Next](Document%20Revision%20History.md)[Previous](trackball.c.md)

# trackball.h

```

#ifndef __trackball_h__
#define __trackball_h__

#ifdef __cplusplus
extern "C" {
#endif

void startTrackball (long x, long y, long originX, long originY, long width, long height);
void rollToTrackball (long x, long y, float rot [4]); // rot is output rotation angle
void addToRotationTrackball (float * dA, float * A);

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Document%20Revision%20History.md)[Previous](trackball.c.md)

