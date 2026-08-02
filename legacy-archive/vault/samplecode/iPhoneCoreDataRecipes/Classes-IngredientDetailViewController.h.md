---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_IngredientDetailViewController_h.html
archived_at: '2026-07-18T03:29:38.316904Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-MetricPickerController.m.md)[Previous](Classes-InstructionsViewController.h.md)

# Classes/IngredientDetailViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Table view controller to manage editing details of a recipe ingredient -- its name and amount.
 */

@class Recipe, Ingredient;

@interface IngredientDetailViewController : UITableViewController

@property (nonatomic, strong) Recipe *recipe;
@property (nonatomic, strong) Ingredient *ingredient;

@end
```

[Next](Classes-MetricPickerController.m.md)[Previous](Classes-InstructionsViewController.h.md)

