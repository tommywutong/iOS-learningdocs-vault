---
title: 'LaunchMe: Using a custom URL scheme to interact with your application'
apple_id: DTS40007417
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/LaunchMe/Listings/LaunchMe_Classes_ResultsViewController_m.html
archived_at: '2026-07-18T03:13:27.626776Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LaunchMe: Using a custom URL scheme to interact with your application](LaunchMe-%20Using%20a%20custom%20URL%20scheme%20to%20interact%20with%20your%20application.md)


[Next](LaunchMe-Classes-ResultsViewController.h.md)[Previous](LaunchMe-Classes-LaunchMeAppDelegate.h.md)

# LaunchMe/Classes/ResultsViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The view controller used to show the results of openURL.
 */

#import "ResultsViewController.h"

@interface ResultsViewController ()

@property (nonatomic, weak) IBOutlet UITextField *resultsTextField;

@end


#pragma mark -

@implementation ResultsViewController

// -------------------------------------------------------------------------------
//  viewDidLoad
// -------------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];

    // Set the background color and text field to the values that were determined when first loaded as a result of openURL.
    self.view.backgroundColor = self.selectedColor;
    self.resultsTextField.text = self.selectedString;
}

@end
```

[Next](LaunchMe-Classes-ResultsViewController.h.md)[Previous](LaunchMe-Classes-LaunchMeAppDelegate.h.md)

