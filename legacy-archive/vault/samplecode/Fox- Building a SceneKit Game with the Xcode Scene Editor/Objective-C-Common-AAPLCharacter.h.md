---
title: 'Fox: Building a SceneKit Game with the Xcode Scene Editor'
apple_id: TP40016154
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: General
technology: SceneKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Fox/Listings/Objective_C_Common_AAPLCharacter_h.html
archived_at: '2026-07-18T03:08:52.354212Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox: Building a SceneKit Game with the Xcode Scene Editor](Fox-%20Building%20a%20SceneKit%20Game%20with%20the%20Xcode%20Scene%20Editor.md)


[Next](Objective-C-Common-AAPLCharacter.m.md)[Previous](Objective-C-Common-AAPLGameView.m.md)

# Objective-C/Common/AAPLCharacter.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This class manages the main character, including its animations, sounds and direction.
*/

@import Foundation;

typedef NS_ENUM(NSUInteger, AAPLGroundType) {
   AAPLGroundTypeGrass,
   AAPLGroundTypeRock,
   AAPLGroundTypeWater,
   AAPLGroundTypeInTheAir,
   AAPLGroundTypeCount
};

@interface AAPLCharacter : NSObject

@property(nonatomic, readonly) SCNNode *node;

- (SCNNode *)walkInDirection:(vector_float3)direction time:(NSTimeInterval)time scene:(SCNScene *)scene groundTypeFromMaterial:(AAPLGroundType(^)(SCNMaterial *))groundTypeFromMaterial;
- (void)catchFire;
- (void)haltFire;

@end
```

[Next](Objective-C-Common-AAPLCharacter.m.md)[Previous](Objective-C-Common-AAPLGameView.m.md)

