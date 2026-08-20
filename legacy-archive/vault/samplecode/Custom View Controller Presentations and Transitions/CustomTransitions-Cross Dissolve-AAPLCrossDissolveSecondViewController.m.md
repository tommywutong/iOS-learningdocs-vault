---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_Cross_Dissolve_AAPLCrossDissolveSecondViewController_m.html
archived_at: '2026-07-18T03:05:41.842182Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-AAPLExternalStoryboardSegue.h.md)[Previous](CustomTransitions-Cross%20Dissolve-AAPLCrossDissolveFirstViewController.m.md)

# CustomTransitions/Cross Dissolve/AAPLCrossDissolveSecondViewController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The presented view controller for the Cross Dissolve demo.
 */

#import "AAPLCrossDissolveSecondViewController.h"

@implementation AAPLCrossDissolveSecondViewController

//| ----------------------------------------------------------------------------
- (IBAction)dismissAction:(id)sender
{
    // For the sake of example, this demo implements the presentation and
    // dismissal logic completely in code.  Take a look at the later demos
    // to learn how to integrate custom transitions with segues.
    [self dismissViewControllerAnimated:YES completion:NULL];
}

@end
```

[Next](CustomTransitions-AAPLExternalStoryboardSegue.h.md)[Previous](CustomTransitions-Cross%20Dissolve-AAPLCrossDissolveFirstViewController.m.md)

