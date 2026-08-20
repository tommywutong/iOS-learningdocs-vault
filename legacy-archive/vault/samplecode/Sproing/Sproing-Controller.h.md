---
title: Sproing
apple_id: DTS10000408
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2011-08-24'
source_url: https://developer.apple.com/library/archive/samplecode/Sproing/Listings/Sproing_Controller_h.html
archived_at: '2026-07-18T03:25:29.176700Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Sproing](Sproing.md)


[Next](Sproing-Controller.m.md)[Previous](README.txt.md)

# Sproing/Controller.h

```objc
/*
     File: Controller.h
 Abstract: This class handles all of the user interface. It has an action method for each
 control in the nib file, and also performs animation using the Rotater class.
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

 Copyright (C) 2011 Apple Inc. All Rights Reserved.

 */

#import <Cocoa/Cocoa.h>
@class Rotater;


@interface Controller : NSObject
{
    //  Control window
    IBOutlet    NSWindow    *window;

    //  Fields to show origin -- one will be empty; the other will show Ò(0, 0)Ó
    IBOutlet    NSTextField *flippedOrigin; // upper left
    IBOutlet    NSTextField *unflippedOrigin; // lower left

    //  Buttons which show springs
    IBOutlet    NSButton    *leftSpring;
    IBOutlet    NSButton    *middleHorizSpring;
    IBOutlet    NSButton    *rightSpring;
    IBOutlet    NSButton    *bottomSpring;
    IBOutlet    NSButton    *middleVerticalSpring;
    IBOutlet    NSButton    *topSpring;

    //  Other controls
    IBOutlet    NSButton    *animatePreviewCheckbox; // starts/stops animation
    IBOutlet    NSButton    *recenterButton;        // restore preview-content position
    IBOutlet    NSButton    *flippedCheckbox;       // changes coordinate system
    IBOutlet    NSButton    *geekyStuffCheckbox;    // toggle drawer

    //  Drawer contents
    IBOutlet    NSTextField *hexText;
    IBOutlet    NSTextField *codeText;


    //  Preview window
    IBOutlet    NSWindow    *previewWindow;
    IBOutlet    NSView      *previewContent; // actually an NSBox, but any view subclass will do


    //  Non-outlet instance variables
    Rotater     *rotater;

    NSRect      originalPreviewContentFrame;            // where preview-box was at startup
    NSRect      originalPreviewContentSuperviewFrame;   // where its superview was at startup
    NSView      *parentView, *childView;                // used in -recenter method only
}


#pragma mark PUBLIC INSTANCE METHODS -- INTERFACE BUILDER ACTIONS

- (IBAction) springChanged: (id) sender;
- (IBAction) animatedChanged: (id) sender;
- (IBAction) recenter: (id) sender;
- (IBAction) flippedChanged: (id) sender;

@end
```

[Next](Sproing-Controller.m.md)[Previous](README.txt.md)

