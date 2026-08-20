---
title: AudioDataOutputToAudioUnit
apple_id: DTS40007766
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2010-10-26'
source_url: https://developer.apple.com/library/archive/samplecode/AudioDataOutputToAudioUnit/Listings/CaptureSessionController_m.html
archived_at: '2026-07-18T03:01:22.303759Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioDataOutputToAudioUnit](AudioDataOutputToAudioUnit.md)


[Next](Document%20Revision%20History.md)[Previous](CaptureSessionController.h.md)

# CaptureSessionController.m

```objc
/*

 File: CaptureSessionController.m

 Abstract: Class that sets up a QTCaptureSession that outputs to a
 QTCaptureAudioDataOutput. The output audio samples are passed through
 an effect audio unit and are then written to a file.

 Version: 1.0

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

 Copyright (C) 2008-2010 Apple Inc. All Rights Reserved.

 */

#import "CaptureSessionController.h"

#import <QTKit/QTKit.h>

static OSStatus PushCurrentInputBufferIntoAudioUnit(void *                          inRefCon,
                                                    AudioUnitRenderActionFlags *    ioActionFlags,
                                                    const AudioTimeStamp *          inTimeStamp,
                                                    UInt32                          inBusNumber,
                                                    UInt32                          inNumberFrames,
                                                    AudioBufferList *               ioData);

@implementation CaptureSessionController

#pragma mark ======== Setup and teardown methods =========

- (id)init
{
    self = [super init];

    if (self) {
        [self setOutputFile:[@"~/Desktop/Audio Recording.aif" stringByStandardizingPath]];
    }

    return self;
}

- (void)awakeFromNib
{
    BOOL success;
    NSError *error;

    /* Find and open an audio input device. */
    QTCaptureDevice *audioDevice = [QTCaptureDevice defaultInputDeviceWithMediaType:QTMediaTypeSound];

    success = [audioDevice open:&error];
    if (!success) {
        [[NSAlert alertWithError:error] runModal];
        return;
    }

    /* Create the capture session. */
    captureSession = [[QTCaptureSession alloc] init];

    /* Add a device input for the audio device to the session. */
    captureAudioDeviceInput = [[QTCaptureDeviceInput alloc] initWithDevice:audioDevice];
    success = [captureSession addInput:captureAudioDeviceInput error:&error];
    if (!success) {
        [captureAudioDeviceInput release];
        captureAudioDeviceInput = nil;
        [audioDevice close];

        [captureSession release];
        captureSession = nil;

        [[NSAlert alertWithError:error] runModal];
        return;
    }

    /* Create an audio data output for reading captured audio buffers and add it to the capture session. */
    captureAudioDataOutput = [[QTCaptureDecompressedAudioOutput alloc] init];
    [captureAudioDataOutput setDelegate:self];  /* Captured audio buffers will be provided to the delegate via the captureOutput:didOutputAudioSampleBuffer:fromConnection: delegate method. */
    success = [captureSession addOutput:captureAudioDataOutput error:&error];
    if (!success) {
        [captureAudioDeviceInput release];
        captureAudioDeviceInput = nil;
        [audioDevice close];        

        [captureAudioDataOutput release];
        captureAudioDataOutput = nil;

        [captureSession release];
        captureSession = nil;

        [[NSAlert alertWithError:error] runModal];
        return;
    }

    /* Create an effect audio unit to add an effect to the audio before it is written to a file. */
    OSStatus err = noErr;

    AudioComponentDescription effectAudioUnitComponentDescription;
    effectAudioUnitComponentDescription.componentType = kAudioUnitType_Effect;
    effectAudioUnitComponentDescription.componentSubType = kAudioUnitSubType_Delay;
    effectAudioUnitComponentDescription.componentManufacturer = kAudioUnitManufacturer_Apple;
    effectAudioUnitComponentDescription.componentFlags = 0;
    effectAudioUnitComponentDescription.componentFlagsMask = 0;

    AudioComponent effectAudioUnitComponent = AudioComponentFindNext(NULL, &effectAudioUnitComponentDescription);

    err = AudioComponentInstanceNew(effectAudioUnitComponent, &effectAudioUnit);

    if (noErr == err) {
        /* Set a callback on the effect unit that will supply the audio buffers received from the audio data output. */
        AURenderCallbackStruct renderCallbackStruct;
        renderCallbackStruct.inputProc = PushCurrentInputBufferIntoAudioUnit;
        renderCallbackStruct.inputProcRefCon = self;
        err = AudioUnitSetProperty(effectAudioUnit, kAudioUnitProperty_SetRenderCallback, kAudioUnitScope_Input, 0, &renderCallbackStruct, sizeof(renderCallbackStruct));       
    }

    if (noErr != err) {
        if (effectAudioUnit) {
            AudioComponentInstanceDispose(effectAudioUnit);
            effectAudioUnit = NULL;
        }

        [captureAudioDeviceInput release];
        captureAudioDeviceInput = nil;
        [audioDevice close];

        [captureSession release];
        captureSession = nil;

        [[NSAlert alertWithError:[NSError errorWithDomain:NSOSStatusErrorDomain code:err userInfo:nil]] runModal];

        return;
    }

    /* Start the capture session. This will cause the audo data output delegate method to be called for each new audio buffer that is captured from the input device. */
    [captureSession startRunning];

    /* Become the window's delegate so that the capture session can be stopped and cleaned up immediately after the window is closed. */
    [window setDelegate:self];
}

- (void)windowWillClose:(NSNotification *)notification
{
    [self setRecording:NO];
    [captureSession stopRunning];
    QTCaptureDevice *audioDevice = [captureAudioDeviceInput device];
    if ([audioDevice isOpen])
        [audioDevice close];
}

- (void)dealloc
{
    [captureSession release];
    [captureAudioDeviceInput release];
    [captureAudioDataOutput release];

    [outputFile release];

    if (extAudioFile)
        ExtAudioFileDispose(extAudioFile);
    if (effectAudioUnit) {
        if (didSetUpAudioUnits)
            AudioUnitUninitialize(effectAudioUnit);
        AudioComponentInstanceDispose(effectAudioUnit);
    }

    [super dealloc];
}

#pragma mark ======== Audio capture methods =========

/*
 Called periodically by the QTCaptureAudioDataOutput as it receives QTSampleBuffer objects containing audio frames captured by the QTCaptureSession.
 Each QTSampleBuffer will contain multiple frames of audio encoded in the canonical non-interleaved linear PCM format compatible with AudioUnits.
 */
- (void)captureOutput:(QTCaptureOutput *)captureOutput didOutputAudioSampleBuffer:(QTSampleBuffer *)sampleBuffer fromConnection:(QTCaptureConnection *)connection
{
    OSStatus err = noErr;

    BOOL isRecording = [self isRecording];

    /* Get the sample buffer's AudioStreamBasicDescription, which will be used to set the input format of the effect audio unit and the ExtAudioFile. */
    QTFormatDescription *formatDescription = [sampleBuffer formatDescription];
    NSValue *sampleBufferASBDValue = [formatDescription attributeForKey:QTFormatDescriptionAudioStreamBasicDescriptionAttribute];
    if (!sampleBufferASBDValue)
        return;

    AudioStreamBasicDescription sampleBufferASBD = {0};
    [sampleBufferASBDValue getValue:&sampleBufferASBD];    

    if ((sampleBufferASBD.mChannelsPerFrame != currentInputASBD.mChannelsPerFrame) || (sampleBufferASBD.mSampleRate != currentInputASBD.mSampleRate)) {
        /* Although QTCaptureAudioDataOutput guarantees that it will output sample buffers in the canonical format, the number of channels or the
         sample rate of the audio can changes at any time while the capture session is running. If this occurs, the audio unit receiving the buffers
         from the QTCaptureAudioDataOutput needs to be reconfigured with the new format. This also must be done when a buffer is received for the
         first time. */

        currentInputASBD = sampleBufferASBD;

        if (didSetUpAudioUnits) {
            /* The audio units were previously set up, so they must be uninitialized now. */
            AudioUnitUninitialize(effectAudioUnit);

            /* If recording was in progress, the recording needs to be stopped because the audio format changed. */
            if (extAudioFile) {
                ExtAudioFileDispose(extAudioFile);
                extAudioFile = NULL;
            }
        } else {
            didSetUpAudioUnits = YES;
        }

        /* Set the input and output formats of the effect audio unit to match that of the sample buffer. */
        err = AudioUnitSetProperty(effectAudioUnit, kAudioUnitProperty_StreamFormat, kAudioUnitScope_Input, 0, &currentInputASBD, sizeof(currentInputASBD));

        if (noErr == err)
            err = AudioUnitSetProperty(effectAudioUnit, kAudioUnitProperty_StreamFormat, kAudioUnitScope_Output, 0, &currentInputASBD, sizeof(currentInputASBD));

        if (noErr == err)
            err = AudioUnitInitialize(effectAudioUnit);

        if (noErr != err) {
            NSLog(@"Failed to set up audio units (%d)", err);

            didSetUpAudioUnits = NO;
            bzero(&currentInputASBD, sizeof(currentInputASBD));
        }
    }

    if (isRecording && !extAudioFile) {
        /* Start recording by creating an ExtAudioFile and configuring it with the same sample rate and channel layout as those of the current sample buffer. */
        AudioStreamBasicDescription recordedASBD = {0};
        recordedASBD.mSampleRate = currentInputASBD.mSampleRate;
        recordedASBD.mFormatID = kAudioFormatLinearPCM;
        recordedASBD.mFormatFlags = kAudioFormatFlagIsBigEndian | kAudioFormatFlagIsSignedInteger | kAudioFormatFlagIsPacked;
        recordedASBD.mBytesPerPacket = 2 * currentInputASBD.mChannelsPerFrame;
        recordedASBD.mFramesPerPacket = 1;
        recordedASBD.mBytesPerFrame = 2 * currentInputASBD.mChannelsPerFrame;
        recordedASBD.mChannelsPerFrame = currentInputASBD.mChannelsPerFrame;
        recordedASBD.mBitsPerChannel = 16;

        NSData *inputChannelLayoutData = [formatDescription attributeForKey:QTFormatDescriptionAudioChannelLayoutAttribute];
        AudioChannelLayout *recordedChannelLayout = (AudioChannelLayout *)[inputChannelLayoutData bytes];

        err = ExtAudioFileCreateWithURL((CFURLRef)[NSURL fileURLWithPath:[self outputFile]],
                                        kAudioFileAIFFType,
                                        &recordedASBD,
                                        recordedChannelLayout,
                                        kAudioFileFlags_EraseFile,
                                        &extAudioFile);
        if (noErr == err) 
            err = ExtAudioFileSetProperty(extAudioFile, kExtAudioFileProperty_ClientDataFormat, sizeof(currentInputASBD), &currentInputASBD);

        if (noErr != err) {
            NSLog(@"Failed to set up ExtAudioFile (%d)", err);

            ExtAudioFileDispose(extAudioFile);
            extAudioFile = NULL;
        }
    } else if (!isRecording && extAudioFile) {
        /* Stop recording by disposing of the ExtAudioFile. */
        ExtAudioFileDispose(extAudioFile);
        extAudioFile = NULL;
    }

    NSUInteger numberOfFrames = [sampleBuffer numberOfSamples]; /* -[QTSampleBuffer numberOfSamples] corresponds to the number of CoreAudio audio frames. */

    /* In order to render continuously, the effect audio unit needs a new time stamp for each buffer. Use the number of frames for each unit of time. */
    currentSampleTime += (double)numberOfFrames;

    AudioTimeStamp timeStamp = {0};
    timeStamp.mSampleTime = currentSampleTime;
    timeStamp.mFlags |= kAudioTimeStampSampleTimeValid;     

    AudioUnitRenderActionFlags flags = 0;

    /* Create an AudioBufferList large enough to hold the number of frames from the sample buffer in 32-bit floating point PCM format. */
    AudioBufferList *outputABL = calloc(1, sizeof(*outputABL) + (currentInputASBD.mChannelsPerFrame - 1)*sizeof(outputABL->mBuffers[0]));
    outputABL->mNumberBuffers = currentInputASBD.mChannelsPerFrame;
    UInt32 channelIndex;
    for (channelIndex = 0; channelIndex < currentInputASBD.mChannelsPerFrame; channelIndex++) {
        UInt32 dataSize = numberOfFrames * currentInputASBD.mBytesPerFrame;
        outputABL->mBuffers[channelIndex].mDataByteSize = dataSize;
        outputABL->mBuffers[channelIndex].mData = malloc(dataSize);
        outputABL->mBuffers[channelIndex].mNumberChannels = 1;
    }

    /*
     Get an audio buffer list from the sample buffer and assign it to the currentInputAudioBufferList instance variable.
     The the effect audio unit render callback, PushCurrentInputBufferIntoAudioUnit(), can access this value by calling the currentInputAudioBufferList method.
     */
    currentInputAudioBufferList = [sampleBuffer audioBufferListWithOptions:QTSampleBufferAudioBufferListOptionAssure16ByteAlignment];

    /* Tell the effect audio unit to render. This will synchronously call PushCurrentInputBufferIntoAudioUnit(), which will feed the audio buffer list into the effect audio unit. */
    err = AudioUnitRender(effectAudioUnit, &flags, &timeStamp, 0, numberOfFrames, outputABL);
    currentInputAudioBufferList = NULL;

    if ((noErr == err) && extAudioFile) {
        err = ExtAudioFileWriteAsync(extAudioFile, numberOfFrames, outputABL);
    }

    for (channelIndex = 0; channelIndex < currentInputASBD.mChannelsPerFrame; channelIndex++) {
        free(outputABL->mBuffers[channelIndex].mData);
    }
    free(outputABL);
}

/* Used by PushCurrentInputBufferIntoAudioUnit() to access the current audio buffer list that has been output by the QTCaptureAudioDataOutput. */
- (AudioBufferList *)currentInputAudioBufferList
{
    return currentInputAudioBufferList;
}

#pragma mark ======== Property and action definitions =========

@synthesize outputFile = outputFile;
@synthesize recording = recording;

- (IBAction)chooseOutputFile:(id)sender
{
    NSSavePanel *savePanel = [NSSavePanel savePanel];
    [savePanel setAllowedFileTypes:[NSArray arrayWithObject:@"aif"]];
    [savePanel setCanSelectHiddenExtension:YES];

    NSInteger result = [savePanel runModal];
    if (NSOKButton == result) {
        [self setOutputFile:[savePanel filename]];
    }
}

@end

#pragma mark ======== AudioUnit render callback =========

/*
 Synchronously called by the effect audio unit whenever AudioUnitRender() us called.
 Used to feed the audio samples output by the ATCaptureAudioDataOutput to the AudioUnit.
 */
static OSStatus PushCurrentInputBufferIntoAudioUnit(void *                          inRefCon,
                                                    AudioUnitRenderActionFlags *    ioActionFlags,
                                                    const AudioTimeStamp *          inTimeStamp,
                                                    UInt32                          inBusNumber,
                                                    UInt32                          inNumberFrames,
                                                    AudioBufferList *               ioData)
{
    CaptureSessionController *self = (CaptureSessionController *)inRefCon;
    AudioBufferList *currentInputAudioBufferList = [self currentInputAudioBufferList];
    UInt32 bufferIndex, bufferCount = currentInputAudioBufferList->mNumberBuffers;

    if (bufferCount != ioData->mNumberBuffers)
        return badFormat;

    /* Fill the provided AudioBufferList with the data from the AudioBufferList output by the audio data output. */
    for (bufferIndex = 0; bufferIndex < bufferCount; bufferIndex++) {
        ioData->mBuffers[bufferIndex].mDataByteSize = currentInputAudioBufferList->mBuffers[bufferIndex].mDataByteSize;
        ioData->mBuffers[bufferIndex].mData = currentInputAudioBufferList->mBuffers[bufferIndex].mData;
        ioData->mBuffers[bufferIndex].mNumberChannels = currentInputAudioBufferList->mBuffers[bufferIndex].mNumberChannels;
    }

    return noErr;
}
```

[Next](Document%20Revision%20History.md)[Previous](CaptureSessionController.h.md)

