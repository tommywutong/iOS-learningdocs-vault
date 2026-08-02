---
title: MakeEffectMovie
apple_id: DTS10001038
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MakeEffectMovie/Listings/Clippings_AddSourceName_txt.html
archived_at: '2026-07-18T03:14:12.104864Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MakeEffectMovie](MakeEffectMovie.md)


[Next](Clippings-CreateEffectDescription.txt.md)[Previous](Clippings-AddMovieResource.txt.md)

# Clippings/AddSourceName.txt

```
    // Add the atoms naming the sources for our effect
    {
        long    myLong;

        if (gSpecCount >= 1) {
            myLong = EndianU32_NtoB(kSourceOneName);
            QTInsertChild(gEffectSample, kParentAtomIsContainer, kEffectSourceName, 1, 0, sizeof(myLong), &myLong, NULL);
        }

        if (gSpecCount >= 2) {
            myLong = EndianU32_NtoB(kSourceTwoName);
            QTInsertChild(gEffectSample, kParentAtomIsContainer, kEffectSourceName, 2, 0, sizeof(myLong), &myLong, NULL);
        }
    }
```

[Next](Clippings-CreateEffectDescription.txt.md)[Previous](Clippings-AddMovieResource.txt.md)

