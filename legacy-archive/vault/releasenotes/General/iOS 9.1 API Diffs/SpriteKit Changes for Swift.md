---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/SpriteKit.html
archived_at: '2026-07-18T02:57:10.960530Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# SpriteKit Changes for Swift

### SpriteKit

Modified [SK3DNode](https://developer.apple.com/documentation/spritekit/sk3dnode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKAction](https://developer.apple.com/documentation/spritekit/skaction)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [SKActionTimingMode [enum]](https://developer.apple.com/documentation/spritekit/skactiontimingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SKAudioNode](https://developer.apple.com/documentation/spritekit/skaudionode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKAudioNode : SKNode {     init(AVAudioNode node: AVAudioNode?)     init?(coder aDecoder: NSCoder)     convenience init(fileNamed name: String)     convenience init(URL url: NSURL)     var avAudioNode: AVAudioNode?     var autoplayLooped: Bool     var positional: Bool } ``` | AnyObject, NSCoding |
| To | ``` class SKAudioNode : SKNode, NSCoding {     init(AVAudioNode node: AVAudioNode?)     init?(coder aDecoder: NSCoder)     convenience init(fileNamed name: String)     convenience init(URL url: NSURL)     var avAudioNode: AVAudioNode?     var autoplayLooped: Bool     var positional: Bool } ``` | NSCoding |

Modified [SKBlendMode [enum]](https://developer.apple.com/documentation/spritekit/skblendmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SKCameraNode](https://developer.apple.com/documentation/spritekit/skcameranode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKConstraint](https://developer.apple.com/documentation/spritekit/skconstraint)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [SKCropNode](https://developer.apple.com/documentation/spritekit/skcropnode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKEffectNode](https://developer.apple.com/documentation/spritekit/skeffectnode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKEmitterNode](https://developer.apple.com/documentation/spritekit/skemitternode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKFieldNode](https://developer.apple.com/documentation/spritekit/skfieldnode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKInterpolationMode [enum]](https://developer.apple.com/documentation/spritekit/skinterpolationmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SKKeyframeSequence](https://developer.apple.com/documentation/spritekit/skkeyframesequence)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [SKLabelHorizontalAlignmentMode [enum]](https://developer.apple.com/documentation/spritekit/sklabelhorizontalalignmentmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SKLabelNode](https://developer.apple.com/documentation/spritekit/sklabelnode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKLabelVerticalAlignmentMode [enum]](https://developer.apple.com/documentation/spritekit/sklabelverticalalignmentmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SKLightNode](https://developer.apple.com/documentation/spritekit/sklightnode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKMutableTexture](https://developer.apple.com/documentation/spritekit/skmutabletexture)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKNode](https://developer.apple.com/documentation/spritekit/sknode)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [SKParticleRenderOrder [enum]](https://developer.apple.com/documentation/spritekit/skparticlerenderorder)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SKPhysicsBody](https://developer.apple.com/documentation/spritekit/skphysicsbody)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [SKPhysicsContact](https://developer.apple.com/documentation/spritekit/skphysicscontact)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKPhysicsJoint](https://developer.apple.com/documentation/spritekit/skphysicsjoint)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [SKPhysicsJointFixed](https://developer.apple.com/documentation/spritekit/skphysicsjointfixed)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKPhysicsJointLimit](https://developer.apple.com/documentation/spritekit/skphysicsjointlimit)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKPhysicsJointPin](https://developer.apple.com/documentation/spritekit/skphysicsjointpin)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKPhysicsJointSliding](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKPhysicsJointSpring](https://developer.apple.com/documentation/spritekit/skphysicsjointspring)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKPhysicsWorld](https://developer.apple.com/documentation/spritekit/skphysicsworld)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [SKRange](https://developer.apple.com/documentation/spritekit/skrange)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [SKReachConstraints](https://developer.apple.com/documentation/spritekit/skreachconstraints)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [SKReferenceNode](https://developer.apple.com/documentation/spritekit/skreferencenode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKRegion](https://developer.apple.com/documentation/spritekit/skregion)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [SKRepeatMode [enum]](https://developer.apple.com/documentation/spritekit/skrepeatmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SKScene](https://developer.apple.com/documentation/spritekit/skscene)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKSceneScaleMode [enum]](https://developer.apple.com/documentation/spritekit/skscenescalemode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SKShader](https://developer.apple.com/documentation/spritekit/skshader)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [SKShapeNode](https://developer.apple.com/documentation/spritekit/skshapenode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKSpriteNode](https://developer.apple.com/documentation/spritekit/skspritenode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKTexture](https://developer.apple.com/documentation/spritekit/sktexture)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [SKTextureAtlas](https://developer.apple.com/documentation/spritekit/sktextureatlas)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [SKTextureFilteringMode [enum]](https://developer.apple.com/documentation/spritekit/sktexturefilteringmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SKTransition](https://developer.apple.com/documentation/spritekit/sktransition)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [SKTransitionDirection [enum]](https://developer.apple.com/documentation/spritekit/sktransitiondirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SKUniform](https://developer.apple.com/documentation/spritekit/skuniform)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [SKUniformType [enum]](https://developer.apple.com/documentation/spritekit/skuniformtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SKVideoNode](https://developer.apple.com/documentation/spritekit/skvideonode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKView](https://developer.apple.com/documentation/spritekit/skview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

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
