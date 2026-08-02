---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_Ingredient_h.html
archived_at: '2026-07-18T03:29:38.418471Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-TypeSelectionViewController.m.md)[Previous](Classes-TemperatureCell.m.md)

# Classes/Ingredient.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Model class to represent an ingredient.
 */

@class Recipe;

@interface Ingredient : NSManagedObject

@property (nonatomic, strong) NSString *name;
@property (nonatomic, strong) NSString *amount;
@property (nonatomic, strong) Recipe *recipe;
@property (nonatomic, strong) NSNumber *displayOrder;

@end
```

[Next](Classes-TypeSelectionViewController.m.md)[Previous](Classes-TemperatureCell.m.md)

