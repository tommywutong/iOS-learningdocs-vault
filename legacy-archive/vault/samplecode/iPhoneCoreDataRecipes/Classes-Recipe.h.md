---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_Recipe_h.html
archived_at: '2026-07-18T03:29:39.279099Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-TemperatureCell.h.md)[Previous](Classes-RecipeAddViewController.h.md)

# Classes/Recipe.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Model class to represent a recipe.
 */

@interface ImageToDataTransformer : NSValueTransformer
@end

@interface Recipe : NSManagedObject

@property (nonatomic, strong) NSString *instructions;
@property (nonatomic, strong) NSString *name;
@property (nonatomic, strong) NSString *overview;
@property (nonatomic, strong) NSString *prepTime;
@property (nonatomic, strong) NSSet *ingredients;
@property (nonatomic, strong) UIImage *thumbnailImage;

@property (nonatomic, strong) NSManagedObject *image;
@property (nonatomic, strong) NSManagedObject *type;

@end

@interface Recipe (CoreDataGeneratedAccessors)

- (void)addIngredientsObject:(NSManagedObject *)value;
- (void)removeIngredientsObject:(NSManagedObject *)value;
- (void)addIngredients:(NSSet *)value;
- (void)removeIngredients:(NSSet *)value;

@end
```

[Next](Classes-TemperatureCell.h.md)[Previous](Classes-RecipeAddViewController.h.md)

