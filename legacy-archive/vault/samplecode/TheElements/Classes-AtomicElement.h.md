---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Listings/Classes_AtomicElement_h.html
archived_at: '2026-07-18T03:26:45.703528Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TheElements](TheElements.md)


[Next](Classes-ElementsTableViewController.h.md)[Previous](Classes-AtomicElementTileView.m.md)

# Classes/AtomicElement.h

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Simple object that encapsulate the Atomic Element values and images for the states.
*/

@interface AtomicElement : NSObject

@property (nonatomic, strong) NSNumber *atomicNumber;
@property (nonatomic, strong) NSString *name;
@property (nonatomic, strong) NSString *symbol;
@property (nonatomic, strong) NSString *state;
@property (weak, readonly) UIImage *flipperImageForAtomicElementNavigationItem;
@property (weak, readonly) UIImage *stateImageForAtomicElementTileView;
@property (weak, readonly) UIImage *stateImageForAtomicElementView;
@property (nonatomic, strong) NSString *atomicWeight;
@property (nonatomic, strong) NSNumber *group;
@property (nonatomic, strong) NSNumber *period;
@property (nonatomic, strong) NSString *discoveryYear;

- (instancetype)initWithDictionary:(NSDictionary *)aDictionary;

@end
```

[Next](Classes-ElementsTableViewController.h.md)[Previous](Classes-AtomicElementTileView.m.md)

