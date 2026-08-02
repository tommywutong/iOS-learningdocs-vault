---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_AAPLExternalStoryboardSegue_m.html
archived_at: '2026-07-18T03:05:41.098647Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-Slide-AAPLSlideTransitionDelegate.m.md)[Previous](CustomTransitions-Swipe-AAPLSwipeTransitionDelegate.m.md)

# CustomTransitions/AAPLExternalStoryboardSegue.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A custom storyboard segue that loads its destination view controller from an
  external storyboard (named by the segue's identifier), then presents it 
  modally.
 */

#import "AAPLExternalStoryboardSegue.h"

//  NOTE: iOS 9 introduces storyboard references which allow a segue to
//        target the initial scene in an external storyboard.  If your
//        application targets iOS 9 and above, you should use storyboard
//        references rather than the technique shown here.

@implementation AAPLExternalStoryboardSegue

//| ----------------------------------------------------------------------------
- (instancetype)initWithIdentifier:(NSString *)identifier source:(UIViewController *)source destination:(UIViewController *)destination
{
    // Load the storyboard named by this segue's identifier.
    UIStoryboard *externalStoryboard = [UIStoryboard storyboardWithName:identifier bundle:[NSBundle bundleForClass:self.class]];

    // Instantiate the storyboard's initial view controller.
    id initialViewController = [externalStoryboard instantiateInitialViewController];

    return [super initWithIdentifier:identifier source:source destination:initialViewController];
}


//| ----------------------------------------------------------------------------
- (void)perform
{
    [self.sourceViewController presentViewController:self.destinationViewController animated:YES completion:NULL];
}

@end
```

[Next](CustomTransitions-Slide-AAPLSlideTransitionDelegate.m.md)[Previous](CustomTransitions-Swipe-AAPLSwipeTransitionDelegate.m.md)

