---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_AAPLMenuViewController_m.html
archived_at: '2026-07-18T03:05:41.176525Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-AAPLMenuViewController.h.md)[Previous](CustomTransitions-AAPLAppDelegate.h.md)

# CustomTransitions/AAPLMenuViewController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Displays the list of examples.
 */

#import "AAPLMenuViewController.h"

@implementation AAPLMenuViewController

//| ----------------------------------------------------------------------------
- (BOOL)shouldPerformSegueWithIdentifier:(NSString *)identifier sender:(id)sender
{
    // Certain examples are only supported on iOS 8 and later.
    if ([UIDevice currentDevice].systemVersion.floatValue < 8.f)
    {
        NSArray *iOS7Examples = @[@"CrossDissolve", @"Dynamics", @"Swipe", @"Checkerboard", @"Slide"];

        if ([iOS7Examples containsObject:identifier] == NO) {
            [self.tableView deselectRowAtIndexPath:self.tableView.indexPathForSelectedRow animated:YES];

            UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Can not load example." message:@"This example requires iOS 8 or later." delegate:nil cancelButtonTitle:@"OK" otherButtonTitles:nil];
            [alert show];

            return NO;
        }
    }

    return YES;
}


//| ----------------------------------------------------------------------------
- (IBAction)unwindToMenuViewController:(UIStoryboardSegue*)sender
{ }

@end
```

[Next](CustomTransitions-AAPLMenuViewController.h.md)[Previous](CustomTransitions-AAPLAppDelegate.h.md)

