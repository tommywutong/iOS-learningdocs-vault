---
title: Simple UISearchBar with State Restoration
apple_id: DTS40007848
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2013-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/TableSearch/Listings/TableSearch_APLProduct_h.html
archived_at: '2026-07-18T03:26:12.389817Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simple UISearchBar with State Restoration](Simple%20UISearchBar%20with%20State%20Restoration.md)


[Next](TableSearch-APLAppDelegate.m.md)[Previous](TableSearch-APLViewController.h.md)

# TableSearch/APLProduct.h

```objc

/*
 Copyright (C) 2013-2015 Apple Inc. All Rights Reserved.
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

+ (instancetype)productWithType:(NSString *)type name:(NSString *)name;

+ (NSArray *)deviceTypeNames;
+ (NSString *)displayNameForType:(NSString *)type;

@end
```

[Next](TableSearch-APLAppDelegate.m.md)[Previous](TableSearch-APLViewController.h.md)

