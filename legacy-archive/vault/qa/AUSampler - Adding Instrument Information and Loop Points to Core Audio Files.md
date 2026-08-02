---
title: AUSampler - Adding Instrument Information and Loop Points to Core Audio Files
apple_id: DTS40013358
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2013-05-29'
source_url: https://developer.apple.com/library/archive/qa/qa1527/_index.html
archived_at: '2026-07-18T02:32:11.995349Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1527

# AUSampler - Adding Instrument Information and Loop Points to Core Audio Files

## Q:  How can I add Music Instrument Information and Sample Loop Points to Core Audio (.caf) files so I can use them with the AUSampler Audio Unit?

A: The Core Audio File Format Specification provides two chunk types to specify instrument data including looping Information to a .caf file. The Instrument chunk type and the Region chunks work together allowing you to build a list of Region descriptions containing markers annotating position(s) in an audio file which are then referred to by the Instrument chunk to define an instrument.

For more information see the [Apple Core Audio Format Specification](https://developer.apple.com/library/mac/#documentation/MusicAudio/Reference/CAFSpec/CAF_intro/CAF_intro.html#//apple_ref/doc/uid/TP40001862-CH203-TPXREF101) and `AudioFile.h` which is part of the `AudioToolbox.framework`.

Listing 1 demonstrates how to add an Instrument chunk with a single sustain loop region as well as specifying a bass, low and high pitch range when provided with an open Core Audio File (.caf) file.

__Listing 1__

```swift
OSStatus SetupInstrument(AudioFileID inFileID,
                         UInt64 inFileLength,   // length in frames (samples)
                         UInt8 inBaseNote,      // MIDI note (0-127)
                         UInt8 inLowNote,       // MIDI note (0-127, <= inBaseNote)
                         UInt8 inHighNote) // MIDI note (0-127, >= inBaseNote)
{

    const UInt32 numRegionChunks = 1; // For our sustain loop, one region
    const UInt32 numMarkers = 2; // Two markers - One for loop start, one for loop end
    UInt32 totalChunkSize = 0;

    /**** Region Chunk ****/

    // Add up the total memory size we need to allocate for the variable-size AudioFileRegionList

    totalChunkSize += offsetof(AudioFileRegionList, mRegions);
    totalChunkSize += numRegionChunks * offsetof(AudioFileRegion, mMarkers);
    totalChunkSize += numRegionChunks * numMarkers * sizeof(AudioFileMarker);

    // Allocate the region chunk

    AudioFileRegionList *pRegionList = (AudioFileRegionList *) malloc(totalChunkSize);
    pRegionList->mNumberRegions = numRegionChunks;
    pRegionList->mSMPTE_TimeType = kCAF_SMPTE_TimeTypeNone; // Not used

    // Access the region

    AudioFileRegion *pRegion = &pRegionList->mRegions[0];
    pRegion->mRegionID = 6789; // Arbitrary, but must match the values used
                               // in the Instrument Chunk below
    pRegion->mName = NULL;
    pRegion->mNumberMarkers = numMarkers; // From above
    pRegion->mFlags = kAudioFileRegionFlag_LoopEnable |
                      kAudioFileRegionFlag_PlayForward; // enable forward looping for this region

    // Access the marker array

    AudioFileMarker *pMarkers = &pRegion->mMarkers[0];

    // Set up loop start
    pMarkers[0].mType = kCAFMarkerType_SustainLoopStart;
    memset(&pMarkers[0].mSMPTETime, 0, sizeof(pMarkers[0].mSMPTETime)); // zero out; not used
    pMarkers[0].mFramePosition = 0; // Loop from first sample
    pMarkers[0].mMarkerID = 1;
    pMarkers[0].mName = NULL; // Unused
    pMarkers[0].mChannel = 0; // Unused

    // Set up loop end
    pMarkers[1].mType = kCAFMarkerType_SustainLoopEnd;
    memset(&pMarkers[1].mSMPTETime, 0, sizeof(pMarkers[0].mSMPTETime)); // zero out; not used
    pMarkers[1].mFramePosition = inFileLength - 1; // Loop to the last sample
    pMarkers[1].mMarkerID = 2;
    pMarkers[1].mName = NULL; // Unused
    pMarkers[1].mChannel = 0; // Unused

    // Write out entire AudioFileRegionList into the file
    // Note that we use the full allocated size

    OSStatus err = AudioFileSetProperty(inFileID, kAudioFilePropertyRegionList, totalChunkSize, pRegionList);
     if (err) { free(pRegionList); return err; }

    // Set up Instrument Chunk, referencing the ID for the region chunk that we just wrote to the file

    CAFInstrumentChunk instChunk;
    instChunk.mBaseNote = (Float32) inBaseNote;
    instChunk.mMIDILowNote = inLowNote;
    instChunk.mMIDIHighNote = inHighNote;
    instChunk.mMIDILowVelocity = 0; // For this example, just setting full velocity range
    instChunk.mMIDIHighVelocity = 127;
    instChunk.mdBGain = 0.0f; // 0.0 dB means unity gain
    instChunk.mStartRegionID = 0; // Unused
    instChunk.mSustainRegionID = pRegion->mRegionID; // Set up above
    instChunk.mReleaseRegionID = 0; // Unused
    instChunk.mInstrumentID = 0;

    // CAF Specification requires all chunks to be BigEndian

    MakeCAFInstrumentBigEndian(&instChunk);

    // Write out CAFInstrumentChunk into the file

    err = AudioFileSetUserData(inFileID, kCAF_InstrumentChunkID, 0, sizeof(instChunk), &instChunk);
    free(pRegionList);

    return err;
}
```



```c
#include <stddef.h>
#include "CAByteOrder.h" // from Core Audio public utilities

// CAF Files are big-endian, so the chunks contents need to be swapped

static void MakeCAFInstrumentBigEndian(CAFInstrumentChunk *chunk)
{
    chunk->mBaseNote = CASwapFloat32HostToBig(chunk->mBaseNote);
    chunk->mdBGain = CASwapFloat32HostToBig(chunk->mdBGain);
    chunk->mStartRegionID = CFSwapInt32HostToBig(chunk->mStartRegionID);
    chunk->mSustainRegionID = CFSwapInt32HostToBig(chunk->mSustainRegionID);
    chunk->mReleaseRegionID = CFSwapInt32HostToBig(chunk->mReleaseRegionID);
    chunk->mInstrumentID = CFSwapInt32HostToBig(chunk->mInstrumentID);
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-05-29 | New document that discusses how to add Music Instrument Information and Sample Loop Points to Core Audio (.caf) files so they can be used with the AUSampler. |

