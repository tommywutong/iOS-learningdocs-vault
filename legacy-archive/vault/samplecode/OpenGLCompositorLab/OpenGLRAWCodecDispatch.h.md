---
title: OpenGLCompositorLab
apple_id: DTS10000541
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2003-04-21'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGLCompositorLab/Listings/OpenGLRAWCodecDispatch_h.html
archived_at: '2026-07-18T03:18:00.346004Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGLCompositorLab](OpenGLCompositorLab.md)


[Next](Quartz2DLayer.h.md)[Previous](OpenGLRAWCodec.m.md)

# OpenGLRAWCodecDispatch.h

```
/*
    File:       SoftCodecDispatch.h

    Description: Component dispatcher for Soft Codec

    Author:     QuickTime Engineering

    Copyright:  © Copyright 1998-2001 Apple Computer, Inc. All rights reserved.

    Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple Computer, Inc.
                ("Apple") in consideration of your agreement to the following terms, and your
                use, installation, modification or redistribution of this Apple software
                constitutes acceptance of these terms.  If you do not agree with these terms,
                please do not use, install, modify or redistribute this Apple software.

                In consideration of your agreement to abide by the following terms, and subject
                to these terms, Apple grants you a personal, non-exclusive license, under AppleÕs
                copyrights in this original Apple software (the "Apple Software"), to use,
                reproduce, modify and redistribute the Apple Software, with or without
                modifications, in source and/or binary forms; provided that if you redistribute
                the Apple Software in its entirety and without modifications, you must retain
                this notice and the following text and disclaimers in all such redistributions of
                the Apple Software.  Neither the name, trademarks, service marks or logos of
                Apple Computer, Inc. may be used to endorse or promote products derived from the
                Apple Software without specific prior written permission from Apple.  Except as
                expressly stated in this notice, no other rights or licenses, express or implied,
                are granted by Apple herein, including but not limited to any patent rights that
                may be infringed by your derivative works or by other works in which the Apple
                Software may be incorporated.

                The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO
                WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED
                WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A PARTICULAR
                PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND OPERATION ALONE OR IN
                COMBINATION WITH YOUR PRODUCTS.

                IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR
                CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
                GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
                ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION
                OF THE APPLE SOFTWARE, HOWEVER CAUSED AND WHETHER UNDER THEORY OF CONTRACT, TORT
                (INCLUDING NEGLIGENCE), STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN
                ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

    Change History (most recent first):
*/

    ComponentComment ("Dispatch file for OpenGLCodec")

    ComponentSelectorOffset (-kComponentGetMPWorkFunctionSelect)

    ComponentRangeCount (4)
    ComponentRangeShift (8)
    ComponentRangeMask  (FF)

    ComponentRangeBegin (0)
/*      StdComponentCall  (GetMPWorkFunction) */
        ComponentError    (GetMPWorkFunction)
        ComponentError    (Unregister)
        StdComponentCall  (Target)
        StdComponentCall  (Register)
        StdComponentCall  (Version)
        StdComponentCall  (CanDo)
        StdComponentCall  (Close)
        StdComponentCall  (Open)
    ComponentRangeEnd   (0)

    ComponentRangeBegin (1)
        ComponentCall     (GetCodecInfo)

        ComponentDelegate (GetCompressionTime)
        ComponentDelegate (GetMaxCompressionSize)
        ComponentDelegate (PreCompress)
        ComponentDelegate (BandCompress)
        ComponentDelegate (PreDecompress)
        ComponentDelegate (BandDecompress)
        ComponentDelegate (Busy)
        ComponentDelegate (GetCompressedImageSize)
        ComponentDelegate (GetSimilarity)
        ComponentDelegate (TrimImage)
        ComponentDelegate (RequestSettings)
        ComponentDelegate (GetSettings)
        ComponentDelegate (SetSettings)
        ComponentDelegate (Flush)
        ComponentDelegate (SetTimeCode)
        ComponentDelegate (IsImageDescriptionEquivalent)
        ComponentDelegate (NewMemory)
        ComponentDelegate (DisposeMemory)
        ComponentDelegate (HitTestData)
        ComponentDelegate (NewImageBufferMemory)
        ComponentDelegate (ExtractAndCombineFields)
        ComponentDelegate (GetMaxCompressionSizeWithSources)
        ComponentDelegate (SetTimeBase)
        ComponentDelegate (SourceChanged)
        ComponentDelegate (FlushFrame)
        ComponentDelegate (GetSettingsAsText)
        ComponentDelegate (GetParameterListHandle)
        ComponentDelegate (GetParameterList)
        ComponentDelegate (CreateStandardParameterDialog)
        ComponentDelegate (IsStandardParameterDialogEvent)
        ComponentDelegate (DismissStandardParameterDialog)
        ComponentDelegate (StandardParameterDialogDoAction)

        ComponentDelegate (NewImageGWorld)
        ComponentDelegate (DisposeImageGWorld)

        ComponentDelegate (HitTestDataWithFlags)
        ComponentDelegate (ValidateParameters)
        ComponentDelegate (GetBaseMPWorkFunction)

        ComponentDelegate (LockBits)
        ComponentDelegate (UnlockBits)

        ComponentDelegate (RequestGammaLevel)
        ComponentDelegate (GetSourceDataGammaLevel)
        ComponentDelegate (GetDecompressLatency)
    ComponentRangeEnd   (1)

    ComponentComment ("SubType range, eg. JPEG")
    ComponentRangeUnused (2)

    ComponentComment ("Base Range")
    ComponentRangeBegin (3)
        ComponentCall  (Preflight)
        ComponentCall  (Initialize)
        ComponentCall  (BeginBand)
        ComponentCall  (DrawBand)
        ComponentCall  (EndBand)
        ComponentCall  (QueueStarting)
        ComponentCall  (QueueStopping)

        ComponentError (DroppingFrame)
        ComponentError (ScheduleFrame)
        ComponentError (CancelTrigger)
    ComponentRangeEnd   (3)

    ComponentComment ("Effect Range")
    ComponentRangeUnused (4)
```

[Next](Quartz2DLayer.h.md)[Previous](OpenGLRAWCodec.m.md)

