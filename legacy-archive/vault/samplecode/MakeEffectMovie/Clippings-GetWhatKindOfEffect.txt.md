---
title: MakeEffectMovie
apple_id: DTS10001038
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MakeEffectMovie/Listings/Clippings_GetWhatKindOfEffect_txt.html
archived_at: '2026-07-18T03:14:12.266316Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MakeEffectMovie](MakeEffectMovie.md)


[Next](Clippings-SelectAnEffect.txt.md)[Previous](Clippings-CreateInputMap.txt.md)

# Clippings/GetWhatKindOfEffect.txt

```
    // Extract the 'what' atom to find out what kind of effect it is.
    // This information is returned to us by the effects dialog which
    // is invoked using the QTStandardParameterDialogDoAction function.
    // We'll use this information when we build the effects description
    // a bit further down in the code.

    {
        QTAtom          myEffectAtom;
        QTAtomID        myEffectAtomID;
        long            myEffectCodeSize;
        Ptr             myEffectCodePtr;

        myEffectAtom = QTFindChildByIndex(gEffectSample, kParentAtomIsContainer, kParameterWhatName, kParameterWhatID, &myEffectAtomID);

        myErr = QTLockContainer(gEffectSample);
        BailError(myErr);

        myErr = QTGetAtomDataPtr(gEffectSample, myEffectAtom, &myEffectCodeSize, &myEffectCodePtr);
        BailError(myErr);

        if (myEffectCodeSize != sizeof(OSType)) {
            myErr = paramErr;
            goto bail;
        }

        // get the effect code
        myEffectCode = *(OSType *)myEffectCodePtr;      // "tsk"
        myEffectCode = EndianU32_BtoN(myEffectCode);    // because the data is read from an atom container

        myErr = QTUnlockContainer(gEffectSample);
        BailError(myErr);
    }
```

[Next](Clippings-SelectAnEffect.txt.md)[Previous](Clippings-CreateInputMap.txt.md)

