---
title: Embedding Instruments
apple_id: DTS10000321
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Embedding_Instruments/Listings/MusicHelper_h.html
archived_at: '2026-07-18T03:07:44.538461Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Embedding Instruments](Embedding%20Instruments.md)


[Next](TuneGeneration2.0.c.md)[Previous](MusicHelper.c.md)

# MusicHelper.h

```c
/* file: MusicHelper.h
 *
 * Started 7 February 1994, 11:14am
 *
 */

#include <Files.h>
#include <Types.h>
#include <QuickTimeComponents.h>

/*--------------------
    Simple things
--------------------*/
#ifndef _MusicHelper_
#define _MusicHelper_


#ifndef _MusicHelperC_
    typedef struct {long data[1];} *MusicScore;
    typedef struct {long data[1];} *MusicMovie;
#endif



MusicScore NewMusicScore(void);
void DisposeMusicScore(MusicScore *ms);

short AddMusicScoreGMInstrument(MusicScore ms,short gmInstrument);
short AddMusicScoreInstrument(MusicScore ms,ToneDescription *td);
short AddMusicScoreFlatInstrument(MusicScore ms,FlatInstrument *flat);

void AddMusicScoreNote(MusicScore ms,
        short part,Fixed pitch,long velocity,TimeValue noteDuration);
void AddMusicScoreRest(MusicScore ms,TimeValue restDuration);

Handle GetMusicScoreHeader(MusicScore ms);
Handle GetMusicScoreScore(MusicScore ms);


MusicMovie StartMusicMovie(FSSpec *movieSpec,Handle header);
void AddMusicMovieSample(MusicMovie mm,Handle score);
void FinishMusicMovie(MusicMovie *mm);

#endif _MusicHelper_
```

[Next](TuneGeneration2.0.c.md)[Previous](MusicHelper.c.md)

