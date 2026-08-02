---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_LTSlide_m.html
archived_at: '2026-07-18T03:13:31.174265Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-LTViewController.h.md)[Previous](LightTable-LTSlide.h.md)

# LightTable/LTSlide.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This is the completion of the slide entity from our Core Data model. We needed to create a class in order for our entity to return CGRect data. We accomplish this by using the methods in "Core Data Programming Guide: Non-Standard Persistent Attributes"
 */

#import "LTSlide.h"


@implementation LTSlide

// We need to @synthetize the iVars for value properties.
@synthesize frame = ivar_frame;
@synthesize photoFrame = ivar_photoFrame;

// Cribbed from "Core Data Programming Guide"
- (CGRect)_rectForIvar:(CGRect *)pIvarRect forKey:(NSString *)key {
    [self willAccessValueForKey:key];
    CGRect rect = *pIvarRect;
    [self didAccessValueForKey:key];

    if(rect.size.width == 0.0) {
        NSString *rectAsString = [self valueForKey:[NSString stringWithFormat:@"%@AsString", key]];
        if(rectAsString != nil) {
            *pIvarRect = NSRectToCGRect(NSRectFromString(rectAsString));
        }
    }

    return *pIvarRect;
}

- (void)awakeFromInsert
{
    [super awakeFromInsert];
    ivar_frame = CGRectZero;
    ivar_photoFrame = CGRectZero;
}

- (void)_setRect:(CGRect)rect forIvar:(CGRect *)pIvarRect forKey:(NSString *)key {
    [self willChangeValueForKey:key];
    *pIvarRect = rect;
    [self didChangeValueForKey:key];

    NSString *rectAsString = NSStringFromRect(NSRectFromCGRect(*pIvarRect));
    [self setValue:rectAsString forKey:[NSString stringWithFormat:@"%@AsString", key]];

}

- (CGRect)frame {
    return [self _rectForIvar:&ivar_frame forKey:@"frame"];
}

- (void)setFrame:(CGRect)rect {
    [self _setRect:rect forIvar:&ivar_frame forKey:@"frame"];
}

- (CGRect)photoFrame {
    return [self _rectForIvar:&ivar_photoFrame forKey:@"photoFrame"];
}

- (void)setPhotoFrame:(CGRect)rect {
    [self _setRect:rect forIvar:&ivar_photoFrame forKey:@"photoFrame"];
}

- (void)setNilValueForKey:(NSString *)key {
    if([key isEqualToString:@"frame"]) {
        [self _setRect:CGRectZero forIvar:&ivar_frame forKey:@"frame"];

        return;
    }

    if([key isEqualToString:@"photoFrame"]) {
        [self _setRect:CGRectZero forIvar:&ivar_photoFrame forKey:@"photoFrame"];

        return;
    }

    [super setNilValueForKey:key];
}

@end
```

[Next](LightTable-LTViewController.h.md)[Previous](LightTable-LTSlide.h.md)

