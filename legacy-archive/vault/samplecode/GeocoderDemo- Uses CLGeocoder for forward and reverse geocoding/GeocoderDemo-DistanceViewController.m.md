---
title: 'GeocoderDemo: Uses CLGeocoder for forward and reverse geocoding'
apple_id: DTS40011097
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreLocation
published: '2015-10-30'
source_url: https://developer.apple.com/library/archive/samplecode/GeocoderDemo/Listings/GeocoderDemo_DistanceViewController_m.html
archived_at: '2026-07-18T03:10:42.448335Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GeocoderDemo: Uses CLGeocoder for forward and reverse geocoding](GeocoderDemo-%20Uses%20CLGeocoder%20for%20forward%20and%20reverse%20geocoding.md)


[Next](GeocoderDemo-ForwardViewController.h.md)[Previous](GeocoderDemo-GeocoderDemoAppDelegate.m.md)

# GeocoderDemo/DistanceViewController.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller in charge of measuring distance between 2 locations.
 */

#import "DistanceViewController.h"

#import "CoordinateSelectorTableViewController.h"
#import "PlacemarksListViewController.h"


@interface DistanceViewController ()

@property (readonly) CoordinateSelectorTableViewController *toCoordinateSelector;  
@property (readonly) CoordinateSelectorTableViewController *fromCoordinateSelector;  

@end


#pragma mark -

@implementation DistanceViewController

#pragma mark - View lifecycle

- (void)viewDidLoad
{
    [super viewDidLoad];

    _toCoordinateSelector = [[CoordinateSelectorTableViewController alloc] init];
    _fromCoordinateSelector = [[CoordinateSelectorTableViewController alloc] init];

    self.tableView.estimatedRowHeight = 44.f;
    self.tableView.rowHeight = UITableViewAutomaticDimension;
}

- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];
    [self.tableView reloadData];
}


#pragma mark - Distance Calculation

- (double)distanceBetweenCoordinates
{
    CLLocationDegrees latitude, longitude;

    latitude = self.toCoordinateSelector.selectedCoordinate.latitude;
    longitude = self.toCoordinateSelector.selectedCoordinate.longitude;
    CLLocation *to = [[CLLocation alloc] initWithLatitude:latitude longitude:longitude];

    latitude = self.fromCoordinateSelector.selectedCoordinate.latitude;
    longitude = self.fromCoordinateSelector.selectedCoordinate.longitude;
    CLLocation *from = [[CLLocation alloc] initWithLatitude:latitude longitude:longitude];

    CLLocationDistance distance = [to distanceFromLocation:from];

    return distance;
}


#pragma mark - UITableViewDataSource

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
    // return the number of sections
    return 2;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    // return the number of rows in the section
    return 1;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    UITableViewCell *cell = nil;

    // to and from cells
    if (indexPath.section == 0 || indexPath.section == 1)
    {
        cell = [tableView dequeueReusableCellWithIdentifier:@"selectorCell"];
        if (cell == nil)
        {
            cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle reuseIdentifier:@"selectorCell"];
            cell.accessoryType = UITableViewCellAccessoryDisclosureIndicator;
        }

        CoordinateSelectorTableViewController *selector;
        switch (indexPath.section)
        {
            default:
            case 0:
                selector = self.toCoordinateSelector;
                break;
            case 1:
                selector = self.fromCoordinateSelector;
                break;
        }

        if (selector.selectedType != CoordinateSelectorLastSelectedTypeUndefined)
        {
            cell.accessoryType = UITableViewCellAccessoryDisclosureIndicator;
            (cell.textLabel).lineBreakMode = NSLineBreakByWordWrapping;
            cell.textLabel.numberOfLines = 0;
            cell.textLabel.font = [UIFont systemFontOfSize:16.0];
            cell.textLabel.text = selector.selectedName;

            if (CLLocationCoordinate2DIsValid(selector.selectedCoordinate))
            {
                (cell.detailTextLabel).lineBreakMode = NSLineBreakByWordWrapping;
                cell.detailTextLabel.numberOfLines = 0;
                cell.detailTextLabel.font = [UIFont boldSystemFontOfSize:16.0];

                cell.detailTextLabel.text = [NSString stringWithFormat:@"φ:%.4F, λ:%.4F", selector.selectedCoordinate.latitude, selector.selectedCoordinate.longitude];
            }
        }
        else
        {
            cell.textLabel.text = @"Select a Place";
            cell.detailTextLabel.text = @"";
        }
    }

    return cell;
}

- (NSString *)tableView:(UITableView *)tableView titleForFooterInSection:(NSInteger)section
{
    if (section == 1)
    {
        if (self.toCoordinateSelector.selectedType != CoordinateSelectorLastSelectedTypeUndefined &&
            self.fromCoordinateSelector.selectedType != CoordinateSelectorLastSelectedTypeUndefined)
        {
            return [NSString stringWithFormat:@"%.1f km\n(as the crow flies)", [self distanceBetweenCoordinates] / 1000];
        }
        else
        {
            return @"- km";
        }
    }
    return nil;
}


#pragma mark - UITableViewDelegate

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    [[tableView cellForRowAtIndexPath:indexPath] setSelected:NO];

    if (indexPath.section == 0)
    {
        [self.navigationController pushViewController:self.toCoordinateSelector animated:YES];
    }
    else if (indexPath.section == 1)
    {
        [self.navigationController pushViewController:self.fromCoordinateSelector animated:YES];
    }
}

@end
```

[Next](GeocoderDemo-ForwardViewController.h.md)[Previous](GeocoderDemo-GeocoderDemoAppDelegate.m.md)

