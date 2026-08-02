---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_TemperatureConverterViewController_m.html
archived_at: '2026-07-18T03:29:39.557374Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](ReadMe.md.md)[Previous](Classes-RecipesAppDelegate.m.md)

# Classes/TemperatureConverterViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller to display cooking temperatures in Centigrade, Fahrenheit, and Gas Mark.
 */

#import "TemperatureConverterViewController.h"
#import "TemperatureCell.h"

@interface TemperatureConverterViewController ()

@property (nonatomic, strong) NSArray *temperatureData;

@end


#pragma mark -

@implementation TemperatureConverterViewController

static NSString *MyIdentifier = @"MyIdentifier";


#pragma mark - UITableViewDataSource

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {

    return self.temperatureData.count;
}

- (UITableViewCell *)tableView:(UITableView *)aTableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {

    // Create a new TemperatureCell.
    TemperatureCell *cell =
        (TemperatureCell *)[aTableView dequeueReusableCellWithIdentifier:MyIdentifier
                                                            forIndexPath:indexPath];

    // Configure the temperature cell with the relevant data.
    NSDictionary *temperatureDictionary = (self.temperatureData)[indexPath.row];
    [cell setTemperatureDataFromDictionary:temperatureDictionary];

    return cell;
}


#pragma mark - Temperature data

- (NSArray *)temperatureData {

    if (_temperatureData == nil) {
        // Get the temperature data from the TemperatureData property list.
        NSString *temperatureDataPath = [[NSBundle mainBundle] pathForResource:@"TemperatureData" ofType:@"plist"];
        NSArray *array = [[NSArray alloc] initWithContentsOfFile:temperatureDataPath];
        self.temperatureData = array;
    }
    return _temperatureData;
}


#pragma mark - Memory management

- (void)didReceiveMemoryWarning {

    [super didReceiveMemoryWarning];
    self.temperatureData = nil;
}

@end
```

[Next](ReadMe.md.md)[Previous](Classes-RecipesAppDelegate.m.md)

