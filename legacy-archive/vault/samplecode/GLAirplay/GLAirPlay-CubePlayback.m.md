---
title: GLAirplay
apple_id: DTS40013259
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/GLAirplay/Listings/GLAirPlay_CubePlayback_m.html
archived_at: '2026-07-18T03:09:49.826633Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLAirplay](GLAirplay.md)


[Next](GLAirPlay-MyOpenALSupport.h.md)[Previous](GLAirPlay-MainViewController.h.md)

# GLAirPlay/CubePlayback.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An Obj-C class which wraps an OpenAL playback environment
 */

#import "CubePlayback.h"
#import "MyOpenALSupport.h"

@interface CubePlayback ()
{
    ALuint          _source;
    ALuint          _buffer;
    ALCcontext*     context;
    ALCdevice*      device;
    void            *_data;
    ALfloat         _sourceVolume;
    float           _sourcePos[3];
    float           _listenerPos[3];
    float           _listenerRotation;
}
@end

@implementation CubePlayback

#pragma mark Object Init / Maintenance

void interruptionListener(  void *  inClientData,
                          UInt32    inInterruptionState)
{
    CubePlayback *THIS = (__bridge CubePlayback*)inClientData;
    if (inInterruptionState == kAudioSessionBeginInterruption)
    {
        // do nothing
        [THIS teardownOpenAL];
        if ([THIS isPlaying]) {
            THIS->_wasInterrupted = YES;
            THIS->_isPlaying = NO;
        }
    }
    else if (inInterruptionState == kAudioSessionEndInterruption)
    {
        NSError *error;
        BOOL success = [[AVAudioSession sharedInstance] setActive:true error:&error];
        if (!success) {
            NSLog(@"Error setting audio session active! %@", error.localizedDescription);
        }
        [THIS initOpenAL];
        if (THIS->_wasInterrupted)
        {
            [THIS startSound];
            THIS->_wasInterrupted = NO;
        }
    }
}

// handle[Notification Name]Notification:   handleAVAudioSessionInterruptionNotification
#pragma mark AVAudioSession
- (void)handleAVAudioSessionInterruptionNotification:(NSNotification *)notification
{
    NSUInteger theInterruptionType = [[notification.userInfo valueForKey:AVAudioSessionInterruptionTypeKey] intValue];

    NSLog(@"Session interrupted > --- %s ---\n", theInterruptionType == AVAudioSessionInterruptionTypeBegan ? "Begin Interruption" : "End Interruption");

    if (theInterruptionType == AVAudioSessionInterruptionTypeBegan) {
        alcMakeContextCurrent(NULL);
        if (self.isPlaying) {
            self.wasInterrupted = YES;
        }
    } else if (theInterruptionType == AVAudioSessionInterruptionTypeEnded) {
        // make sure to activate the session
        NSError *error;
        bool success = [[AVAudioSession sharedInstance] setActive:YES error:&error];
        if (!success) NSLog(@"Error setting session active! %@\n", [error localizedDescription]);

        alcMakeContextCurrent(self.context);

        if (self.wasInterrupted)
        {
            [self startSound];
            self.wasInterrupted = NO;
        }
    }
}

- (void)initAVAudioSession
{
    // Configure the audio session
    AVAudioSession *sessionInstance = [AVAudioSession sharedInstance];
    NSError *error;

    // set the session category
    bool success = [sessionInstance setCategory:AVAudioSessionCategoryAmbient error:&error];
    if (!success) NSLog(@"Error setting AVAudioSession category! %@\n", [error localizedDescription]);

    double hwSampleRate = 44100.0;
    success = [sessionInstance setPreferredSampleRate:hwSampleRate error:&error];
    if (!success) NSLog(@"Error setting preferred sample rate! %@\n", [error localizedDescription]);

    // add interruption handler
    [[NSNotificationCenter defaultCenter]   addObserver:self
                                               selector:@selector(handleAVAudioSessionInterruptionNotification:)
                                                   name:AVAudioSessionInterruptionNotification
                                                 object:sessionInstance];

    // activate the audio session
    success = [sessionInstance setActive:YES error:&error];
    if (!success) NSLog(@"Error setting session active! %@\n", [error localizedDescription]);
}

- (id)init
{
    if (self = [super init]) {
        // initial position of the sound source and
        // initial position and rotation of the listener
        // will be set by the view

        // Setup AVAudioSession
        [self initAVAudioSession];

        _wasInterrupted = NO;

        // Initialize our OpenAL environment
        [self initOpenAL];
    }

    return self;
}

- (void)dealloc
{
    if (_data) free(_data);

    [self teardownOpenAL];
}

#pragma mark OpenAL

- (void) initBuffer
{
    ALenum      error = AL_NO_ERROR;
    ALenum      format = 0;
    ALsizei     size = 0;
    ALsizei     freq = 0;

    NSBundle*   bundle = [NSBundle mainBundle];

    // get some audio data from a wave file
    CFURLRef fileURL = CFBridgingRetain([NSURL fileURLWithPath:[bundle pathForResource:@"sound" ofType:@"wav"]]);

    if (fileURL)
    {
        _data = MyGetOpenALAudioData(fileURL, &size, &format, &freq);
        CFRelease(fileURL);

        if((error = alGetError()) != AL_NO_ERROR) {
            printf("error loading sound: %x\n", error);
            exit(1);
        }

        // use the static buffer data API
        alBufferDataStaticProc(_buffer, format, _data, size, freq);

        if((error = alGetError()) != AL_NO_ERROR) {
            printf("error attaching audio to buffer: %x\n", error);
        }
    }
    else
    {
        printf("Could not find file!\n");
        _data = NULL;
    }
}

- (void) initSource
{
    ALenum error = AL_NO_ERROR;
    alGetError(); // Clear the error

    // Turn Looping ON
    alSourcei(_source, AL_LOOPING, AL_TRUE);

    // Set Source Position
    alSourcefv(_source, AL_POSITION, _sourcePos);

    // Set Source Reference Distance
    alSourcef(_source, AL_REFERENCE_DISTANCE, 0.15f);

    // attach OpenAL Buffer to OpenAL Source
    alSourcei(_source, AL_BUFFER, _buffer);

    if((error = alGetError()) != AL_NO_ERROR) {
        printf("Error attaching buffer to source: %x\n", error);
        exit(1);
    }
}


- (void)initOpenAL
{
    ALenum          error = AL_NO_ERROR;

    // Create a new OpenAL Device
    // Pass NULL to specify the system’s default output device
    device = alcOpenDevice(NULL);
    if (device != NULL)
    {
        // Create a new OpenAL Context
        // The new context will render to the OpenAL Device just created
        context = alcCreateContext(device, 0);
        if (context != NULL)
        {
            // Make the new context the Current OpenAL Context
            alcMakeContextCurrent(context);

            // Create some OpenAL Buffer Objects
            alGenBuffers(1, &_buffer);
            if((error = alGetError()) != AL_NO_ERROR) {
                printf("Error Generating Buffers: %x", error);
                exit(1);
            }

            // Create some OpenAL Source Objects
            alGenSources(1, &_source);
            if(alGetError() != AL_NO_ERROR)
            {
                printf("Error generating sources! %x\n", error);
                exit(1);
            }

        }
    }
    // clear any errors
    alGetError();

    [self initBuffer];
    [self initSource];
}

- (void)teardownOpenAL
{
    // Delete the Sources
    alDeleteSources(1, &_source);
    // Delete the Buffers
    alDeleteBuffers(1, &_buffer);

    //Release context
    alcDestroyContext(context);
    //Close device
    alcCloseDevice(device);
}

#pragma mark Play / Pause

- (void)startSound
{
    ALenum error;

    // Begin playing our source file
    alSourcePlay(_source);
    if((error = alGetError()) != AL_NO_ERROR) {
        printf("error starting source: %x\n", error);
    } else {
        // Mark our state as playing
        self.isPlaying = YES;
    }
}

- (void)stopSound
{
    ALenum error;

    // Stop playing our source file
    alSourceStop(_source);
    if((error = alGetError()) != AL_NO_ERROR) {
        printf("error stopping source: %x\n", error);
    } else {
        // Mark our state as not playing
        self.isPlaying = NO;
    }
}

#pragma mark Setters / Getters

- (ALCcontext *)context
{
    return context;
}

- (float*)sourcePos
{
    return _sourcePos;
}

- (void)setSourcePos:(float*)pos
{
    int i;
    for (i=0; i<3; i++)
        _sourcePos[i] = pos[i];

    // Move our audio source coordinates
    alSourcefv(_source, AL_POSITION, _sourcePos);
}



- (float*)listenerPos
{
    return _listenerPos;
}

- (void)setListenerPos:(float*)pos
{
    int i;
    for (i=0; i<3; i++)
        _listenerPos[i] = pos[i];

    // Move our listener coordinates
    alListenerfv(AL_POSITION, _listenerPos);
}



- (float)listenerRotation
{
    return _listenerRotation;
}

- (void)setListenerRotation:(float)radians
{
    _listenerRotation = radians;
    float ori[] = {cosf(radians), 0., sinf(radians), 0., 1., 0.}; //forward & up
    // Set our listener orientation (rotation)
    alListenerfv(AL_ORIENTATION, ori);
}

@end
```

[Next](GLAirPlay-MyOpenALSupport.h.md)[Previous](GLAirPlay-MainViewController.h.md)

