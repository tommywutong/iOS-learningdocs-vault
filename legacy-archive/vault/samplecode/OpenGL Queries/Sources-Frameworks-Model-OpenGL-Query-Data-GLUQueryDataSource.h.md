---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_OpenGL_Query_Data_GLUQueryDataSource_h.html
archived_at: '2026-07-18T03:18:13.875957Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-OpenGL-Containers-GLContainers.h.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Data-GLUQueryDataSource.mm.md)

# Sources/Frameworks/Model/OpenGL/Query/Data/GLUQueryDataSource.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Query data source for OpenGL renderer and device quaries.
 */

#import <Foundation/Foundation.h>

#import "GLUQueryDevices.h"
#import "GLUQueryRenderers.h"

@interface GLUQueryDataSource : NSObject

@property (nonatomic, readonly) NSMutableDictionary*  dictionary;
@property (nonatomic, readonly) NSMutableSet*         parent;
@property (nonatomic, readonly) NSMutableSet*         childern;

+ (instancetype) query;

- (BOOL) isChild:(NSString *)string;
- (BOOL) isParent:(NSString *)string;

@end
```

[Next](Sources-Frameworks-Model-OpenGL-Containers-GLContainers.h.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Data-GLUQueryDataSource.mm.md)

