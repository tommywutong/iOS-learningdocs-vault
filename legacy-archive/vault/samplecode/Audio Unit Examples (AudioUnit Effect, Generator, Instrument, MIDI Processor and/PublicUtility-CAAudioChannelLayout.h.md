---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CAAudioChannelLayout_h.html
archived_at: '2026-07-26T19:54:11.425846Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CADebugPrintf.h.md)[Previous](PublicUtility-CAMath.h.md)

# PublicUtility/CAAudioChannelLayout.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

#if !defined(__CAAudioChannelLayout_h__)
#define __CAAudioChannelLayout_h__

//=============================================================================
//  Includes
//=============================================================================

//  System Includes
#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <CoreAudio/CoreAudioTypes.h>
    #include <CoreFoundation/CoreFoundation.h>
#else
    #include <CoreAudioTypes.h>
    #include <CoreFoundation.h>
#endif
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "CADebugMacros.h"
#include "CAAutoDisposer.h"

#if !HAL_Build
    #include "CAReferenceCounted.h"
#endif

//=============================================================================
//  CAAudioChannelLayout
//=============================================================================

bool    operator== (const AudioChannelLayout &x, const AudioChannelLayout &y);
bool    operator!= (const AudioChannelLayout &x, const AudioChannelLayout &y);

extern "C" void     CAShowAudioChannelLayout (FILE* file, const AudioChannelLayout *layout);

class CAAudioChannelLayout
{
//  static Construction/Destruction
public:
    static AudioChannelLayout*  Create(UInt32 inNumberChannelDescriptions);
    static void                 Destroy(AudioChannelLayout* inChannelLayout);
    static UInt32               CalculateByteSize(UInt32 inNumberChannelDescriptions) {
                                    return SizeOf32(AudioChannelLayout) - SizeOf32(AudioChannelDescription) + (inNumberChannelDescriptions * SizeOf32(AudioChannelDescription));
                                }
    static void                 SetAllToUnknown(AudioChannelLayout& outChannelLayout, UInt32 inNumberChannelDescriptions);
    static UInt32               NumberChannels(const AudioChannelLayout& inLayout);

#if !HAL_Build
// object methods
public:
                                CAAudioChannelLayout ();

                                CAAudioChannelLayout (UInt32 inNumberChannels, bool inChooseSurround);
                                    // if inChooseSurround is false, then symmetrical speaker arrangements
                                    // are chosen in place of surround layouts if there is a choice
                                    // This call chooses layouts based on the expected defaults in
                                    // AudioUnit usage
                                CAAudioChannelLayout (AudioChannelLayoutTag inTag);
                                CAAudioChannelLayout (const CAAudioChannelLayout &c);
                                CAAudioChannelLayout (const AudioChannelLayout* inChannelLayout);
                                ~CAAudioChannelLayout();

    CAAudioChannelLayout&       operator= (const AudioChannelLayout* inChannelLayout);
    CAAudioChannelLayout&       operator= (const CAAudioChannelLayout& c);
    bool                        operator== (const CAAudioChannelLayout &c) const;
    bool                        operator!= (const CAAudioChannelLayout &c) const;

    void                        SetWithTag(AudioChannelLayoutTag inTag);

    bool                        IsValid() const { return NumberChannels() > 0; }
    UInt32                      Size() const { return mLayout ? mLayout->Size() : 0; }

    UInt32                      NumberChannels() const { return mLayout ? mLayout->NumberChannels() : 0; }

    AudioChannelLayoutTag       Tag() const { return Layout().mChannelLayoutTag; }
    const AudioChannelLayout&   Layout() const { return mLayout->Layout(); }
    operator const AudioChannelLayout *() const { return &Layout(); }

    void                        Print () const { Print (stdout); }
    void                        Print (FILE* file) const;

    OSStatus                    Save (CFPropertyListRef *outData) const;
    OSStatus                    Restore (CFPropertyListRef &inData);

private:
    class RefCountedLayout : public CAReferenceCounted {
        void *  operator new(size_t /* size */, size_t aclSize)
        {
            return CA_malloc(sizeof(RefCountedLayout) - sizeof(AudioChannelLayout) + aclSize);
        }

        void    operator delete(void *mem)
        {
            free(mem);
        }

        RefCountedLayout(UInt32 inDataSize) :
            mByteSize(inDataSize)
        {
            memset(&mACL, 0, inDataSize);
        }

    public:
        static RefCountedLayout *CreateWithNumberChannelDescriptions(unsigned nChannels) {
                                size_t size = CAAudioChannelLayout::CalculateByteSize(nChannels);
                                return new(size) RefCountedLayout((UInt32)size);
                            }

        static RefCountedLayout *CreateWithLayout(const AudioChannelLayout *layout) {
                                size_t size = CAAudioChannelLayout::CalculateByteSize(layout->mNumberChannelDescriptions);
                                RefCountedLayout *acl = new(size) RefCountedLayout((UInt32)size);
                                memcpy(&acl->mACL, layout, size);
                                return acl;
                            }
        static RefCountedLayout *CreateWithLayoutTag(AudioChannelLayoutTag layoutTag) {
                                RefCountedLayout *acl = CreateWithNumberChannelDescriptions(0);
                                acl->mACL.mChannelLayoutTag = layoutTag;
                                return acl;
                            }

        const AudioChannelLayout &  Layout() const { return mACL; }

        UInt32                      Size () const { return mByteSize; }

        UInt32                      NumberChannels() { return CAAudioChannelLayout::NumberChannels(Layout()); }

    private:
        const UInt32        mByteSize;
        AudioChannelLayout  mACL;
        // * * * mACL is variable length and thus must be last * * *

            // only the constructors can change the actual state of the layout
        friend CAAudioChannelLayout::CAAudioChannelLayout (UInt32 inNumberChannels, bool inChooseSurround);
        friend OSStatus CAAudioChannelLayout::Restore (CFPropertyListRef &inData);
        friend CAAudioChannelLayout& CAAudioChannelLayout::operator= (const AudioChannelLayout* inChannelLayout);
        friend void CAAudioChannelLayout::SetWithTag(AudioChannelLayoutTag inTag);

        AudioChannelLayout *    GetLayout() { return &mACL; }

    private:
        // prohibited methods: private and unimplemented.
        RefCountedLayout();
        RefCountedLayout(const RefCountedLayout& c);
        RefCountedLayout& operator=(const RefCountedLayout& c);
    };

    RefCountedLayout        *mLayout;
#endif  //  HAL_Build

};

#endif
```

[Next](PublicUtility-CADebugPrintf.h.md)[Previous](PublicUtility-CAMath.h.md)

