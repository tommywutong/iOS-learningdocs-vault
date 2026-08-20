---
title: Record sound specific rate
apple_id: DTS10000367
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/Record_sound_specific_rate/Listings/headers_Record_Sound_h.html
archived_at: '2026-07-18T03:22:01.749115Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Record sound specific rate](Record%20sound%20specific%20rate.md)


[Next](source-Recordsoundatrate.c.md)[Previous](Record%20sound%20specific%20rate.md)

# headers/Record_Sound.h

```c
#ifndef __RECORD_SOUND__
#define __RECORD_SOUND__

#include <SoundInput.h>

//So we can pass our A5 and other info to our PBWrite completion routines
typedef struct myRecordingParamBlockRec {
    ParamBlockRec           pb;
    long                    myA5;
    Boolean                 pbInUse,
                            lastWrite;
} myRecordingParamBlockRec, *myRecordingParmBlkPtr;

//Keep track of the info needed to record
typedef struct {
    long                    sanitycheck;
    OSErr                   theErr;     //last error returned by SPBRecord or PBWrite
    SPBPtr                  recordRec;
    myRecordingParmBlkPtr   pb0,
                            pb1;
    Ptr                     recBuffer0,
                            recBuffer1,
                            resampledBuf0,
                            resampledBuf1;
    SoundConverter          sc;
    SoundComponentData      inputFormat,
                            outputFormat;
    Fixed                   sampleRate;
    OSType                  compression;
    unsigned long           totalBytes,
                            inputFrames;
    long                    myA5,
                            devBuffer,
                            parID,
                            soundRefNum,
                            initialOffset;
    short                   whichBuffer,
                            fileRefNum,
                            volRefNum,
                            numChannels,
                            sampleSize,
                            AGC;
    Str255                  nameString;
} Vars, *VarsPtr;

OSErr           PrepairToRecordToDisk   (VarsPtr myVars, short refNum, short sampleSize, UnsignedFixed sampleRate, short numChannels, OSType compression, short AGC);
OSErr           RecordToDisk            (VarsPtr myVars);
pascal void     MyRecComp               (SPBPtr inParamPtr);
OSErr           FinishRecording         (VarsPtr myVars);

#if GENERATINGCFM
pascal void     MyPB0WriteComp          (myRecordingParmBlkPtr passedPB);
pascal void     MyPB1WriteComp          (myRecordingParmBlkPtr passedPB);
#else 
pascal void     MyPB0WriteComp          (myRecordingParmBlkPtr passedPB:__a0);
pascal void     MyPB1WriteComp          (myRecordingParmBlkPtr passedPB:__a0);
#endif

#endif
```

[Next](source-Recordsoundatrate.c.md)[Previous](Record%20sound%20specific%20rate.md)

