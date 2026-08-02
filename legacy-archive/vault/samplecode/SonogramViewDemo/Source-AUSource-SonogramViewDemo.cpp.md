---
title: SonogramViewDemo
apple_id: DTS40008647
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-01-24'
source_url: https://developer.apple.com/library/archive/samplecode/SonogramViewDemo/Listings/Source_AUSource_SonogramViewDemo_cpp.html
archived_at: '2026-07-18T03:25:01.405776Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SonogramViewDemo](SonogramViewDemo.md)


[Next](Source-AUSource-SonogramViewDemo.h.md)[Previous](ReadMe.txt.md)

# Source/AUSource/SonogramViewDemo.cpp

```c
/*
    File: SonogramViewDemo.cpp
Abstract: n/a
 Version: 1.0.1

Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
Inc. ("Apple") in consideration of your agreement to the following
terms, and your use, installation, modification or redistribution of
this Apple software constitutes acceptance of these terms.  If you do
not agree with these terms, please do not use, install, modify or
redistribute this Apple software.

In consideration of your agreement to abide by the following terms, and
subject to these terms, Apple grants you a personal, non-exclusive
license, under Apple's copyrights in this original Apple software (the
"Apple Software"), to use, reproduce, modify and redistribute the Apple
Software, with or without modifications, in source and/or binary forms;
provided that if you redistribute the Apple Software in its entirety and
without modifications, you must retain this notice and the following
text and disclaimers in all such redistributions of the Apple Software.
Neither the name, trademarks, service marks or logos of Apple Inc. may
be used to endorse or promote products derived from the Apple Software
without specific prior written permission from Apple.  Except as
expressly stated in this notice, no other rights or licenses, express or
implied, are granted by Apple herein, including but not limited to any
patent rights that may be infringed by your derivative works or by other
works in which the Apple Software may be incorporated.

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

Copyright (C) 2012 Apple Inc. All Rights Reserved.

*/

#include "SonogramViewDemo.h"


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#if __MAC_OS_X_VERSION_MIN_REQUIRED < 1070
COMPONENT_ENTRY(SonogramViewDemo)
#else
AUDIOCOMPONENT_ENTRY(AUBaseFactory, SonogramViewDemo)
#endif


void SonogramViewDemo::Cleanup()
{

    mSpectralProcessor.free();
    if (mSpectrumBuffer) delete(mSpectrumBuffer);
    if (mFetchingBufferList) delete(mFetchingBufferList);
    if (mSpectralDataBufferList) delete(mSpectralDataBufferList);

    if (mMinAmp) free(mMinAmp);
    if (mMaxAmp) free(mMaxAmp);

    mSpectrumBuffer = NULL;
    mFetchingBufferList = NULL;
    mSpectralDataBufferList = NULL;

    mMinAmp = NULL;
    mMaxAmp = NULL;
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  SonogramViewDemo::SonogramViewDemo
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SonogramViewDemo::SonogramViewDemo(AudioUnit component)
    : AUEffectBase(component, true)
{   

    mSpectrumBuffer = NULL;
    mFetchingBufferList = NULL;
    mSpectralDataBufferList = NULL;

    mMinAmp = NULL;
    mMaxAmp = NULL;
}

SonogramViewDemo::~SonogramViewDemo()
{
    Cleanup();
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  WaveformViewDemo::Initialize
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OSStatus            SonogramViewDemo::Initialize()
{
    OSStatus result = AUEffectBase::Initialize();

    if(result == noErr )
    {
        AllocateBuffers();
    }

    return result;
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  SonogramViewDemo::GetParameterValueStrings
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OSStatus            SonogramViewDemo::GetParameterValueStrings(AudioUnitScope       inScope,
                                                                AudioUnitParameterID    inParameterID,
                                                                CFArrayRef *        outStrings)
{

    return kAudioUnitErr_InvalidProperty;
}



//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  SonogramViewDemo::GetParameterInfo
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OSStatus            SonogramViewDemo::GetParameterInfo(AudioUnitScope       inScope,
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
//  SonogramViewDemo::GetPropertyInfo
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OSStatus            SonogramViewDemo::GetPropertyInfo (AudioUnitPropertyID  inID,
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

            case kAudioUnitProperty_SonogramOverview:
                outWritable = true;
                outDataSize = sizeof(SonogramOverview);
                return noErr;

        }
    }

    return AUEffectBase::GetPropertyInfo (inID, inScope, inElement, outDataSize, outWritable);
}


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  SonogramViewDemo::GetProperty
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OSStatus            SonogramViewDemo::GetProperty(      AudioUnitPropertyID inID,
                                                        AudioUnitScope      inScope,
                                                        AudioUnitElement    inElement,
                                                        void *              outData )
{
if (inScope == kAudioUnitScope_Global) {
        switch (inID) {
            case kAudioUnitProperty_CocoaUI:
            {
                // Look for a resource in the main bundle by name and type.
                CFBundleRef bundle = CFBundleGetBundleWithIdentifier( CFSTR("com.apple.demo.audiounit.SonogramViewDemo") );

                if (bundle == NULL) return fnfErr;

                CFURLRef bundleURL = CFBundleCopyResourceURL( bundle, 
                    CFSTR("SonogramViewDemoViewFactory"), 
                    CFSTR("bundle"), 
                    NULL);

                if (bundleURL == NULL) return fnfErr;

                CFStringRef className = CFSTR("SonogramViewDemoViewFactory");
                AudioUnitCocoaViewInfo cocoaInfo = { bundleURL, {className} };
                *((AudioUnitCocoaViewInfo *)outData) = cocoaInfo;

                return noErr;
        }
        case kAudioUnitProperty_SonogramOverview:
        {
            SonogramOverview *overview = (SonogramOverview*)outData;
            return GetSonogramOverview(overview);
        }

        case kAudioUnitProperty_SampleTimeStamp:
        {
            *(static_cast<Float64*>(outData)) = mRenderStamp.mSampleTime;       
            return noErr;
        }
      }
    }

    return AUEffectBase::GetProperty (inID, inScope, inElement, outData);
}

#pragma mark CommuniationWithView


void    SonogramViewDemo::AllocateBuffers()
{
    mBlockSize = 1024;
    mNumBins = mBlockSize>>1;

    if (mSpectrumBuffer) {
        // delete calls deallocate
        delete (mSpectrumBuffer);
    }
    mSpectrumBuffer = new CARingBuffer();
    mSpectrumBuffer->Allocate(GetNumberOfChannels(), mNumBins*sizeof(Float32), kMaxSonogramLatency);

    CAStreamBasicDescription    bufClientDesc;      
    bufClientDesc.SetCanonical(GetNumberOfChannels(), false);
    bufClientDesc.mSampleRate = GetSampleRate();

    UInt32 frameLength = kDefaultValue_BufferSize*sizeof(Float32);

    if (mFetchingBufferList) {      
        mFetchingBufferList->DeallocateBuffers();
        delete(mFetchingBufferList);
    }
    mFetchingBufferList = CABufferList::New("fetch buffer", bufClientDesc );
    mFetchingBufferList->AllocateBuffers(frameLength);

    if (mSpectralDataBufferList) {
        mSpectralDataBufferList->DeallocateBuffers();
        delete(mSpectralDataBufferList);
    }
    mSpectralDataBufferList = CABufferList::New("temp buffer", bufClientDesc );
    mSpectralDataBufferList->AllocateBuffers(frameLength);

    memset (&mRenderStamp, 0, sizeof(AudioTimeStamp));
    mRenderStamp.mFlags = kAudioTimeStampSampleTimeValid;   


    mSpectralProcessor.free();
    mSpectralProcessor = new CASpectralProcessor(mBlockSize, mNumBins, GetNumberOfChannels(), GetMaxFramesPerSlice());

    if (mMinAmp) free(mMinAmp);
    mMinAmp = (Float32*) calloc(GetNumberOfChannels(), sizeof(Float32));

    if (mMaxAmp) free(mMaxAmp);
    mMaxAmp = (Float32*) calloc(GetNumberOfChannels(), sizeof(Float32));


}

OSStatus            SonogramViewDemo::ChangeStreamFormat(   AudioUnitScope                      inScope,
                                                            AudioUnitElement                    inElement,
                                                            const CAStreamBasicDescription &    inPrevFormat,
                                                            const CAStreamBasicDescription &    inNewFormat )
{   
    // we could change the default buffer size here because the sample rate may have changed or the
    // number of samples we are pulling may have changed
    return  AUBase::ChangeStreamFormat(inScope, inElement, inPrevFormat, inNewFormat);      
}

OSStatus        SonogramViewDemo::GetSonogramOverview(SonogramOverview* data)
{   
    #pragma warning we are pulling all the data but only need a certain channel

    data->mNumBins = mNumBins;  
    data->mMinAmp = mMinAmp[data->mChannel];
    data->mMaxAmp = mMaxAmp[data->mChannel];    

    UInt32 num = data->mNumSlices; 

    if (num > kMaxSonogramLatency) return kAudioUnitErr_TooManyFramesToProcess; 

    AudioBufferList *bufferList = &mFetchingBufferList->GetModifiableBufferList();
    SampleTime t = (SampleTime) data->mFetchStamp.mSampleTime;
#if __MAC_OS_X_VERSION_MIN_REQUIRED < 1070    
    mSpectrumBuffer->Fetch(bufferList, num, t, false);  // you fetch mNumBins * mNumSlices of data
#else
    mSpectrumBuffer->Fetch(bufferList, num, t);         // you fetch mNumBins * mNumSlices of data
#endif

    Float32* b = (Float32*) bufferList->mBuffers[data->mChannel].mData;
    memcpy(data->mOverview, b, num*mNumBins*sizeof(Float32));       
    data->mFetchStamp.mSampleTime += num;
    return noErr;

}


OSStatus    SonogramViewDemo::Render(   AudioUnitRenderActionFlags      &ioActionFlags,
                                                const AudioTimeStamp &          inTimeStamp,
                                                UInt32                          inFramesToProcess )
{
    UInt32 actionFlags = 0;
    OSStatus err = PullInput(0, actionFlags, inTimeStamp, inFramesToProcess);
    if (err) return err;

    AUInputElement* inputBus = GetInput(0);
    AUOutputElement* outputBus = GetOutput(0);  
    outputBus->PrepareBuffer(inFramesToProcess); // prepare the output buffer list  
    AudioBufferList& inputBufList = inputBus->GetBufferList();

    if (
        mSpectralProcessor->ProcessForwards(inFramesToProcess, &inputBufList)
    ){


        AudioBufferList* sdBufferList = &mSpectralDataBufferList->GetModifiableBufferList(); 
        mSpectralProcessor->GetMagnitude(sdBufferList, mMinAmp, mMaxAmp);
        // copy mNumBins of numbers out

        SampleTime s = (SampleTime) (mRenderStamp.mSampleTime);
        mSpectrumBuffer->Store(sdBufferList, 1, s);

        mRenderStamp.mSampleTime += 1; 
    }           
    return AUEffectBase::Render(ioActionFlags, inTimeStamp, inFramesToProcess);

}

#pragma mark ____SonogramViewDemoEffectKernel


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  SonogramViewDemoKernel::Reset()
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
void        SonogramViewDemoKernel::Reset()
{
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  SonogramViewDemoKernel::Process
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
void SonogramViewDemoKernel::Process(   const Float32       *inSourceP,
                                              Float32       *inDestP,
                                              UInt32        inFramesToProcess,
                                              UInt32        inNumChannels, // for version 2 AudioUnits inNumChannels is always 1
                                              bool          &ioSilence )
{

    //This code will pass-thru the audio data.
    //This is where you want to process data to produce an effect.

 }
```

[Next](Source-AUSource-SonogramViewDemo.h.md)[Previous](ReadMe.txt.md)

