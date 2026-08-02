---
title: UITableView Fundamentals for iOS
apple_id: DTS40007318
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-04-07'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewSuite/Listings/2_SimpleSectionedTableView_SimpleSectionedTableView_APLViewController_m.html
archived_at: '2026-07-18T03:26:14.776800Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UITableView Fundamentals for iOS](UITableView%20Fundamentals%20for%20iOS.md)


[Next](5CustomTableViewCell-CustomTableViewCell-APLTimeZoneCell.m.md)[Previous](2SimpleSectionedTableView-SimpleSectionedTableView-APLAppDelegate.m.md)

# 2_SimpleSectionedTableView/SimpleSectionedTableView/APLViewController.m

```objc

/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller that sets up the table view and serves as the table view's data source and delegate.
 */

#import "APLViewController.h"
#import "APLAppDelegate.h"
#import "APLRegion.h"
#import "APLTimeZoneWrapper.h"

@interface APLViewController ()

@property (nonatomic) NSArray *displayList;
@property (nonatomic) NSCalendar *calendar;

@end

@implementation APLViewController

#pragma mark - View Life Cycle

- (void)viewDidLoad {
    [super viewDidLoad];

    //  Build Model
    NSCalendar *calendar= [[NSCalendar alloc] initWithCalendarIdentifier:NSCalendarIdentifierGregorian];
    self.calendar = calendar;
    self.displayList = [self regionsWithCalendar:calendar];
}

#pragma mark - Workers

- (NSArray *)regionsWithCalendar:(NSCalendar *)calendar {
    /*
     Create an array of Region objects.
     Each object represents a geographical region.  Each region contains time zones.
     Much of the information required to display a time zone is expensive to compute, so rather than using NSTimeZone objects directly use wrapper objects that calculate the required derived values on demand and cache the results.
     */
    NSArray *knownTimeZoneNames = [NSTimeZone knownTimeZoneNames];

    NSMutableArray *regions = [[NSMutableArray alloc] init];

    for (NSString *timeZoneName in knownTimeZoneNames) {

        NSArray *components = [timeZoneName componentsSeparatedByString:@"/"];
        NSString *regionName = components[0];

        APLRegion *region = [APLRegion regionNamed:regionName];
        if (region == nil) {
            region = [APLRegion newRegionWithName:regionName];
            region.calendar = calendar;
            [regions addObject:region];
        }

        NSTimeZone *timeZone = [[NSTimeZone alloc] initWithName:timeZoneName];
        [region addTimeZone:timeZone nameComponents:components];
    }

    // Now sort the time zones by name.
    NSDate *date = [[NSDate alloc] init];
    for (APLRegion *region in regions) {
        [region sortZones];
        [region setDate:date];
    }

    // Sort the regions by name.
    NSArray *sortedRegions = [regions sortedArrayUsingComparator:^(APLRegion * region1, APLRegion * region2) {
        NSString *name1 = region1.name;
        NSString *name2 = region2.name;
        // Do comparison
        return [name1 localizedStandardCompare:name2];
    }];

    return sortedRegions;
}

#pragma mark - UITableViewDataSource

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
    // Number of sections is the number of regions.
    return self.displayList.count;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    // Number of rows is the number of time zones in the region for the specified section.
    APLRegion *region = self.displayList[section];
    return region.timeZoneWrappers.count;
}

- (NSString *)tableView:(UITableView *)tableView titleForHeaderInSection:(NSInteger)section {
    // The header for the section is the region name -- get this from the region at the section index.
    APLRegion *region = self.displayList[section];
    return region.name;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {

    static NSString *MyIdentifier = @"MyIdentifier";

    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:MyIdentifier];

    // Get the section index, and so the region for that section.
    APLRegion *region = self.displayList[indexPath.section];
    APLTimeZoneWrapper *timeZoneWrapper = region.timeZoneWrappers[indexPath.row];

    // Set the cell's text to the name of the time zone at the row
    cell.textLabel.text = timeZoneWrapper.timeZoneLocaleName;
    return cell;
}

@end
```

[Next](5CustomTableViewCell-CustomTableViewCell-APLTimeZoneCell.m.md)[Previous](2SimpleSectionedTableView-SimpleSectionedTableView-APLAppDelegate.m.md)

