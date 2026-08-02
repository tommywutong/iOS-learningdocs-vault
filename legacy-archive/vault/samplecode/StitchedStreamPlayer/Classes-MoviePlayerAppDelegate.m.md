---
title: StitchedStreamPlayer
apple_id: DTS40010092
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-07-14'
source_url: https://developer.apple.com/library/archive/samplecode/StitchedStreamPlayer/Listings/Classes_MoviePlayerAppDelegate_m.html
archived_at: '2026-07-18T03:25:45.578647Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [StitchedStreamPlayer](StitchedStreamPlayer.md)


[Next](Classes-MyStreamingMovieViewController.m.md)[Previous](Classes-MyPlayerLayerView.m.md)

# Classes/MoviePlayerAppDelegate.m

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
A simple UIApplication delegate class that adds the StreamingViewController
view to the window as a subview.
*/

#import "MoviePlayerAppDelegate.h"

@class MyStreamingMovieViewController;

@implementation MoviePlayerAppDelegate

@synthesize window;
@synthesize streamingViewController;

- (void)applicationDidFinishLaunching:(UIApplication *)application 
{   
    // Specify the streaming view controller as the root view controller of the window
    window.rootViewController = streamingViewController;

    [window makeKeyAndVisible];
}

- (void)dealloc 
{
    [window release];
    [streamingViewController release];

    [super dealloc];
}

@end
```

[Next](Classes-MyStreamingMovieViewController.m.md)[Previous](Classes-MyPlayerLayerView.m.md)

