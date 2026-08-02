---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Utils_h.html
archived_at: '2026-07-18T03:23:19.102167Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLSlideTextManager.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Utils.m.md)

# Scene Kit Session WWDC 2014/Sources/Utils.h

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This file contains some utilities such as titled box, loading DAE files, loading images etc...
 */

#import <SceneKit/SceneKit.h>

typedef NS_ENUM(NSInteger, AAPLLabelSize) {
    AAPLLabelSizeSmall = 1,
    AAPLLabelSizeNormal = 2,
    AAPLLabelSizeLarge = 4
};

@interface SCNNode (AAPLAdditions)

// create a node tree from an image
+ (SCNNode *) nodeWithPixelatedImage:(NSImage *) image pixelSize:(CGFloat) size;

// Add the node named 'name' found in the DAE document located at 'path' as a child of the receiver
- (instancetype)asc_addChildNodeNamed:(NSString *)name fromSceneNamed:(NSString *)path withScale:(CGFloat)scale;

// Setup a 3D box with a title
+ (instancetype)asc_boxNodeWithTitle:(NSString *)title frame:(NSRect)frame color:(NSColor *)color cornerRadius:(CGFloat)cornerRadius centered:(BOOL)centered;

// Create a 3D plan with the specified image mapped on it
+ (instancetype)asc_planeNodeWithImage:(NSImage *)image size:(CGFloat)size isLit:(BOOL)isLit;
+ (instancetype)asc_planeNodeWithImageNamed:(NSString *)imageName size:(CGFloat)size isLit:(BOOL)isLit;

// Create a 3D text node
+ (instancetype)asc_labelNodeWithString:(NSString *)text size:(AAPLLabelSize)size isLit:(BOOL)isLit;

// Create a 3D gauge
+ (instancetype)asc_gaugeNodeWithTitle:(NSString *)title progressNode:(SCNNode * __strong *)progressNode;

@end

@interface NSBezierPath (AAPLAdditions)

// Create an arrow
+ (instancetype)asc_arrowBezierPathWithBaseSize:(NSSize)baseSize tipSize:(NSSize)tipSize hollow:(CGFloat)hollow twoSides:(BOOL)twoSides;

@end

@interface NSImage (AAPLAdditions)

// Load an image that represents the application named
+ (instancetype)asc_imageForApplicationNamed:(NSString *)name;

// Create and return an image with the closest resolution to "size"
- (instancetype)asc_copyWithResolution:(CGFloat)size;

@end


@interface SCNAction (AAPLAddition)

+ (SCNAction *) removeFromParentNodeOnMainThread:(SCNNode *) node;

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLSlideTextManager.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Utils.m.md)

