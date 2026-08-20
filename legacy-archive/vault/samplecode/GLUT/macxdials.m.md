---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/macx_dials_m.html
archived_at: '2026-07-18T03:29:24.882317Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](macxdstr.m.md)[Previous](macxcursor.m.md)

# macx_dials.m

```objc

/* Copyright (c) Dietmar Planitzer, 1998, 2002 */

/* This program is freely distributable without licensing fees 
   and is provided without guarantee or warrantee expressed or 
   implied. This program is -not- in the public domain. */

#import "macx_glut.h"
#import "GLUTView.h"




void APIENTRY glutButtonBoxFunc(void (*func)(int button, int state))
{
   GLUTAPI_DECLARATIONS_FAST
   GLUTAPI_BEGIN_FAST
      [__glutCurrentView setButtonBoxCallback: func];
   GLUTAPI_END_FAST
}

void APIENTRY glutDialsFunc(void (*func)(int dial, int value))
{
   GLUTAPI_DECLARATIONS_FAST
   GLUTAPI_BEGIN_FAST
      [__glutCurrentView setDialCallback: func];
   GLUTAPI_END_FAST
}
```

[Next](macxdstr.m.md)[Previous](macxcursor.m.md)

