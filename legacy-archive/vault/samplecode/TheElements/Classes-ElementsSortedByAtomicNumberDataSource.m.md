---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Listings/Classes_ElementsSortedByAtomicNumberDataSource_m.html
archived_at: '2026-07-18T03:26:45.888908Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TheElements](TheElements.md)


[Next](Classes-AtomicElementTableViewCell.m.md)[Previous](Classes-ElementsSortedByNameDataSource.m.md)

# Classes/ElementsSortedByAtomicNumberDataSource.m

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Provides the table view data for the elements sorted by atomic number.
*/


#import "ElementsSortedByAtomicNumberDataSource.h"
#import "PeriodicElements.h"
#import "AtomicElementTableViewCell.h"


@implementation ElementsSortedByAtomicNumberDataSource

// protocol methods for "ElementsDataSourceProtocol"

// return the data used by the navigation controller and tab bar item

- (NSString *)navigationBarName {

    return @"Sorted by Atomic Number";
}

- (NSString *)name {

    return @"Number";
}

- (UIImage *)tabBarImage {

    return [UIImage imageNamed:@"number_gray.png"];
}

// atomic number is displayed in a plain style tableview
- (UITableViewStyle)tableViewStyle {

    return UITableViewStylePlain;
}

// return the atomic element at the index in the sorted by numbers array
- (AtomicElement *)atomicElementForIndexPath:(NSIndexPath *)indexPath {

    return [[PeriodicElements sharedPeriodicElements] elementsSortedByNumber][indexPath.row];
}


#pragma mark - UITableViewDataSource

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {

    AtomicElementTableViewCell *cell =
        (AtomicElementTableViewCell *)[tableView dequeueReusableCellWithIdentifier:@"AtomicElementTableViewCell"];

    // set the element for this cell as specified by the datasource. The atomicElementForIndexPath: is declared
    // as part of the ElementsDataSource Protocol and will return the appropriate element for the index row
    //
    cell.element = [self atomicElementForIndexPath:indexPath];

    return cell;
}

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {

    // this table has only one section
    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView  numberOfRowsInSection:(NSInteger)section {

    // get the shared elements object
    // ask for, and return, the number of elements in the array of elements sorted by number
    return [[[PeriodicElements sharedPeriodicElements] elementsSortedByNumber] count];
}

@end
```

[Next](Classes-AtomicElementTableViewCell.m.md)[Previous](Classes-ElementsSortedByNameDataSource.m.md)

