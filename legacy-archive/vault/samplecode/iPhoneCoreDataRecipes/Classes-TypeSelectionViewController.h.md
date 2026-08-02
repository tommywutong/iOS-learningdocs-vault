---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_TypeSelectionViewController_h.html
archived_at: '2026-07-18T03:29:39.592179Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-RecipeTableViewCell.m.md)[Previous](main.m.md)

# Classes/TypeSelectionViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Table view controller to allow the user to select the recipe type.
  The options are presented as items in the table view; the selected item has a check mark in the accessory view. The controller caches the index path of the selected item to avoid the need to perform repeated string comparisons after an update.
 */

@class Recipe;

@interface TypeSelectionViewController : UITableViewController

@property (nonatomic, strong) Recipe *recipe;

@end
```

[Next](Classes-RecipeTableViewCell.m.md)[Previous](main.m.md)

