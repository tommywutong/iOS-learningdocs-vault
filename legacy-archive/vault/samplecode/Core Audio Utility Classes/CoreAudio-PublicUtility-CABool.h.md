---
title: Core Audio Utility Classes
apple_id: DTS40012328
resource_type: Sample Code
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2014-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/CoreAudioUtilityClasses/Listings/CoreAudio_PublicUtility_CABool_h.html
archived_at: '2026-07-18T03:04:39.478777Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Core Audio Utility Classes](Core%20Audio%20Utility%20Classes.md)


[Next](CoreAudio-PublicUtility-CABufferList.cpp.md)[Previous](CoreAudio-PublicUtility-CABitOperations.h.md)

# CoreAudio/PublicUtility/CABool.h

```c
/*
     File: CABool.h
 Abstract: Part of CoreAudio Utility Classes
  Version: 1.1

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

 Copyright (C) 2014 Apple Inc. All Rights Reserved.

*/
#if !defined(__CABool_h__)
#define __CABool_h__

//=============================================================================
//  Includes
//=============================================================================

//  System Includes
#include "CADebugMacros.h"
#include "CAException.h"

//=============================================================================
//  CABool
//
//  This class implements a boolean value that has a third state that marks
//  it as uninitialized. Accessing the value of an instance of this class that
//  is uninitialized will throw an exception.
//=============================================================================

class CABool
{

//  Construction/Destruction
public:
                    CABool() : mValue(-1) {}
                    CABool(bool inValue) : mValue(inValue ? 1 : 0) {}
                    CABool(const CABool& inValue) : mValue(inValue.mValue) {}
                    ~CABool() {}

    CABool&         operator=(bool inValue) { mValue = inValue; return *this; }
    CABool&         operator=(const CABool& inValue) { mValue = inValue.mValue; return *this; }

                    operator bool() const { ThrowIf(mValue == -1, CAException('nope'), "CABool: uninitialized"); return mValue != 0; }
    bool            IsInitialized() const { return mValue != -1; }
    void            Uninitialize() { mValue = -1; }

private:
    SInt32          mValue;

                    CABool(const void*);    // prevent accidental instantiation with a pointer via bool constructor
};

#endif
```

[Next](CoreAudio-PublicUtility-CABufferList.cpp.md)[Previous](CoreAudio-PublicUtility-CABitOperations.h.md)

