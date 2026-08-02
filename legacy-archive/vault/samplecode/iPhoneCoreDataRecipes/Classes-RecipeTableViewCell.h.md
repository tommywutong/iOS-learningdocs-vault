---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_RecipeTableViewCell_h.html
archived_at: '2026-07-18T03:29:39.164805Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-EditingTableViewCell.h.md)[Previous](Classes-EditingTableViewCell.m.md)

# Classes/RecipeTableViewCell.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A table view cell that displays information about a Recipe.  It uses individual subviews of its content view to show the name, picture, description, and preparation time for each recipe.  If the table view switches to editing mode, the cell reformats itself to move the preparation time off-screen, and resizes the name and description fields accordingly.
 */

#import "Recipe.h"

@interface RecipeTableViewCell : UITableViewCell

@property (nonatomic, strong) Recipe *recipe;

@end
```

[Next](Classes-EditingTableViewCell.h.md)[Previous](Classes-EditingTableViewCell.m.md)

