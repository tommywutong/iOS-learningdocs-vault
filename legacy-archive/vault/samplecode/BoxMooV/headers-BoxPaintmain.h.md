---
title: BoxMooV
apple_id: DTS10000099
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BoxMooV/Listings/headers_BoxPaint_main_h.html
archived_at: '2026-07-18T03:02:14.024814Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BoxMooV](BoxMooV.md)


[Next](headers-BoxPaintmenu.h.md)[Previous](headers-BoxMooVwindow.h.md)

# headers/BoxPaint_main.h

```
/*  main.h                                                                      

  This is BoxPaint, a sample app designed to show how getting UV data from
  a pick object can be used to draw on a texture. This app does not have        
  graceful error handling - it's purpose is to demonstrate UV picking.                                                                      

  Michael Bishop - August 21 1996                                                   
  Nick Thompson
  Robert Dierkes                                                                                
  (c)1994-96 Apple Computer Inc., All Rights Reserved                               

*/

#ifndef _MAIN_H_
#define _MAIN_H_

/* ------------------------------------------------------------------------------------------- */
/*  globals - defined in main.c */
extern Boolean gQuitFlag ;
extern Boolean gForeground;
extern  short   gTicks ;

/* ------------------------------------------------------------------------------------------- */
/*  constants - defined in main.c */

/*  function prototypes */

void        Main_DoAbout( void );

#endif
```

[Next](headers-BoxPaintmenu.h.md)[Previous](headers-BoxMooVwindow.h.md)

