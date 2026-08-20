---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_TemperatureCell_h.html
archived_at: '2026-07-18T03:29:39.454752Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-RecipesAppDelegate.m.md)[Previous](Classes-Recipe.h.md)

# Classes/TemperatureCell.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A table view cell that displays temperature in Centigrade, Fahrenheit, and Gas Mark.
 */

@interface TemperatureCell : UITableViewCell

@property (nonatomic, strong) IBOutlet UILabel *cLabel;
@property (nonatomic, strong) IBOutlet UILabel *fLabel;
@property (nonatomic, strong) IBOutlet UILabel *gLabel;

- (void)setTemperatureDataFromDictionary:(NSDictionary *)temperatureDictionary;

@end
```

[Next](Classes-RecipesAppDelegate.m.md)[Previous](Classes-Recipe.h.md)

