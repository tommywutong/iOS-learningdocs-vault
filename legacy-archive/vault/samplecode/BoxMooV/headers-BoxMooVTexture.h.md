---
title: BoxMooV
apple_id: DTS10000099
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BoxMooV/Listings/headers_BoxMooV_Texture_h.html
archived_at: '2026-07-18T03:02:13.835739Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BoxMooV](BoxMooV.md)


[Next](headers-BoxMooVwindow.h.md)[Previous](headers-BoxMooVQuickTime.h.md)

# headers/BoxMooV_Texture.h

```c
/*  BoxMooV_texture.h                                                                           
 *  
 *  Rick Evans                                                  
 *  Robert Dierkes                                                                              
 *  (c)1994-96 Apple Computer Inc., All Rights Reserved                             
 *  
*/
#ifndef _TEXTURE_H_
#define _TEXTURE_H_

#include <QDOffscreen.h>
#include <Movies.h>

#include "QD3D.h"
#include "QD3DGroup.h"
#include "QD3DStorage.h"

/*----------------------*/
/*  Type Declarations   */
/*----------------------*/

struct _AnimTxt {
    TQ3StoragePixmap    fStoragePixmap;     /*  The QD3D Pixmap */

    GWorldPtr           fpGWorld;           /*  The Offscreen Buffer    */

    Movie               fMovie;             /*  The Movie source    */

    int                 resolution;         /*  the height and width of the pict    */
};

typedef struct _AnimTxt TAnimatedTexture, *TAnimatedTexturePtr, **TAnimatedTextureHdl;

/*--------------*/
/*  Prototypes  */
/*--------------*/

TAnimatedTextureHdl Texture_New(void);
Boolean             Texture_Delete(TAnimatedTextureHdl  theTexture);
int                 Texture_GetResolution(TAnimatedTextureHdl   theTexture);
TQ3Status           Texture_AddToGroup(TAnimatedTextureHdl  theTexture, TQ3GroupObject  theGroup) ;
Boolean             Texture_NextFrame(TAnimatedTextureHdl pAnimTxtr);

#endif
```

[Next](headers-BoxMooVwindow.h.md)[Previous](headers-BoxMooVQuickTime.h.md)

