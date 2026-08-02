---
title: audiocodec
apple_id: DTS10000812
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/audiocodec/Listings/uLawCodecDispatch_h.html
archived_at: '2026-07-18T03:28:50.474133Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [audiocodec](audiocodec.md)


[Next](uLawCompressor.c.md)[Previous](uLawCodec.r.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#samplecode/AudioCodecSDK/Introduction/Intro.html](https://developer.apple.com/library/mac/#samplecode/AudioCodecSDK/Introduction/Intro.html)

# uLawCodecDispatch.h

```
    ComponentSelectorOffset (6)

    ComponentRangeCount (2)
    ComponentRangeShift (8)
    ComponentRangeMask  (FF)

    ComponentStorageType (Ptr)
    ComponentDelegateByteOffset (0)

    ComponentRangeBegin (0)
        ComponentError (Target)
        ComponentError (Register)
        StdComponentCall (Version)
        StdComponentCall (CanDo)
        StdComponentCall (Close)
        StdComponentCall (Open)
    ComponentRangeEnd (0)

    ComponentRangeBegin (1)
        ComponentError (0)
        ComponentDelegate (InitOutputDevice)
        ComponentCall (SetSource)
        ComponentDelegate (GetSource)
        ComponentCall (GetSourceData)
        ComponentCall (SetOutput)
    ComponentRangeEnd (1)

    ComponentRangeBegin (2)
        ComponentError (0)
        ComponentDelegate (AddSource)
        ComponentDelegate (RemoveSource)
        ComponentCall (GetInfo)
        ComponentCall (SetInfo)
        ComponentDelegate (StartSource)
        ComponentCall (StopSource)
        ComponentDelegate (PauseSource)
        ComponentCall (PlaySourceBuffer)
    ComponentRangeEnd (2)
```

[Next](uLawCompressor.c.md)[Previous](uLawCodec.r.md)

