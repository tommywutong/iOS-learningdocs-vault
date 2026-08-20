---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CAReferenceCounted_h.html
archived_at: '2026-07-26T19:54:11.250196Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CADebugger.cpp.md)[Previous](AudioUnitGeneratorExample-ReadMe.md.md)

# PublicUtility/CAReferenceCounted.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

#ifndef __CAReferenceCounted_h__
#define __CAReferenceCounted_h__

#include "CAAtomic.h"

// base class for reference-counted objects
class CAReferenceCounted {
public:
    CAReferenceCounted() : mRefCount(1) {}

    void    retain() { CAAtomicIncrement32(&mRefCount); }

    void    release()
            {
                SInt32 rc = CAAtomicDecrement32(&mRefCount);
                if (rc == 0) {
                    releaseObject();
                }
            }

    class Retainer {
    public:
        Retainer(CAReferenceCounted *obj) : mObject(obj) { mObject->retain(); }
        ~Retainer() { mObject->release(); }

    private:
        CAReferenceCounted *    mObject;
    };

protected:
    virtual ~CAReferenceCounted() { }

    virtual void releaseObject ()
            {
                delete this;
            }

#if DEBUG
public:
#endif
    SInt32  GetReferenceCount() const { return mRefCount; }
private:
    SInt32      mRefCount;

    CAReferenceCounted(const CAReferenceCounted &a);
    CAReferenceCounted &operator=(const CAReferenceCounted &a);
};

#endif // __CAReferenceCounted_h__
```

[Next](PublicUtility-CADebugger.cpp.md)[Previous](AudioUnitGeneratorExample-ReadMe.md.md)

