---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/SpriteKit.html
archived_at: '2026-07-18T02:56:27.807970Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# SpriteKit Changes

## SpriteKit

Added SKNode.isEqualToNode(SKNode!) -> BoolAdded SKUniform.floatMatrix2ValueAdded SKUniform.floatMatrix3ValueAdded SKUniform.floatMatrix4ValueAdded SKUniform.floatVector2ValueAdded SKUniform.floatVector3ValueAdded SKUniform.floatVector4ValueAdded SKUniform.init(name: String!, floatMatrix2: GLKMatrix2)Added SKUniform.init(name: String!, floatMatrix3: GLKMatrix3)Added SKUniform.init(name: String!, floatMatrix4: GLKMatrix4)Added SKUniform.init(name: String!, floatVector2: GLKVector2)Added SKUniform.init(name: String!, floatVector3: GLKVector3)Added SKUniform.init(name: String!, floatVector4: GLKVector4)Modified SKConstraint.distance(SKRange!, toNode: SKNode!) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func distance(_ range: SKRange!, toNode node: SKNode!) -> Self! ``` | iOS 8.0 |
| To | ``` class func distance(_ range: SKRange!, toNode node: SKNode!) -> Self ``` | iOS 8.3 |

Modified SKConstraint.distance(SKRange, toPoint: CGPoint) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func distance(_ range: SKRange, toPoint point: CGPoint) -> Self! ``` | iOS 8.0 |
| To | ``` class func distance(_ range: SKRange, toPoint point: CGPoint) -> Self ``` | iOS 8.3 |

Modified SKConstraint.distance(SKRange, toPoint: CGPoint, inNode: SKNode) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func distance(_ range: SKRange, toPoint point: CGPoint, inNode node: SKNode) -> Self! ``` | iOS 8.0 |
| To | ``` class func distance(_ range: SKRange, toPoint point: CGPoint, inNode node: SKNode) -> Self ``` | iOS 8.3 |

Modified SKConstraint.orientToNode(SKNode, offset: SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func orientToNode(_ node: SKNode, offset radians: SKRange) -> Self! ``` | iOS 8.0 |
| To | ``` class func orientToNode(_ node: SKNode, offset radians: SKRange) -> Self ``` | iOS 8.3 |

Modified SKConstraint.orientToPoint(CGPoint, inNode: SKNode, offset: SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func orientToPoint(_ point: CGPoint, inNode node: SKNode, offset radians: SKRange) -> Self! ``` | iOS 8.0 |
| To | ``` class func orientToPoint(_ point: CGPoint, inNode node: SKNode, offset radians: SKRange) -> Self ``` | iOS 8.3 |

Modified SKConstraint.orientToPoint(CGPoint, offset: SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func orientToPoint(_ point: CGPoint, offset radians: SKRange) -> Self! ``` | iOS 8.0 |
| To | ``` class func orientToPoint(_ point: CGPoint, offset radians: SKRange) -> Self ``` | iOS 8.3 |

Modified SKConstraint.positionX(SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func positionX(_ range: SKRange) -> Self! ``` | iOS 8.0 |
| To | ``` class func positionX(_ range: SKRange) -> Self ``` | iOS 8.3 |

Modified SKConstraint.positionX(SKRange, y: SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func positionX(_ xRange: SKRange, y yRange: SKRange) -> Self! ``` | iOS 8.0 |
| To | ``` class func positionX(_ xRange: SKRange, y yRange: SKRange) -> Self ``` | iOS 8.3 |

Modified SKConstraint.positionY(SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func positionY(_ range: SKRange) -> Self! ``` | iOS 8.0 |
| To | ``` class func positionY(_ range: SKRange) -> Self ``` | iOS 8.3 |

Modified SKConstraint.zRotation(SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func zRotation(_ zRange: SKRange) -> Self! ``` | iOS 8.0 |
| To | ``` class func zRotation(_ zRange: SKRange) -> Self ``` | iOS 8.3 |

Modified SKMutableTexture.modifyPixelDataWithBlock((UnsafeMutablePointer<Void>, Int) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func modifyPixelDataWithBlock(_ block: (UnsafeMutablePointer<Void>, UInt) -> Void) ``` | iOS 8.0 |
| To | ``` func modifyPixelDataWithBlock(_ block: (UnsafeMutablePointer<Void>, Int) -> Void) ``` | iOS 8.3 |

Modified SKRange.rangeWithNoLimits() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func rangeWithNoLimits() -> Self! ``` | iOS 8.0 |
| To | ``` class func rangeWithNoLimits() -> Self ``` | iOS 8.3 |

Modified SKRegion.infiniteRegion() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func infiniteRegion() -> Self! ``` | iOS 8.0 |
| To | ``` class func infiniteRegion() -> Self ``` | iOS 8.3 |

Modified SKRegion.inverseRegion() -> Self

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func inverseRegion() -> Self! ``` | iOS 8.0 |
| To | ``` func inverseRegion() -> Self ``` | iOS 8.3 |

Modified SKRegion.regionByDifferenceFromRegion(SKRegion) -> Self

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func regionByDifferenceFromRegion(_ region: SKRegion) -> Self! ``` | iOS 8.0 |
| To | ``` func regionByDifferenceFromRegion(_ region: SKRegion) -> Self ``` | iOS 8.3 |

Modified SKShapeNode.init(points: UnsafeMutablePointer<CGPoint>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(points points: UnsafeMutablePointer<CGPoint>, count numPoints: UInt) ``` |
| To | ``` convenience init(points points: UnsafeMutablePointer<CGPoint>, count numPoints: Int) ``` |

Modified SKShapeNode.init(splinePoints: UnsafeMutablePointer<CGPoint>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(splinePoints points: UnsafeMutablePointer<CGPoint>, count numPoints: UInt) ``` |
| To | ``` convenience init(splinePoints points: UnsafeMutablePointer<CGPoint>, count numPoints: Int) ``` |

Modified SKTexture.textureByApplyingCIFilter(CIFilter) -> Self

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func textureByApplyingCIFilter(_ filter: CIFilter) -> Self! ``` | iOS 8.0 |
| To | ``` func textureByApplyingCIFilter(_ filter: CIFilter) -> Self ``` | iOS 8.3 |

Modified SKVideoNode.init(videoFileNamed: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(videoFileNamed videoFile: String) ``` |
| To | ``` init!(videoFileNamed videoFile: String) ``` |

Modified SKVideoNode.init(videoURL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(videoURL url: NSURL) ``` |
| To | ``` init!(videoURL url: NSURL) ``` |

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
