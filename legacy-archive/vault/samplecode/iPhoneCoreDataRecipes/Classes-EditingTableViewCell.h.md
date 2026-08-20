---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_EditingTableViewCell_h.html
archived_at: '2026-07-18T03:29:38.140200Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-RecipeDetailViewController.m.md)[Previous](Classes-RecipeTableViewCell.h.md)

# Classes/EditingTableViewCell.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A table view cell that displays a label and a text field so that a value can be edited. The user interface is loaded from a nib file.
 */

@interface EditingTableViewCell : UITableViewCell

@property (nonatomic, strong) IBOutlet UILabel *label;
@property (nonatomic, strong) IBOutlet UITextField *textField;

@end
```

[Next](Classes-RecipeDetailViewController.m.md)[Previous](Classes-RecipeTableViewCell.h.md)

