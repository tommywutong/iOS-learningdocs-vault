---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/macx_modifier_m.html
archived_at: '2026-07-18T03:29:26.339562Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](macxoverlay.m.md)[Previous](macxmenu.m.md)

# macx_modifier.m

```objc

/* Copyright (c) Dietmar Planitzer, 1998, 2002 */

/* This program is freely distributable without licensing fees 
   and is provided without guarantee or warrantee expressed or 
   implied. This program is -not- in the public domain. */

#import "macx_glut.h"
#import "GLUTView.h"


/* Modifier mask of ~0 implies not in core input callback. */
unsigned int __glutModifierMask = (unsigned int) ~0;



/* CENTRY */
int APIENTRY glutGetModifiers(void)
{
   int  modifiers;

   if(__glutModifierMask == (unsigned int) ~0) {
      __glutWarning("glutCurrentModifiers: do not call outside core input callback.");
      return 0;
   }
   modifiers = 0;

   if(__glutModifierMask & NSShiftKeyMask)
      modifiers |= GLUT_ACTIVE_SHIFT;
   if(__glutModifierMask & NSControlKeyMask)
      modifiers |= GLUT_ACTIVE_CTRL;
   if(__glutModifierMask & NSAlternateKeyMask)
      modifiers |= GLUT_ACTIVE_ALT;
   return modifiers;
}
/* ENDCENTRY */
```

[Next](macxoverlay.m.md)[Previous](macxmenu.m.md)

