---
title: 'Tabster: Various techniques in using UITabBarController'
apple_id: DTS40011213
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-02-15'
source_url: https://developer.apple.com/library/archive/samplecode/Tabster/Listings/Tabster_Classes_SubLevelViewController_m.html
archived_at: '2026-07-18T03:26:20.369201Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabster: Various techniques in using UITabBarController](Tabster-%20Various%20techniques%20in%20using%20UITabBarController.md)


[Next](Tabster-Classes-ThreeViewController.m.md)[Previous](Tabster-Classes-SubLevelViewController.h.md)

# Tabster/Classes/SubLevelViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  The view controller for sublevel 2. 
 */

#import "SubLevelViewController.h"
#import "ModalViewController.h"

@interface SubLevelViewController ()

@property (nonatomic, strong) NSArray *dataArray;
@property (nonatomic, strong) ModalViewController *myModalViewController;

@end

#pragma mark -

@implementation SubLevelViewController

- (void)viewDidLoad
{
    [super viewDidLoad];

    _dataArray = @[@"Feature 1", @"Feature 2"];
}

#pragma mark - UITableViewDelegate

- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    if ([segue.identifier isEqualToString:@"modalSegue"])
    {
        ModalViewController *myModalViewController1 = segue.destinationViewController;
        myModalViewController1.owningViewController = self;
        UITableViewCell *cell = sender;
        self.currentSelectionTitle = cell.textLabel.text;
    }
}

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    [tableView deselectRowAtIndexPath:indexPath animated:NO];
}

#pragma mark - UITableViewDataSource

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return self.dataArray.count;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *kCellID2 = @"cellID2";

    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:kCellID2];
    cell.textLabel.text = self.dataArray[indexPath.row];

    return cell;
}

- (IBAction)unwindToSub:(UIStoryboardSegue *)unwindSegue
{ }

@end
```

[Next](Tabster-Classes-ThreeViewController.m.md)[Previous](Tabster-Classes-SubLevelViewController.h.md)

