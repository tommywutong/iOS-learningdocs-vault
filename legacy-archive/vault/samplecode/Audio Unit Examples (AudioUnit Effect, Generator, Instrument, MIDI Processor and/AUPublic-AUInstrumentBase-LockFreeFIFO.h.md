---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_AUInstrumentBase_LockFreeFIFO_h.html
archived_at: '2026-07-26T19:54:12.839829Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitEffectExample-Source-AUSource-FilterVersion.h.md)[Previous](AUPublic-AUInstrumentBase-SynthElement.cpp.md)

# AUPublic/AUInstrumentBase/LockFreeFIFO.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio AUInstrument Base Classes
*/

#include <libkern/OSAtomic.h>

template <class ITEM>
class LockFreeFIFOWithFree
{
    LockFreeFIFOWithFree(); // private, unimplemented.
public:
    LockFreeFIFOWithFree(UInt32 inMaxSize)
        : mReadIndex(0), mWriteIndex(0), mFreeIndex(0)
    {
        //assert(IsPowerOfTwo(inMaxSize));
        mItems = new ITEM[inMaxSize];
        mMask = inMaxSize - 1;
    }

    ~LockFreeFIFOWithFree()
    {
        delete [] mItems;
    }

    void Reset()
    {
        FreeItems();
        mReadIndex = 0;
        mWriteIndex = 0;
        mFreeIndex = 0;
    }

    ITEM* WriteItem()
    {
        //printf("WriteItem %d %d\n", mReadIndex, mWriteIndex);
        FreeItems(); // free items on the write thread.
        int32_t nextWriteIndex = (mWriteIndex + 1) & mMask;
        if (nextWriteIndex == mFreeIndex) return NULL;
        return &mItems[mWriteIndex];
    }

    ITEM* ReadItem()
    {
        //printf("ReadItem %d %d\n", mReadIndex, mWriteIndex);
        if (mReadIndex == mWriteIndex) return NULL;
        return &mItems[mReadIndex];
    }
    void AdvanceWritePtr() { OSAtomicCompareAndSwap32(mWriteIndex, (mWriteIndex + 1) & mMask, &mWriteIndex); }
    void AdvanceReadPtr()  { OSAtomicCompareAndSwap32(mReadIndex,  (mReadIndex  + 1) & mMask, &mReadIndex); }
private:
    ITEM* FreeItem()
    {
        if (mFreeIndex == mReadIndex) return NULL;
        return &mItems[mFreeIndex];
    }
    void AdvanceFreePtr() { OSAtomicCompareAndSwap32(mFreeIndex, (mFreeIndex + 1) & mMask, &mFreeIndex); }

    void FreeItems()
    {
        ITEM* item;
        while ((item = FreeItem()) != NULL)
        {
            item->Free();
            AdvanceFreePtr();
        }
    }

    volatile int32_t mReadIndex, mWriteIndex, mFreeIndex;
    int32_t mMask;
    ITEM *mItems;
};

// Same as above but no free.

template <class ITEM>
class LockFreeFIFO
{
    LockFreeFIFO(); // private, unimplemented.
public:
    LockFreeFIFO(UInt32 inMaxSize)
        : mReadIndex(0), mWriteIndex(0)
    {
        //assert(IsPowerOfTwo(inMaxSize));
        mItems = new ITEM[inMaxSize];
        mMask = inMaxSize - 1;
    }

    ~LockFreeFIFO()
    {
        delete [] mItems;
    }

    void Reset()
    {
        mReadIndex = 0;
        mWriteIndex = 0;
    }

    ITEM* WriteItem()
    {
        int32_t nextWriteIndex = (mWriteIndex + 1) & mMask;
        if (nextWriteIndex == mReadIndex) return NULL;
        return &mItems[mWriteIndex];
    }

    ITEM* ReadItem()
    {
        if (mReadIndex == mWriteIndex) return NULL;
        return &mItems[mReadIndex];
    }

        // the CompareAndSwap will always succeed. We use CompareAndSwap because it calls the PowerPC sync instruction,
        // plus any processor bug workarounds for various CPUs.
    void AdvanceWritePtr() { OSAtomicCompareAndSwap32(mWriteIndex, (mWriteIndex + 1) & mMask, &mWriteIndex); }
    void AdvanceReadPtr()  { OSAtomicCompareAndSwap32(mReadIndex,  (mReadIndex  + 1) & mMask, &mReadIndex); }

private:

    volatile int32_t mReadIndex, mWriteIndex;
    int32_t mMask;
    ITEM *mItems;
};
```

[Next](AudioUnitEffectExample-Source-AUSource-FilterVersion.h.md)[Previous](AUPublic-AUInstrumentBase-SynthElement.cpp.md)

