---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_RecipePhotoViewController_m.html
archived_at: '2026-07-18T03:29:39.109296Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-IngredientDetailViewController.m.md)[Previous](Classes-RecipeDetailViewController.h.md)

# Classes/RecipePhotoViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller to manage a view to display a recipe's photo.
  The image view is created programmatically.
 */

#import "RecipePhotoViewController.h"
#import "Recipe.h"

@interface RecipePhotoViewController ()

@property(nonatomic, strong) UIImageView *imageView;

@end


#pragma mark -

@implementation RecipePhotoViewController

- (void)viewDidLoad {

    [super viewDidLoad];

    self.title = NSLocalizedString(@"Photo", @"");

    _imageView = [[UIImageView alloc] initWithFrame:[UIScreen mainScreen].bounds];
    self.imageView.contentMode = UIViewContentModeScaleAspectFit;
    self.imageView.backgroundColor = [UIColor blackColor];

    self.view = self.imageView;
}

- (void)viewWillAppear:(BOOL)animated {

    [super viewWillAppear:animated];
    self.imageView.image = [self.recipe.image valueForKey:@"image"];
}

@end
```

[Next](Classes-IngredientDetailViewController.m.md)[Previous](Classes-RecipeDetailViewController.h.md)

