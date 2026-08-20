---
title: MakeEffectMovie
apple_id: DTS10001038
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MakeEffectMovie/Listings/Clippings_AddEffectsDescription_txt.html
archived_at: '2026-07-18T03:14:11.992633Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MakeEffectMovie](MakeEffectMovie.md)


[Next](Clippings-AddInputMap.txt.md)[Previous](Application%20Files-ComResource.h.md)

# Clippings/AddEffectsDescription.txt

```
        // add the effects sample to the movie

        myErr = BeginMediaEdits(videoMediaFX);
        BailError(myErr);

        // add the sample to the media
        myErr = AddMediaSample(videoMediaFX, gEffectSample, 0, GetHandleSize(gEffectSample), myEffectDuration, (SampleDescriptionHandle)myDesc, 1, 0, &mySampleTime);
        BailError(myErr);

        myErr = EndMediaEdits(videoMediaFX);
        BailError(myErr);

        QTDisposeAtomContainer(gEffectSample);
        DisposeHandle((Handle)myDesc);

        // add the media to the track
        myErr = InsertMediaIntoTrack(videoTrackFX, 0, mySampleTime, myEffectDuration, fixed1);
        BailError(myErr);
```

[Next](Clippings-AddInputMap.txt.md)[Previous](Application%20Files-ComResource.h.md)

