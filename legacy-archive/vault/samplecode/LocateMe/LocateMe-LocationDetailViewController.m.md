---
title: LocateMe
apple_id: DTS40007801
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreLocation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LocateMe/Listings/LocateMe_LocationDetailViewController_m.html
archived_at: '2026-07-18T03:13:46.258773Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LocateMe](LocateMe.md)


[Next](LocateMe-GetLocationViewController.h.md)[Previous](LocateMe-CLLocation%2BStrings.h.md)

# LocateMe/LocationDetailViewController.m

```objc
/*
Copyright (C) 2014 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

*/

#import "LocationDetailViewController.h"
#import "CLLocation+Strings.h"

@interface LocationDetailViewController ()

@property (nonatomic, strong) NSDateFormatter *dateFormatter;

@end


#pragma mark -

@implementation LocationDetailViewController

@synthesize location;

- (NSDateFormatter *)dateFormatter {
    if (_dateFormatter == nil) {
        _dateFormatter = [[NSDateFormatter alloc] init];
        [_dateFormatter setDateStyle:NSDateFormatterMediumStyle];
        [_dateFormatter setTimeStyle:NSDateFormatterLongStyle];
    }
    return _dateFormatter;
}

- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    self.title = NSLocalizedString(@"LocationInfo", @"LocationInfo");
    [self.tableView reloadData];
}


#pragma mark - UITableViewDataSource

- (NSInteger)numberOfSectionsInTableView:(UITableView *)table {
    return 3;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return (section == 0) ? 3: 2;
}

- (NSString *)tableView:(UITableView *)tableView titleForHeaderInSection:(NSInteger)section {
    NSString *headerTitle = nil;

    switch (section) {
        case 0: {
            headerTitle = NSLocalizedString(@"Attributes", @"Attributes");
            break;
        }
        case 1: {
            headerTitle = NSLocalizedString(@"Accuracy", @"Accuracy");
            break;
        }
        default: {
            headerTitle = NSLocalizedString(@"Course and Speed", @"Course and Speed");
            break;
        }
    }

    return headerTitle;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    static NSString *kLocationAttributeCellID = @"LocationAttributeCellID";
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:kLocationAttributeCellID];
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleValue2 reuseIdentifier:kLocationAttributeCellID];
        cell.selectionStyle = UITableViewCellSelectionStyleNone;
    }
    if (indexPath.section == 0) {
        switch (indexPath.row) {
            case 0: {
                cell.textLabel.text = NSLocalizedString(@"timestamp", @"timestamp");
                cell.detailTextLabel.text = [self.dateFormatter stringFromDate:location.timestamp];
            } break;
            case 1: {
                cell.textLabel.text = NSLocalizedString(@"coordinate", @"coordinate");
                if (location.horizontalAccuracy < 0) {
                } else {
                    cell.detailTextLabel.text = location.localizedCoordinateString;
                }
            } break;
            default: {
                cell.textLabel.text = NSLocalizedString(@"altitude", @"altitude");
                cell.detailTextLabel.text = location.localizedAltitudeString;
            } break;
        }
    } else if (indexPath.section == 1) {
        switch (indexPath.row) {
            case 0: {
                cell.textLabel.text = NSLocalizedString(@"horizontal", @"horizontal");
                cell.detailTextLabel.text = location.localizedHorizontalAccuracyString;
            } break;
            default: {
                cell.textLabel.text = NSLocalizedString(@"vertical", @"vertical");
                cell.detailTextLabel.text = location.localizedVerticalAccuracyString;
            } break;
        }
    } else {
        switch (indexPath.row) {
            case 0: {
                cell.textLabel.text = NSLocalizedString(@"course", @"course");
                cell.detailTextLabel.text = location.localizedCourseString;
            } break;
            default: {
                cell.textLabel.text = NSLocalizedString(@"speed", @"speed");
                cell.detailTextLabel.text = location.localizedSpeedString;
            } break;
        }
    }
    return cell;
}

@end
```

[Next](LocateMe-GetLocationViewController.h.md)[Previous](LocateMe-CLLocation%2BStrings.h.md)

