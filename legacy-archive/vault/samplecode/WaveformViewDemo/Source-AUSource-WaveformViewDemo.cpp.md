---
title: WaveformViewDemo
apple_id: DTS40008653
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/WaveformViewDemo/Listings/Source_AUSource_WaveformViewDemo_cpp.html
archived_at: '2026-07-18T03:28:08.792784Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WaveformViewDemo](WaveformViewDemo.md)


[Next](Source-AUSource-WaveformViewDemo.h.md)[Previous](ReadMe.txt.md)

# Source/AUSource/WaveformViewDemo.cpp

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
#include "WaveformViewDemo.h"

#include <vecLib/vDSP.h>

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

COMPONENT_ENTRY(WaveformViewDemo)


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  WaveformViewDemo::WaveformViewDemo
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
WaveformViewDemo::WaveformViewDemo(AudioUnit component)
    : AUEffectBase(component)
{

    mAudioBuffer = NULL;
    mFetchingBufferList = NULL;
}

WaveformViewDemo::~WaveformViewDemo()
{

}


void WaveformViewDemo::Cleanup()
{
    if (mAudioBuffer) delete (mAudioBuffer);
    if (mFetchingBufferList) delete(mFetchingBufferList);
    mAudioBuffer = NULL;
    mFetchingBufferList = NULL;
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  WaveformViewDemo::Initialize
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OSStatus            WaveformViewDemo::Initialize()
{
    OSStatus result = AUEffectBase::Initialize();

    if(result == noErr )
    {
        AllocateBuffers();
    }

    return result;
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  WaveformViewDemo::GetParameterValueStrings
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OSStatus            WaveformViewDemo::GetParameterValueStrings(AudioUnitScope           inScope,
                                                                AudioUnitParameterID    inParameterID,
                                                                CFArrayRef *            outStrings)
{

    return kAudioUnitErr_InvalidProperty;
}



//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  WaveformViewDemo::GetParameterInfo
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OSStatus            WaveformViewDemo::GetParameterInfo(AudioUnitScope           inScope,
                                                        AudioUnitParameterID    inParameterID,
                                                        AudioUnitParameterInfo  &outParameterInfo )
{
    OSStatus result = noErr;

    outParameterInfo.flags =    kAudioUnitParameterFlag_IsWritable
                        |       kAudioUnitParameterFlag_IsReadable;

    if (inScope == kAudioUnitScope_Global) {
        switch(inParameterID)
        {
             default:
                result = kAudioUnitErr_InvalidParameter;
                break;
            }
    } else {
        result = kAudioUnitErr_InvalidParameter;
    }

    return result;
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  WaveformViewDemo::GetPropertyInfo
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OSStatus            WaveformViewDemo::GetPropertyInfo (AudioUnitPropertyID  inID,
                                                        AudioUnitScope      inScope,
                                                        AudioUnitElement    inElement,
                                                        UInt32 &            outDataSize,
                                                        Boolean &           outWritable)
{
 if (inScope == kAudioUnitScope_Global) {
        switch (inID) {

            case kAudioUnitProperty_CocoaUI:
                outWritable = false;
                outDataSize = sizeof (AudioUnitCocoaViewInfo);
                return noErr;

            case kAudioUnitProperty_SampleTimeStamp:
                outWritable = false;
                outDataSize = sizeof(Float64*);
                return noErr;

            case kAudioUnitProperty_WaveformOverview:
                outWritable = true;
                outDataSize = sizeof(WaveformOverview);
                return noErr;

        }
    }

    return AUEffectBase::GetPropertyInfo (inID, inScope, inElement, outDataSize, outWritable);
}

void            WaveformViewDemo::GetWaveformOverview(WaveformOverview* data)
{   
    AudioBufferList *bufferList = &mFetchingBufferList->GetModifiableBufferList();
    UInt32 num = data->mNumDataPoints;
    SampleTime t = (SampleTime) data->mFetchStamp.mSampleTime;
    mAudioBuffer->Fetch(bufferList, num, t, false); 

    Float32* b = (Float32*) bufferList->mBuffers[data->mChannel].mData;
    memcpy(data->mOverview, b, num*sizeof(Float32));    

    vDSP_maxmgv(b, 1, &(data->mMax), num);
    vDSP_minmgv (b, 1,&(data->mMin), num);


#pragma warning we are pulling all the data but only need a certain channel
    data->mFetchStamp.mSampleTime += (Float64) num; 
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  WaveformViewDemo::GetProperty
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OSStatus            WaveformViewDemo::GetProperty(      AudioUnitPropertyID     inID,
                                                        AudioUnitScope          inScope,
                                                        AudioUnitElement        inElement,
                                                        void *                  outData )
{
    if (inScope == kAudioUnitScope_Global) {
        switch (inID) {
            case kAudioUnitProperty_CocoaUI:
            {
                // Look for a resource in the main bundle by name and type.
                CFBundleRef bundle = CFBundleGetBundleWithIdentifier( CFSTR("com.apple.demo.audiounit.WaveformViewDemo") );

                if (bundle == NULL) return fnfErr;

                CFURLRef bundleURL = CFBundleCopyResourceURL( bundle, 
                    CFSTR("WaveformViewDemoViewFactory"), 
                    CFSTR("bundle"), 
                    NULL);

                if (bundleURL == NULL) return fnfErr;

                CFStringRef className = CFSTR("WaveformViewDemoViewFactory");
                AudioUnitCocoaViewInfo cocoaInfo = { bundleURL, className };
                *((AudioUnitCocoaViewInfo *)outData) = cocoaInfo;

                return noErr;
            }
            case kAudioUnitProperty_WaveformOverview:
            {
                WaveformOverview *overview = (WaveformOverview*)outData;
                GetWaveformOverview(overview);
                return noErr;
            }

            case kAudioUnitProperty_SampleTimeStamp:
            {
                *(static_cast<Float64*>(outData)) =mRenderStamp.mSampleTime;        
                return noErr;
            }
        } //end switch
    }//end global if

    return AUEffectBase::GetProperty (inID, inScope, inElement, outData);
}




//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  WaveformViewDemo::SetProperty
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OSStatus            WaveformViewDemo::  SetProperty(AudioUnitPropertyID         inID,
                                                    AudioUnitScope              inScope,
                                                    AudioUnitElement            inElement,
                                                    const void *                inData,
                                                    UInt32                      inDataSize)
{                                           
    return AUEffectBase::SetProperty (inID, inScope, inElement, inData, inDataSize);
}


void            WaveformViewDemo::AllocateBuffers()
{
    if (mAudioBuffer) delete (mAudioBuffer);
    mAudioBuffer = new CARingBuffer();
    mAudioBuffer->Allocate(GetNumberOfChannels(), sizeof(Float32), kDefaultValue_BufferSize); 
    // unlike the spectral buffers we write one number at a time, the spectral ones do entire analysis at a time

    CAStreamBasicDescription    bufClientDesc;      
    bufClientDesc.SetCanonical(GetNumberOfChannels(), false);
    bufClientDesc.mSampleRate = GetSampleRate();

    if (mFetchingBufferList) {
        mFetchingBufferList->DeallocateBuffers();
        delete(mFetchingBufferList);
    }
    mFetchingBufferList = CABufferList::New("fetch buffer", bufClientDesc );
    mFetchingBufferList->AllocateBuffers(sizeof(Float32) * kDefaultValue_BufferSize);



    memset (&mRenderStamp, 0, sizeof(AudioTimeStamp));
    mRenderStamp.mFlags = kAudioTimeStampSampleTimeValid;

}

OSStatus            WaveformViewDemo::ChangeStreamFormat(   AudioUnitScope                      inScope,
                                                            AudioUnitElement                    inElement,
                                                            const CAStreamBasicDescription &    inPrevFormat,
                                                            const CAStreamBasicDescription &    inNewFormat )
{   
    // we could change the default buffer size here because the sample rate may have changed or the
    // number of samples we are pulling may have changed
    return  AUBase::ChangeStreamFormat(inScope, inElement, inPrevFormat, inNewFormat);      
}


OSStatus    WaveformViewDemo::ProcessBufferLists(   AudioUnitRenderActionFlags &    ioActionFlags,
                                                    const AudioBufferList &         inBuffer,
                                                    AudioBufferList &               outBuffer,
                                                    UInt32                          inFramesToProcess )
{       
    SampleTime s = (SampleTime) (mRenderStamp.mSampleTime);
    mAudioBuffer->Store(&inBuffer, inFramesToProcess, s);
    mRenderStamp.mSampleTime += (Float64) inFramesToProcess;

    return AUEffectBase::ProcessBufferLists(ioActionFlags, inBuffer, outBuffer, inFramesToProcess);
}

#pragma mark ___KernelFunctions___

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  WaveformViewKernel::WaveformViewKernel()
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
WaveformViewKernel::WaveformViewKernel(AUEffectBase *inAudioUnit )
    : AUKernelBase(inAudioUnit)
{
    Reset();
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  WaveformViewKernel::~WaveformViewKernel()
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
WaveformViewKernel::~WaveformViewKernel( )
{
}


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  WaveformViewKernel::Reset()
//
//      It's very important to fully reset all filter state variables to their
//      initial settings here.  For delay/reverb effects, the delay buffers must
//      also be cleared here.
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
void        WaveformViewKernel::Reset()
{
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  WaveformViewKernel::Process(int inFramesToProcess)
//
//      We process one non-interleaved stream at a time
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
void WaveformViewKernel::Process(   const Float32   *inSourceP,
                            Float32         *inDestP,
                            UInt32          inFramesToProcess,
                            UInt32          inNumChannels,  // for version 2 AudioUnits inNumChannels is always 1
                            bool &          ioSilence)
{
    // passthrough

    const Float32 *sourceP = inSourceP;
    Float32 *destP = inDestP;
    int n = inFramesToProcess;

    memcpy(destP, sourceP, n*sizeof(Float32));
}
```

[Next](Source-AUSource-WaveformViewDemo.h.md)[Previous](ReadMe.txt.md)

