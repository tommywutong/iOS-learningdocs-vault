---
title: DiagnosticAUs
apple_id: DTS40008639
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/DiagnosticAUs/Listings/DebugAU_cpp.html
archived_at: '2026-07-18T03:06:50.076093Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DiagnosticAUs](DiagnosticAUs.md)


[Next](DebugAU.r.md)[Previous](AUValidSamplesView.cpp.md)

# DebugAU.cpp

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
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  DebugAU.cpp
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#include "AUBase.h"
#include "DebugAUVersion.h"

#include <AudioUnit/AudioUnitProperties.h>

#include "AUDebugDispatcher.h"

static const AUChannelInfo sChannels[1] = { {-1, -1} };

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#pragma mark ____DebugAU

/*
    virtual OSStatus            PrepareInstrument(MusicDeviceInstrumentID inInstrument) = 0;

    virtual OSStatus            ReleaseInstrument(MusicDeviceInstrumentID inInstrument) = 0;

    virtual OSStatus            StartNote(      MusicDeviceInstrumentID     inInstrument, 
                                                MusicDeviceGroupID          inGroupID, 
                                                NoteInstanceID              &outNoteInstanceID, 
                                                UInt32                      inOffsetSampleFrame, 
                                                const MusicDeviceNoteParams &inParams) = 0;

    virtual OSStatus            StopNote(       MusicDeviceGroupID          inGroupID, 
                                                NoteInstanceID              inNoteInstanceID, 
                                                UInt32                      inOffsetSampleFrame) = 0;
*/

class DebugAU : public AUBase
{
public:
                                DebugAU(AudioUnit component);
    virtual                     ~DebugAU () 
                                { 
                                    delete mDebugDispatcher; 
                                }    

    virtual bool                StreamFormatWritable(   AudioUnitScope                  scope,
                                                        AudioUnitElement                element)
                                {
                                    return IsInitialized() ? false : element == 0;
                                }

    virtual bool                SupportsTail () 
                                { 
                                    return true; 
                                }

    virtual UInt32              SupportedNumChannels (const AUChannelInfo**                 outInfo)
                                {
                                    if (outInfo) *outInfo = sChannels;
                                    return sizeof (sChannels) / sizeof (AUChannelInfo);
                                }

    virtual OSStatus            Initialize();

    virtual OSStatus            Version() 
                                { 
                                    return kDebugAUVersion; 
                                }

    virtual OSStatus    Render( AudioUnitRenderActionFlags  & ioActionFlags,
                                        const AudioTimeStamp        & inTimeStamp,
                                        UInt32                      nFrames);
};

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

COMPONENT_ENTRY(DebugAU)


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  DebugAU::DebugAU
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DebugAU::DebugAU(AudioUnit component)
    : AUBase(component, 1, 1)
{
    mDebugDispatcher = new AUDebugDispatcher (this);
}

OSStatus            DebugAU::Initialize()
{
        // get our current numChannels for input and output
    UInt32 auNumInputChan = GetInput(0)->GetStreamFormat().mChannelsPerFrame;
    UInt32 auNumOutputChan = GetOutput(0)->GetStreamFormat().mChannelsPerFrame;

    if (auNumInputChan != auNumOutputChan) 
        return kAudioUnitErr_FormatNotSupported;

    return noErr;
}

// we can use render here as we know that we're only rendering on bus zero.
OSStatus    DebugAU::Render(    AudioUnitRenderActionFlags  & ioActionFlags,
                                        const AudioTimeStamp        & inTimeStamp,
                                        UInt32                      nFrames)
{
    if (!HasInput(0))
        return kAudioUnitErr_NoConnection;

    AUInputElement *theInput = GetInput(0);
    OSStatus result = theInput->PullInput(ioActionFlags, inTimeStamp, 0 /* element */, nFrames);

    if (result == noErr)
    {
        AUOutputElement *theOutput = GetOutput(0);  // throws if error
        theInput->CopyBufferContentsTo (theOutput->GetBufferList());
    }

    return result;
}
```

[Next](DebugAU.r.md)[Previous](AUValidSamplesView.cpp.md)

