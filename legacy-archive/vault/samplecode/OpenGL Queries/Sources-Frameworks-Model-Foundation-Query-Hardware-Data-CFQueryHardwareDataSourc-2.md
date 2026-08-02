---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_Foundation_Query_Hardware_Data_CFQueryHardwareDataSource_h.html
archived_at: '2026-07-18T03:18:13.051337Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-Foundation-Text-Text.h.md)[Previous](Sources-Frameworks-Model-Foundation-Query-Hardware-Data-CFQueryHardwareDataSourc.md)

# Sources/Frameworks/Model/Foundation/Query/Hardware/Data/CFQueryHardwareDataSource.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Query data source for hardware property queries.
 */

#import <Foundation/Foundation.h>

#import "CFQueryHardware.h"

@interface CFQueryHardwareDataSource : NSObject

@property (nonatomic, readonly) NSMutableDictionary*  dictionary;
@property (nonatomic, readonly) NSMutableSet*         parent;
@property (nonatomic, readonly) NSMutableSet*         childern;

+ (instancetype) query;

- (BOOL) isChild:(NSString *)string;
- (BOOL) isParent:(NSString *)string;

@end
```

[Next](Sources-Frameworks-Model-Foundation-Text-Text.h.md)[Previous](Sources-Frameworks-Model-Foundation-Query-Hardware-Data-CFQueryHardwareDataSourc.md)

