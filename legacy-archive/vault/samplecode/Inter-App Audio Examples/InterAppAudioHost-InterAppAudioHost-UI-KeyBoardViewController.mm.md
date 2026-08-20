---
title: Inter-App Audio Examples
apple_id: DTS40013418
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2014-03-24'
source_url: https://developer.apple.com/library/archive/samplecode/InterAppAudioSuite/Listings/InterAppAudioHost_InterAppAudioHost_UI_KeyBoardViewController_mm.html
archived_at: '2026-07-18T03:13:05.304654Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Inter-App Audio Examples](Inter-App%20Audio%20Examples.md)


[Next](InterAppAudioHost-InterAppAudioHost-UI-PublishedEffectsViewController.h.md)[Previous](InterAppAudioHost-InterAppAudioHost-UI-KeyBoardViewController.h.md)

# InterAppAudioHost/InterAppAudioHost/UI/KeyBoardViewController.mm

```objc
/*
     File: KeyBoardViewController.mm
 Abstract: 
  Version: 1.1.2

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

#import "KeyBoardViewController.h"

@implementation KeyBoardViewController
@synthesize delegate = _delegate;

#pragma mark - Initialization/ Deallocation
- (void) viewDidLoad {
    [super viewDidLoad];
    _keyBoardView.engine = AUDIO_ENGINE;
    _keyBoardView.displayKeyStart = 24;    
}

- (void) dealloc {
    [_doneButton release];
    [_keyBoardView release];
    [_octaveLabel release];

    [super dealloc];
}

#pragma mark - Action methods
- (IBAction) doneToggle:(id) sender {
    [self.delegate closeView];
}

- (IBAction) downOctaveButtonPressed:(id) sender {
    UInt32 currentStartKey = (UInt32)_keyBoardView.displayKeyStart;
    if (currentStartKey >= 12) {
        _keyBoardView.displayKeyStart -= 12;
        [self updateOctaveLabel];
    }
}

- (IBAction) upOctaveButtonPressed:(id) sender {
    UInt32 currentStartKey = (UInt32)_keyBoardView.displayKeyStart;
    if (currentStartKey <= 64) {
        _keyBoardView.displayKeyStart += 12;
        [self updateOctaveLabel];
    }
}

- (void) updateOctaveLabel {
    UInt32 currentStartKey = (UInt32)_keyBoardView.displayKeyStart;
    SInt32 octave = (currentStartKey / 12) - 3;
    _octaveLabel.text = [NSString stringWithFormat: @"%@%d Octaves", octave >= 0 ? @"+" : @"", (int)octave];
}

@end
```

[Next](InterAppAudioHost-InterAppAudioHost-UI-PublishedEffectsViewController.h.md)[Previous](InterAppAudioHost-InterAppAudioHost-UI-KeyBoardViewController.h.md)

