---
title: 'PhotoHandoff: Implementing NSUserActivity to hand off user actions'
apple_id: TP40014785
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoHandoff/Listings/PhotoHandoff_AAPLImageFilter_m.html
archived_at: '2026-07-18T03:18:50.865160Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoHandoff: Implementing NSUserActivity to hand off user actions](PhotoHandoff-%20Implementing%20NSUserActivity%20to%20hand%20off%20user%20actions.md)


[Next](PhotoHandoff-AAPLViewController.h.md)[Previous](PhotoHandoff-AAPLDetailViewController.m.md)

# PhotoHandoff/AAPLImageFilter.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.

 See LICENSE.txt for this sample’s licensing information

 */

#import "AAPLImageFilter.h"

@implementation AAPLImageFilter

- (instancetype)initFilter:(BOOL)useDefaultState {

    self = [super init];
    if (self != nil && useDefaultState) {
        self.active = YES;
    }
    return self;
}


#pragma mark - UIStateRestoration

#define kImageFilterActiveKey @"kImageFilterActiveKey"

- (void)encodeRestorableStateWithCoder:(NSCoder *)coder {

    [coder encodeFloat:self.active forKey:kImageFilterActiveKey];
}

- (void)decodeRestorableStateWithCoder:(NSCoder *)coder {

    if ([coder containsValueForKey:kImageFilterActiveKey]) {
        self.active = [coder decodeFloatForKey:kImageFilterActiveKey];
    }
}

@end


#pragma mark - BlurFilter

@implementation BlurFilter

- (instancetype)initFilter:(BOOL)useDefaultState {

    self = [super initFilter:useDefaultState];
    if (self && useDefaultState) {
        self.blurRadius = 0.0;  // start off with no blur
    }
    return self;
}

#pragma mark - UIStateRestoration

#define kImageFilterBlurRadiusKey @"kImageFilterBlurRadiusKey"

- (void)encodeRestorableStateWithCoder:(NSCoder *)coder {

    [super encodeRestorableStateWithCoder:coder];
    [coder encodeFloat:self.blurRadius forKey:kImageFilterBlurRadiusKey];
}

- (void)decodeRestorableStateWithCoder:(NSCoder *)coder {

    [super decodeRestorableStateWithCoder:coder];
    if ([coder containsValueForKey:kImageFilterBlurRadiusKey]) {
        self.blurRadius = [coder decodeFloatForKey:kImageFilterBlurRadiusKey];
    }
}

@end


#pragma mark - ModifyFilter

@implementation ModifyFilter

- (instancetype)initFilter:(BOOL)useDefaultState {

    self = [super initFilter:useDefaultState];
    if (self && useDefaultState) {
        self.intensity = 0.0;   // start off with no sepia intensity
    }
    return self;
}


#pragma mark - UIStateRestoration

#define kImageFilterIntensityKey @"kImageFilterIntensityKey"

- (void)encodeRestorableStateWithCoder:(NSCoder *)coder {

    [super encodeRestorableStateWithCoder:coder];
    [coder encodeFloat:self.intensity forKey:kImageFilterIntensityKey];
}

- (void)decodeRestorableStateWithCoder:(NSCoder *)coder {

    [super decodeRestorableStateWithCoder:coder];
    if ([coder containsValueForKey:kImageFilterIntensityKey]) {
        self.intensity = [coder decodeFloatForKey:kImageFilterIntensityKey];
    }
}

@end
```

[Next](PhotoHandoff-AAPLViewController.h.md)[Previous](PhotoHandoff-AAPLDetailViewController.m.md)

