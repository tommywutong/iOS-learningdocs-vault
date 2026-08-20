---
title: MakeEffectMovie
apple_id: DTS10001038
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MakeEffectMovie/Listings/Clippings_CreateInputMap_txt.html
archived_at: '2026-07-18T03:14:12.213988Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MakeEffectMovie](MakeEffectMovie.md)


[Next](Clippings-GetWhatKindOfEffect.txt.md)[Previous](Clippings-CreateEffectsTrack.txt.md)

# Clippings/CreateInputMap.txt

```
    // create and add the input map - this tells the effect
    // which tracks in the movie are affected

        long                myRefIndex1, myRefIndex2;
        QTAtomContainer     myInputMap;
        QTAtom              myInputAtom;
        OSType              myInputType;
        long                myLong;

        QTNewAtomContainer(&myInputMap);

        // first input
        if (videoTracks[0]) {

            // setup a reference between our effect and the first input track
            AddTrackReference(videoTrackFX, videoTracks[0], kTrackModifierReference, &myRefIndex1);
            QTInsertChild(myInputMap, kParentAtomIsContainer, kTrackModifierInput, myRefIndex1, 0, 0, NULL, &myInputAtom);

            // add modifier track type ('vide')
            myInputType = EndianU32_NtoB(kTrackModifierTypeImage);
            QTInsertChild(myInputMap, myInputAtom, kTrackModifierType, 1, 0, sizeof(myInputType), &myInputType, NULL);

            // source name for first source - there is a corresponding
            // kEffectSourceName atom in the effect description to 
            // identify the source
            myLong = EndianU32_NtoB(kSourceOneName);
            QTInsertChild(myInputMap, myInputAtom, kEffectDataSourceType, 1, 0, sizeof(myLong), &myLong, NULL);
        }

        // second input
        if (videoTracks[1]) {

            // setup a reference between our effect and the second input track
            AddTrackReference(videoTrackFX, videoTracks[1], kTrackModifierReference, &myRefIndex2);
            QTInsertChild(myInputMap, kParentAtomIsContainer, kTrackModifierInput, myRefIndex2, 0, 0, NULL, &myInputAtom);

            //  modifier track type ('vide')
            myInputType = EndianU32_NtoB(kTrackModifierTypeImage);
            QTInsertChild(myInputMap, myInputAtom, kTrackModifierType, 1, 0, sizeof(myInputType), &myInputType, NULL);

            // source name for second source - there is a corresponding
            // kEffectSourceName atom in the effect description to
            // identify the source
            myLong = EndianU32_NtoB(kSourceTwoName);
            QTInsertChild(myInputMap, myInputAtom, kEffectDataSourceType, 1, 0, sizeof(myLong), &myLong, NULL);
        }
```

[Next](Clippings-GetWhatKindOfEffect.txt.md)[Previous](Clippings-CreateEffectsTrack.txt.md)

