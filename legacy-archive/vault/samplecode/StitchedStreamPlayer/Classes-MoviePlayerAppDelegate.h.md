---
title: StitchedStreamPlayer
apple_id: DTS40010092
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-07-14'
source_url: https://developer.apple.com/library/archive/samplecode/StitchedStreamPlayer/Listings/Classes_MoviePlayerAppDelegate_h.html
archived_at: '2026-07-18T03:25:45.542912Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [StitchedStreamPlayer](StitchedStreamPlayer.md)


[Next](ReadMe.md.md)[Previous](Classes-MyStreamingMovieViewController.m.md)

# Classes/MoviePlayerAppDelegate.h

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
A simple UIApplication delegate class that adds the StreamingViewController
view to the window as a subview.
*/

@import UIKit;
#import "MyStreamingMovieViewController.h"

@interface MoviePlayerAppDelegate : NSObject <UIApplicationDelegate, UITabBarControllerDelegate> {
    UIWindow *window;
    MyStreamingMovieViewController *streamingViewController;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet MyStreamingMovieViewController *streamingViewController;

@end
```

[Next](ReadMe.md.md)[Previous](Classes-MyStreamingMovieViewController.m.md)

