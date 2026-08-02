---
title: Advanced UISearchBar
apple_id: DTS40013493
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2013-07-24'
source_url: https://developer.apple.com/library/archive/samplecode/AdvancedTableSearch/Listings/AdvancedTableSearch_APLProduct_m.html
archived_at: '2026-07-18T03:00:48.938678Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Advanced UISearchBar](Advanced%20UISearchBar.md)


[Next](AdvancedTableSearch-APLViewController.m.md)[Previous](AdvancedTableSearch-APLAppDelegate.m.md)

# AdvancedTableSearch/APLProduct.m

```objc
/*
Copyright (C) 2013-2014 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Simple class to represent a product, with a product type and name. Provides methods to retrieve the names of the available types of product, and the localized name of a product for display.
*/

#import "APLProduct.h"

NSString *ProductTypeDevice = @"Device";
NSString *ProductTypeDesktop = @"Desktop";
NSString *ProductTypePortable = @"Portable";


@implementation APLProduct

+ (instancetype)productWithType:(NSString *)type name:(NSString *)name year:(NSNumber *)year price:(NSNumber *)price
{
    APLProduct *newProduct = [[self alloc] init];
    newProduct.type = type;
    newProduct.name = name;
    newProduct.yearIntroduced = year;
    newProduct.introPrice = price;

    return newProduct;
}

+ (NSArray *)deviceTypeNames
{
    static NSArray *deviceTypeNames = nil;
    static dispatch_once_t once;

    dispatch_once(&once, ^{
        deviceTypeNames = @[ProductTypeDevice, ProductTypePortable, ProductTypeDesktop];
    });

    return deviceTypeNames;
}

+ (NSString *)displayNameForType:(NSString *)type
{
    static NSMutableDictionary *deviceTypeDisplayNamesDictionary = nil;
    static dispatch_once_t once;

    dispatch_once(&once, ^{
        deviceTypeDisplayNamesDictionary = [[NSMutableDictionary alloc] init];
        for (NSString *deviceType in self.deviceTypeNames)
        {
            NSString *displayName = NSLocalizedString(deviceType, @"dynamic");
            deviceTypeDisplayNamesDictionary[deviceType] = displayName;
        }
    });

    return deviceTypeDisplayNamesDictionary[type];
}


#pragma mark - Archiving

static NSString *NameKey = @"NameKey";
static NSString *TypeKey = @"TypeKey";
static NSString *YearKey = @"YearKey";
static NSString *PriceKey = @"PriceKey";

- (id)initWithCoder:(NSCoder *)aDecoder
{
    self = [super init];
    if (self) {
        _name = [aDecoder decodeObjectForKey:NameKey];
        _type = [aDecoder decodeObjectForKey:TypeKey];
        _yearIntroduced = [aDecoder decodeObjectForKey:YearKey];
        _introPrice = [aDecoder decodeObjectForKey:PriceKey];
    }
    return self;
}

- (void)encodeWithCoder:(NSCoder *)aCoder
{
    [aCoder encodeObject:self.name forKey:NameKey];
    [aCoder encodeObject:self.type forKey:TypeKey];
    [aCoder encodeObject:self.yearIntroduced forKey:YearKey];
    [aCoder encodeObject:self.introPrice forKey:PriceKey];
}

@end
```

[Next](AdvancedTableSearch-APLViewController.m.md)[Previous](AdvancedTableSearch-APLAppDelegate.m.md)

