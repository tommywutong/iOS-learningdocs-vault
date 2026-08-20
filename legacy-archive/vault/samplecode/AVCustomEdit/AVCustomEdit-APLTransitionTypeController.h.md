---
title: AVCustomEdit
apple_id: DTS40013411
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVCustomEdit/Listings/AVCustomEdit_APLTransitionTypeController_h.html
archived_at: '2026-07-18T03:00:10.774410Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCustomEdit](AVCustomEdit.md)


[Next](AVCustomEdit-APLCrossDissolveRenderer.h.md)[Previous](AVCustomEdit-APLAppDelegate.h.md)

# AVCustomEdit/APLTransitionTypeController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 UITableViewController subclass which lets the user select the type of transition for their composition.
 */

#import <UIKit/UIKit.h>

#define kDiagonalWipeTransition  0 
#define kCrossDissolveTransition 1

@protocol APLTransitionTypePickerDelegate;

@interface APLTransitionTypeController : UITableViewController

@property IBOutlet UITableViewCell *diagonalWipeCell;
@property IBOutlet UITableViewCell *crossDissolveCell;

@property NSInteger currentTransition;

@property id <APLTransitionTypePickerDelegate> delegate;

- (IBAction)transitionSelected:(id)sender;

@end

@protocol APLTransitionTypePickerDelegate <NSObject>

- (void)transitionTypeController:(APLTransitionTypeController *)controller didPickTransitionType:(int)transitionType;

@end
```

[Next](AVCustomEdit-APLCrossDissolveRenderer.h.md)[Previous](AVCustomEdit-APLAppDelegate.h.md)

