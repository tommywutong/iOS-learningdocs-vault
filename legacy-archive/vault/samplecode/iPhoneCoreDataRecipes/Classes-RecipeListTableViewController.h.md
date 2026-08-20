---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_RecipeListTableViewController_h.html
archived_at: '2026-07-18T03:29:38.939097Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-TemperatureCell.m.md)[Previous](Classes-MetricPickerController.m.md)

# Classes/RecipeListTableViewController.h

```objc
/*
  Copyright (C) 2017 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  Table view controller to manage an editable table view that displays a list of recipes.
    Recipes are displayed in a custom table view cell.
*/

#import "RecipeAddViewController.h"

@interface RecipeListTableViewController : UITableViewController

@property (nonatomic, strong) NSManagedObjectContext *managedObjectContext;

@end
```

[Next](Classes-TemperatureCell.m.md)[Previous](Classes-MetricPickerController.m.md)

