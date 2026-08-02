---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_RecipeDetailViewController_h.html
archived_at: '2026-07-18T03:29:38.751482Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-RecipePhotoViewController.m.md)[Previous](Classes-InstructionsViewController.m.md)

# Classes/RecipeDetailViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Table view controller to manage an editable table view that displays information about a recipe.
  The table view uses different cell types for different row types.
 */

@class Recipe;

@interface RecipeDetailViewController : UITableViewController

@property (nonatomic, strong) Recipe *recipe;

@end
```

[Next](Classes-RecipePhotoViewController.m.md)[Previous](Classes-InstructionsViewController.m.md)

