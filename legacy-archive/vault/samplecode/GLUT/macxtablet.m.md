---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/macx_tablet_m.html
archived_at: '2026-07-18T03:29:26.615452Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](macxutil.m.md)[Previous](macxswap.m.md)

# macx_tablet.m

```objc

/* Copyright (c) Dietmar Planitzer, 1998, 2002 */

/* This program is freely distributable without licensing fees 
   and is provided without guarantee or warrantee expressed or 
   implied. This program is -not- in the public domain. */

#import "macx_glut.h"
#import "GLUTView.h"


/* CENTRY */
void APIENTRY glutTabletMotionFunc(void (*func)(int x, int y))
{
   GLUTAPI_DECLARATIONS_FAST
   GLUTAPI_BEGIN_FAST
    [__glutCurrentView setTabletMotionCallback: func];
   GLUTAPI_END_FAST
}

void APIENTRY glutTabletButtonFunc(void (*func)(int button, int state, int x, int y))
{
   GLUTAPI_DECLARATIONS_FAST
   GLUTAPI_BEGIN_FAST
    [__glutCurrentView setTabletButtonCallback: func];
   GLUTAPI_END_FAST
}
/* ENDCENTRY */
```

[Next](macxutil.m.md)[Previous](macxswap.m.md)

