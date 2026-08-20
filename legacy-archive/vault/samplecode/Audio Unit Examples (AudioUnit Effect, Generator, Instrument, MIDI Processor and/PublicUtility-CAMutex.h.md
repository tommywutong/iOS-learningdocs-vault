---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CAMutex_h.html
archived_at: '2026-07-26T19:54:11.755404Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CAXException.cpp.md)[Previous](PublicUtility-CAAudioChannelLayoutObject.cpp.md)

# PublicUtility/CAMutex.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

#ifndef __CAMutex_h__
#define __CAMutex_h__

//==================================================================================================
//  Includes
//==================================================================================================

//  System Includes
#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <CoreAudio/CoreAudioTypes.h>
#else
    #include <CoreAudioTypes.h>
#endif

#if TARGET_OS_MAC
    #include <pthread.h>
#elif TARGET_OS_WIN32
    #include <windows.h>
#else
    #error  Unsupported operating system
#endif

//==================================================================================================
//  A recursive mutex.
//==================================================================================================

class   CAMutex
{
//  Construction/Destruction
public:
                    CAMutex(const char* inName);
    virtual         ~CAMutex();

//  Actions
public:
    virtual bool    Lock();
    virtual void    Unlock();
    virtual bool    Try(bool& outWasLocked);    // returns true if lock is free, false if not

    virtual bool    IsFree() const;
    virtual bool    IsOwnedByCurrentThread() const;

//  Implementation
protected:
    const char*     mName;
#if TARGET_OS_MAC
    pthread_t       mOwner;
    pthread_mutex_t mMutex;
#elif TARGET_OS_WIN32
    UInt32          mOwner;
    HANDLE          mMutex;
#endif

//  Helper class to manage taking and releasing recursively
public:
    class           Locker
    {

    //  Construction/Destruction
    public:
                    Locker(CAMutex& inMutex) : mMutex(&inMutex), mNeedsRelease(false) { mNeedsRelease = mMutex->Lock(); }
                    Locker(CAMutex* inMutex) : mMutex(inMutex), mNeedsRelease(false) { mNeedsRelease = (mMutex != NULL && mMutex->Lock()); }
                        // in this case the mutex can be null
                    ~Locker() { if(mNeedsRelease) { mMutex->Unlock(); } }

    private:
                    Locker(const Locker&);
        Locker&     operator=(const Locker&);

    //  Implementation
    private:
        CAMutex*    mMutex;
        bool        mNeedsRelease;

    };

// Unlocker
    class Unlocker
    {
    public:
                        Unlocker(CAMutex& inMutex);
                        ~Unlocker();

    private:
        CAMutex&    mMutex;
        bool        mNeedsLock;

        // Hidden definitions of copy ctor, assignment operator
        Unlocker(const Unlocker& copy);             // Not implemented
        Unlocker& operator=(const Unlocker& copy);  // Not implemented
    };

// you can use this with Try - if you take the lock in try, pass in the outWasLocked var
    class Tryer {

    //  Construction/Destruction
    public:
        Tryer (CAMutex &mutex) : mMutex(mutex), mNeedsRelease(false), mHasLock(false) { mHasLock = mMutex.Try (mNeedsRelease); }
        ~Tryer () { if (mNeedsRelease) mMutex.Unlock(); }

        bool HasLock () const { return mHasLock; }

    private:
                    Tryer(const Tryer&);
        Tryer&      operator=(const Tryer&);

    //  Implementation
    private:
        CAMutex &       mMutex;
        bool            mNeedsRelease;
        bool            mHasLock;
    };
};

#endif // __CAMutex_h__
```

[Next](PublicUtility-CAXException.cpp.md)[Previous](PublicUtility-CAAudioChannelLayoutObject.cpp.md)

