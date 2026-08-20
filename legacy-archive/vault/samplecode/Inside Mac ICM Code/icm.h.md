---
title: Inside Mac ICM Code
apple_id: DTS10000892
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Inside_Mac_ICM_Code/Listings/icm_h.html
archived_at: '2026-07-18T03:12:58.476109Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Inside Mac ICM Code](Inside%20Mac%20ICM%20Code.md)


[Next](Document%20Revision%20History.md)[Previous](icm.c.md)

# icm.h

```c
/*
    File:       icm.h

    Contains:   

    Written by:     

    Copyright:  Copyright © 1992-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/16/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1
                12/4/94     khs             changed the format of the file to the new look and feel

*/


// HEADER FILES
#include <QuickDraw.h>
#include <Windows.h>
#include <Memory.h>
#include <Resources.h>
#include <OSUtils.h>
#include <Files.h>
#include <StandardFile.h>
#include <ImageCompression.h>
#include <Fonts.h>
#include <Menus.h>
#include <Errors.h>
#include <Packages.h>
#include <TextUtils.h>
#include <SegLoad.h>


// FUNCTION PROTOTYPES
void MakeMyResource(StandardFileReply fileReply,
                    ImageDescriptionHandle description);
void SequenceSave(void);
void CheckError(OSErr error,
                Str255 displayString);
void DrawFrame(const Rect* imageRect,
               long frameNum);
void CompressSequence(short* dfRef,
                      ImageDescriptionHandle* description);
void MakeMyResource(StandardFileReply fileReply,
                    ImageDescriptionHandle description);
void SequenceSave(void);
void SequencePlay(void);
PicHandle GetQTCompressedPict(CGrafPtr port);
```

[Next](Document%20Revision%20History.md)[Previous](icm.c.md)

