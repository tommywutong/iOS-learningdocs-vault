---
title: Simple UISearchBar with State Restoration
apple_id: DTS40007848
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2013-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/TableSearch/Listings/TableSearch_APLProduct_m.html
archived_at: '2026-07-18T03:26:12.425415Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simple UISearchBar with State Restoration](Simple%20UISearchBar%20with%20State%20Restoration.md)


[Next](TableSearch-APLViewController.m.md)[Previous](TableSearch-APLAppDelegate.m.md)

# TableSearch/APLProduct.m

```objc
/*
 Copyright (C) 2013-2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Simple class to represent a product, with a product type and name. Provides methods to retrieve the names of the available types of product, and the localized name of a product for display.
 */

#import "APLProduct.h"


NSString *ProductTypeDevice = @"Device";
NSString *ProductTypeDesktop = @"Desktop";
NSString *ProductTypePortable = @"Portable";


@implementation APLProduct

+ (instancetype)productWithType:(NSString *)type name:(NSString *)name
{
    APLProduct *newProduct = [[self alloc] init];
    newProduct.type = type;
    newProduct.name = name;
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


static NSString *NameKey = @"NameKey";
static NSString *TypeKey = @"TypeKey";

-(id)initWithCoder:(NSCoder *)aDecoder
{
    self = [super init];
    if (self) {
        _name = [aDecoder decodeObjectForKey:NameKey];
        _type = [aDecoder decodeObjectForKey:TypeKey];
    }
    return self;
}

-(void)encodeWithCoder:(NSCoder *)aCoder
{
    [aCoder encodeObject:self.name forKey:NameKey];
    [aCoder encodeObject:self.type forKey:TypeKey];
}

@end
```

[Next](TableSearch-APLViewController.m.md)[Previous](TableSearch-APLAppDelegate.m.md)

