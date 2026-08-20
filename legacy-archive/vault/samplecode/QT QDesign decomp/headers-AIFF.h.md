---
title: QT QDesign decomp
apple_id: DTS10000911
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QT_QDesign_decomp/Listings/headers_AIFF_h.html
archived_at: '2026-07-18T03:21:23.062238Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QT QDesign decomp](QT%20QDesign%20decomp.md)


[Next](headers-DBFFErrors.h.md)[Previous](QT%20QDesign%20decomp.md)

# headers/AIFF.h

```c
/*
**  Apple Macintosh Developer Technical Support
**
**  Headers for routines demonstrating how to parse an AIFF sound header.
**
**  by Mark Cookson, Apple Developer Technical Support
**
**  File:   AIFF.h
**
**  Copyright ©1996 Apple Computer, Inc.
**  All rights reserved.
**
**  You may incorporate this sample code into your applications without
**  restriction, though the sample code has been provided "AS IS" and the
**  responsibility for its operation is 100% yours.  However, what you are
**  not permitted to do is to redistribute the source as "Apple Sample
**  Code" after having made changes. If you're going to re-distribute the
**  source, we require that you make it clear in the source that the code
**  was descended from Apple Sample Code, but that you've made changes.
*/

#ifndef __MyAIFF__
#define __MyAIFF__

#include <AIFF.h>
#include <Errors.h>
#include <Files.h>
#include <Sound.h>

#ifndef __DBFFERRORS__
#include "DBFF_Errors.h"
#endif

#ifndef __SETUPDBHEADER__
#include "SetupDBHeader.h"
#endif

#ifndef __LDANDFIX__
#include "LDandFix.h"
#endif

#ifndef __DEFINES__
#include "Defines.h"
#endif

#define kChunkBufferSize    128
#define kChunkHeaderSize    8

/* these are bit positions for a long flag */
#define kFORM                   (1<<0)
#define kFormatVersion          (1<<1)
#define kCommon                 (1<<2)
#define kSoundData              (1<<3)
#define kMarker                 (1<<4)
#define kInstrument             (1<<5)
#define kMIDIData               (1<<6)
#define kAudioRecording         (1<<7)
#define kApplicationSpecific    (1<<8)
#define kComment                (1<<9)
#define kName                   (1<<10)
#define kAuthor                 (1<<12)
#define kCopyright              (1<<13)
#define kAnnotation             (1<<14)

typedef union {
    ChunkHeader                 generic;
    ContainerChunk              container;
    FormatVersionChunk          formatVersion;
    CommonChunk                 common;
    ExtCommonChunk              extCommon;
    SoundDataChunk              soundData;
    MarkerChunk                 marker;
    InstrumentChunk             instrument;
    MIDIDataChunk               midiData;
    AudioRecordingChunk         audioRecording;
    CommentsChunk               comments;
    TextChunk                   text;
} ChunkTemplate, *ChunkTemplatePtr;

#define stillMoreDataToRead     ((chunkFlags & kFORM) && (!(chunkFlags & kCommon) || !(chunkFlags & kSoundData)) && (err == noErr))

OSErr   ASoundGetAIFFHeader     (SoundInfoPtr theSoundInfo, long *length, void *waveChunk);

#endif
```

[Next](headers-DBFFErrors.h.md)[Previous](QT%20QDesign%20decomp.md)

