---
title: Hello Metronome
apple_id: TP40017587
resource_type: Sample Code
platform: watchOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-02-24'
source_url: https://developer.apple.com/library/archive/samplecode/HelloMetronome/Listings/iOSHelloMetronome_watchOSMetronome_Extension_ExtensionDelegate_m.html
archived_at: '2026-07-18T03:11:51.951233Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Hello Metronome](Hello%20Metronome.md)


[Next](iOSHelloMetronome-watchOSMetronome%20Extension-InterfaceController.h.md)[Previous](iOSHelloMetronome-watchOSMetronome%20Extension-Metronome.m.md)

# iOSHelloMetronome/watchOSMetronome Extension/ExtensionDelegate.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

*/

#import "ExtensionDelegate.h"

@implementation ExtensionDelegate

- (void)applicationDidFinishLaunching {
    // Perform any final initialization of your application.
    // Override point for customization after application launch.

    NSError *error = nil;

    NSLog(@"Hello, Metronome!\n");

    AVAudioSession *audioSession = [AVAudioSession sharedInstance];

    [audioSession setCategory:AVAudioSessionCategoryAmbient error:&error];
    if (error) {
        NSLog(@"AVAudioSession setCategory error %d, %@", error.code, error.localizedDescription);
    }

    [audioSession setActive:YES error:&error];
    if (error) {
        NSLog(@"AVAudioSession setActive error %d, %@", error.code, error.localizedDescription);
    }
}

- (void)applicationDidBecomeActive {
    // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.

    NSError *error = nil;

    [[AVAudioSession sharedInstance] setActive:YES error:&error];
    if (error) {
        NSLog(@"AVAudioSession setActive error %d, %@", error.code, error.localizedDescription);
    }
}

- (void)handleBackgroundTasks:(NSSet<WKRefreshBackgroundTask *> *)backgroundTasks {
    // Sent when the system needs to launch the application in the background to process tasks. Tasks arrive in a set, so loop through and process each one.
    for (WKRefreshBackgroundTask * task in backgroundTasks) {
        // Check the Class of each task to decide how to process it
        if ([task isKindOfClass:[WKApplicationRefreshBackgroundTask class]]) {
            // Be sure to complete the background task once you’re done.
            WKApplicationRefreshBackgroundTask *backgroundTask = (WKApplicationRefreshBackgroundTask*)task;
            [backgroundTask setTaskCompleted];
        } else if ([task isKindOfClass:[WKSnapshotRefreshBackgroundTask class]]) {
            // Snapshot tasks have a unique completion call, make sure to set your expiration date
            WKSnapshotRefreshBackgroundTask *snapshotTask = (WKSnapshotRefreshBackgroundTask*)task;
            [snapshotTask setTaskCompletedWithDefaultStateRestored:YES estimatedSnapshotExpiration:[NSDate distantFuture] userInfo:nil];
        } else if ([task isKindOfClass:[WKWatchConnectivityRefreshBackgroundTask class]]) {
            // Be sure to complete the background task once you’re done.
            WKWatchConnectivityRefreshBackgroundTask *backgroundTask = (WKWatchConnectivityRefreshBackgroundTask*)task;
            [backgroundTask setTaskCompleted];
        } else if ([task isKindOfClass:[WKURLSessionRefreshBackgroundTask class]]) {
            // Be sure to complete the background task once you’re done.
            WKURLSessionRefreshBackgroundTask *backgroundTask = (WKURLSessionRefreshBackgroundTask*)task;
            [backgroundTask setTaskCompleted];
        } else {
            // make sure to complete unhandled task types
            [task setTaskCompleted];
        }
    }
}

@end
```

[Next](iOSHelloMetronome-watchOSMetronome%20Extension-InterfaceController.h.md)[Previous](iOSHelloMetronome-watchOSMetronome%20Extension-Metronome.m.md)

