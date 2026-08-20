---
title: MatrixMixerTest
apple_id: DTS40008645
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/MatrixMixerTest/Listings/MixerController_h.html
archived_at: '2026-07-18T03:14:31.982550Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MatrixMixerTest](MatrixMixerTest.md)


[Next](ReadMe.md.md)[Previous](MixerController.mm.md)

# MixerController.h

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The Main Mixer Controller
*/

#import <Cocoa/Cocoa.h>
#import <CoreAudio/CoreAudio.h>
#import <AudioToolbox/AudioToolbox.h>

typedef struct {
    AudioStreamBasicDescription asbd;
    float *data;
    UInt32 numFrames;
    UInt32 phase;
    NSString *name;
} SndBuf;

#define MAXBUFS 8

struct SynthData
{
    int numbufs;
    SndBuf bufs[MAXBUFS];
    int select;
};

@interface MixerController : NSObject <NSApplicationDelegate>
{
    AUGraph mGraph;
    AudioUnit mixer;
    //AudioUnit defaultOutputUnit;

    IBOutlet NSWindow* theWindow;

    NSMutableArray *meterInPreArray;
    NSMutableArray *meterInArray;
    NSMutableArray *meterOutArray;
    NSMutableArray *xpmeterArray;

    IBOutlet NSSlider* xpslider11;
    IBOutlet NSSlider* xpslider12;
    IBOutlet NSSlider* xpslider13;
    IBOutlet NSSlider* xpslider14;
    IBOutlet NSSlider* xpslider15;
    IBOutlet NSSlider* xpslider21;
    IBOutlet NSSlider* xpslider22;
    IBOutlet NSSlider* xpslider23;
    IBOutlet NSSlider* xpslider24;
    IBOutlet NSSlider* xpslider25;
    IBOutlet NSSlider* xpslider31;
    IBOutlet NSSlider* xpslider32;
    IBOutlet NSSlider* xpslider33;
    IBOutlet NSSlider* xpslider34;
    IBOutlet NSSlider* xpslider35;
    IBOutlet NSSlider* xpslider41;
    IBOutlet NSSlider* xpslider42;
    IBOutlet NSSlider* xpslider43;
    IBOutlet NSSlider* xpslider44;
    IBOutlet NSSlider* xpslider45;

    NSTimer* mTimer;
    SynthData d;
    Boolean isPlaying;
    Boolean automate;
    int automatePhase;
}

- (void)awakeFromNib;
- (void)initializeGraph;
- (void)doTimer: (NSTimer*) timer;

- (IBAction)play:(id)sender;
- (IBAction)setInputVolume:(id)sender;
- (IBAction)setMasterVolume:(id)sender;
- (IBAction)setMatrixVolume:(id)sender;
- (IBAction)setOutputVolume:(id)sender;
- (IBAction)stop:(id)sender;
- (IBAction)enableInput:(id)sender;
- (IBAction)enableOutput:(id)sender;
- (IBAction)addFile:(id)sender;
- (IBAction)automateOn:(id)sender;
- (IBAction)automateOff:(id)sender;

@end
```

[Next](ReadMe.md.md)[Previous](MixerController.mm.md)

