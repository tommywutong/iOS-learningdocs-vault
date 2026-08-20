---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/glut_bwidth_c.html
archived_at: '2026-07-18T03:29:20.281283Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](glutcindex.c.md)[Previous](glutbitmap.c.md)

# glut_bwidth.c

```c

/* Copyright (c) Mark J. Kilgard, 1994. */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */

#if defined(__APPLE__)
#include "glut.h"
#include "macx_utilities.h"
#else
#include "glutint.h"
#endif
#include "glutbitmap.h"

/* CENTRY */
int APIENTRY 
glutBitmapWidth(GLUTbitmapFont font, int c)
{
  BitmapFontPtr fontinfo;
  const BitmapCharRec *ch;

#ifdef _WIN32
  fontinfo = (BitmapFontPtr) __glutFont(font);
#else
  fontinfo = (BitmapFontPtr) font;
#endif

  if (c < fontinfo->first || c >= fontinfo->first + fontinfo->num_chars)
    return 0;
  ch = fontinfo->ch[c - fontinfo->first];
  if (ch)
    return ch->advance;
  else
    return 0;
}

int APIENTRY 
glutBitmapLength(GLUTbitmapFont font, const unsigned char *string)
{
  int c, length;
  BitmapFontPtr fontinfo;
  const BitmapCharRec *ch;

#ifdef _WIN32
  fontinfo = (BitmapFontPtr) __glutFont(font);
#else
  fontinfo = (BitmapFontPtr) font;
#endif

  length = 0;
  for (; *string != '\0'; string++) {
    c = *string;
    if (c >= fontinfo->first && c < fontinfo->first + fontinfo->num_chars) {
      ch = fontinfo->ch[c - fontinfo->first];
      if (ch)
        length += ch->advance;
    }
  }
  return length;
}

/* ENDCENTRY */
```

[Next](glutcindex.c.md)[Previous](glutbitmap.c.md)

