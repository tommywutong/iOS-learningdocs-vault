---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/macx_utilities_h.html
archived_at: '2026-07-18T03:29:26.771669Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](macxwarp.m.md)[Previous](macxutil.m.md)

# macx_utilities.h

```

/* Copyright (c) Dietmar Planitzer, 1998 */

/* This program is freely distributable without licensing fees 
   and is provided without guarantee or warrantee expressed or 
   implied. This program is -not- in the public domain. */

#ifndef APIENTRY
#define APIENTRY
#endif

void *__glutGetGLProcAddress(const char *name);

char *  __glutStrdup(const char *string);
void    __glutWarning(char *format,...);
void    __glutFatalError(char *format,...);
void    __glutFatalUsage(char *format,...);

// uses static library routines to make this app foreground capable and set to front
void    __glutSetForeground(void);
```

[Next](macxwarp.m.md)[Previous](macxutil.m.md)

