---
title: Embedding Instruments
apple_id: DTS10000321
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Embedding_Instruments/Listings/BigEasy_BigEasyGrafish_h.html
archived_at: '2026-07-18T03:07:42.906793Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Embedding Instruments](Embedding%20Instruments.md)


[Next](BigEasy-BigEasyPPC.c.md)[Previous](BigEasy-BigEasyGrafish.c.md)

# BigEasy/BigEasyGrafish.h

```
/*
    File:       BigEasyGrafish.h

    Contains:   xxx put contents here xxx

    Written by: xxx put writers here xxx

    Copyright:  © 1991, 1994 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

         <4>      9-8-94    dvb     
         <2>     1/20/92    dvb     Add more routines.

*/

/* file: BigEasyGrafish.h
 *
 * Started 25 August 1989, more or less.
 *
 * Headers for BigEasyGrafish.c
 *
 */

#ifndef BigEasyGrafish
    extern char dGrayPat[];
    extern char dBlackPat[];
#endif

#ifdef __cplusplus
extern "C" {
#endif

void RGBFore(unsigned short,unsigned short,unsigned short);
void RGBBack(unsigned short,unsigned short,unsigned short);
void GoBlack(void);
void GoGray(void);
void GoWhite(void);
void GoBW(void);

void RGBOp(unsigned short,unsigned short,unsigned short);
void RGBHilite(unsigned short,unsigned short,unsigned short);
void PmHilite(short);
void RampColorTable(CTabHandle,short start,short length,unsigned short r1,unsigned short g1,unsigned short b1,
        unsigned short r2,unsigned short g2,unsigned short b2);

void FrameRectOutside(Rect *r);
void DrawIcl8Resource(short id,Rect *r);
void DrawPixMap(PixMap *pm,Rect *src,Rect *dst,short mode);
void DrawPixMapOffset(PixMap *pm,short x,short y,short mode);

Boolean EasyHasColor(void);

#ifdef __cplusplus
}
#endif
```

[Next](BigEasy-BigEasyPPC.c.md)[Previous](BigEasy-BigEasyGrafish.c.md)

