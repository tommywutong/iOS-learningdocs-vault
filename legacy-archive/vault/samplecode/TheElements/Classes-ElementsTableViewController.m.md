---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Listings/Classes_ElementsTableViewController_m.html
archived_at: '2026-07-18T03:26:46.304521Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TheElements](TheElements.md)


[Next](Classes-AtomicElementViewController.h.md)[Previous](Classes-PeriodicElements.m.md)

# Classes/ElementsTableViewController.m

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Coordinates the tableviews and element data sources. It also responds to changes of selection in the table view and provides the cells.
*/


#import "ElementsTableViewController.h"
#import "AtomicElementViewController.h"


@implementation ElementsTableViewController

- (void)setDataSource:(id<ElementsDataSource,UITableViewDataSource>)dataSource {

    // retain the data source
    _dataSource = dataSource;

    // set the title, and tab bar images from the dataSource
    // object. These are part of the ElementsDataSource Protocol
    self.title = [_dataSource name];
    self.tabBarItem.image = [_dataSource tabBarImage];

    // set the long name shown in the navigation bar
    self.navigationItem.title = [_dataSource navigationBarName];
}

- (void)viewDidLoad {

    [super viewDidLoad];

    self.tableView.sectionIndexMinimumDisplayRowCount = 10;

    self.tableView.delegate = self;
    self.tableView.dataSource = self.dataSource;

    // create a custom navigation bar button and set it to always say "back"
    UIBarButtonItem *temporaryBarButtonItem = [[UIBarButtonItem alloc] init];
    temporaryBarButtonItem.title = @"Back";
    self.navigationItem.backBarButtonItem = temporaryBarButtonItem;
}


#pragma mark - UITableViewDelegate

- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {

    if ([segue.identifier isEqualToString:@"showDetail"]) {
        NSIndexPath *selectedIndexPath = [self.tableView indexPathForSelectedRow];

        // find the right view controller
        AtomicElement *element = [self.dataSource atomicElementForIndexPath:selectedIndexPath];
        AtomicElementViewController *viewController =
            (AtomicElementViewController *)segue.destinationViewController;

        // hide the bottom tabbar when we push this view controller
        viewController.hidesBottomBarWhenPushed = YES;

        // pass the element to this detail view controller
        viewController.element = element;
    }
}

@end
```

[Next](Classes-AtomicElementViewController.h.md)[Previous](Classes-PeriodicElements.m.md)

