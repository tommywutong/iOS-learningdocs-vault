---
title: WhackedTV
apple_id: DTS10003727
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/WhackedTV/Listings/Sources_Classes_WhackedTVController_h.html
archived_at: '2026-07-18T03:28:14.085303Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WhackedTV](WhackedTV.md)


[Next](Sources-Classes-WhackedTVController.m.md)[Previous](Sources-Classes-Utility-NSOpaqueGrayRulerView.m.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#samplecode/AVRecorder/Introduction/Intro.html](https://developer.apple.com/library/mac/#samplecode/AVRecorder/Introduction/Intro.html)

# Sources/Classes/WhackedTVController.h

```objc
/*  Copyright:  © Copyright 2005 Apple Computer, Inc. All rights reserved.

    Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple Computer, Inc.
            ("Apple") in consideration of your agreement to the following terms, and your
            use, installation, modification or redistribution of this Apple software
            constitutes acceptance of these terms.  If you do not agree with these terms,
            please do not use, install, modify or redistribute this Apple software.

            In consideration of your agreement to abide by the following terms, and subject
            to these terms, Apple grants you a personal, non-exclusive license, under Apple’s
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
*/

#import <Cocoa/Cocoa.h>
#import <QuickTime/QuickTime.h>
#import "SeqGrab.h"

// This is the main controller object in the WhackedTV app.

@interface WhackedTVController : NSObject 
{
    SeqGrab *                   mGrabber;

    IBOutlet NSWindow *         mWhackedWindow;
    IBOutlet NSTextField *      mCaptureToField;
    IBOutlet NSButton *         mBrowseButton;
    IBOutlet NSTableView *      mTableView;
    IBOutlet NSButton *         mAddVideoButton;
    IBOutlet NSButton *         mAddAudioButton;
    IBOutlet NSButton *         mRecordPauseButton;
    IBOutlet NSButton *         mStopButton;

    float                       mVideoPreviewFrameRate;
    CodecQ                      mVideoPreviewQuality;
}

- (IBAction)browseCaptureFile:(id)sender;

- (IBAction)addVideoTrack:(id)sender;
- (IBAction)addAudioTrack:(id)sender;

- (IBAction)setVideoPreviewFrameRate:(id)sender;
- (IBAction)setVideoPreviewQuality:(id)sender;

- (IBAction)recordPause:(id)sender;
- (IBAction)stop:(id)sender;

- (IBAction)doChannelSettings:(id)sender;

- (IBAction)removeChannel:(id)sender;

- (IBAction)saveSettings:(id)sender;
- (IBAction)restoreSettings:(id)sender;

@end
```

[Next](Sources-Classes-WhackedTVController.m.md)[Previous](Sources-Classes-Utility-NSOpaqueGrayRulerView.m.md)

