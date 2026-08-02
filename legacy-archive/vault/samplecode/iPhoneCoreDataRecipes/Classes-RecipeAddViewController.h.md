---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_RecipeAddViewController_h.html
archived_at: '2026-07-18T03:29:38.654981Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-Recipe.h.md)[Previous](Classes-WeightConverterViewController.h.md)

# Classes/RecipeAddViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller to allow the user to add a new recipe and choose its picture using the image picker.
  If the user taps Save, the recipe detail view controller is pushed so that the user can edit the new item.
 */

@protocol RecipeAddDelegate;

@class Recipe;

@interface RecipeAddViewController : UIViewController

@property (nonatomic, strong) Recipe *recipe;
@property (nonatomic, unsafe_unretained) id <RecipeAddDelegate> delegate;

@end


#pragma mark -

@protocol RecipeAddDelegate <NSObject>

// recipe == nil on cancel
- (void)recipeAddViewController:(RecipeAddViewController *)recipeAddViewController didAddRecipe:(Recipe *)recipe;

@end
```

[Next](Classes-Recipe.h.md)[Previous](Classes-WeightConverterViewController.h.md)

