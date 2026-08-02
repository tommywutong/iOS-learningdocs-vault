---
title: Advanced UISearchBar
apple_id: DTS40013493
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2013-07-24'
source_url: https://developer.apple.com/library/archive/samplecode/AdvancedTableSearch/Listings/AdvancedTableSearch_APLProduct_h.html
archived_at: '2026-07-18T03:00:48.909182Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Advanced UISearchBar](Advanced%20UISearchBar.md)


[Next](AdvancedTableSearch-APLAppDelegate.m.md)[Previous](AdvancedTableSearch-APLViewController.h.md)

# AdvancedTableSearch/APLProduct.h

```objc
/*
 Copyright (C) 2013-2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Simple class to represent a product, with a product type and name. Provides methods to retrieve the names of the available types of product, and the localized name of a product for display.
 */


extern NSString *ProductTypeDevice;
extern NSString *ProductTypeDesktop;
extern NSString *ProductTypePortable;


@interface APLProduct : NSObject <NSCoding>

@property (nonatomic, copy) NSString *name;
@property (nonatomic, copy) NSString *type;
@property (nonatomic, copy) NSNumber *yearIntroduced;
@property (nonatomic) NSNumber *introPrice;

+ (instancetype)productWithType:(NSString *)type name:(NSString *)name year:(NSNumber *)year price:(NSNumber *)price;

+ (NSArray *)deviceTypeNames;
+ (NSString *)displayNameForType:(NSString *)type;

@end
```

[Next](AdvancedTableSearch-APLAppDelegate.m.md)[Previous](AdvancedTableSearch-APLViewController.h.md)

