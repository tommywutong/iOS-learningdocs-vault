---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/SpriteKit.html
archived_at: '2026-07-18T02:56:16.414554Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# SpriteKit Changes

## SpriteKit

Removed SK3DNode.nodeWithViewportSize(CGSize) -> Self! [class]Removed SKMutableTexture.mutableTextureWithSize(CGSize) -> Self! [class]Removed SKNode.node() -> Self! [class]Removed SKNode.objectForKeyedSubscript(String) -> [AnyObject]Removed SKRange.rangeWithLowerLimit(CGFloat, upperLimit: CGFloat) -> Self! [class]Removed SKScene.sceneWithSize(CGSize) -> Self! [class]Removed SKShader.shaderWithSource(String!) -> Self! [class]Removed SKShader.shaderWithSource(String!, uniforms:[AnyObject]!) -> Self! [class]Added SK3DNode.init(coder: NSCoder)Added SK3DNode.pointOfViewAdded SK3DNode.scnSceneAdded SKKeyframeSequence.init(coder: NSCoder)Added SKNode.init(coder: NSCoder)Added SKSpriteNode.init(coder: NSCoder)Added SKVideoNode.init(AVPlayer: AVPlayer!)Added SKVideoNode.init(coder: NSCoder)Added UITouch.locationInNode(SKNode!) -> CGPointAdded UITouch.previousLocationInNode(SKNode!) -> CGPointModified SKActionTimingMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKBlendMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKKeyframeSequence.init(keyframeValues: [AnyObject], times:[AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(keyframeValues values: [AnyObject], times times: [AnyObject]) ``` |
| To | ``` init!(keyframeValues values: [AnyObject], times times: [AnyObject]) ``` |

Modified SKLabelHorizontalAlignmentMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKLabelVerticalAlignmentMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKNode.init(fileNamed: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fileNamed filename: String) ``` |
| To | ``` convenience init!(fileNamed filename: String) ``` |

Modified SKPhysicsBody.init(polygonFromPath: CGPath!)

|  | Declaration |
| --- | --- |
| From | ``` init(polygonFromPath path: CGPath!) -> SKPhysicsBody ``` |
| To | ``` init!(polygonFromPath path: CGPath!) -> SKPhysicsBody ``` |

Modified SKPhysicsBody.init(rectangleOfSize: CGSize)

|  | Declaration |
| --- | --- |
| From | ``` init(rectangleOfSize s: CGSize) -> SKPhysicsBody ``` |
| To | ``` init!(rectangleOfSize s: CGSize) -> SKPhysicsBody ``` |

Modified SKPhysicsBody.init(rectangleOfSize: CGSize, center: CGPoint)

|  | Declaration |
| --- | --- |
| From | ``` init(rectangleOfSize s: CGSize, center center: CGPoint) -> SKPhysicsBody ``` |
| To | ``` init!(rectangleOfSize s: CGSize, center center: CGPoint) -> SKPhysicsBody ``` |

Modified SKPhysicsBody.init(texture: SKTexture!, alphaThreshold: Float, size: CGSize)

|  | Declaration |
| --- | --- |
| From | ``` init(texture texture: SKTexture!, alphaThreshold alphaThreshold: Float, size size: CGSize) -> SKPhysicsBody ``` |
| To | ``` init!(texture texture: SKTexture!, alphaThreshold alphaThreshold: Float, size size: CGSize) -> SKPhysicsBody ``` |

Modified SKPhysicsBody.init(texture: SKTexture!, size: CGSize)

|  | Declaration |
| --- | --- |
| From | ``` init(texture texture: SKTexture!, size size: CGSize) -> SKPhysicsBody ``` |
| To | ``` init!(texture texture: SKTexture!, size size: CGSize) -> SKPhysicsBody ``` |

Modified SKSceneScaleMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKShader.init(fileNamed: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fileNamed name: String) ``` |
| To | ``` convenience init!(fileNamed name: String) ``` |

Modified SKTexture.init(data: NSData!, size: CGSize)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data pixelData: NSData!, size size: CGSize) ``` |
| To | ``` convenience init!(data pixelData: NSData!, size size: CGSize) ``` |

Modified SKTexture.init(data: NSData!, size: CGSize, flipped: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data pixelData: NSData!, size size: CGSize, flipped flipped: Bool) ``` |
| To | ``` convenience init!(data pixelData: NSData!, size size: CGSize, flipped flipped: Bool) ``` |

Modified SKTexture.init(data: NSData!, size: CGSize, rowLength: UInt32, alignment: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data pixelData: NSData!, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) ``` |
| To | ``` convenience init!(data pixelData: NSData!, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) ``` |

Modified SKTexture.init(imageNamed: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(imageNamed name: String) ``` |
| To | ``` convenience init!(imageNamed name: String) ``` |

Modified SKTexture.init(noiseWithSmoothness: CGFloat, size: CGSize, grayscale: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(noiseWithSmoothness smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool) ``` |
| To | ``` convenience init!(noiseWithSmoothness smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool) ``` |

Modified SKTexture.init(vectorNoiseWithSmoothness: CGFloat, size: CGSize)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(vectorNoiseWithSmoothness smoothness: CGFloat, size size: CGSize) ``` |
| To | ``` convenience init!(vectorNoiseWithSmoothness smoothness: CGFloat, size size: CGSize) ``` |

Modified SKTextureAtlas.init(dictionary: [NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` convenience init(dictionary properties: [NSObject : AnyObject]) ``` |
| To | ``` convenience init!(dictionary properties: [NSObject : AnyObject]) ``` |

Modified SKTextureAtlas.init(named: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(named name: String) ``` |
| To | ``` convenience init!(named name: String) ``` |

Modified SKTextureFilteringMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKTransitionDirection [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKUniform.init(name: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!) ``` |
| To | ``` init!(name name: String!) ``` |

Modified SKUniform.init(name: String!, float: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, float value: Float) ``` |
| To | ``` init!(name name: String!, float value: Float) ``` |

Modified SKUniform.init(name: String!, texture: SKTexture!)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, texture texture: SKTexture!) ``` |
| To | ``` init!(name name: String!, texture texture: SKTexture!) ``` |

Modified SKVideoNode.init(videoFileNamed: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(videoFileNamed videoFile: String!) -> SKVideoNode ``` |
| To | ``` init!(videoFileNamed videoFile: String!) -> SKVideoNode ``` |

Modified SKVideoNode.init(videoFileNamed: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(videoFileNamed videoFile: String) ``` |
| To | ``` convenience init!(videoFileNamed videoFile: String) ``` |

Modified SKVideoNode.init(videoURL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(videoURL videoURL: NSURL!) -> SKVideoNode ``` |
| To | ``` init!(videoURL videoURL: NSURL!) -> SKVideoNode ``` |

Modified SKVideoNode.init(videoURL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(videoURL url: NSURL) ``` |
| To | ``` convenience init!(videoURL url: NSURL) ``` |

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
