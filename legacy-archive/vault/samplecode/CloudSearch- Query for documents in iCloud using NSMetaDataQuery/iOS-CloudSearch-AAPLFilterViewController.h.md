---
title: 'CloudSearch: Query for documents in iCloud using NSMetaDataQuery'
apple_id: DTS40013494
resource_type: Sample Code
platform: iOS|macOS
topic: Data Management
technology: ApplicationServices
published: '2016-03-24'
source_url: https://developer.apple.com/library/archive/samplecode/CloudSearch/Listings/iOS_CloudSearch_AAPLFilterViewController_h.html
archived_at: '2026-07-18T03:03:35.401280Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudSearch: Query for documents in iCloud using NSMetaDataQuery](CloudSearch-%20Query%20for%20documents%20in%20iCloud%20using%20NSMetaDataQuery.md)


[Next](iOS-CloudSearch-AAPLFilterViewController.m.md)[Previous](iOS-CloudSearch-AAPLAppDelegate.h.md)

# iOS/CloudSearch/AAPLFilterViewController.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Table view for choosing the file extension to filter.
 */

@import UIKit;

@protocol AAPLFilterViewControllerDelegate;

@interface AAPLFilterViewController : UITableViewController

@property (nonatomic, weak, readwrite) id<AAPLFilterViewControllerDelegate> filterDelegate;
@property (nonatomic, strong) NSIndexPath *extensionToFilter;

@end


#pragma mark -

// protocol used to inform our parent table view controller to update its table if the given record has changed
@protocol AAPLFilterViewControllerDelegate <NSObject>

@required
- (void)filterViewController:(AAPLFilterViewController *)viewController didSelectExtension:(NSIndexPath *)extension;

@end
```

[Next](iOS-CloudSearch-AAPLFilterViewController.m.md)[Previous](iOS-CloudSearch-AAPLAppDelegate.h.md)

