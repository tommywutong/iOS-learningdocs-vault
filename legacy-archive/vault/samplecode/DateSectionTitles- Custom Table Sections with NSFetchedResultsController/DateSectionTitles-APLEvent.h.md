---
title: 'DateSectionTitles: Custom Table Sections with NSFetchedResultsController'
apple_id: DTS40009939
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/DateSectionTitles/Listings/DateSectionTitles_APLEvent_h.html
archived_at: '2026-07-18T03:06:05.611066Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DateSectionTitles: Custom Table Sections with NSFetchedResultsController](DateSectionTitles-%20Custom%20Table%20Sections%20with%20NSFetchedResultsController.md)


[Next](DateSectionTitles-APLMasterViewController.m.md)[Previous](DateSectionTitles-APLAppDelegate.h.md)

# DateSectionTitles/APLEvent.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom class for the Event entity.
  The timeStamp and title are persistent attributes; the sectionIdentifier is transient and derived from timeStamp.
  * timeStamp is the date on which the event occurred.
  * title is displayed in the table view rows.
  When the default data is created in the application delegate, the title is initialized to a string representation of the date.
  * sectionIdentifier is used to divide the events into sections in the table view.
  sectionIdentifier is a string value representing the number ((year * 1000) + month). Using this value, events can be correctly ordered and grouped regardless of the actual name of the month. It is calculated and cached on demand in the custom accessor method.
 */

@import CoreData;

@interface APLEvent : NSManagedObject

@property (nonatomic) NSString *title;
@property (nonatomic) NSDate *timeStamp;
@property (nonatomic) NSString *sectionIdentifier;

@end
```

[Next](DateSectionTitles-APLMasterViewController.m.md)[Previous](DateSectionTitles-APLAppDelegate.h.md)

