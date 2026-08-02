---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_AAPLSlideTextManager_h.html
archived_at: '2026-07-18T03:23:14.383472Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLView.h.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLView.m.md)

# Scene Kit Session WWDC 2014/Sources/AAPLSlideTextManager.h

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 AAPLSlideTextManager manages the layout of the different types of text presented in the slides.
 */

#import <SceneKit/SceneKit.h>

typedef NS_ENUM(NSInteger, AAPLTextType) {
    AAPLTextTypeNone,
    AAPLTextTypeChapter,
    AAPLTextTypeTitle,
    AAPLTextTypeSubtitle,
    AAPLTextTypeBullet,
    AAPLTextTypeBody,
    AAPLTextTypeCode,
    AAPLTextTypeFootPrint,
    AAPLTextTypeCount
};

@interface AAPLSlideTextManager : NSObject

#pragma mark - Add text content to the slide

- (SCNNode *)setTitle:(NSString *)title;
- (SCNNode *)setSubtitle:(NSString *)title;
- (SCNNode *)setChapterTitle:(NSString *)title;
- (SCNNode *)addBullet:(NSString *)text atLevel:(NSUInteger)level;
- (SCNNode *)addCode:(NSString *)text;
- (SCNNode *)addText:(NSString *)text atLevel:(NSUInteger)level;
- (SCNNode *)addFootPrint:(NSString *)text;
- (void)addEmptyLine;

#pragma mark - Animations

- (void)highlightBulletAtIndex:(NSUInteger)index;
- (void)highlightCodeChunks:(NSArray *)chunks;
- (void)flipOutTextOfType:(AAPLTextType)type;
- (void)flipInTextOfType:(AAPLTextType)type;
- (void)fadeOutTextOfType:(AAPLTextType)type;

#pragma mark - Properties

@property (strong) SCNNode *textNode;
@property BOOL fadesIn;

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLView.h.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLView.m.md)

