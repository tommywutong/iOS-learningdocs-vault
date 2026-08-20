---
title: 'LaunchMe: Using a custom URL scheme to interact with your application'
apple_id: DTS40007417
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/LaunchMe/Listings/LaunchMe_Classes_ResultsViewController_h.html
archived_at: '2026-07-18T03:13:27.583081Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LaunchMe: Using a custom URL scheme to interact with your application](LaunchMe-%20Using%20a%20custom%20URL%20scheme%20to%20interact%20with%20your%20application.md)


[Next](LaunchMe-Classes-LaunchMeAppDelegate.m.md)[Previous](LaunchMe-Classes-ResultsViewController.m.md)

# LaunchMe/Classes/ResultsViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The view controller used to show the results of openURL.
 */

@import UIKit;

@interface ResultsViewController : UIViewController

// The displayed UIColor.  If the app was launched with a valid URL,
// this will be set by the AppDelegate to the decoded color.
@property (nonatomic, strong) UIColor *selectedColor;

// The displayed NSString.  If the app was launched with a valid URL,
// this will be set by the AppDelegate to the decoded string.
@property (nonatomic, strong) NSString *selectedString;

@end
```

[Next](LaunchMe-Classes-LaunchMeAppDelegate.m.md)[Previous](LaunchMe-Classes-ResultsViewController.m.md)

