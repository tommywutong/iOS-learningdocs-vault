---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__iOS__CloudPhotos_PhotoTableCell_m.html
archived_at: '2026-07-18T03:03:33.596297Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28iOS%29-CloudPhotos-APLMainTableViewController.m.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-AppDelegate.m.md)

# CloudPhotos (iOS)/CloudPhotos/PhotoTableCell.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom UITableViewCell for displaying photo information in the main table view.
 */

#import "PhotoTableCell.h"
#import "APLCloudManager.h"
#import "AppDelegate.h"
#import "CloudPhoto.h"

@interface PhotoTableCell ()

@property (nonatomic, weak) IBOutlet UILabel *nameLabel;
@property (nonatomic, weak) IBOutlet UILabel *ownerLabel;
@property (nonatomic, weak) IBOutlet UIImageView *photoImage;
@property (nonatomic, weak) IBOutlet UIActivityIndicatorView *activityIndicator;

@end


#pragma mark -

@implementation PhotoTableCell

- (void)layoutSubviews
{
    [super layoutSubviews];

    if (self.photo != nil)
    {
        self.nameLabel.text = [self.photo getPhotoTitle];

        // find the CKAsset (pointing to the actual photo)
        self.photoImage.image = [self.photo getPhotoImage];

        // we provide the owner of the current photo in the subtite of our cell,
        // this could take a while, so provide activity indicator
        //
        self.ownerLabel.hidden = YES;
        self.activityIndicator.hidden = NO;
        [self.activityIndicator startAnimating];

        [self.photo photoOwner:^(NSString *owner) {

            self.activityIndicator.hidden = YES;
            [self.activityIndicator stopAnimating];

            self.ownerLabel.hidden = NO;
            self.ownerLabel.text = owner;
        }];
    }
}

@end
```

[Next](CloudPhotos%20%28iOS%29-CloudPhotos-APLMainTableViewController.m.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-AppDelegate.m.md)

