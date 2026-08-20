---
title: MakeEffectMovie
apple_id: DTS10001038
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MakeEffectMovie/Listings/Clippings_CreateEffectsTrack_txt.html
archived_at: '2026-07-18T03:14:12.183844Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MakeEffectMovie](MakeEffectMovie.md)


[Next](Clippings-CreateInputMap.txt.md)[Previous](Clippings-CreateEffectDescription.txt.md)

# Clippings/CreateEffectsTrack.txt

```
    {
        // videoTrackFX is the special track that implements the effect
        videoTrackFX = NewMovieTrack(myDestMovie, videoTrackFXWidth, videoTrackFXHeight, 0);
        BailNil(videoTrackFX);

        // create the media for our effects track
        videoMediaFX = NewTrackMedia(videoTrackFX, VideoMediaType, myMovieTimeScale, NULL, 0);
        BailNil(videoMediaFX);
    }
```

[Next](Clippings-CreateInputMap.txt.md)[Previous](Clippings-CreateEffectDescription.txt.md)

