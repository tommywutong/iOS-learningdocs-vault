---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_iOS_AAPLGameViewController_m.html
archived_at: '2026-07-26T19:54:17.104190Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20iOS-AAPLButtonOverlay.h.md)[Previous](Objective-C-fox2%20iOS-AAPLPadOverlay.h.md)

# Objective-C/fox2 iOS/AAPLGameViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The app's main view controller.
 */

#import <SceneKit/SceneKit.h>
#import "AAPLGameViewController.h"
#import "AAPLGameController.h"

@interface AAPLGameViewController ()

@property (readonly) SCNView *gameView;
@property (strong, nonatomic) AAPLGameController *gameController;

@end

@implementation AAPLGameViewController

- (SCNView *)gameView {
    return (SCNView *)self.view;
}

- (void)viewDidLoad {
    [super viewDidLoad];

    // 1.3x on iPads
    if ([[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPad) {
        self.gameView.contentScaleFactor = MIN(1.3, self.gameView.contentScaleFactor);
        self.gameView.preferredFramesPerSecond = 60.0;
    }

    self.gameController = [[AAPLGameController alloc] initWithSCNView:self.gameView];

    // Configure the view
    self.gameView.backgroundColor = [UIColor blackColor];
}

- (BOOL)shouldAutorotate {
    return YES;
}

- (UIInterfaceOrientationMask)supportedInterfaceOrientations {
    if ([[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPhone) {
        return UIInterfaceOrientationMaskAllButUpsideDown;
    } else {
        return UIInterfaceOrientationMaskAll;
    }
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
}

- (BOOL)prefersStatusBarHidden {
    return YES;
}

@end
```

[Next](Objective-C-fox2%20iOS-AAPLButtonOverlay.h.md)[Previous](Objective-C-fox2%20iOS-AAPLPadOverlay.h.md)

