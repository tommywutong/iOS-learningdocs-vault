---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_Recipe_m.html
archived_at: '2026-07-18T03:29:39.324066Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-ImperialPickerController.h.md)[Previous](Classes-RecipeDetailViewController.m.md)

# Classes/Recipe.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Model class to represent a recipe.
 */

#import "Recipe.h"

@implementation Recipe

@dynamic name, image, overview, thumbnailImage, instructions, ingredients, type, prepTime;

@end

#pragma mark -

@implementation ImageToDataTransformer

+ (BOOL)allowsReverseTransformation {
    return YES;
}

+ (Class)transformedValueClass {
    return [NSData class];
}

- (id)transformedValue:(id)value {
    NSData *data = UIImagePNGRepresentation(value);
    return data;
}

- (id)reverseTransformedValue:(id)value {
    UIImage *uiImage = [[UIImage alloc] initWithData:value];
    return uiImage;
}

@end
```

[Next](Classes-ImperialPickerController.h.md)[Previous](Classes-RecipeDetailViewController.m.md)

