---
title: 'PhotoHandoff: Implementing NSUserActivity to hand off user actions'
apple_id: TP40014785
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoHandoff/Listings/PhotoHandoff_AAPLDataSource_m.html
archived_at: '2026-07-18T03:18:50.459796Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoHandoff: Implementing NSUserActivity to hand off user actions](PhotoHandoff-%20Implementing%20NSUserActivity%20to%20hand%20off%20user%20actions.md)


[Next](PhotoHandoff-AAPLDetailViewController.h.md)[Previous](PhotoHandoff-AAPLAppDelegate.h.md)

# PhotoHandoff/AAPLDataSource.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 */

#import "AAPLDataSource.h"

@interface AAPLDataSource ()
@property (nonatomic, strong) NSDictionary *data;
@end


#pragma mark -

@implementation AAPLDataSource

- (instancetype)init {

    self = [super init];
    if (self != nil) {
        NSString *pathToData = [[NSBundle mainBundle] pathForResource:@"Data" ofType:@"plist"];
        self.data = [NSDictionary dictionaryWithContentsOfFile:pathToData];
    }
    return self;
}

- (NSInteger)numberOfItemsInSection:(NSInteger)section {
    return 32;
}

- (NSString *)identifierForIndexPath:(NSIndexPath *)indexPath {
    return [NSString stringWithFormat:@"%ld", (long)indexPath.row];
}

- (NSString *)titleForIdentifier:(NSString *)identifier {

    NSString *title = identifier ? (self.data)[identifier] : nil;
    if (title == nil) {
        title = @"Image";
    }
    return title;
}

- (UIImage *)thumbnailForIdentifier:(NSString *)identifier {

    if (identifier == nil) {
        return nil;
    }
    NSString *pathToImage = [[NSBundle mainBundle] pathForResource:identifier ofType:@"JPG"];
    return [[UIImage alloc] initWithContentsOfFile:pathToImage];
}

- (UIImage *)imageForIdentifier:(NSString *)identifier {

    if (identifier == nil) {
        return nil;
    }
    NSString *imageName = [NSString stringWithFormat:@"%@_full", identifier];
    NSString *pathToImage = [[NSBundle mainBundle] pathForResource:imageName ofType:@"JPG"];
    UIImage *image = [[UIImage alloc] initWithContentsOfFile:pathToImage];
    return image;
}

@end
```

[Next](PhotoHandoff-AAPLDetailViewController.h.md)[Previous](PhotoHandoff-AAPLAppDelegate.h.md)

