---
title: 'DateSectionTitles: Custom Table Sections with NSFetchedResultsController'
apple_id: DTS40009939
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/DateSectionTitles/Listings/DateSectionTitles_APLMasterViewController_h.html
archived_at: '2026-07-18T03:06:05.727776Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DateSectionTitles: Custom Table Sections with NSFetchedResultsController](DateSectionTitles-%20Custom%20Table%20Sections%20with%20NSFetchedResultsController.md)


[Next](ReadMe.md.md)[Previous](DateSectionTitles-APLEvent.m.md)

# DateSectionTitles/APLMasterViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Table view controller to display Events by section.
 */

@import UIKit;
@import CoreData;

@interface APLMasterViewController : UITableViewController <NSFetchedResultsControllerDelegate>

@property (strong, nonatomic) NSManagedObjectContext *managedObjectContext;

@end
```

[Next](ReadMe.md.md)[Previous](DateSectionTitles-APLEvent.m.md)

