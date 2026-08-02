---
title: watchOS 3.1 API Diffs
apple_id: TP40017546
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS31APIDiffs/Swift/SpriteKit.html
archived_at: '2026-07-18T02:58:38.932778Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.1 API Diffs](watchOS%203.0%20to%20watchOS%203.1%20API%20Differences.md)


# SpriteKit Changes for Swift

### SpriteKit

Modified [SKFieldNode](https://developer.apple.com/documentation/spritekit/skfieldnode)

|  | Declaration |
| --- | --- |
| From | ``` class SKFieldNode : SKNode {     var region: SKRegion?     var strength: Float     var falloff: Float     var minimumRadius: Float     var isEnabled: Bool     var isExclusive: Bool     var categoryBitMask: UInt32     var direction: vector_float3     var smoothness: Float     var animationSpeed: Float     var texture: SKTexture?     class func dragField() -> SKFieldNode     class func vortexField() -> SKFieldNode     class func radialGravityField() -> SKFieldNode     class func linearGravityField(withVector direction: vector_float3) -> SKFieldNode     class func velocityField(withVector direction: vector_float3) -> SKFieldNode     class func velocityField(with velocityTexture: SKTexture) -> SKFieldNode     class func noiseField(withSmoothness smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode     class func turbulenceField(withSmoothness smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode     class func springField() -> SKFieldNode     class func electricField() -> SKFieldNode     class func magneticField() -> SKFieldNode     class func customField(evaluationBlock block: SpriteKit.SKFieldForceEvaluator) -> SKFieldNode } ``` |
| To | ``` class SKFieldNode : SKNode {     var region: SKRegion?     var strength: Float     var falloff: Float     var minimumRadius: Float     var isEnabled: Bool     var isExclusive: Bool     var categoryBitMask: UInt32     var direction: vector_float3     var smoothness: Float     var animationSpeed: Float     var texture: SKTexture?     class func dragField() -> SKFieldNode     class func vortexField() -> SKFieldNode     class func radialGravityField() -> SKFieldNode     class func linearGravityField(withVector direction: vector_float3) -> SKFieldNode     class func velocityField(withVector direction: vector_float3) -> SKFieldNode     class func velocityField(with velocityTexture: SKTexture) -> SKFieldNode     class func noiseField(withSmoothness smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode     class func turbulenceField(withSmoothness smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode     class func springField() -> SKFieldNode     class func electricField() -> SKFieldNode     class func magneticField() -> SKFieldNode     class func customField(evaluationBlock block: @escaping SpriteKit.SKFieldForceEvaluator) -> SKFieldNode } ``` |

Modified [SKFieldNode.customField(evaluationBlock: SpriteKit.SKFieldForceEvaluator) -> SKFieldNode [class]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519710-customfieldwithevaluationblock)

|  | Declaration |
| --- | --- |
| From | ``` class func customField(evaluationBlock block: SpriteKit.SKFieldForceEvaluator) -> SKFieldNode ``` |
| To | ``` class func customField(evaluationBlock block: @escaping SpriteKit.SKFieldForceEvaluator) -> SKFieldNode ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
