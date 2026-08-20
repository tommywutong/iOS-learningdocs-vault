---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_Query_QueryDataSource_h.html
archived_at: '2026-07-18T03:18:14.676853Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-Graphics-Displays-Modes-CGDisplayModes.mm.md)[Previous](Sources-Frameworks-Model-Query-QueryDataSource.mm.md)

# Sources/Frameworks/Model/Query/QueryDataSource.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Query data source for the outline view.
 */

#import <Foundation/Foundation.h>

@interface QueryDataSource : NSObject

@property (nonatomic, readonly) NSMutableArray* data;

+ (instancetype) query;

- (BOOL) isChild:(NSString *)string;
- (BOOL) isParent:(NSString *)string;

@end
```

[Next](Sources-Frameworks-Model-Graphics-Displays-Modes-CGDisplayModes.mm.md)[Previous](Sources-Frameworks-Model-Query-QueryDataSource.mm.md)

