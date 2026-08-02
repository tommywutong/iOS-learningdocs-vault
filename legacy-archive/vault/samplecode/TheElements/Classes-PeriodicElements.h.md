---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Listings/Classes_PeriodicElements_h.html
archived_at: '2026-07-18T03:26:46.350741Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TheElements](TheElements.md)


[Next](Classes-ElementsSortedBySymbolDataSource.h.md)[Previous](Classes-ElementsDataSourceProtocol.h.md)

# Classes/PeriodicElements.h

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Encapsulates the collection of elements and returns them in presorted states.
*/


@interface PeriodicElements : NSObject

@property (nonatomic, strong) NSMutableDictionary *statesDictionary;
@property (nonatomic, strong) NSMutableDictionary *elementsDictionary;
@property (nonatomic, strong) NSMutableDictionary *nameIndexesDictionary;
@property (nonatomic, strong) NSArray *elementNameIndexArray;
@property (nonatomic, strong) NSArray *elementsSortedByNumber;
@property (nonatomic, strong) NSArray *elementsSortedBySymbol;
@property (nonatomic, strong) NSArray *elementPhysicalStatesArray;

+ (PeriodicElements*)sharedPeriodicElements;

- (NSArray *)elementsWithPhysicalState:(NSString*)aState;
- (NSArray *)elementsWithInitialLetter:(NSString*)aKey;

@end
```

[Next](Classes-ElementsSortedBySymbolDataSource.h.md)[Previous](Classes-ElementsDataSourceProtocol.h.md)

