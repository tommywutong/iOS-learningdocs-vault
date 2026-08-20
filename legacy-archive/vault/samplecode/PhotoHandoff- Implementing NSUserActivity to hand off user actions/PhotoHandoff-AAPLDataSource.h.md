---
title: 'PhotoHandoff: Implementing NSUserActivity to hand off user actions'
apple_id: TP40014785
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoHandoff/Listings/PhotoHandoff_AAPLDataSource_h.html
archived_at: '2026-07-18T03:18:50.422368Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoHandoff: Implementing NSUserActivity to hand off user actions](PhotoHandoff-%20Implementing%20NSUserActivity%20to%20hand%20off%20user%20actions.md)


[Next](PhotoHandoff-AAPLFilterViewController.h.md)[Previous](PhotoHandoff-AAPLDetailViewController.h.md)

# PhotoHandoff/AAPLDataSource.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Data Source to manage assets used by this application

 */

#import <Foundation/Foundation.h>

@interface AAPLDataSource : NSObject <UIStateRestoring>

- (NSInteger)numberOfItemsInSection:(NSInteger)section;
- (NSString *)identifierForIndexPath:(NSIndexPath *)indexPath;
- (NSString *)titleForIdentifier:(NSString *)identifier;
- (UIImage *)thumbnailForIdentifier:(NSString *)identifier;
- (UIImage *)imageForIdentifier:(NSString *)identifier;

@end
```

[Next](PhotoHandoff-AAPLFilterViewController.h.md)[Previous](PhotoHandoff-AAPLDetailViewController.h.md)

