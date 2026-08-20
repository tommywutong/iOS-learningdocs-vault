---
title: Audio Unit Effect Templates
apple_id: DTS10003458
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2005-06-06'
source_url: https://developer.apple.com/library/archive/samplecode/AudioUnitEffectTemplates/Listings/Audio_Units_Audio_Unit_Effect_with_Carbon_View_Source_AUSource_StarterAU_h.html
archived_at: '2026-07-18T03:01:32.266964Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Effect Templates](Audio%20Unit%20Effect%20Templates.md)


[Next](AudioUnits-AudioUnitEffectwithCarbonView-Source-AUSource-StarterAU.r.md)[Previous](AudioUnits-AudioUnitEffectwithCarbonView-Source-AUSource-StarterAU.cpp.md)

# Audio_Units/Audio_Unit_Effect_with_Carbon_View/Source/AUSource/StarterAU.h

```c
/*
*   File:       ÇPROJECTNAMEÈ.h
*   
*   Version:    1.0
* 
*   Created:    ÇDATEÈ
*   
*   Copyright:  Copyright © ÇYEARÈ ÇORGANIZATIONNAMEÈ, All Rights Reserved
* 
*   Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple Computer, Inc. ("Apple") in 
*               consideration of your agreement to the following terms, and your use, installation, modification 
*               or redistribution of this Apple software constitutes acceptance of these terms.  If you do 
*               not agree with these terms, please do not use, install, modify or redistribute this Apple 
*               software.
*
*               In consideration of your agreement to abide by the following terms, and subject to these terms, 
*               Apple grants you a personal, non-exclusive license, under Apple's copyrights in this 
*               original Apple software (the "Apple Software"), to use, reproduce, modify and redistribute the 
*               Apple Software, with or without modifications, in source and/or binary forms; provided that if you 
*               redistribute the Apple Software in its entirety and without modifications, you must retain this 
*               notice and the following text and disclaimers in all such redistributions of the Apple Software. 
*               Neither the name, trademarks, service marks or logos of Apple Computer, Inc. may be used to 
*               endorse or promote products derived from the Apple Software without specific prior written 
*               permission from Apple.  Except as expressly stated in this notice, no other rights or 
*               licenses, express or implied, are granted by Apple herein, including but not limited to any 
*               patent rights that may be infringed by your derivative works or by other works in which the 
*               Apple Software may be incorporated.
*
*               The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO WARRANTIES, EXPRESS OR 
*               IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY 
*               AND FITNESS FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND OPERATION ALONE 
*               OR IN COMBINATION WITH YOUR PRODUCTS.
*
*               IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR CONSEQUENTIAL 
*               DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS 
*               OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, 
*               REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED AND WHETHER 
*               UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY OR OTHERWISE, EVEN 
*               IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*
*/
#include "AUEffectBase.h"
#include "ÇPROJECTNAMEÈVersion.h"
#if AU_DEBUG_DISPATCHER
#include "AUDebugDispatcher.h"
#endif


#ifndef __ÇPROJECTNAMEÈ_h__
#define __ÇPROJECTNAMEÈ_h__

#pragma mark ____ÇPROJECTNAMEÈ Parameters

// parameters
static const float kDefaultValue_ParamOne = 0.5;

static CFStringRef kParameterOneName = CFSTR("Parameter One");

enum {
    kParam_One =0,
    //Add your parameters here...
    kNumberOfParameters=1
};

#pragma mark ____ÇPROJECTNAMEÈ 
class ÇPROJECTNAMEÈ : public AUEffectBase
{
public:
    ÇPROJECTNAMEÈ(AudioUnit component);
#if AU_DEBUG_DISPATCHER
    virtual ~ÇPROJECTNAMEÈ () { delete mDebugDispatcher; }
#endif

    virtual AUKernelBase *      NewKernel() { return new ÇPROJECTNAMEÈKernel(this); }

    virtual ComponentResult     GetParameterValueStrings(AudioUnitScope         inScope,
                                                         AudioUnitParameterID       inParameterID,
                                                         CFArrayRef *           outStrings);

    virtual ComponentResult     GetParameterInfo(AudioUnitScope         inScope,
                                                 AudioUnitParameterID   inParameterID,
                                                 AudioUnitParameterInfo &outParameterInfo);

    virtual ComponentResult     GetPropertyInfo(AudioUnitPropertyID     inID,
                                                AudioUnitScope          inScope,
                                                AudioUnitElement        inElement,
                                                UInt32 &            outDataSize,
                                                Boolean &           outWritable );

    virtual ComponentResult     GetProperty(AudioUnitPropertyID inID,
                                            AudioUnitScope      inScope,
                                            AudioUnitElement        inElement,
                                            void *          outData);

    virtual bool                SupportsTail () { return false; }

    /*! @method Version */
    virtual ComponentResult Version() { return kÇPROJECTNAMEÈVersion; }

    int     GetNumCustomUIComponents () { return 1; }

    void    GetUIComponentDescs (ComponentDescription* inDescArray) {
        inDescArray[0].componentType = kAudioUnitCarbonViewComponentType;
        inDescArray[0].componentSubType = ÇPROJECTNAMEÈ_COMP_SUBTYPE;
        inDescArray[0].componentManufacturer = ÇPROJECTNAMEÈ_COMP_MANF;
        inDescArray[0].componentFlags = 0;
        inDescArray[0].componentFlagsMask = 0;
    }


protected:
        class ÇPROJECTNAMEÈKernel : public AUKernelBase     // most real work happens here
    {
public:
        ÇPROJECTNAMEÈKernel(AUEffectBase *inAudioUnit )
        : AUKernelBase(inAudioUnit)
    {

    }

        // *Required* overides for the process method for this effect
        // processes one channel of interleaved samples
        virtual void        Process(    const Float32   *inSourceP,
                                        Float32         *inDestP,
                                        UInt32          inFramesToProcess,
                                        UInt32          inNumChannels,
                                        bool            &ioSilence);

        virtual void        Reset();

        //private: //state variables...
    };
};

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#endif
```

[Next](AudioUnits-AudioUnitEffectwithCarbonView-Source-AUSource-StarterAU.r.md)[Previous](AudioUnits-AudioUnitEffectwithCarbonView-Source-AUSource-StarterAU.cpp.md)

