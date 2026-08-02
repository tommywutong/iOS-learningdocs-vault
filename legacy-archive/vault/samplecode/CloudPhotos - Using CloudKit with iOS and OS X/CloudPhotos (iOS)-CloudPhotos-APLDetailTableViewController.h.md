---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__iOS__CloudPhotos_APLDetailTableViewController_h.html
archived_at: '2026-07-18T03:03:32.543409Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28iOS%29-CloudPhotos-APLDetailTableViewController.m.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-AppDelegate.h.md)

# CloudPhotos (iOS)/CloudPhotos/APLDetailTableViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The detail view controller showing a specific photo.
 */

@import UIKit;
@import CloudKit;

@class CloudPhoto;

@protocol DetailViewControllerDelegate;

@interface APLDetailTableViewController : UITableViewController

@property (nonatomic, weak, readwrite) id<DetailViewControllerDelegate> delegate;

@property (nonatomic, strong) CloudPhoto *photo;

// called when we receive notification from our App Delegate that the user logged in our out
- (void)loginUpdate;

@end


#pragma mark -

// protocol used to inform our parent table view controller to update its table if the given photo was added, changed or deleted
@protocol DetailViewControllerDelegate <NSObject>

@required

- (void)detailViewController:(APLDetailTableViewController *)viewController didChangeCloudPhoto:(CloudPhoto *)photo;
- (void)detailViewController:(APLDetailTableViewController *)viewController didAddCloudPhoto:(CloudPhoto *)photo;
- (void)detailViewController:(APLDetailTableViewController *)viewController didDeleteCloudPhoto:(CloudPhoto *)photo;

@end
```

[Next](CloudPhotos%20%28iOS%29-CloudPhotos-APLDetailTableViewController.m.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-AppDelegate.h.md)

