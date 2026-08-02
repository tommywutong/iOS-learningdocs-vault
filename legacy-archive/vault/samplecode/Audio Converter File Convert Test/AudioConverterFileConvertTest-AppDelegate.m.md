---
title: Audio Converter File Convert Test
apple_id: DTS40010581
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-09-29'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneACFileConvertTest/Listings/AudioConverterFileConvertTest_AppDelegate_m.html
archived_at: '2026-07-18T03:29:37.378133Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Converter File Convert Test](Audio%20Converter%20File%20Convert%20Test.md)


[Next](AudioConverterFileConvertTest-ViewController.m.md)[Previous](AudioConverterFileConvertTest-ViewController.h.md)

# AudioConverterFileConvertTest/AppDelegate.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The application delegate.
 */

#import "AppDelegate.h"
@import AVFoundation;

@interface AppDelegate ()

@end

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    NSError *error = nil;

    // Configure the audio session
    AVAudioSession *sessionInstance = [AVAudioSession sharedInstance];

    // our default category -- we change this for conversion and playback appropriately
    [sessionInstance setCategory:AVAudioSessionCategoryPlayback error:&error];

    // we don't do anything special in the route change notification
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(handleAudioSessionRouteChangeNotification:)
                                                 name:AVAudioSessionRouteChangeNotification
                                               object:sessionInstance];

    // the session must be active for offline conversion
    [sessionInstance setActive:YES error:&error];

    return YES;
}

// MARK: Notification Handler.

- (void)handleAudioSessionRouteChangeNotification:(NSNotification *)notification {
    AVAudioSessionRouteChangeReason reasonValue = [[notification.userInfo valueForKey:AVAudioSessionRouteChangeReasonKey] unsignedIntegerValue];

    AVAudioSessionRouteDescription *routeDescription = [notification.userInfo valueForKey:AVAudioSessionRouteChangePreviousRouteKey];

    NSLog(@"Route change:");
    switch (reasonValue) {
        case AVAudioSessionRouteChangeReasonNewDeviceAvailable:
            NSLog(@"     NewDeviceAvailable");
            break;
        case AVAudioSessionRouteChangeReasonOldDeviceUnavailable:
            NSLog(@"     OldDeviceUnavailable");
            break;
        case AVAudioSessionRouteChangeReasonCategoryChange:
            NSLog(@"     CategoryChange");
            NSLog(@" New Category: %@", [[AVAudioSession sharedInstance] category]);
            break;
        case AVAudioSessionRouteChangeReasonOverride:
            NSLog(@"     Override");
            break;
        case AVAudioSessionRouteChangeReasonWakeFromSleep:
            NSLog(@"     WakeFromSleep");
            break;
        case AVAudioSessionRouteChangeReasonNoSuitableRouteForCategory:
            NSLog(@"     NoSuitableRouteForCategory");
            break;
        default:
            NSLog(@"     ReasonUnknown");
    }

    NSLog(@"Previous route:\n");
    NSLog(@"%@", routeDescription);
}

@end
```

[Next](AudioConverterFileConvertTest-ViewController.m.md)[Previous](AudioConverterFileConvertTest-ViewController.h.md)

