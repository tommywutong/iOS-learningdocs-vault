---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_TemperatureCell_m.html
archived_at: '2026-07-18T03:29:39.484073Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-Ingredient.h.md)[Previous](Classes-RecipeListTableViewController.h.md)

# Classes/TemperatureCell.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A table view cell that displays temperature in Centigrade, Fahrenheit, and Gas Mark.
 */

#import "TemperatureCell.h"

@implementation TemperatureCell

- (void)setTemperatureDataFromDictionary:(NSDictionary *)temperatureDictionary {

    // Update text in labels from the dictionary.
    self.cLabel.text = temperatureDictionary[@"c"];
    self.fLabel.text = temperatureDictionary[@"f"];
    self.gLabel.text = temperatureDictionary[@"g"];
}

@end
```

[Next](Classes-Ingredient.h.md)[Previous](Classes-RecipeListTableViewController.h.md)

