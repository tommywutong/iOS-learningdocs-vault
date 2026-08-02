---
title: Hello Metronome
apple_id: TP40017587
resource_type: Sample Code
platform: watchOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-02-24'
source_url: https://developer.apple.com/library/archive/samplecode/HelloMetronome/Listings/iOSHelloMetronome_ViewController_h.html
archived_at: '2026-07-18T03:11:51.675041Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Hello Metronome](Hello%20Metronome.md)


[Next](iOSHelloMetronome-main.m.md)[Previous](iOSHelloMetronome-iOSHelloMetronome-Bridging-Header.h.md)

# iOSHelloMetronome/ViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

*/

@import UIKit;
@import AVFoundation;

#import "iOSHelloMetronome-Swift.h"

@interface ViewController : UIViewController <MetronomeDelegate> {
    Metronome *metronome;
}

@end
```

[Next](iOSHelloMetronome-main.m.md)[Previous](iOSHelloMetronome-iOSHelloMetronome-Bridging-Header.h.md)

