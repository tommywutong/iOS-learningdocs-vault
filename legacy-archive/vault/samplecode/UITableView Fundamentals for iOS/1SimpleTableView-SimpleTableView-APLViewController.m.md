---
title: UITableView Fundamentals for iOS
apple_id: DTS40007318
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-04-07'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewSuite/Listings/1_SimpleTableView_SimpleTableView_APLViewController_m.html
archived_at: '2026-07-18T03:26:14.556596Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UITableView Fundamentals for iOS](UITableView%20Fundamentals%20for%20iOS.md)


[Next](2SimpleSectionedTableView-SimpleSectionedTableView-APLAppDelegate.h.md)[Previous](1SimpleTableView-SimpleTableView-APLAppDelegate.m.md)

# 1_SimpleTableView/SimpleTableView/APLViewController.m

```objc

/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller that sets up the table view and serves as the table view's data source and delegate.
 */

#import "APLViewController.h"

@interface APLViewController ()

@property (nonatomic) NSArray *timeZoneNames;

@end

@implementation APLViewController

#pragma mark - View Life Cycle

- (void)viewDidLoad {
    [super viewDidLoad];

    //  Build Model
    NSArray *timeZones = [NSTimeZone knownTimeZoneNames];
    self.timeZoneNames = [timeZones sortedArrayUsingSelector:@selector(localizedStandardCompare:)];
}

#pragma mark - UITableViewDataSource

/*
 There's no need to implement numberOfSectionsInTableView: because there's only one section and the method defaults to returning 1.
 */

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    // Return the number of time zone names.
    return self.timeZoneNames.count;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {

    static NSString *MyIdentifier = @"MyIdentifier";

    /*
     Retrieve a cell with the given identifier from the table view.
     The cell is defined in the main storyboard: its identifier is MyIdentifier, and  its selection style is set to None.
     */
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:MyIdentifier];

    // Set up the cell.
    NSString *timeZoneName = self.timeZoneNames[indexPath.row];
    cell.textLabel.text = timeZoneName;

    return cell;
}

@end
```

[Next](2SimpleSectionedTableView-SimpleSectionedTableView-APLAppDelegate.h.md)[Previous](1SimpleTableView-SimpleTableView-APLAppDelegate.m.md)

