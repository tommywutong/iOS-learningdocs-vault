---
title: MakeEffectMovie
apple_id: DTS10001038
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MakeEffectMovie/Listings/Clippings_CreateEffectDescription_txt.html
archived_at: '2026-07-18T03:14:12.132911Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MakeEffectMovie](MakeEffectMovie.md)


[Next](Clippings-CreateEffectsTrack.txt.md)[Previous](Clippings-AddSourceName.txt.md)

# Clippings/CreateEffectDescription.txt

```
        ImageDescriptionHandle      myDesc = NULL;

#if USES_MAKE_IMAGE_DESC_FOR_EFFECT

        OSErr                       myErr = noErr;

        // create a new sample description for the effect - we use
        // the MakeImageDescriptionForEffect function if we want to
        // create stacked effects, where one effect track acts as a
        // source for another effect
        myErr = MakeImageDescriptionForEffect(myEffectCode, &myDesc);
        if (myErr != noErr)
            BailError(myErr);
#else
        // create a new sample description - in this case, we'll construct
        // the image description ourselves using the NewHandleClear function,
        // since we're not going to create a stacked effect (in which case
        // you'd need to use MakeImageDescriptionForEffect as described above)
        myDesc = (ImageDescriptionHandle)NewHandleClear(sizeof(ImageDescription));
        BailNil(myDesc);

        (**myDesc).idSize = sizeof(ImageDescription);
        (**myDesc).cType = myEffectCode;
        (**myDesc).hRes = 72L << 16;
        (**myDesc).vRes = 72L << 16;
        (**myDesc).dataSize = 0L;
        (**myDesc).frameCount = 1;
        (**myDesc).depth = 0;
        (**myDesc).clutID = -1;
#endif
        // fill in the fields of the sample description
        (**myDesc).vendor = kAppleManufacturer;
        (**myDesc).temporalQuality = codecNormalQuality;
        (**myDesc).spatialQuality = codecNormalQuality;
        (**myDesc).width = videoTrackFXWidth >> 16;
        (**myDesc).height = videoTrackFXHeight >> 16;
```

[Next](Clippings-CreateEffectsTrack.txt.md)[Previous](Clippings-AddSourceName.txt.md)

