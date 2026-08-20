---
title: aiffwriter.win
apple_id: DTS10000905
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/aiffwriter.win/Listings/SoundOutputDispatch_h.html
archived_at: '2026-07-18T03:28:48.727288Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [aiffwriter.win](aiffwriter.win.md)


[Next](WinPrefix.h.md)[Previous](dllmain.c.md)

# SoundOutputDispatch.h

```
    ComponentSelectorOffset (6)

    ComponentRangeCount (2)
    ComponentRangeShift (8)
    ComponentRangeMask  (FF)

    ComponentStorageType (Ptr)
    ComponentDelegateByteOffset (0)

    ComponentRangeBegin (0)
        ComponentError (Target)
        StdComponentCall (Register)
        StdComponentCall (Version)
        StdComponentCall (CanDo)
        StdComponentCall (Close)
        StdComponentCall (Open)
    ComponentRangeEnd (0)

    ComponentRangeBegin (1)
        ComponentError (0)
        ComponentCall (InitOutputDevice)
        ComponentError (SetSource)
        ComponentError (GetSource)
        ComponentError (GetSourceData)
        ComponentError (SetOutput)
    ComponentRangeEnd (1)

    ComponentRangeBegin (2)
        ComponentError (0)
        ComponentDelegate (AddSource)
        ComponentDelegate (RemoveSource)
        ComponentCall (GetInfo)
        ComponentCall (SetInfo)
        ComponentCall (StartSource)
        ComponentDelegate (StopSource)
        ComponentDelegate (PauseSource)
        ComponentCall (PlaySourceBuffer)
    ComponentRangeEnd (2)
```

[Next](WinPrefix.h.md)[Previous](dllmain.c.md)

