---
title: AVCustomEdit
apple_id: DTS40013411
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVCustomEdit/Listings/AVCustomEdit_APLTransitionTypeController_m.html
archived_at: '2026-07-18T03:00:10.819353Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCustomEdit](AVCustomEdit.md)


[Next](AVCustomEdit-APLOpenGLRenderer.h.md)[Previous](AVCustomEdit-APLCustomVideoCompositor.m.md)

# AVCustomEdit/APLTransitionTypeController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 UITableViewController subclass which lets the user select the type of transition for their composition.
 */

#import "APLTransitionTypeController.h"

@implementation APLTransitionTypeController

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    UITableViewCell *selectedCell = [tableView cellForRowAtIndexPath:indexPath];
    [selectedCell setAccessoryType:UITableViewCellAccessoryCheckmark];

    switch ([selectedCell tag]) {
        case kDiagonalWipeTransition:{
            [self.crossDissolveCell setAccessoryType:UITableViewCellAccessoryNone];
            [self.delegate transitionTypeController:self didPickTransitionType:kDiagonalWipeTransition];
            self.currentTransition = kDiagonalWipeTransition;
            break;
        }
        case kCrossDissolveTransition:{
            [self.diagonalWipeCell setAccessoryType:UITableViewCellAccessoryNone];
            [self.delegate transitionTypeController:self didPickTransitionType:kCrossDissolveTransition];
            self.currentTransition = kCrossDissolveTransition;
            break;
        }
        default:
            break;
    }

    [tableView deselectRowAtIndexPath:indexPath animated:YES];
}

- (IBAction)transitionSelected:(id)sender
{
    [self.delegate transitionTypeController:self didPickTransitionType:(int)self.currentTransition];
}

@end
```

[Next](AVCustomEdit-APLOpenGLRenderer.h.md)[Previous](AVCustomEdit-APLCustomVideoCompositor.m.md)

