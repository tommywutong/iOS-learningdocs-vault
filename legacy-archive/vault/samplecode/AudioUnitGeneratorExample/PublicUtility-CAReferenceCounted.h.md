---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/PublicUtility_CAReferenceCounted_h.html
archived_at: '2026-07-18T02:59:52.429593Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](PublicUtility-CAStreamBasicDescription.cpp.md)[Previous](PublicUtility-CAMutex.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# PublicUtility/CAReferenceCounted.h

```c
/*
 <codex> 
 <abstract>Part of CoreAudio Utility Classes</abstract>
 <\codex>
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
                SInt32 rc = CAAtomicDecrement32 (&mRefCount);
                if (rc == 0) {
                    releaseObject();
                }
            }

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

[Next](PublicUtility-CAStreamBasicDescription.cpp.md)[Previous](PublicUtility-CAMutex.h.md)

