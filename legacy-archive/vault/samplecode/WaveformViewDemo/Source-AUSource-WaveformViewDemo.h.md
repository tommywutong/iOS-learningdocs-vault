---
title: WaveformViewDemo
apple_id: DTS40008653
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/WaveformViewDemo/Listings/Source_AUSource_WaveformViewDemo_h.html
archived_at: '2026-07-18T03:28:08.899673Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WaveformViewDemo](WaveformViewDemo.md)


[Next](Source-AUSource-WaveformViewDemo.r.md)[Previous](Source-AUSource-WaveformViewDemo.cpp.md)

# Source/AUSource/WaveformViewDemo.h

```c
/*  Copyright © 2007 Apple Inc. All Rights Reserved.

    Disclaimer: IMPORTANT:  This Apple software is supplied to you by 
            Apple Inc. ("Apple") in consideration of your agreement to the
            following terms, and your use, installation, modification or
            redistribution of this Apple software constitutes acceptance of these
            terms.  If you do not agree with these terms, please do not use,
            install, modify or redistribute this Apple software.

            In consideration of your agreement to abide by the following terms, and
            subject to these terms, Apple grants you a personal, non-exclusive
            license, under Apple's copyrights in this original Apple software (the
            "Apple Software"), to use, reproduce, modify and redistribute the Apple
            Software, with or without modifications, in source and/or binary forms;
            provided that if you redistribute the Apple Software in its entirety and
            without modifications, you must retain this notice and the following
            text and disclaimers in all such redistributions of the Apple Software. 
            Neither the name, trademarks, service marks or logos of Apple Inc. 
            may be used to endorse or promote products derived from the Apple
            Software without specific prior written permission from Apple.  Except
            as expressly stated in this notice, no other rights or licenses, express
            or implied, are granted by Apple herein, including but not limited to
            any patent rights that may be infringed by your derivative works or by
            other works in which the Apple Software may be incorporated.

            The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
            MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
            THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
            FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
            OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

            IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
            OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
            SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
            INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
            MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
            AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
            STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
            POSSIBILITY OF SUCH DAMAGE.
*/
#ifndef __WaveformViewDemo_h__
#define __WaveformViewDemo_h__



#include "WaveformViewDemoVersion.h"
#include "AUEffectBase.h"
#include "CARingBuffer.h"
#include "CABufferList.h"

#include "CAWaveformViewSharedData.h"


#if AU_DEBUG_DISPATCHER
    #include "AUDebugDispatcher.h"
#endif


// Here we define a custom property so the view is able to retrieve the wavefrom overview
// curve.  The curve changes often...
// custom properties id's must be 64000 or greater
// see <AudioUnit/AudioUnitProperties.h> for a list of Apple-defined standard properties
//
#pragma mark ___WaveformViewDemo Properties
enum
{
    kAudioUnitProperty_WaveformOverview = 65536,
    kAudioUnitProperty_SampleTimeStamp = 65537
};


#pragma mark ____WaveformViewDemo Parameters

#define kMaxWaveformSamples 44100

static const UInt64 kDefaultValue_BufferSize = kMaxWaveformSamples;


class WaveformViewKernel : public AUKernelBase      // the actual filter DSP happens here
{
public:
    WaveformViewKernel(AUEffectBase *inAudioUnit );
    virtual ~WaveformViewKernel();

    // processes one channel of non-interleaved samples
    virtual void        Process(    const Float32   *inSourceP,
                                    Float32         *inDestP,
                                    UInt32          inFramesToProcess,
                                    UInt32          inNumChannels,
                                    bool &          ioSilence);

    // resets the filter state
    virtual void        Reset();

    private:

};


#pragma mark ____WaveformViewDemo
class WaveformViewDemo : public AUEffectBase
{
public:
    WaveformViewDemo(AudioUnit component);
    virtual ~WaveformViewDemo ();

    void    Cleanup();

    virtual AUKernelBase *      NewKernel() { return new WaveformViewKernel(this); }

    void                        AllocateBuffers();

    void                        GetWaveformOverview(WaveformOverview* data);

    virtual OSStatus            GetParameterValueStrings(AudioUnitScope             inScope,
                                                         AudioUnitParameterID       inParameterID,
                                                         CFArrayRef *               outStrings);

    virtual OSStatus            GetParameterInfo(AudioUnitScope             inScope,
                                                 AudioUnitParameterID       inParameterID,
                                                 AudioUnitParameterInfo     &outParameterInfo);

    virtual OSStatus            GetPropertyInfo(AudioUnitPropertyID     inID,
                                                AudioUnitScope          inScope,
                                                AudioUnitElement        inElement,
                                                UInt32 &                outDataSize,
                                                Boolean &               outWritable );

    virtual OSStatus            GetProperty(AudioUnitPropertyID     inID,
                                            AudioUnitScope          inScope,
                                            AudioUnitElement        inElement,
                                            void *                  outData);

    virtual OSStatus            SetProperty(AudioUnitPropertyID         inID,
                                            AudioUnitScope              inScope,
                                            AudioUnitElement            inElement,
                                            const void *                inData,
                                            UInt32                      inDataSize);

    virtual Float64             GetTailTime(){return(0.0);}
    virtual bool                SupportsTail () { return true; }

    /*! @method Version */
    virtual OSStatus            Version() { return kWaveformViewDemoVersion; }

    virtual OSStatus            Initialize();

    virtual OSStatus            ChangeStreamFormat (AudioUnitScope                      inScope,
                                                    AudioUnitElement                    inElement,
                                                    const CAStreamBasicDescription &    inPrevFormat,
                                                    const CAStreamBasicDescription &    inNewFormat);

    OSStatus                    ProcessBufferLists( AudioUnitRenderActionFlags &    ioActionFlags,
                                                    const AudioBufferList &         inBuffer,
                                                    AudioBufferList &               outBuffer,
                                                    UInt32                          inFramesToProcess );

    private:
        CARingBuffer*           mAudioBuffer;       
        CABufferList*           mFetchingBufferList;

        AudioTimeStamp          mRenderStamp;
};

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#endif
```

[Next](Source-AUSource-WaveformViewDemo.r.md)[Previous](Source-AUSource-WaveformViewDemo.cpp.md)

