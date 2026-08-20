---
title: 'Tabster: Various techniques in using UITabBarController'
apple_id: DTS40011213
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-02-15'
source_url: https://developer.apple.com/library/archive/samplecode/Tabster/Listings/Tabster_Classes_LandscapeViewController_m.html
archived_at: '2026-07-18T03:26:20.097614Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabster: Various techniques in using UITabBarController](Tabster-%20Various%20techniques%20in%20using%20UITabBarController.md)


[Next](Tabster-Classes-AppDelegate.m.md)[Previous](Tabster-Classes-FourViewController.h.md)

# Tabster/Classes/LandscapeViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  The application view controller used when the device is in landscape orientation. 
 */

#import "LandscapeViewController.h"

@interface LandscapeViewController ()

@property (strong, nonatomic) IBOutlet UIImageView *imageView;

- (IBAction)actionCompleted:(id)sender;

@end

#pragma mark -

@implementation LandscapeViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
}

- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];
    self.imageView.image = self.image;
}

- (IBAction)actionCompleted:(id)sender
{
    [self dismissViewControllerAnimated:NO completion:nil];
}

- (UIInterfaceOrientationMask)supportedInterfaceOrientations
{
    return UIInterfaceOrientationMaskLandscape;
}

- (BOOL)shouldAutorotate
{
    return YES;
}

@end
```

[Next](Tabster-Classes-AppDelegate.m.md)[Previous](Tabster-Classes-FourViewController.h.md)

