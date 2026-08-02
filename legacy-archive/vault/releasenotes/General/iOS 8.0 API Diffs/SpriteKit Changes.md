---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/SpriteKit.html
archived_at: '2026-07-18T02:56:00.979672Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# SpriteKit Changes

## SpriteKit

SK3DNode.h (Added)Added [SK3DNode](https://developer.apple.com/documentation/spritekit/sk3dnode)Added [SK3DNode.autoenablesDefaultLighting](https://developer.apple.com/documentation/spritekit/sk3dnode/1519676-autoenablesdefaultlighting)Added [-[SK3DNode hitTest:options:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1519782-hittest)Added [-[SK3DNode initWithViewportSize:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1519708-init)Added [SK3DNode.loops](https://developer.apple.com/documentation/spritekit/sk3dnode/1519549-loops)Added [+[SK3DNode nodeWithViewportSize:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1537481-nodewithviewportsize)Added [SK3DNode.playing](https://developer.apple.com/documentation/spritekit/sk3dnode/1520297-isplaying)Added [SK3DNode.pointOfView](https://developer.apple.com/documentation/spritekit/sk3dnode/1519786-pointofview)Added [-[SK3DNode projectPoint:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1520400-projectpoint)Added [SK3DNode.sceneTime](https://developer.apple.com/documentation/spritekit/sk3dnode/1519738-scenetime)Added [SK3DNode.scnScene](https://developer.apple.com/documentation/spritekit/sk3dnode/1519834-scnscene)Added [-[SK3DNode unprojectPoint:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1520024-unprojectpoint)Added [SK3DNode.viewportSize](https://developer.apple.com/documentation/spritekit/sk3dnode/1520078-viewportsize)SKAction.hAdded [+[SKAction falloffBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417766-falloffby)Added [+[SKAction falloffTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417758-falloff)Added [+[SKAction followPath:asOffset:orientToPath:speed:]](https://developer.apple.com/documentation/spritekit/skaction/1417798-followpath)Added [+[SKAction followPath:speed:]](https://developer.apple.com/documentation/spritekit/skaction/1417786-follow)Added [+[SKAction hide]](https://developer.apple.com/documentation/spritekit/skaction/1417704-hide)Added [+[SKAction reachTo:rootNode:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417773-reachto)Added [+[SKAction reachTo:rootNode:velocity:]](https://developer.apple.com/documentation/spritekit/skaction/1417720-reachto)Added [+[SKAction reachToNode:rootNode:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417827-reachtonode)Added [+[SKAction reachToNode:rootNode:velocity:]](https://developer.apple.com/documentation/spritekit/skaction/1417801-reach)Added [+[SKAction strengthBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417762-strengthby)Added [+[SKAction strengthTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417815-strengthto)Added [SKAction.timingFunction](https://developer.apple.com/documentation/spritekit/skaction/1417666-timingfunction)Added [+[SKAction unhide]](https://developer.apple.com/documentation/spritekit/skaction/1417660-unhide)Added [SKActionTimingFunction](https://developer.apple.com/documentation/spritekit/skactiontimingfunction)SKConstraint.h (Added)Added [SKConstraint](https://developer.apple.com/documentation/spritekit/skconstraint)Added [+[SKConstraint distance:toNode:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519750-distance)Added [+[SKConstraint distance:toPoint:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519688-distance)Added [+[SKConstraint distance:toPoint:inNode:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519746-distance)Added [SKConstraint.enabled](https://developer.apple.com/documentation/spritekit/skconstraint/1519669-enabled)Added [+[SKConstraint orientToNode:offset:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519744-orienttonode)Added [+[SKConstraint orientToPoint:inNode:offset:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519627-orienttopoint)Added [+[SKConstraint orientToPoint:offset:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519686-orienttopoint)Added [+[SKConstraint positionX:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519716-positionx)Added [+[SKConstraint positionX:Y:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519760-positionx)Added [+[SKConstraint positionY:]](https://developer.apple.com/documentation/spritekit/skconstraint/1520356-positiony)Added [SKConstraint.referenceNode](https://developer.apple.com/documentation/spritekit/skconstraint/1520369-referencenode)Added [+[SKConstraint zRotation:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519706-zrotation)Added [SKRange](https://developer.apple.com/documentation/spritekit/skrange)Added [-[SKRange initWithLowerLimit:upperLimit:]](https://developer.apple.com/documentation/spritekit/skrange/1520307-init)Added [SKRange.lowerLimit](https://developer.apple.com/documentation/spritekit/skrange/1520000-lowerlimit)Added [+[SKRange rangeWithConstantValue:]](https://developer.apple.com/documentation/spritekit/skrange/1520276-rangewithconstantvalue)Added [+[SKRange rangeWithLowerLimit:]](https://developer.apple.com/documentation/spritekit/skrange/1520137-rangewithlowerlimit)Added [+[SKRange rangeWithLowerLimit:upperLimit:]](https://developer.apple.com/documentation/spritekit/skrange/1534324-rangewithlowerlimit)Added [+[SKRange rangeWithNoLimits]](https://developer.apple.com/documentation/spritekit/skrange/1519920-withnolimits)Added [+[SKRange rangeWithUpperLimit:]](https://developer.apple.com/documentation/spritekit/skrange/1519559-rangewithupperlimit)Added [+[SKRange rangeWithValue:variance:]](https://developer.apple.com/documentation/spritekit/skrange/1519842-init)Added [SKRange.upperLimit](https://developer.apple.com/documentation/spritekit/skrange/1519596-upperlimit)SKCropNode.hModified [SKCropNode.maskNode](https://developer.apple.com/documentation/spritekit/skcropnode/1520449-masknode)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) SKNode *maskNode ``` |
| To | ``` @property(nonatomic, retain) SKNode *maskNode ``` |

SKEffectNode.hAdded [SKEffectNode.shader](https://developer.apple.com/documentation/spritekit/skeffectnode/1459388-shader)Modified [SKEffectNode.filter](https://developer.apple.com/documentation/spritekit/skeffectnode/1459392-filter)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) CIFilter *filter ``` |
| To | ``` @property(nonatomic, retain) CIFilter *filter ``` |

SKEmitterNode.hAdded [SKEmitterNode.fieldBitMask](https://developer.apple.com/documentation/spritekit/skemitternode/1398006-fieldbitmask)Added [SKEmitterNode.particleZPositionSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398008-particlezpositionspeed)Added [SKEmitterNode.shader](https://developer.apple.com/documentation/spritekit/skemitternode/1398069-shader)Modified [SKEmitterNode.particleAction](https://developer.apple.com/documentation/spritekit/skemitternode/1397970-particleaction)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, nonatomic) SKAction *particleAction ``` |
| To | ``` @property(nonatomic, copy) SKAction *particleAction ``` |

Modified [SKEmitterNode.particleAlphaSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1398057-particlealphasequence)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) SKKeyframeSequence *particleAlphaSequence ``` |
| To | ``` @property(nonatomic, retain) SKKeyframeSequence *particleAlphaSequence ``` |

Modified [SKEmitterNode.particleColor](https://developer.apple.com/documentation/spritekit/skemitternode/1398049-particlecolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) UIColor *particleColor ``` |
| To | ``` @property(nonatomic, retain) UIColor *particleColor ``` |

Modified [SKEmitterNode.particleColorBlendFactorSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1397980-particlecolorblendfactorsequence)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) SKKeyframeSequence *particleColorBlendFactorSequence ``` |
| To | ``` @property(nonatomic, retain) SKKeyframeSequence *particleColorBlendFactorSequence ``` |

Modified [SKEmitterNode.particleColorSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1397992-particlecolorsequence)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) SKKeyframeSequence *particleColorSequence ``` |
| To | ``` @property(nonatomic, retain) SKKeyframeSequence *particleColorSequence ``` |

Modified [SKEmitterNode.particleScaleSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1398029-particlescalesequence)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) SKKeyframeSequence *particleScaleSequence ``` |
| To | ``` @property(nonatomic, retain) SKKeyframeSequence *particleScaleSequence ``` |

Modified [SKEmitterNode.particleTexture](https://developer.apple.com/documentation/spritekit/skemitternode/1398004-particletexture)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) SKTexture *particleTexture ``` |
| To | ``` @property(nonatomic, retain) SKTexture *particleTexture ``` |

Modified [SKEmitterNode.targetNode](https://developer.apple.com/documentation/spritekit/skemitternode/1398012-targetnode)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, nonatomic) SKNode *targetNode ``` |
| To | ``` @property(nonatomic, weak) SKNode *targetNode ``` |

SKFieldNode.h (Added)Added [SKFieldNode](https://developer.apple.com/documentation/spritekit/skfieldnode)Added [SKFieldNode.animationSpeed](https://developer.apple.com/documentation/spritekit/skfieldnode/1519822-animationspeed)Added [SKFieldNode.categoryBitMask](https://developer.apple.com/documentation/spritekit/skfieldnode/1520143-categorybitmask)Added [+[SKFieldNode customFieldWithEvaluationBlock:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519710-customfieldwithevaluationblock)Added [SKFieldNode.direction](https://developer.apple.com/documentation/spritekit/skfieldnode/1520091-direction)Added [+[SKFieldNode dragField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520225-dragfield)Added [+[SKFieldNode electricField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520396-electricfield)Added [SKFieldNode.enabled](https://developer.apple.com/documentation/spritekit/skfieldnode/1520079-isenabled)Added [SKFieldNode.exclusive](https://developer.apple.com/documentation/spritekit/skfieldnode/1520365-exclusive)Added [SKFieldNode.falloff](https://developer.apple.com/documentation/spritekit/skfieldnode/1520445-falloff)Added [+[SKFieldNode linearGravityFieldWithVector:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520145-lineargravityfield)Added [+[SKFieldNode magneticField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520134-magneticfield)Added [SKFieldNode.minimumRadius](https://developer.apple.com/documentation/spritekit/skfieldnode/1519804-minimumradius)Added [+[SKFieldNode noiseFieldWithSmoothness:animationSpeed:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519947-noisefieldwithsmoothness)Added [+[SKFieldNode radialGravityField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520382-radialgravityfield)Added [SKFieldNode.region](https://developer.apple.com/documentation/spritekit/skfieldnode/1519551-region)Added [SKFieldNode.smoothness](https://developer.apple.com/documentation/spritekit/skfieldnode/1520273-smoothness)Added [+[SKFieldNode springField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519694-springfield)Added [SKFieldNode.strength](https://developer.apple.com/documentation/spritekit/skfieldnode/1520152-strength)Added [SKFieldNode.texture](https://developer.apple.com/documentation/spritekit/skfieldnode/1519928-texture)Added [+[SKFieldNode turbulenceFieldWithSmoothness:animationSpeed:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520018-turbulencefieldwithsmoothness)Added [+[SKFieldNode velocityFieldWithTexture:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519778-velocityfieldwithtexture)Added [+[SKFieldNode velocityFieldWithVector:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520271-velocityfieldwithvector)Added [+[SKFieldNode vortexField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520157-vortexfield)Added [SKFieldForceEvaluator](https://developer.apple.com/documentation/spritekit/skfieldforceevaluator)SKLabelNode.hAdded [+[SKLabelNode labelNodeWithText:]](https://developer.apple.com/documentation/spritekit/sklabelnode/1519612-labelnodewithtext)Modified [SKLabelNode.color](https://developer.apple.com/documentation/spritekit/sklabelnode/1519938-color)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) UIColor *color ``` |
| To | ``` @property(nonatomic, retain) UIColor *color ``` |

Modified [SKLabelNode.fontColor](https://developer.apple.com/documentation/spritekit/sklabelnode/1520057-fontcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) UIColor *fontColor ``` |
| To | ``` @property(nonatomic, retain) UIColor *fontColor ``` |

Modified [SKLabelNode.fontName](https://developer.apple.com/documentation/spritekit/sklabelnode/1520129-fontname)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, nonatomic) NSString *fontName ``` |
| To | ``` @property(nonatomic, copy) NSString *fontName ``` |

Modified [SKLabelNode.text](https://developer.apple.com/documentation/spritekit/sklabelnode/1519788-text)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, nonatomic) NSString *text ``` |
| To | ``` @property(nonatomic, copy) NSString *text ``` |

SKLightNode.h (Added)Added [SKLightNode](https://developer.apple.com/documentation/spritekit/sklightnode)Added [SKLightNode.ambientColor](https://developer.apple.com/documentation/spritekit/sklightnode/1520139-ambientcolor)Added [SKLightNode.categoryBitMask](https://developer.apple.com/documentation/spritekit/sklightnode/1519940-categorybitmask)Added [SKLightNode.enabled](https://developer.apple.com/documentation/spritekit/sklightnode/1519826-enabled)Added [SKLightNode.falloff](https://developer.apple.com/documentation/spritekit/sklightnode/1519776-falloff)Added [SKLightNode.lightColor](https://developer.apple.com/documentation/spritekit/sklightnode/1520244-lightcolor)Added [SKLightNode.shadowColor](https://developer.apple.com/documentation/spritekit/sklightnode/1519844-shadowcolor)SKMutableTexture.h (Added)Added [SKMutableTexture](https://developer.apple.com/documentation/spritekit/skmutabletexture)Added [-[SKMutableTexture initWithSize:]](https://developer.apple.com/documentation/spritekit/skmutabletexture/1397883-init)Added [-[SKMutableTexture initWithSize:pixelFormat:]](https://developer.apple.com/documentation/spritekit/skmutabletexture/1397879-init)Added [-[SKMutableTexture modifyPixelDataWithBlock:]](https://developer.apple.com/documentation/spritekit/skmutabletexture/1397881-modifypixeldatawithblock)Added [+[SKMutableTexture mutableTextureWithSize:]](https://developer.apple.com/documentation/spritekit/skmutabletexture/1397874-mutabletexturewithsize)SKNode.hAdded [SKNode.constraints](https://developer.apple.com/documentation/spritekit/sknode/1483124-constraints)Added [-[SKNode init]](https://developer.apple.com/documentation/spritekit/sknode/1483097-init)Added [+[SKNode nodeWithFileNamed:]](https://developer.apple.com/documentation/spritekit/sknode/1483083-init)Added [-[SKNode objectForKeyedSubscript:]](https://developer.apple.com/documentation/spritekit/sknode/1483070-subscript)Added [SKNode.reachConstraints](https://developer.apple.com/documentation/spritekit/sknode/1483019-reachconstraints)Modified [SKNode.children](https://developer.apple.com/documentation/spritekit/sknode/1483028-children)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *children ``` |
| To | ``` @property(nonatomic, readonly) NSArray *children ``` |

Modified [SKNode.frame](https://developer.apple.com/documentation/spritekit/sknode/1483026-frame)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CGRect frame ``` |
| To | ``` @property(nonatomic, readonly) CGRect frame ``` |

Modified [SKNode.hidden](https://developer.apple.com/documentation/spritekit/sknode/1483048-hidden)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isHidden, nonatomic) BOOL hidden ``` |
| To | ``` @property(nonatomic, getter=isHidden) BOOL hidden ``` |

Modified [SKNode.name](https://developer.apple.com/documentation/spritekit/sknode/1483136-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, nonatomic) NSString *name ``` |
| To | ``` @property(nonatomic, copy) NSString *name ``` |

Modified [SKNode.parent](https://developer.apple.com/documentation/spritekit/sknode/1483080-parent)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) SKNode *parent ``` |
| To | ``` @property(nonatomic, readonly) SKNode *parent ``` |

Modified [SKNode.paused](https://developer.apple.com/documentation/spritekit/sknode/1483113-paused)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isPaused, nonatomic) BOOL paused ``` |
| To | ``` @property(nonatomic, getter=isPaused) BOOL paused ``` |

Modified [SKNode.physicsBody](https://developer.apple.com/documentation/spritekit/sknode/1483117-physicsbody)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) SKPhysicsBody *physicsBody ``` |
| To | ``` @property(nonatomic, retain) SKPhysicsBody *physicsBody ``` |

Modified [SKNode.scene](https://developer.apple.com/documentation/spritekit/sknode/1483064-scene)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) SKScene *scene ``` |
| To | ``` @property(nonatomic, readonly) SKScene *scene ``` |

Modified [SKNode.userData](https://developer.apple.com/documentation/spritekit/sknode/1483121-userdata)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) NSMutableDictionary *userData ``` |
| To | ``` @property(nonatomic, retain) NSMutableDictionary *userData ``` |

Modified [SKNode.userInteractionEnabled](https://developer.apple.com/documentation/spritekit/sknode/1483109-userinteractionenabled)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isUserInteractionEnabled) BOOL userInteractionEnabled ``` |
| To | ``` @property(nonatomic, getter=isUserInteractionEnabled) BOOL userInteractionEnabled ``` |

SKPhysicsBody.hAdded [+[SKPhysicsBody bodyWithTexture:alphaThreshold:size:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519689-bodywithtexture)Added [+[SKPhysicsBody bodyWithTexture:size:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519690-bodywithtexture)Added [SKPhysicsBody.charge](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519881-charge)Added [SKPhysicsBody.fieldBitMask](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520280-fieldbitmask)Added [SKPhysicsBody.pinned](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520354-pinned)Modified [SKPhysicsBody.affectedByGravity](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519774-affectedbygravity)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) BOOL affectedByGravity ``` |
| To | ``` @property(nonatomic, assign) BOOL affectedByGravity ``` |

Modified [SKPhysicsBody.angularDamping](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519913-angulardamping)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) CGFloat angularDamping ``` |
| To | ``` @property(nonatomic, assign) CGFloat angularDamping ``` |

Modified [SKPhysicsBody.area](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520034-area)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CGFloat area ``` |
| To | ``` @property(nonatomic, readonly) CGFloat area ``` |

Modified [SKPhysicsBody.categoryBitMask](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519869-categorybitmask)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) uint32_t categoryBitMask ``` |
| To | ``` @property(nonatomic, assign) uint32_t categoryBitMask ``` |

Modified [SKPhysicsBody.collisionBitMask](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520003-collisionbitmask)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) uint32_t collisionBitMask ``` |
| To | ``` @property(nonatomic, assign) uint32_t collisionBitMask ``` |

Modified [SKPhysicsBody.contactTestBitMask](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519781-contacttestbitmask)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) uint32_t contactTestBitMask ``` |
| To | ``` @property(nonatomic, assign) uint32_t contactTestBitMask ``` |

Modified [SKPhysicsBody.dynamic](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520132-isdynamic)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isDynamic, nonatomic) BOOL dynamic ``` |
| To | ``` @property(nonatomic, getter=isDynamic) BOOL dynamic ``` |

Modified [SKPhysicsBody.joints](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519849-joints)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *joints ``` |
| To | ``` @property(nonatomic, readonly) NSArray *joints ``` |

Modified [SKPhysicsBody.linearDamping](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519796-lineardamping)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) CGFloat linearDamping ``` |
| To | ``` @property(nonatomic, assign) CGFloat linearDamping ``` |

Modified [SKPhysicsBody.node](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520049-node)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, weak, nonatomic) SKNode *node ``` |
| To | ``` @property(nonatomic, readonly, weak) SKNode *node ``` |

Modified [SKPhysicsBody.resting](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520256-resting)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isResting, nonatomic) BOOL resting ``` |
| To | ``` @property(nonatomic, getter=isResting) BOOL resting ``` |

SKPhysicsContact.hAdded [SKPhysicsContact.contactNormal](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478528-contactnormal)Modified [SKPhysicsContact.bodyA](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478533-bodya)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) SKPhysicsBody *bodyA ``` |
| To | ``` @property(nonatomic, readonly) SKPhysicsBody *bodyA ``` |

Modified [SKPhysicsContact.bodyB](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478526-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) SKPhysicsBody *bodyB ``` |
| To | ``` @property(nonatomic, readonly) SKPhysicsBody *bodyB ``` |

Modified [SKPhysicsContact.collisionImpulse](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478523-collisionimpulse)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CGFloat collisionImpulse ``` |
| To | ``` @property(nonatomic, readonly) CGFloat collisionImpulse ``` |

Modified [SKPhysicsContact.contactPoint](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478524-contactpoint)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CGPoint contactPoint ``` |
| To | ``` @property(nonatomic, readonly) CGPoint contactPoint ``` |

SKPhysicsJoint.hAdded [SKPhysicsJoint.reactionForce](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1519866-reactionforce)Added [SKPhysicsJoint.reactionTorque](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1519682-reactiontorque)Added [SKPhysicsJointPin.rotationSpeed](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1520259-rotationspeed)Modified [SKPhysicsJoint.bodyA](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1520403-bodya)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) SKPhysicsBody *bodyA ``` |
| To | ``` @property(nonatomic, retain) SKPhysicsBody *bodyA ``` |

Modified [SKPhysicsJoint.bodyB](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1519693-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) SKPhysicsBody *bodyB ``` |
| To | ``` @property(nonatomic, retain) SKPhysicsBody *bodyB ``` |

SKPhysicsWorld.hAdded [-[SKPhysicsWorld sampleFieldsAt:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449627-samplefieldsat)Modified [-[SKPhysicsContactDelegate didBeginContact:]](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate/1449595-didbegin)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[SKPhysicsContactDelegate didEndContact:]](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate/1449599-didendcontact)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [SKPhysicsWorld.contactDelegate](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449602-contactdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) id<SKPhysicsContactDelegate> contactDelegate ``` |
| To | ``` @property(nonatomic, assign) id<SKPhysicsContactDelegate> contactDelegate ``` |

SKReachConstraints.h (Added)Added [SKReachConstraints](https://developer.apple.com/documentation/spritekit/skreachconstraints)Added [-[SKReachConstraints initWithLowerAngleLimit:upperAngleLimit:]](https://developer.apple.com/documentation/spritekit/skreachconstraints/1520170-initwithloweranglelimit)Added [SKReachConstraints.lowerAngleLimit](https://developer.apple.com/documentation/spritekit/skreachconstraints/1519923-loweranglelimit)Added [SKReachConstraints.upperAngleLimit](https://developer.apple.com/documentation/spritekit/skreachconstraints/1519699-upperanglelimit)SKRegion.h (Added)Added [SKRegion](https://developer.apple.com/documentation/spritekit/skregion)Added [-[SKRegion containsPoint:]](https://developer.apple.com/documentation/spritekit/skregion/1519695-containspoint)Added [+[SKRegion infiniteRegion]](https://developer.apple.com/documentation/spritekit/skregion/1520061-infinite)Added [-[SKRegion initWithPath:]](https://developer.apple.com/documentation/spritekit/skregion/1519857-initwithpath)Added [-[SKRegion initWithRadius:]](https://developer.apple.com/documentation/spritekit/skregion/1520219-init)Added [-[SKRegion initWithSize:]](https://developer.apple.com/documentation/spritekit/skregion/1520385-initwithsize)Added [-[SKRegion inverseRegion]](https://developer.apple.com/documentation/spritekit/skregion/1519700-inverse)Added [SKRegion.path](https://developer.apple.com/documentation/spritekit/skregion/1520042-path)Added [-[SKRegion regionByDifferenceFromRegion:]](https://developer.apple.com/documentation/spritekit/skregion/1519879-bydifference)Added [-[SKRegion regionByIntersectionWithRegion:]](https://developer.apple.com/documentation/spritekit/skregion/1519646-regionbyintersectionwithregion)Added [-[SKRegion regionByUnionWithRegion:]](https://developer.apple.com/documentation/spritekit/skregion/1519702-regionbyunionwithregion)SKScene.hAdded [SKScene.delegate](https://developer.apple.com/documentation/spritekit/skscene/1520213-delegate)Added [-[SKScene didApplyConstraints]](https://developer.apple.com/documentation/spritekit/skscene/1520006-didapplyconstraints)Added [-[SKScene didFinishUpdate]](https://developer.apple.com/documentation/spritekit/skscene/1520269-didfinishupdate)Added [SKSceneDelegate](https://developer.apple.com/documentation/spritekit/skscenedelegate)Added [-[SKSceneDelegate didApplyConstraintsForScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1520375-didapplyconstraintsforscene)Added [-[SKSceneDelegate didEvaluateActionsForScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1520071-didevaluateactions)Added [-[SKSceneDelegate didFinishUpdateForScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1519814-didfinishupdate)Added [-[SKSceneDelegate didSimulatePhysicsForScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1520392-didsimulatephysicsforscene)Added [-[SKSceneDelegate update:forScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1519757-update)Modified [SKScene.backgroundColor](https://developer.apple.com/documentation/spritekit/skscene/1520278-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) UIColor *backgroundColor ``` |
| To | ``` @property(nonatomic, retain) UIColor *backgroundColor ``` |

Modified [SKScene.physicsWorld](https://developer.apple.com/documentation/spritekit/skscene/1519584-physicsworld)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) SKPhysicsWorld *physicsWorld ``` |
| To | ``` @property(nonatomic, readonly) SKPhysicsWorld *physicsWorld ``` |

Modified [SKScene.view](https://developer.apple.com/documentation/spritekit/skscene/1519726-view)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, readonly, nonatomic) SKView *view ``` |
| To | ``` @property(nonatomic, weak, readonly) SKView *view ``` |

SKShader.h (Added)Added [SKShader](https://developer.apple.com/documentation/spritekit/skshader)Added [-[SKShader addUniform:]](https://developer.apple.com/documentation/spritekit/skshader/1477561-adduniform)Added [-[SKShader initWithSource:]](https://developer.apple.com/documentation/spritekit/skshader/1477571-initwithsource)Added [-[SKShader initWithSource:uniforms:]](https://developer.apple.com/documentation/spritekit/skshader/1477555-initwithsource)Added [-[SKShader removeUniformNamed:]](https://developer.apple.com/documentation/spritekit/skshader/1477553-removeuniformnamed)Added [+[SKShader shader]](https://developer.apple.com/documentation/spritekit/skshader/1477559-shader)Added [+[SKShader shaderWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skshader/1477557-shaderwithfilenamed)Added [+[SKShader shaderWithSource:]](https://developer.apple.com/documentation/spritekit/skshader/1477563-shaderwithsource)Added [+[SKShader shaderWithSource:uniforms:]](https://developer.apple.com/documentation/spritekit/skshader/1477569-shaderwithsource)Added [SKShader.source](https://developer.apple.com/documentation/spritekit/skshader/1477544-source)Added [-[SKShader uniformNamed:]](https://developer.apple.com/documentation/spritekit/skshader/1477567-uniformnamed)Added [SKShader.uniforms](https://developer.apple.com/documentation/spritekit/skshader/1477565-uniforms)SKShapeNode.hAdded [SKShapeNode.fillShader](https://developer.apple.com/documentation/spritekit/skshapenode/1519629-fillshader)Added [SKShapeNode.fillTexture](https://developer.apple.com/documentation/spritekit/skshapenode/1519956-filltexture)Added [SKShapeNode.lineCap](https://developer.apple.com/documentation/spritekit/skshapenode/1520360-linecap)Added [SKShapeNode.lineJoin](https://developer.apple.com/documentation/spritekit/skshapenode/1520358-linejoin)Added [SKShapeNode.lineLength](https://developer.apple.com/documentation/spritekit/skshapenode/1520398-linelength)Added [SKShapeNode.miterLimit](https://developer.apple.com/documentation/spritekit/skshapenode/1520240-miterlimit)Added [+[SKShapeNode shapeNodeWithCircleOfRadius:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519570-shapenodewithcircleofradius)Added [+[SKShapeNode shapeNodeWithEllipseInRect:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520412-shapenodewithellipseinrect)Added [+[SKShapeNode shapeNodeWithEllipseOfSize:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519980-init)Added [+[SKShapeNode shapeNodeWithPath:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520022-shapenodewithpath)Added [+[SKShapeNode shapeNodeWithPath:centered:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519649-init)Added [+[SKShapeNode shapeNodeWithPoints:count:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520120-shapenodewithpoints)Added [+[SKShapeNode shapeNodeWithRect:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520047-init)Added [+[SKShapeNode shapeNodeWithRect:cornerRadius:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519769-init)Added [+[SKShapeNode shapeNodeWithRectOfSize:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520147-init)Added [+[SKShapeNode shapeNodeWithRectOfSize:cornerRadius:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519712-init)Added [+[SKShapeNode shapeNodeWithSplinePoints:count:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520140-init)Added [SKShapeNode.strokeShader](https://developer.apple.com/documentation/spritekit/skshapenode/1519784-strokeshader)Added [SKShapeNode.strokeTexture](https://developer.apple.com/documentation/spritekit/skshapenode/1519824-stroketexture)Modified [SKShapeNode.antialiased](https://developer.apple.com/documentation/spritekit/skshapenode/1519719-antialiased)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isAntialiased, nonatomic) BOOL antialiased ``` |
| To | ``` @property(nonatomic, getter=isAntialiased) BOOL antialiased ``` |

Modified [SKShapeNode.fillColor](https://developer.apple.com/documentation/spritekit/skshapenode/1520154-fillcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) UIColor *fillColor ``` |
| To | ``` @property(nonatomic, retain) UIColor *fillColor ``` |

Modified [SKShapeNode.strokeColor](https://developer.apple.com/documentation/spritekit/skshapenode/1519748-strokecolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) UIColor *strokeColor ``` |
| To | ``` @property(nonatomic, retain) UIColor *strokeColor ``` |

SKSpriteNode.hAdded [SKSpriteNode.lightingBitMask](https://developer.apple.com/documentation/spritekit/skspritenode/1519637-lightingbitmask)Added [SKSpriteNode.normalTexture](https://developer.apple.com/documentation/spritekit/skspritenode/1519657-normaltexture)Added [SKSpriteNode.shader](https://developer.apple.com/documentation/spritekit/skspritenode/1519714-shader)Added [SKSpriteNode.shadowCastBitMask](https://developer.apple.com/documentation/spritekit/skspritenode/1520325-shadowcastbitmask)Added [SKSpriteNode.shadowedBitMask](https://developer.apple.com/documentation/spritekit/skspritenode/1519974-shadowedbitmask)Added [+[SKSpriteNode spriteNodeWithImageNamed:normalMapped:]](https://developer.apple.com/documentation/spritekit/skspritenode/1519721-init)Added [+[SKSpriteNode spriteNodeWithTexture:normalMap:]](https://developer.apple.com/documentation/spritekit/skspritenode/1520153-spritenodewithtexture)Modified [SKSpriteNode.color](https://developer.apple.com/documentation/spritekit/skspritenode/1519639-color)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) UIColor *color ``` |
| To | ``` @property(nonatomic, retain) UIColor *color ``` |

Modified [SKSpriteNode.texture](https://developer.apple.com/documentation/spritekit/skspritenode/1520011-texture)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) SKTexture *texture ``` |
| To | ``` @property(nonatomic, retain) SKTexture *texture ``` |

SKTexture.hAdded [-[SKTexture textureByGeneratingNormalMap]](https://developer.apple.com/documentation/spritekit/sktexture/1519687-texturebygeneratingnormalmap)Added [-[SKTexture textureByGeneratingNormalMapWithSmoothness:contrast:]](https://developer.apple.com/documentation/spritekit/sktexture/1520441-texturebygeneratingnormalmapwith)Added [+[SKTexture textureNoiseWithSmoothness:size:grayscale:]](https://developer.apple.com/documentation/spritekit/sktexture/1519971-texturenoisewithsmoothness)Added [+[SKTexture textureVectorNoiseWithSmoothness:size:]](https://developer.apple.com/documentation/spritekit/sktexture/1520393-texturevectornoisewithsmoothness)Added [+[SKTexture textureWithData:size:flipped:]](https://developer.apple.com/documentation/spritekit/sktexture/1519674-texturewithdata)Modified [-[SKTexture textureByApplyingCIFilter:]](https://developer.apple.com/documentation/spritekit/sktexture/1520388-texturebyapplyingcifilter)

|  | Declaration |
| --- | --- |
| From | ``` - (SKTexture *)textureByApplyingCIFilter:(CIFilter *)filter ``` |
| To | ``` - (instancetype)textureByApplyingCIFilter:(CIFilter *)filter ``` |

Modified [+[SKTexture textureWithCGImage:]](https://developer.apple.com/documentation/spritekit/sktexture/1519576-init)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTexture *)textureWithCGImage:(CGImageRef)image ``` |
| To | ``` + (instancetype)textureWithCGImage:(CGImageRef)image ``` |

Modified [+[SKTexture textureWithData:size:]](https://developer.apple.com/documentation/spritekit/sktexture/1519962-texturewithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTexture *)textureWithData:(NSData *)pixelData size:(CGSize)size ``` |
| To | ``` + (instancetype)textureWithData:(NSData *)pixelData size:(CGSize)size ``` |

Modified [+[SKTexture textureWithData:size:rowLength:alignment:]](https://developer.apple.com/documentation/spritekit/sktexture/1520181-texturewithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTexture *)textureWithData:(NSData *)pixelData size:(CGSize)size rowLength:(unsigned int)rowLength alignment:(unsigned int)alignment ``` |
| To | ``` + (instancetype)textureWithData:(NSData *)pixelData size:(CGSize)size rowLength:(unsigned int)rowLength alignment:(unsigned int)alignment ``` |

Modified [+[SKTexture textureWithImage:]](https://developer.apple.com/documentation/spritekit/sktexture/1520136-init)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTexture *)textureWithImage:(UIImage *)image ``` |
| To | ``` + (instancetype)textureWithImage:(UIImage *)image ``` |

Modified [+[SKTexture textureWithImageNamed:]](https://developer.apple.com/documentation/spritekit/sktexture/1520086-texturewithimagenamed)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTexture *)textureWithImageNamed:(NSString *)name ``` |
| To | ``` + (instancetype)textureWithImageNamed:(NSString *)name ``` |

Modified [+[SKTexture textureWithRect:inTexture:]](https://developer.apple.com/documentation/spritekit/sktexture/1520425-texturewithrect)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTexture *)textureWithRect:(CGRect)rect inTexture:(SKTexture *)texture ``` |
| To | ``` + (instancetype)textureWithRect:(CGRect)rect inTexture:(SKTexture *)texture ``` |

SKTextureAtlas.hAdded [+[SKTextureAtlas atlasWithDictionary:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427383-atlaswithdictionary)Modified [+[SKTextureAtlas atlasNamed:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427381-atlasnamed)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTextureAtlas *)atlasNamed:(NSString *)name ``` |
| To | ``` + (instancetype)atlasNamed:(NSString *)name ``` |

Modified [SKTextureAtlas.textureNames](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427373-texturenames)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *textureNames ``` |
| To | ``` @property(nonatomic, readonly) NSArray *textureNames ``` |

SKUniform.h (Added)Added [SKUniform](https://developer.apple.com/documentation/spritekit/skuniform)Added [SKUniform.floatMatrix2Value](https://developer.apple.com/documentation/spritekit/skuniform/1455410-floatmatrix2value)Added [SKUniform.floatMatrix3Value](https://developer.apple.com/documentation/spritekit/skuniform/1455438-floatmatrix3value)Added [SKUniform.floatMatrix4Value](https://developer.apple.com/documentation/spritekit/skuniform/1455460-floatmatrix4value)Added [SKUniform.floatValue](https://developer.apple.com/documentation/spritekit/skuniform/1455406-floatvalue)Added [SKUniform.floatVector2Value](https://developer.apple.com/documentation/spritekit/skuniform/1455436-floatvector2value)Added [SKUniform.floatVector3Value](https://developer.apple.com/documentation/spritekit/skuniform/1455434-floatvector3value)Added [SKUniform.floatVector4Value](https://developer.apple.com/documentation/spritekit/skuniform/1455404-floatvector4value)Added [-[SKUniform initWithName:]](https://developer.apple.com/documentation/spritekit/skuniform/1455420-initwithname)Added [-[SKUniform initWithName:float:]](https://developer.apple.com/documentation/spritekit/skuniform/1455447-init)Added [-[SKUniform initWithName:floatMatrix2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455431-initwithname)Added [-[SKUniform initWithName:floatMatrix3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455462-init)Added [-[SKUniform initWithName:floatMatrix4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455429-init)Added [-[SKUniform initWithName:floatVector2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455444-initwithname)Added [-[SKUniform initWithName:floatVector3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455416-initwithname)Added [-[SKUniform initWithName:floatVector4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455418-initwithname)Added [-[SKUniform initWithName:texture:]](https://developer.apple.com/documentation/spritekit/skuniform/1455452-init)Added [SKUniform.name](https://developer.apple.com/documentation/spritekit/skuniform/1455442-name)Added [SKUniform.textureValue](https://developer.apple.com/documentation/spritekit/skuniform/1455449-texturevalue)Added [SKUniform.uniformType](https://developer.apple.com/documentation/spritekit/skuniform/1455440-uniformtype)Added [+[SKUniform uniformWithName:]](https://developer.apple.com/documentation/spritekit/skuniform/1455458-uniformwithname)Added [+[SKUniform uniformWithName:float:]](https://developer.apple.com/documentation/spritekit/skuniform/1455412-uniformwithname)Added [+[SKUniform uniformWithName:floatMatrix2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455463-uniformwithname)Added [+[SKUniform uniformWithName:floatMatrix3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455402-uniformwithname)Added [+[SKUniform uniformWithName:floatMatrix4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455446-uniformwithname)Added [+[SKUniform uniformWithName:floatVector2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455472-uniformwithname)Added [+[SKUniform uniformWithName:floatVector3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455414-uniformwithname)Added [+[SKUniform uniformWithName:floatVector4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455465-uniformwithname)Added [+[SKUniform uniformWithName:texture:]](https://developer.apple.com/documentation/spritekit/skuniform/1455470-uniformwithname)Added [SKUniformType](https://developer.apple.com/documentation/spritekit/skuniformtype)Added [SKUniformTypeFloat](https://developer.apple.com/documentation/spritekit/skuniformtype/float)Added [SKUniformTypeFloatMatrix2](https://developer.apple.com/documentation/spritekit/skuniformtype/floatmatrix2)Added [SKUniformTypeFloatMatrix3](https://developer.apple.com/documentation/spritekit/skuniformtype/floatmatrix3)Added [SKUniformTypeFloatMatrix4](https://developer.apple.com/documentation/spritekit/skuniformtype/floatmatrix4)Added [SKUniformTypeFloatVector2](https://developer.apple.com/documentation/spritekit/skuniformtype/skuniformtypefloatvector2)Added [SKUniformTypeFloatVector3](https://developer.apple.com/documentation/spritekit/skuniformtype/floatvector3)Added [SKUniformTypeFloatVector4](https://developer.apple.com/documentation/spritekit/skuniformtype/skuniformtypefloatvector4)Added [SKUniformTypeNone](https://developer.apple.com/documentation/spritekit/skuniformtype/skuniformtypenone)Added [SKUniformTypeTexture](https://developer.apple.com/documentation/spritekit/skuniformtype/texture)SKView.hAdded [SKView.allowsTransparency](https://developer.apple.com/documentation/spritekit/skview/1519697-allowstransparency)Added [SKView.shouldCullNonVisibleNodes](https://developer.apple.com/documentation/spritekit/skview/1519683-shouldcullnonvisiblenodes)Added [SKView.showsFields](https://developer.apple.com/documentation/spritekit/skview/1520443-showsfields)Added [SKView.showsQuadCount](https://developer.apple.com/documentation/spritekit/skview/1519652-showsquadcount)Added [-[SKView textureFromNode:crop:]](https://developer.apple.com/documentation/spritekit/skview/1519994-texturefromnode)Modified [SKView.asynchronous](https://developer.apple.com/documentation/spritekit/skview/1520229-asynchronous)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isAsynchronous, nonatomic) BOOL asynchronous ``` |
| To | ``` @property(nonatomic, getter=isAsynchronous) BOOL asynchronous ``` |

Modified [SKView.paused](https://developer.apple.com/documentation/spritekit/skview/1519654-ispaused)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isPaused, nonatomic) BOOL paused ``` |
| To | ``` @property(nonatomic, getter=isPaused) BOOL paused ``` |

Modified [SKView.scene](https://developer.apple.com/documentation/spritekit/skview/1520084-scene)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) SKScene *scene ``` |
| To | ``` @property(nonatomic, readonly) SKScene *scene ``` |

Modified [SKView.showsPhysics](https://developer.apple.com/documentation/spritekit/skview/1520389-showsphysics)

|  | Introduction |
| --- | --- |
| From | iOS 7.1 |
| To | iOS 8.0 |

SpriteKitBase.hAdded [vector_float3](https://developer.apple.com/documentation/spritekit/vector_float3)

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
