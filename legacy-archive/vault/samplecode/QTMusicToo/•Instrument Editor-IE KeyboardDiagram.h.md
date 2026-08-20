---
title: QTMusicToo
apple_id: DTS10000915
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-19'
source_url: https://developer.apple.com/library/archive/samplecode/QTMusicToo/Listings/_Instrument_Editor_IE_KeyboardDiagram_h.html
archived_at: '2026-07-18T03:21:05.863359Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTMusicToo](QTMusicToo.md)


[Next](%E2%80%A2Instrument%20Editor-IE%20PrintUtilities.c.md)[Previous](%E2%80%A2Instrument%20Editor-IE%20KeyboardDiagram.c.md)

# •Instrument Editor/IE KeyboardDiagram.h

```c
/*
    File:       KeyboardDiagram.h

    Contains:   xxx put contents here xxx

    Written by: xxx put writers here xxx

    Copyright:  © 1994 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

         <2>     2/14/94    dvb     Velocity Vector
         <1>      2/4/94    dvb     first checked in

*/

#define kKeyboardPict 128
#define kJunkWhite 128
#define kJunkBlack 129

#define kKeyboardHeight 0x1F
#define kKeyboardOctaveWidth 0x3F

#include <Types.h>

typedef struct
    {
    short octaveCount;
    short lowKey;
    short keyCount;
    Boolean mod;
    short modOffset;
    Rect r;
    short **whiteKey;               /* 'Junk 428' and 429 */
    short **keyRight;
    unsigned char keyVel[128];
    Boolean gray;
    } KeyboardDiagram;


void InitializeKeyboard(KeyboardDiagram *kd,Rect *r,short octaveCount,short lowKey);
void TerminateKeyboard(KeyboardDiagram *kd);

void SetKeyboardTopLeft(KeyboardDiagram *kd,short top, short left);

void DrawKeyboardPiece(KeyboardDiagram *kd, short octave);
void DrawKeyboardDropShadow(KeyboardDiagram *kd);
void DrawKeyboard(KeyboardDiagram *kd);
void SetKeyboardGray(KeyboardDiagram *kd,Boolean gray);
void PaintKeyboardKey(KeyboardDiagram *kd,short pitch,short gray);  /* 0-255, gray; -1, invert; -2, forecolor */
void PaintKeyboardVector(KeyboardDiagram *kd,unsigned char *keyVel);
void GoGray(void);

short GetKeyboardKey(KeyboardDiagram *kd,Point p);
```

[Next](%E2%80%A2Instrument%20Editor-IE%20PrintUtilities.c.md)[Previous](%E2%80%A2Instrument%20Editor-IE%20KeyboardDiagram.c.md)

