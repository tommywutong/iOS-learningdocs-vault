---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_AAPLAppDelegate_m.html
archived_at: '2026-07-18T03:23:13.654834Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-AAPLAppDelegate.h.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLSlideTextManager.m.md)

# Scene Kit Session WWDC 2014/AAPLAppDelegate.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This is the main controller for the application. It instantiates and runs a presentation.
 */

#import "AAPLAppDelegate.h"
#import <IOKit/pwr_mgt/IOPMLib.h>

@implementation AAPLAppDelegate {
    AAPLPresentationViewController *_presentationViewController;
    IOPMAssertionID _assertionID;
}

- (void)applicationWillFinishLaunching:(NSNotification *)notification {
    [self disableDisplaySleeping];

    // Create a presentation from a plist file
    _presentationViewController = [[AAPLPresentationViewController alloc] initWithContentsOfFile:@"Scene Kit Presentation"];
    _presentationViewController.delegate = self;

    // Populate the 'Go' menu for direct access to slides
    [self populateGoMenu];

    // Start the presentation
    [self.window.contentView addSubview:_presentationViewController.presentationView];
    _presentationViewController.presentationView.frame = [self.window.contentView bounds];
    _presentationViewController.presentationView.autoresizingMask = NSViewWidthSizable | NSViewHeightSizable;
}

- (void) applicationDidFinishLaunching:(NSNotification *)notification
{
    [_presentationViewController applicationDidFinishLaunching];
}

- (void)applicationWillTerminate:(NSNotification *)notification {
    //restore default display settings
    [self enableDisplaySleeping];
}

#pragma mark - Presentation delegate

- (void)presentationViewController:(AAPLPresentationViewController *)presentationViewController willPresentSlideAtIndex:(NSUInteger)slideIndex step:(NSUInteger)step {
    // Update the window's title depending on the current slide
    if (step == 0) {
        self.window.title = [NSString stringWithFormat:@"SceneKit slide %ld", slideIndex];
    } else {
        self.window.title = [NSString stringWithFormat:@"SceneKit slide %ld step %ld", slideIndex, step];
    }
}

#pragma mark - 'Go' menu

- (void)populateGoMenu {
    for (NSUInteger i = 0; i < _presentationViewController.numberOfSlides; i++) {
        NSString *slideName = NSStringFromClass([_presentationViewController classOfSlideAtIndex:i]);
        NSRange prefixRange = NSMakeRange(0, @"AAPLSlide".length);
        NSString *title = [slideName stringByReplacingCharactersInRange:prefixRange withString:[NSString stringWithFormat:@"%lu ", (unsigned long)i]];
        NSMenuItem *item = [[NSMenuItem alloc] initWithTitle:title action:@selector(goTo:) keyEquivalent:@""];
        item.representedObject = @(i);
        [_goMenu addItem:item];
    }
}

#pragma mark - Actions

- (IBAction)nextSlide:(id)sender {
    [_presentationViewController goToNextSlideStep];
}

- (IBAction)previousSlide:(id)sender {
    [_presentationViewController goToPreviousSlide];
}

- (IBAction)goTo:(NSMenuItem *)sender {
    NSInteger index = [sender.representedObject integerValue];
    [_presentationViewController goToSlideAtIndex:index];
}

- (IBAction)exportSlidesToImages:(NSMenuItem *)sender {
    [_presentationViewController exportSlidesToImages:sender];
}

- (IBAction)exportSlidesToSCN:(NSMenuItem *)sender {
    [_presentationViewController exportSlidesToSCN:sender];
}

- (IBAction) autoPlay:(id) sender{
    [_presentationViewController autoPlay:sender];
}

- (IBAction)toggleCursor:(id)sender {
    static BOOL hidden = NO;
    if (hidden) {
        [NSCursor unhide];
        hidden = NO;
    } else {
        [NSCursor hide];
        hidden = YES;
    }
}

#pragma mark - NSApplicationDelegate

- (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)sender {
    return YES;
}

#pragma mark - Sleep

- (void)disableDisplaySleeping {
    CFStringRef reasonForActivity = CFSTR("Scene Kit Presentation");
    IOPMAssertionCreateWithName(kIOPMAssertionTypeNoDisplaySleep, kIOPMAssertionLevelOn, reasonForActivity, &_assertionID);
}

- (void)enableDisplaySleeping {
    if (_assertionID)
        IOPMAssertionRelease(_assertionID);
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-AAPLAppDelegate.h.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLSlideTextManager.m.md)

