---
title: iChatTheater
apple_id: DTS10004197
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: InstantMessage
published: '2012-08-27'
source_url: https://developer.apple.com/library/archive/samplecode/iChatTheater/Listings/Controller_m.html
archived_at: '2026-07-18T03:29:34.400009Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iChatTheater](iChatTheater.md)


[Next](DropQCView.h.md)[Previous](Controller.h.md)

# Controller.m

```objc
/*

 File: Controller.m

 Abstract: The iChat Theater video source is set according the currently
           selected tab, as set by the user via the popup button.
           The SlideshowView and QTMovieView will be automatically started
           when an iChat Theater session begins.

 Version: 2.0

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

 Copyright (C) 2007 - 2008 Apple Inc. All Rights Reserved.

 */

#import "Controller.h"
#import "SlideshowView.h"
#import "DropQTMovieView.h"
#import <InstantMessage/IMService.h>
#import <InstantMessage/IMAVManager.h>
#import <InstantMessage/IMAVControl.h>
#import <QTKit/QTMovie.h>
#import <QTKit/QTTrack.h>
#import <QTKit/QTMedia.h>
#import <WebKit/WebKit.h>

NSString * const kPixelBufferTabViewItemIdentifier = @"PixelBufferTabViewIdentifier";
NSString * const kOpenGLBufferTabViewIdentifier = @"OpenGLBufferTabViewIdentifier";
NSString * const kNSViewTabViewIdentifier = @"NSViewTabViewIdentifier";
NSString * const kNSOpenGLViewTabViewIdentifier = @"NSOpenGLViewTabViewIdentifier";
NSString * const kQTMovieViewTabViewIdentifier = @"QTMovieViewTabViewIdentifier";
NSString * const kQCViewTabViewItemIdentifier = @"QCViewTabViewIdentifier";

@interface Controller (Private)
- (void) _activateTabViewItem: (NSTabViewItem *) item;
- (void) _deactivateTabViewItem: (NSTabViewItem *) item;
@end


#pragma mark -

@implementation Controller

#pragma mark -
#pragma mark App Lifecycle

- (void) awakeFromNib {
    // Populate _sourcePopUp with items in _sourceTabView.
    NSMenu *sourceMenu = [_sourcePopUp menu];
    [sourceMenu removeItemAtIndex:0];
    for (NSTabViewItem *tab in [_sourceTabView tabViewItems]) {
        NSMenuItem *item = [[NSMenuItem alloc] initWithTitle:[tab label]
                                                      action:NULL
                                               keyEquivalent:@""];
        [item setRepresentedObject:tab];
        [sourceMenu addItem:item];
        [item release];
    }

    // Start with the NSOpenGLView by default. Find its index in the tab view so we can pick it below.
    NSInteger startIndex = [_sourceTabView indexOfTabViewItemWithIdentifier: kNSOpenGLViewTabViewIdentifier];

    // Sync source popup and tab view.
    [_sourcePopUp selectItemAtIndex: startIndex];
    [self selectSource:_sourcePopUp];

    // Set initial state for items in Video menu.

    // Enable iChat Theater (register for its notifications)
    [self setEnableTheater: YES];

    // Disable iChat Theater controls
    [self setEnableTheaterControls: NO];

    // Don't use replacement mode
    [self setReplaceVideo: NO];

    // Set an initial URL on the web view so we'll have something to display.
    [_webView setMainFrameURL: @"http://www.apple.com"];
}

- (BOOL) applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)sender {
    // We're a single-window application.
    return YES;
}


- (NSUInteger) _numberOfAudioChannels {
    // single channel for the slideshow pause/unpause sounds
    if ([_slideshowView window] != nil)
        return 1;

    // look for an audio track in the QTMovieView, promise single-channel sound
    if ([_movieView window] != nil) {
        QTMovie *movie = [_movieView movie];
        NSArray *tracks = [movie tracks];
        for (QTTrack *track in tracks)
            if ([[track media] hasCharacteristic:QTMediaCharacteristicAudio])
                return 1;
    }

    // no audio found
    return 0;
}

- (void) _setOptimizationOptions {
    // The "stills" optimization option is specified in the nib via the tab identifier.
    IMVideoOptimizationOptions options = IMVideoOptimizationDefault;
    if ([[[_sourceTabView selectedTabViewItem] identifier] isEqualToString: kPixelBufferTabViewItemIdentifier]
        || [[[_sourceTabView selectedTabViewItem] identifier] isEqualToString: kNSViewTabViewIdentifier])
        options |= IMVideoOptimizationStills;

    // The "replacement" option is set by the menu item
    if (_replaceVideo)
        options |= IMVideoOptimizationReplacement;

    [[IMAVManager sharedAVManager] setVideoOptimizationOptions:options];
}

- (void) _stateChanged:(NSNotification *)aNotification {
    // Read the state.
    IMAVManager *avManager = [IMAVManager sharedAVManager];
    IMAVManagerState state = [avManager state];

    // When the state changes to IMAVRequested, tell iChat we're ready
    // to provide frames
    if (state == IMAVRequested) {
        [avManager start];
    }
    // when state moves to IMAVRunning, if we're looking at the slideshow or movie,
    // start playing the content.
    else if (state == IMAVRunning) {
        [self _activateTabViewItem: [_sourceTabView selectedTabViewItem]];
    }
}

#pragma mark -
#pragma mark Accessors

- (void) setEnableTheater: (BOOL) enable
{
    if (_enableTheater != enable) {
        _enableTheater = enable;

        if (_enableTheater) {
            // If we are turning on iChat Theater:

            // Subscribe to state-changed notifications, and sync initial state.
            [[IMService notificationCenter] addObserver:self
                                               selector:@selector(_stateChanged:)
                                                   name:IMAVManagerStateChangedNotification
                                                 object:nil];
            [self performSelector:@selector(_stateChanged:) withObject:nil];

        }
        else {
            // If we are turning off iChat Theater:

            // Stop the IMAVManager if it's already running.
            IMAVManager *avManager = [IMAVManager sharedAVManager];
            if ([avManager state] == IMAVRunning) {
                [avManager stop];
            }

            // Unsubscribe for notifications.
            [[IMService notificationCenter] removeObserver: self];
        }
    }
}

- (void) setEnableTheaterControls: (BOOL) enable
{
    if (_enableTheaterControls != enable) {
        _enableTheaterControls = enable;

        IMAVManager *manager = [IMAVManager sharedAVManager];
        IMAVControlBar *controlBar = [manager controlBar];

        if (_enableTheaterControls) {
            // If controls are enabled, add the relevant controls.
            IMAVButton *backwardButton = [IMAVButton forwardButton];
            [backwardButton setEnabled: YES];
            [backwardButton setTarget: self];
            [backwardButton setAction: @selector(selectPreviousSource:)];
            [controlBar addControl: backwardButton];

            IMAVButton *forwardButton = [IMAVButton backwardButton];
            [forwardButton setEnabled: YES];
            [forwardButton setTarget: self];
            [forwardButton setAction: @selector(selectNextSource:)];
            [controlBar addControl: forwardButton];
        }
        else {
            // If controls are disabled, just remove everything.
            [controlBar removeAllControls];
        } 
    }
}

- (void) setReplaceVideo: (BOOL) replace
{
    if (_replaceVideo != replace) {
        _replaceVideo = replace;
        [self _setOptimizationOptions];
    }
}

#pragma mark -
#pragma mark Actions

- (void) setMovie:(QTMovie *)aMovie {
    [_movieView setMovie:aMovie];

    // the audio may have changed
    IMAVManager *avManager = [IMAVManager sharedAVManager];
    [avManager setNumberOfAudioChannels:[self _numberOfAudioChannels]];

    [_movieView play:nil];
}

- (IBAction) selectSource:(id)sender {
    // Select the tab.
    NSTabViewItem *tab = [[sender selectedItem] representedObject];
    [_sourceTabView selectTabViewItem:tab];
}

// This method selects the next source in the tab view.
// If it reaches the end, it will look back to the beginning.
- (IBAction) selectNextSource: (id) sender
{
    NSInteger newIndex = [_sourcePopUp indexOfSelectedItem];
    newIndex = (newIndex + 1) % [[_sourcePopUp itemArray] count];
    [_sourcePopUp selectItemAtIndex: newIndex];
    [self selectSource:_sourcePopUp];
}

// This method selects the preview source in the tab view.
// If it reaches the end, it will look back to the end.
- (IBAction) selectPreviousSource: (id) sender
{
    NSInteger newIndex = [_sourcePopUp indexOfSelectedItem];
    newIndex = (newIndex - 1) % [[_sourcePopUp itemArray] count];
    [_sourcePopUp selectItemAtIndex: newIndex];
    [self selectSource:_sourcePopUp];
}

- (IBAction) toggleTheater: (id) sender
{
    [self setEnableTheater: !_enableTheater];
}

- (IBAction) toggleTheaterControls: (id) sender
{
    [self setEnableTheaterControls: !_enableTheaterControls];
}

- (IBAction) toggleReplaceVideo:(id)sender {
    [self setReplaceVideo: !_replaceVideo];
}

- (BOOL) validateMenuItem:(NSMenuItem *)item {
    SEL action = [item action];

    if (action == @selector(toggleTheater:)) {
        [item setState:(_enableTheater ? NSOnState : NSOffState)];
        return YES;
    } else if (action == @selector(toggleTheaterControls:)) {
        [item setState:(_enableTheaterControls ? NSOnState : NSOffState)];
        return YES;
    } else if (action == @selector(toggleReplaceVideo:)) {
        [item setState:(_replaceVideo ? NSOnState : NSOffState)];
        return YES;
    } else if (action == @selector(selectSource:)) {
        return YES;
    } else if (action == @selector(selectNextSource:)) {
        return YES;
    } else if (action == @selector(selectPreviousSource:)) {
        return YES;
    }

    return NO;
}

#pragma mark -
#pragma mark Tab View Management

- (void) _activateTabViewItem: (NSTabViewItem *) item
{
    if ([[item identifier] isEqualToString: kQTMovieViewTabViewIdentifier]) {
        // For the QTMovieView, start playing the movie.
        [_movieView performSelector: @selector(play:) withObject: self afterDelay: 0.0];
    }
    else if ([[item identifier] isEqualToString: kPixelBufferTabViewItemIdentifier]) {
        // For the pixel buffer SlideshowView, start the slideshow.
        [_slideshowView start];
    }
}

- (void) _deactivateTabViewItem: (NSTabViewItem *) item
{
    if ([[item identifier] isEqualToString: kQTMovieViewTabViewIdentifier]) {
        [_movieView pause:self];
    }
    else if ([[item identifier] isEqualToString: kPixelBufferTabViewItemIdentifier]) {
        [_slideshowView stop];
    }
}

- (void)tabView:(NSTabView *)tabView willSelectTabViewItem:(NSTabViewItem *)tabViewItem
{
    // In this delegate callback, we clean up the tab view that
    // is currently being displayed.
    [self _deactivateTabViewItem: [tabView selectedTabViewItem]];
}

- (void)tabView:(NSTabView *)tabView didSelectTabViewItem:(NSTabViewItem *)tabViewItem
{
    // In this delegate callback, we set up the tab view that is about to be displayed.

    IMAVManager *avManager = [IMAVManager sharedAVManager];

    // If the state is running and we're switching to a view with a slideshow or movie, start
    // playing.
    if ([avManager state] == IMAVRunning) [self _activateTabViewItem: tabViewItem];

    // re-configure the AV manager
    [self _setOptimizationOptions];

    [avManager setNumberOfAudioChannels:[self _numberOfAudioChannels]];

    // set the new video data source
    id newDataSource = nil;

    // for the NSView, we need to point directly to the view so we don't get the location bar.
    if ([[tabViewItem identifier] isEqualToString: kNSViewTabViewIdentifier]) {
        newDataSource = _webView;
    }
    // in all other cases, it's the first subview of the active NSTabViewItem.
    else {
        newDataSource = [[[tabViewItem view] subviews] objectAtIndex: 0];
    }

    // finally, we need to set the video data source.
    [avManager setVideoDataSource: newDataSource];
}

@end
```

[Next](DropQCView.h.md)[Previous](Controller.h.md)

