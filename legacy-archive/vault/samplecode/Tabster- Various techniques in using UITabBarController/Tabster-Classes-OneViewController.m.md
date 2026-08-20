---
title: 'Tabster: Various techniques in using UITabBarController'
apple_id: DTS40011213
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-02-15'
source_url: https://developer.apple.com/library/archive/samplecode/Tabster/Listings/Tabster_Classes_OneViewController_m.html
archived_at: '2026-07-18T03:26:20.280340Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabster: Various techniques in using UITabBarController](Tabster-%20Various%20techniques%20in%20using%20UITabBarController.md)


[Next](Tabster-Classes-FourViewController.m.md)[Previous](Tabster-Classes-FavoritesViewController.h.md)

# Tabster/Classes/OneViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  The view controller for page one. 
 */

#import "OneViewController.h"
#import "SubLevelViewController.h"

@interface OneViewController ()

@property (nonatomic, strong) NSArray *dataArray;

@end

#pragma mark -

@implementation OneViewController

// This is called when its tab is first tapped by the user.
- (void)viewDidLoad
{
    [super viewDidLoad];

    _dataArray = @[@"Mac Pro", @"Mac mini", @"iMac", @"MacBook", @"MacBook Pro", @"MacBook Air"];
}

- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];

    // This UIViewController is about to re-appear, make sure we remove the current selection in our table view.
    NSIndexPath *tableSelection = self.tableView.indexPathForSelectedRow;
    [self.tableView deselectRowAtIndexPath:tableSelection animated:NO];
}


#pragma mark - UITableViewDataSource

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return self.dataArray.count;
}

- (void) prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    if ([segue.identifier isEqualToString:@"SubLevelSegue"]) {

        SubLevelViewController *mySubLevelViewController = segue.destinationViewController;
        UITableViewCell *cell = sender;
        mySubLevelViewController.title = cell.textLabel.text;
    }
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *kCellID = @"cellID";

    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:kCellID];
    cell.textLabel.text = self.dataArray[indexPath.row];

    return cell;
}


@end
```

[Next](Tabster-Classes-FourViewController.m.md)[Previous](Tabster-Classes-FavoritesViewController.h.md)

