---
title: 'CloudSearch: Query for documents in iCloud using NSMetaDataQuery'
apple_id: DTS40013494
resource_type: Sample Code
platform: iOS|macOS
topic: Data Management
technology: ApplicationServices
published: '2016-03-24'
source_url: https://developer.apple.com/library/archive/samplecode/CloudSearch/Listings/iOS_CloudSearch_AAPLFilterViewController_m.html
archived_at: '2026-07-18T03:03:35.429505Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudSearch: Query for documents in iCloud using NSMetaDataQuery](CloudSearch-%20Query%20for%20documents%20in%20iCloud%20using%20NSMetaDataQuery.md)


[Next](OSX-CloudSearch-MyAppDelegate.m.md)[Previous](iOS-CloudSearch-AAPLFilterViewController.h.md)

# iOS/CloudSearch/AAPLFilterViewController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Table view for choosing the file extension to filter.
 */

#import "AAPLFilterViewController.h"

@interface AAPLFilterViewController ()

@property (nonatomic, strong) NSArray *filterItems;

@end


#pragma mark -

@implementation AAPLFilterViewController

//----------------------------------------------------------------------------------------
// viewDidLoad
//----------------------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];

    _filterItems = @[@"TEXT", @"JPEG", @"PDF", @"HTML", @"m4v", @"None"];

    // filter by 'txt' by default
    if (self.extensionToFilter == nil)
    {
        // client has not asked for an extension to filter by
        _extensionToFilter = [NSIndexPath indexPathForRow:0 inSection:0];
    }
}

//----------------------------------------------------------------------------------------
// doneAction:sender
//----------------------------------------------------------------------------------------
- (IBAction)doneAction:(id)sender
{
    [self dismissViewControllerAnimated:YES completion:^{

        // call our delegate to filter by chosen extension
        [self.filterDelegate filterViewController:self didSelectExtension:self.extensionToFilter];
    }];
}


#pragma mark - UITableViewDataSource

//----------------------------------------------------------------------------------------
// numberOfRowsInSection:section
//----------------------------------------------------------------------------------------
- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return self.filterItems.count;
}

//----------------------------------------------------------------------------------------
// cellForRowAtIndexPath:indexPath
//----------------------------------------------------------------------------------------
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"cellID" forIndexPath:indexPath];
    cell.textLabel.text = self.filterItems[indexPath.row];
    if (self.extensionToFilter.row == indexPath.row)
    {
        cell.accessoryType = UITableViewCellAccessoryCheckmark;
    }
    else
    {
        cell.accessoryType = UITableViewCellAccessoryNone;
    }
    return cell;
}


#pragma mark - UITableViewDelegate

//----------------------------------------------------------------------------------------
// didSelectRowAtIndexPath:indexPath
//----------------------------------------------------------------------------------------
- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    // uncheck the previous cell
    UITableViewCell *previouslySelectedCell = [tableView cellForRowAtIndexPath:self.extensionToFilter];
    previouslySelectedCell.accessoryType = UITableViewCellAccessoryNone;

    // check the new cell
    _extensionToFilter = indexPath;
    [tableView cellForRowAtIndexPath:indexPath].accessoryType = UITableViewCellAccessoryCheckmark;
    [tableView deselectRowAtIndexPath:indexPath animated:YES];
}

@end
```

[Next](OSX-CloudSearch-MyAppDelegate.m.md)[Previous](iOS-CloudSearch-AAPLFilterViewController.h.md)

