---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/SceneKit.html
archived_at: '2026-07-18T02:56:16.068619Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# SceneKit Changes

## SceneKit

Removed SCNPhysicsCollisionCategory.valueAdded CAAnimation.animationEventsAdded CAAnimation.fadeInDurationAdded CAAnimation.fadeOutDurationAdded CAAnimation.usesSceneTimeBaseAdded NSValue.init(SCNMatrix4: SCNMatrix4)Added NSValue.SCNMatrix4ValueAdded NSValue.init(SCNVector3: SCNVector3)Added NSValue.SCNVector3ValueAdded NSValue.init(SCNVector4: SCNVector4)Added NSValue.SCNVector4ValueAdded SCNPhysicsCollisionCategory.init(rawValue: UInt)Added SCNSceneRenderer.overlaySKSceneModified SCNParticleSystem.init(named: String, inDirectory: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(named name: String, inDirectory directory: String!) ``` |
| To | ``` convenience init!(named name: String, inDirectory directory: String!) ``` |

Modified SCNPhysicsBallSocketJoint.init(body: SCNPhysicsBody!, anchor: SCNVector3)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(body body: SCNPhysicsBody!, anchor anchor: SCNVector3) ``` |
| To | ``` convenience init!(body body: SCNPhysicsBody!, anchor anchor: SCNVector3) ``` |

Modified SCNPhysicsBallSocketJoint.init(bodyA: SCNPhysicsBody!, anchorA: SCNVector3, bodyB: SCNPhysicsBody!, anchorB: SCNVector3)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(bodyA bodyA: SCNPhysicsBody!, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, anchorB anchorB: SCNVector3) ``` |
| To | ``` convenience init!(bodyA bodyA: SCNPhysicsBody!, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, anchorB anchorB: SCNVector3) ``` |

Modified SCNPhysicsCollisionCategory [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCNPhysicsCollisionCategory : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Default: SCNPhysicsCollisionCategory { get }     static var Static: SCNPhysicsCollisionCategory { get }     static var All: SCNPhysicsCollisionCategory { get } } ``` |
| To | ``` struct SCNPhysicsCollisionCategory : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Default: SCNPhysicsCollisionCategory { get }     static var Static: SCNPhysicsCollisionCategory { get }     static var All: SCNPhysicsCollisionCategory { get } } ``` |

Modified SCNPhysicsCollisionCategory.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified SCNPhysicsSliderJoint.init(body: SCNPhysicsBody!, axis: SCNVector3, anchor: SCNVector3)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(body body: SCNPhysicsBody!, axis axis: SCNVector3, anchor anchor: SCNVector3) ``` |
| To | ``` convenience init!(body body: SCNPhysicsBody!, axis axis: SCNVector3, anchor anchor: SCNVector3) ``` |

Modified SCNPhysicsSliderJoint.init(bodyA: SCNPhysicsBody!, axisA: SCNVector3, anchorA: SCNVector3, bodyB: SCNPhysicsBody!, axisB: SCNVector3, anchorB: SCNVector3)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(bodyA bodyA: SCNPhysicsBody!, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3) ``` |
| To | ``` convenience init!(bodyA bodyA: SCNPhysicsBody!, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3) ``` |

Modified SCNScene.init(URL: NSURL, options:[NSObject: AnyObject]?, error: NSErrorPointer)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | sceneWithURL(_:options:error:) | ``` class func sceneWithURL(_ url: NSURL, options options: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Self! ``` | iOS 8.0 |
| To | init(URL:options:error:) | ``` convenience init?(URL url: NSURL, options options: [NSObject : AnyObject]?, error error: NSErrorPointer) ``` | iOS 8.1 |

Modified SCNScene.init(named: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(named name: String) ``` |
| To | ``` convenience init?(named name: String) ``` |

Modified SCNScene.init(named: String, inDirectory: String?, options:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(named name: String, inDirectory directory: String?, options options: [NSObject : AnyObject]?) ``` |
| To | ``` convenience init?(named name: String, inDirectory directory: String?, options options: [NSObject : AnyObject]?) ``` |

Modified SCNSceneSource.init(URL: NSURL, options:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL, options options: [NSObject : AnyObject]?) ``` |
| To | ``` init?(URL url: NSURL, options options: [NSObject : AnyObject]?) ``` |

Modified SCNSceneSource.init(data: NSData, options:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData, options options: [NSObject : AnyObject]?) ``` |
| To | ``` init?(data data: NSData, options options: [NSObject : AnyObject]?) ``` |

Modified SCNSkinner.init(baseGeometry: SCNGeometry!, bones:[AnyObject]!, boneInverseBindTransforms:[AnyObject]!, boneWeights: SCNGeometrySource!, boneIndices: SCNGeometrySource!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(baseGeometry baseGeometry: SCNGeometry!, bones bones: [AnyObject]!, boneInverseBindTransforms boneInverseBindTransforms: [AnyObject]!, boneWeights boneWeights: SCNGeometrySource!, boneIndices boneIndices: SCNGeometrySource!) ``` |
| To | ``` convenience init!(baseGeometry baseGeometry: SCNGeometry!, bones bones: [AnyObject]!, boneInverseBindTransforms boneInverseBindTransforms: [AnyObject]!, boneWeights boneWeights: SCNGeometrySource!, boneIndices boneIndices: SCNGeometrySource!) ``` |

Modified SCNTechnique.init(bySequencingTechniques: [AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(bySequencingTechniques techniques: [AnyObject]) -> SCNTechnique ``` |
| To | ``` init?(bySequencingTechniques techniques: [AnyObject]) -> SCNTechnique ``` |

Modified SCNTechnique.init(dictionary: [NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(dictionary dictionary: [NSObject : AnyObject]) -> SCNTechnique ``` |
| To | ``` init?(dictionary dictionary: [NSObject : AnyObject]) -> SCNTechnique ``` |

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
