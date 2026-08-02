---
title: MakeEffectMovie
apple_id: DTS10001038
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MakeEffectMovie/Listings/Clippings_SelectAnEffect_txt.html
archived_at: '2026-07-18T03:14:12.343894Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MakeEffectMovie](MakeEffectMovie.md)


[Next](Common%20Files-ComFramework.c.md)[Previous](Clippings-GetWhatKindOfEffect.txt.md)

# Clippings/SelectAnEffect.txt

```
    // Create an atom container to hold the parameters
    // for the effect.
    myErr = QTNewAtomContainer(&gEffectSample);
    BailError(myErr);

    // QTGetEffectsList returns a QTAtomContainer holding a 
    // list of the currently installed effects components
    myErr = QTGetEffectsList(&gEffectList, theSpecCount, theSpecCount, 0);
    BailError(myErr);

    // Ask the user to select an effect. On return, the 
    // gEffectSample atom container holds an effect description 
    // for the effect selected by the user, including the parameter
    // settings. This effect description can then be added
    // to the media of an effect track. You will need to add
    // source atoms to this container for effects that require
    // sources.
    myErr = QTCreateStandardParameterDialog(gEffectList, gEffectSample, 0, &gEffectsDialog);
    BailError(myErr);
```

[Next](Common%20Files-ComFramework.c.md)[Previous](Clippings-GetWhatKindOfEffect.txt.md)

