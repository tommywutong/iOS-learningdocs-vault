---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CAGuard_h.html
archived_at: '2026-07-26T19:54:11.443301Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CAVectorUnit.h.md)[Previous](PublicUtility-CADebugPrintf.h.md)

# PublicUtility/CAGuard.h

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

#if !defined(__CAGuard_h__)
#define __CAGuard_h__

//==================================================================================================
//  Includes
//=============================================================================

//  Super Class Includes
#include "CAMutex.h"

#if CoreAudio_Debug
//  #define Log_Average_Latency 1
#endif

//==================================================================================================
//  CAGuard
//
//  This is your typical mutex with signalling implemented via pthreads.
//  Lock() will return true if and only if the guard is locked on that call.
//  A thread that already has the guard will receive 'false' if it locks it
//  again. Use of the stack-based CAGuard::Locker class is highly recommended
//  to properly manage the recursive nesting. The Wait calls with timeouts
//  will return true if and only if the timeout period expired. They will
//  return false if they receive notification any other way.
//==================================================================================================

class   CAGuard : public CAMutex
{

//  Construction/Destruction
public:
                    CAGuard(const char* inName);
    virtual         ~CAGuard();

//  Actions
public:
    virtual void    Wait();
    virtual bool    WaitFor(UInt64 inNanos);
    virtual bool    WaitUntil(UInt64 inNanos);

    virtual void    Notify();
    virtual void    NotifyAll();

//  Implementation
protected:
#if TARGET_OS_MAC
    pthread_cond_t  mCondVar;
#else
    HANDLE          mEvent;
#endif
#if Log_Average_Latency
    Float64         mAverageLatencyAccumulator;
    UInt32          mAverageLatencyCount;
#endif

//  Helper class to manage taking and releasing recursively
public:
    class           Locker
    {

    //  Construction/Destruction
    public:
                    Locker(CAGuard& inGuard) : mGuard(inGuard), mNeedsRelease(false) { mNeedsRelease = mGuard.Lock(); }
                    ~Locker() { if(mNeedsRelease) { mGuard.Unlock(); } }

    private:
                    Locker(const Locker&);
        Locker&     operator=(const Locker&);

    //  Actions
    public:
        void        Wait() { mGuard.Wait(); }
        bool        WaitFor(UInt64 inNanos) { return mGuard.WaitFor(inNanos); }
        bool        WaitUntil(UInt64 inNanos) { return mGuard.WaitUntil(inNanos); }

        void        Notify() { mGuard.Notify(); }
        void        NotifyAll() { mGuard.NotifyAll(); }

    //  Implementation
    private:
        CAGuard&    mGuard;
        bool        mNeedsRelease;
    };

};

#endif
```

[Next](PublicUtility-CAVectorUnit.h.md)[Previous](PublicUtility-CADebugPrintf.h.md)

