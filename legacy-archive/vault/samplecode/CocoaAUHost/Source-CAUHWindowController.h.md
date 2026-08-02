---
title: CocoaAUHost
apple_id: DTS40008644
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaAUHost/Listings/Source_CAUHWindowController_h.html
archived_at: '2026-07-18T03:03:36.687392Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaAUHost](CocoaAUHost.md)


[Next](Source-CAUHWindowController.mm.md)[Previous](Source-AudioFileReceiverProtocol.h.md)

# Source/CAUHWindowController.h

```objc
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
#include <AudioToolbox/AudioToolbox.h>
#include <AudioUnit/AudioUnit.h>

#import <Cocoa/Cocoa.h>

#import "AudioFileReceiver_Protocol.h"

@class AudioFileListView;
class CAComponent;

@interface HostingWindowController : NSWindowController <AudioFileReceiver>
{
    // IB: AU Selection
    IBOutlet NSMatrix *             uiAUTypeMatrix;
    IBOutlet NSButton *             uiAudioFileButton;
    IBOutlet NSPopUpButton *        uiAUPopUpButton;
    IBOutlet NSBox *                uiAUViewContainer;

    // IB: Audio Transport
    IBOutlet NSButton *             uiPlayStopButton;
    IBOutlet AudioFileListView *    uiAudioFileTableView;
    IBOutlet NSTextField *          uiAudioFileNowPlayingName;

    // Post-nib view manufacturing
    NSScrollView *                  mScrollView;

    // AU Tracking
    OSType                          mComponentHostType;
    CAComponent *                   mAUList;
    NSMutableArray *                mAudioFileList;

    // AudioFile / AUGraph members
    //AudioFilePlayID                   mAFPID;
    AudioFileID                     mAFID;
    AUGraph                         mGraph;
    AUNode                          mFileNode, mTargetNode, mOutputNode;
    AudioUnit                       mFileUnit, mTargetUnit, mOutputUnit;

}

- (void)stopGraph;

#pragma mark IB Actions
- (IBAction)iaAUTypeChanged:(id)sender;
- (IBAction)iaAUPopUpButtonPressed:(id)sender;
- (IBAction)iaPlayStopButtonPressed:(id)sender;

@end
```

[Next](Source-CAUHWindowController.mm.md)[Previous](Source-AudioFileReceiverProtocol.h.md)

