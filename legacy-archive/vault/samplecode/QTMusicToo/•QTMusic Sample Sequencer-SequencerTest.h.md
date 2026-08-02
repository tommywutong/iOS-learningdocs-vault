---
title: QTMusicToo
apple_id: DTS10000915
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-19'
source_url: https://developer.apple.com/library/archive/samplecode/QTMusicToo/Listings/_QTMusic_Sample_Sequencer_SequencerTest_h.html
archived_at: '2026-07-18T03:21:08.424263Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTMusicToo](QTMusicToo.md)


[Next](Document%20Revision%20History.md)[Previous](%E2%80%A2QTMusic%20Sample%20Sequencer-SequencerTest.c.md)

# •QTMusic Sample Sequencer/SequencerTest.h

```c
/*
 * file: SequencerTest.h
 *
 * started 12 January 1992 16:45
 * david van brink
 *
 * A starting point for BigEasy programs
 *
 */

 #ifndef _SequencerTest_
 #define _SequencerTest_

/*--------------------------
    Inclusions
--------------------------*/

#include <Files.h>
#include <Windows.h>

#include <QuickTimeComponents.h>



/*--------------------------
    Structures
--------------------------*/




#define kNoteRangeLow 36
#define kNoteRangeHigh 72
#define kScoreLength 64
#define kScoreParts 4

#define kPipSize 4              /* Pixels for screen display */


#define kScoreLengthLongs ((kScoreLength)+31/32)
#define kScoreHeight (kNoteRangeHigh - kNoteRangeLow + 1)


typedef struct
    {
    ToneDescription tone;
    char junk[28];              /* padding, since tone def changed */
    long score[kScoreHeight][kScoreLengthLongs];
    } ScorePart;


#define kDocVersion 1
typedef struct
    {
    ScorePart score[kScoreParts];
    } TPartialSaveRecord;


typedef struct
    {
    Boolean used;

    Boolean everSaved;
    Boolean changed;
    Boolean littleChanged;      /* Save available, but no "Save Discard?" on close */

    FSSpec docSpec;
    TPartialSaveRecord sr;

    NoteChannel noteChannel[kScoreParts];
    TunePlayer tp;

    Boolean validQTScore;
    Handle qtScore;
    Handle th;
    long position;

    WindowPtr w;
    } TDoc;

typedef struct
    {
    long docVersion;            /* quick check that we can really open the file */
    Rect windowRect;
    TPartialSaveRecord sr;
    } TSaveRecord;


typedef struct
    {
    Rect scoreRect[kScoreParts];
    Rect instrumentNameRect[kScoreParts];
    Rect timeRect;
    short basicDocWidth;
    short basicDocHeight;
    ComponentInstance na;       /* Note Allocator */
    } Globals;




/*--------------------------
    Variables
--------------------------*/

#ifdef globals
    #define VAR
#else
    #define VAR extern
#endif

#define kFirstDocWindow 1
#define kDocMax 5
VAR TDoc *gDoc;
VAR short gDocCount;
VAR Globals g;


#undef VAR


/*--------------------------
    Prototypes
--------------------------*/

void NewDocFromSaveRecord(short docNumber,TSaveRecord *sr);
void FixUpMenus(TDoc *d);
Boolean GetPipBit(ScorePart *sp,short pipX, short pipY);
void UnrollDoc(TDoc *d);
void DoTheHeader(TDoc *d);
Handle BuildMusicHeader(TDoc *d);
void ShowError(long error);

#endif _SequencerTest_
```

[Next](Document%20Revision%20History.md)[Previous](%E2%80%A2QTMusic%20Sample%20Sequencer-SequencerTest.c.md)

