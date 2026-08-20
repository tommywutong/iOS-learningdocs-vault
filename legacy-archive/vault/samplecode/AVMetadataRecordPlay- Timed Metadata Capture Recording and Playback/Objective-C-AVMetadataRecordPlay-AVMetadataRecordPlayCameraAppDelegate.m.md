---
title: 'AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback'
apple_id: TP40016165
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/AVMetadataRecordPlay/Listings/Objective_C_AVMetadataRecordPlay_AVMetadataRecordPlayCameraAppDelegate_m.html
archived_at: '2026-07-18T03:00:19.792368Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback](AVMetadataRecordPlay-%20Timed%20Metadata%20Capture%20Recording%20and%20Playback.md)


[Next](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayAssetGridViewController.m.md)[Previous](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlay%2BUICollectionView%2BConvenien.md)

# Objective-C/AVMetadataRecordPlay/AVMetadataRecordPlayCameraAppDelegate.m

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Application delegate.
*/

#import "AVMetadataRecordPlayCameraAppDelegate.h"

@implementation AVMetadataRecordPlayCameraAppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    // We use the device orientation to set the video orientation of the video preview,
    // and to set the orientation of still images and recorded videos.

    // Inform the device that we want to use the device orientation.
    [[UIDevice currentDevice] beginGeneratingDeviceOrientationNotifications];
    return YES;
}

- (void)applicationWillTerminate:(UIApplication *)application
{
    // Inform the device that we no longer require access the device orientation.
    [[UIDevice currentDevice] endGeneratingDeviceOrientationNotifications];
}

- (void)applicationWillEnterForeground:(UIApplication *)application
{
    // Inform the device that we want to use the device orientation again.
    [[UIDevice currentDevice] beginGeneratingDeviceOrientationNotifications];
}

- (void)applicationDidEnterBackground:(UIApplication *)application
{
    // Let the device power down the accelerometer if not used elsewhere while backgrounded.
    [[UIDevice currentDevice] endGeneratingDeviceOrientationNotifications];
}

@end
```

[Next](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayAssetGridViewController.m.md)[Previous](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlay%2BUICollectionView%2BConvenien.md)

