---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/SpriteKit.html
archived_at: '2026-07-15T07:34:47.388888Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# SpriteKit Changes

## SpriteKit

SK3DNode.h (Added)Added [SK3DNode](https://developer.apple.com/documentation/spritekit/sk3dnode)Added [SK3DNode.autoenablesDefaultLighting](https://developer.apple.com/documentation/spritekit/sk3dnode/1519676-autoenablesdefaultlighting)Added [-[SK3DNode hitTest:options:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1519782-hittest)Added [-[SK3DNode initWithCoder:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1519722-initwithcoder)Added [-[SK3DNode initWithViewportSize:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1519708-init)Added [SK3DNode.loops](https://developer.apple.com/documentation/spritekit/sk3dnode/1519549-loops)Added [+[SK3DNode nodeWithViewportSize:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1537481-nodewithviewportsize)Added [SK3DNode.playing](https://developer.apple.com/documentation/spritekit/sk3dnode/1520297-isplaying)Added [SK3DNode.pointOfView](https://developer.apple.com/documentation/spritekit/sk3dnode/1519786-pointofview)Added [-[SK3DNode projectPoint:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1520400-projectpoint)Added [SK3DNode.sceneTime](https://developer.apple.com/documentation/spritekit/sk3dnode/1519738-scenetime)Added [SK3DNode.scnScene](https://developer.apple.com/documentation/spritekit/sk3dnode/1519834-scnscene)Added [-[SK3DNode unprojectPoint:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1520024-unprojectpoint)Added [SK3DNode.viewportSize](https://developer.apple.com/documentation/spritekit/sk3dnode/1520078-viewportsize)SKAction.hAdded [+[SKAction falloffBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417766-falloffby)Added [+[SKAction falloffTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417758-falloff)Added [+[SKAction followPath:asOffset:orientToPath:speed:]](https://developer.apple.com/documentation/spritekit/skaction/1417798-followpath)Added [+[SKAction followPath:speed:]](https://developer.apple.com/documentation/spritekit/skaction/1417786-follow)Added [+[SKAction hide]](https://developer.apple.com/documentation/spritekit/skaction/1417704-hide)Added [+[SKAction reachTo:rootNode:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417773-reachto)Added [+[SKAction reachTo:rootNode:velocity:]](https://developer.apple.com/documentation/spritekit/skaction/1417720-reachto)Added [+[SKAction reachToNode:rootNode:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417827-reachtonode)Added [+[SKAction reachToNode:rootNode:velocity:]](https://developer.apple.com/documentation/spritekit/skaction/1417801-reach)Added [+[SKAction setTexture:resize:]](https://developer.apple.com/documentation/spritekit/skaction/1417743-settexture)Added [+[SKAction strengthBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417762-strengthby)Added [+[SKAction strengthTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417815-strengthto)Added [SKAction.timingFunction](https://developer.apple.com/documentation/spritekit/skaction/1417666-timingfunction)Added [+[SKAction unhide]](https://developer.apple.com/documentation/spritekit/skaction/1417660-unhide)Added [SKActionTimingFunction](https://developer.apple.com/documentation/spritekit/skactiontimingfunction)Modified [SKAction.duration](https://developer.apple.com/documentation/spritekit/skaction/1417790-duration)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) NSTimeInterval duration ``` |
| To | ``` @property(nonatomic) NSTimeInterval duration ``` |

Modified [SKAction.speed](https://developer.apple.com/documentation/spritekit/skaction/1417718-speed)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat speed ``` |
| To | ``` @property(nonatomic) CGFloat speed ``` |

Modified [SKAction.timingMode](https://developer.apple.com/documentation/spritekit/skaction/1417807-timingmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) SKActionTimingMode timingMode ``` |
| To | ``` @property(nonatomic) SKActionTimingMode timingMode ``` |

SKConstraint.h (Added)Added [SKConstraint](https://developer.apple.com/documentation/spritekit/skconstraint)Added [+[SKConstraint distance:toNode:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519750-distance)Added [+[SKConstraint distance:toPoint:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519688-distance)Added [+[SKConstraint distance:toPoint:inNode:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519746-distance)Added [SKConstraint.enabled](https://developer.apple.com/documentation/spritekit/skconstraint/1519669-enabled)Added [+[SKConstraint orientToNode:offset:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519744-orienttonode)Added [+[SKConstraint orientToPoint:inNode:offset:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519627-orienttopoint)Added [+[SKConstraint orientToPoint:offset:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519686-orienttopoint)Added [+[SKConstraint positionX:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519716-positionx)Added [+[SKConstraint positionX:Y:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519760-positionx)Added [+[SKConstraint positionY:]](https://developer.apple.com/documentation/spritekit/skconstraint/1520356-positiony)Added [SKConstraint.referenceNode](https://developer.apple.com/documentation/spritekit/skconstraint/1520369-referencenode)Added [+[SKConstraint zRotation:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519706-zrotation)Added [SKRange](https://developer.apple.com/documentation/spritekit/skrange)Added [-[SKRange initWithLowerLimit:upperLimit:]](https://developer.apple.com/documentation/spritekit/skrange/1520307-init)Added [SKRange.lowerLimit](https://developer.apple.com/documentation/spritekit/skrange/1520000-lowerlimit)Added [+[SKRange rangeWithConstantValue:]](https://developer.apple.com/documentation/spritekit/skrange/1520276-rangewithconstantvalue)Added [+[SKRange rangeWithLowerLimit:]](https://developer.apple.com/documentation/spritekit/skrange/1520137-rangewithlowerlimit)Added [+[SKRange rangeWithLowerLimit:upperLimit:]](https://developer.apple.com/documentation/spritekit/skrange/1534324-rangewithlowerlimit)Added [+[SKRange rangeWithNoLimits]](https://developer.apple.com/documentation/spritekit/skrange/1519920-withnolimits)Added [+[SKRange rangeWithUpperLimit:]](https://developer.apple.com/documentation/spritekit/skrange/1519559-rangewithupperlimit)Added [+[SKRange rangeWithValue:variance:]](https://developer.apple.com/documentation/spritekit/skrange/1519842-init)Added [SKRange.upperLimit](https://developer.apple.com/documentation/spritekit/skrange/1519596-upperlimit)SKCropNode.hModified [SKCropNode.maskNode](https://developer.apple.com/documentation/spritekit/skcropnode/1520449-masknode)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) SKNode *maskNode ``` |
| To | ``` @property(nonatomic, retain) SKNode *maskNode ``` |

SKEffectNode.hAdded [SKEffectNode.shader](https://developer.apple.com/documentation/spritekit/skeffectnode/1459388-shader)Modified [SKEffectNode.blendMode](https://developer.apple.com/documentation/spritekit/skeffectnode/1459386-blendmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) SKBlendMode blendMode ``` |
| To | ``` @property(nonatomic) SKBlendMode blendMode ``` |

Modified [SKEffectNode.filter](https://developer.apple.com/documentation/spritekit/skeffectnode/1459392-filter)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) CIFilter *filter ``` |
| To | ``` @property(nonatomic, retain) CIFilter *filter ``` |

Modified [SKEffectNode.shouldCenterFilter](https://developer.apple.com/documentation/spritekit/skeffectnode/1459390-shouldcenterfilter)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL shouldCenterFilter ``` |
| To | ``` @property(nonatomic) BOOL shouldCenterFilter ``` |

Modified [SKEffectNode.shouldEnableEffects](https://developer.apple.com/documentation/spritekit/skeffectnode/1459385-shouldenableeffects)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL shouldEnableEffects ``` |
| To | ``` @property(nonatomic) BOOL shouldEnableEffects ``` |

Modified [SKEffectNode.shouldRasterize](https://developer.apple.com/documentation/spritekit/skeffectnode/1459381-shouldrasterize)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL shouldRasterize ``` |
| To | ``` @property(nonatomic) BOOL shouldRasterize ``` |

SKEmitterNode.hAdded [SKEmitterNode.fieldBitMask](https://developer.apple.com/documentation/spritekit/skemitternode/1398006-fieldbitmask)Added [SKEmitterNode.particleZPositionSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398008-particlezpositionspeed)Added [SKEmitterNode.shader](https://developer.apple.com/documentation/spritekit/skemitternode/1398069-shader)Modified [SKEmitterNode.emissionAngle](https://developer.apple.com/documentation/spritekit/skemitternode/1398035-emissionangle)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat emissionAngle ``` |
| To | ``` @property(nonatomic) CGFloat emissionAngle ``` |

Modified [SKEmitterNode.emissionAngleRange](https://developer.apple.com/documentation/spritekit/skemitternode/1398067-emissionanglerange)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat emissionAngleRange ``` |
| To | ``` @property(nonatomic) CGFloat emissionAngleRange ``` |

Modified [SKEmitterNode.numParticlesToEmit](https://developer.apple.com/documentation/spritekit/skemitternode/1398043-numparticlestoemit)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) NSUInteger numParticlesToEmit ``` |
| To | ``` @property(nonatomic) NSUInteger numParticlesToEmit ``` |

Modified [SKEmitterNode.particleAction](https://developer.apple.com/documentation/spritekit/skemitternode/1397970-particleaction)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) SKAction *particleAction ``` |
| To | ``` @property(nonatomic, copy) SKAction *particleAction ``` |

Modified [SKEmitterNode.particleAlpha](https://developer.apple.com/documentation/spritekit/skemitternode/1397988-particlealpha)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleAlpha ``` |
| To | ``` @property(nonatomic) CGFloat particleAlpha ``` |

Modified [SKEmitterNode.particleAlphaRange](https://developer.apple.com/documentation/spritekit/skemitternode/1398031-particlealpharange)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleAlphaRange ``` |
| To | ``` @property(nonatomic) CGFloat particleAlphaRange ``` |

Modified [SKEmitterNode.particleAlphaSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1398057-particlealphasequence)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) SKKeyframeSequence *particleAlphaSequence ``` |
| To | ``` @property(nonatomic, retain) SKKeyframeSequence *particleAlphaSequence ``` |

Modified [SKEmitterNode.particleAlphaSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398021-particlealphaspeed)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleAlphaSpeed ``` |
| To | ``` @property(nonatomic) CGFloat particleAlphaSpeed ``` |

Modified [SKEmitterNode.particleBirthRate](https://developer.apple.com/documentation/spritekit/skemitternode/1398039-particlebirthrate)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleBirthRate ``` |
| To | ``` @property(nonatomic) CGFloat particleBirthRate ``` |

Modified [SKEmitterNode.particleBlendMode](https://developer.apple.com/documentation/spritekit/skemitternode/1397978-particleblendmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) SKBlendMode particleBlendMode ``` |
| To | ``` @property(nonatomic) SKBlendMode particleBlendMode ``` |

Modified [SKEmitterNode.particleColor](https://developer.apple.com/documentation/spritekit/skemitternode/1398049-particlecolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) NSColor *particleColor ``` |
| To | ``` @property(nonatomic, retain) NSColor *particleColor ``` |

Modified [SKEmitterNode.particleColorAlphaRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397976-particlecoloralpharange)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleColorAlphaRange ``` |
| To | ``` @property(nonatomic) CGFloat particleColorAlphaRange ``` |

Modified [SKEmitterNode.particleColorAlphaSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398051-particlecoloralphaspeed)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleColorAlphaSpeed ``` |
| To | ``` @property(nonatomic) CGFloat particleColorAlphaSpeed ``` |

Modified [SKEmitterNode.particleColorBlendFactor](https://developer.apple.com/documentation/spritekit/skemitternode/1398071-particlecolorblendfactor)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleColorBlendFactor ``` |
| To | ``` @property(nonatomic) CGFloat particleColorBlendFactor ``` |

Modified [SKEmitterNode.particleColorBlendFactorRange](https://developer.apple.com/documentation/spritekit/skemitternode/1398047-particlecolorblendfactorrange)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleColorBlendFactorRange ``` |
| To | ``` @property(nonatomic) CGFloat particleColorBlendFactorRange ``` |

Modified [SKEmitterNode.particleColorBlendFactorSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1397980-particlecolorblendfactorsequence)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) SKKeyframeSequence *particleColorBlendFactorSequence ``` |
| To | ``` @property(nonatomic, retain) SKKeyframeSequence *particleColorBlendFactorSequence ``` |

Modified [SKEmitterNode.particleColorBlendFactorSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398037-particlecolorblendfactorspeed)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleColorBlendFactorSpeed ``` |
| To | ``` @property(nonatomic) CGFloat particleColorBlendFactorSpeed ``` |

Modified [SKEmitterNode.particleColorBlueRange](https://developer.apple.com/documentation/spritekit/skemitternode/1398075-particlecolorbluerange)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleColorBlueRange ``` |
| To | ``` @property(nonatomic) CGFloat particleColorBlueRange ``` |

Modified [SKEmitterNode.particleColorBlueSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398023-particlecolorbluespeed)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleColorBlueSpeed ``` |
| To | ``` @property(nonatomic) CGFloat particleColorBlueSpeed ``` |

Modified [SKEmitterNode.particleColorGreenRange](https://developer.apple.com/documentation/spritekit/skemitternode/1398065-particlecolorgreenrange)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleColorGreenRange ``` |
| To | ``` @property(nonatomic) CGFloat particleColorGreenRange ``` |

Modified [SKEmitterNode.particleColorGreenSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398033-particlecolorgreenspeed)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleColorGreenSpeed ``` |
| To | ``` @property(nonatomic) CGFloat particleColorGreenSpeed ``` |

Modified [SKEmitterNode.particleColorRedRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397998-particlecolorredrange)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleColorRedRange ``` |
| To | ``` @property(nonatomic) CGFloat particleColorRedRange ``` |

Modified [SKEmitterNode.particleColorRedSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398041-particlecolorredspeed)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleColorRedSpeed ``` |
| To | ``` @property(nonatomic) CGFloat particleColorRedSpeed ``` |

Modified [SKEmitterNode.particleColorSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1397992-particlecolorsequence)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) SKKeyframeSequence *particleColorSequence ``` |
| To | ``` @property(nonatomic, retain) SKKeyframeSequence *particleColorSequence ``` |

Modified [SKEmitterNode.particleLifetime](https://developer.apple.com/documentation/spritekit/skemitternode/1398000-particlelifetime)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleLifetime ``` |
| To | ``` @property(nonatomic) CGFloat particleLifetime ``` |

Modified [SKEmitterNode.particleLifetimeRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397994-particlelifetimerange)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleLifetimeRange ``` |
| To | ``` @property(nonatomic) CGFloat particleLifetimeRange ``` |

Modified [SKEmitterNode.particlePosition](https://developer.apple.com/documentation/spritekit/skemitternode/1398019-particleposition)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGPoint particlePosition ``` |
| To | ``` @property(nonatomic) CGPoint particlePosition ``` |

Modified [SKEmitterNode.particlePositionRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397972-particlepositionrange)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGVector particlePositionRange ``` |
| To | ``` @property(nonatomic) CGVector particlePositionRange ``` |

Modified [SKEmitterNode.particleRotation](https://developer.apple.com/documentation/spritekit/skemitternode/1398025-particlerotation)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleRotation ``` |
| To | ``` @property(nonatomic) CGFloat particleRotation ``` |

Modified [SKEmitterNode.particleRotationRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397996-particlerotationrange)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleRotationRange ``` |
| To | ``` @property(nonatomic) CGFloat particleRotationRange ``` |

Modified [SKEmitterNode.particleRotationSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1397968-particlerotationspeed)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleRotationSpeed ``` |
| To | ``` @property(nonatomic) CGFloat particleRotationSpeed ``` |

Modified [SKEmitterNode.particleScale](https://developer.apple.com/documentation/spritekit/skemitternode/1398014-particlescale)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleScale ``` |
| To | ``` @property(nonatomic) CGFloat particleScale ``` |

Modified [SKEmitterNode.particleScaleRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397990-particlescalerange)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleScaleRange ``` |
| To | ``` @property(nonatomic) CGFloat particleScaleRange ``` |

Modified [SKEmitterNode.particleScaleSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1398029-particlescalesequence)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) SKKeyframeSequence *particleScaleSequence ``` |
| To | ``` @property(nonatomic, retain) SKKeyframeSequence *particleScaleSequence ``` |

Modified [SKEmitterNode.particleScaleSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398073-particlescalespeed)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleScaleSpeed ``` |
| To | ``` @property(nonatomic) CGFloat particleScaleSpeed ``` |

Modified [SKEmitterNode.particleSize](https://developer.apple.com/documentation/spritekit/skemitternode/1398063-particlesize)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGSize particleSize ``` |
| To | ``` @property(nonatomic) CGSize particleSize ``` |

Modified [SKEmitterNode.particleSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398061-particlespeed)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleSpeed ``` |
| To | ``` @property(nonatomic) CGFloat particleSpeed ``` |

Modified [SKEmitterNode.particleSpeedRange](https://developer.apple.com/documentation/spritekit/skemitternode/1398045-particlespeedrange)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleSpeedRange ``` |
| To | ``` @property(nonatomic) CGFloat particleSpeedRange ``` |

Modified [SKEmitterNode.particleTexture](https://developer.apple.com/documentation/spritekit/skemitternode/1398004-particletexture)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) SKTexture *particleTexture ``` |
| To | ``` @property(nonatomic, retain) SKTexture *particleTexture ``` |

Modified [SKEmitterNode.particleZPosition](https://developer.apple.com/documentation/spritekit/skemitternode/1398055-particlezposition)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleZPosition ``` |
| To | ``` @property(nonatomic) CGFloat particleZPosition ``` |

Modified [SKEmitterNode.particleZPositionRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397974-particlezpositionrange)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat particleZPositionRange ``` |
| To | ``` @property(nonatomic) CGFloat particleZPositionRange ``` |

Modified [SKEmitterNode.targetNode](https://developer.apple.com/documentation/spritekit/skemitternode/1398012-targetnode)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, atomic) SKNode *targetNode ``` |
| To | ``` @property(nonatomic, weak) SKNode *targetNode ``` |

Modified [SKEmitterNode.xAcceleration](https://developer.apple.com/documentation/spritekit/skemitternode/1398017-xacceleration)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat xAcceleration ``` |
| To | ``` @property(nonatomic) CGFloat xAcceleration ``` |

Modified [SKEmitterNode.yAcceleration](https://developer.apple.com/documentation/spritekit/skemitternode/1397982-yacceleration)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat yAcceleration ``` |
| To | ``` @property(nonatomic) CGFloat yAcceleration ``` |

SKFieldNode.h (Added)Added [SKFieldNode](https://developer.apple.com/documentation/spritekit/skfieldnode)Added [SKFieldNode.animationSpeed](https://developer.apple.com/documentation/spritekit/skfieldnode/1519822-animationspeed)Added [SKFieldNode.categoryBitMask](https://developer.apple.com/documentation/spritekit/skfieldnode/1520143-categorybitmask)Added [+[SKFieldNode customFieldWithEvaluationBlock:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519710-customfieldwithevaluationblock)Added [SKFieldNode.direction](https://developer.apple.com/documentation/spritekit/skfieldnode/1520091-direction)Added [+[SKFieldNode dragField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520225-dragfield)Added [+[SKFieldNode electricField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520396-electricfield)Added [SKFieldNode.enabled](https://developer.apple.com/documentation/spritekit/skfieldnode/1520079-isenabled)Added [SKFieldNode.exclusive](https://developer.apple.com/documentation/spritekit/skfieldnode/1520365-exclusive)Added [SKFieldNode.falloff](https://developer.apple.com/documentation/spritekit/skfieldnode/1520445-falloff)Added [+[SKFieldNode linearGravityFieldWithVector:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520145-lineargravityfield)Added [+[SKFieldNode magneticField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520134-magneticfield)Added [SKFieldNode.minimumRadius](https://developer.apple.com/documentation/spritekit/skfieldnode/1519804-minimumradius)Added [+[SKFieldNode noiseFieldWithSmoothness:animationSpeed:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519947-noisefieldwithsmoothness)Added [+[SKFieldNode radialGravityField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520382-radialgravityfield)Added [SKFieldNode.region](https://developer.apple.com/documentation/spritekit/skfieldnode/1519551-region)Added [SKFieldNode.smoothness](https://developer.apple.com/documentation/spritekit/skfieldnode/1520273-smoothness)Added [+[SKFieldNode springField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519694-springfield)Added [SKFieldNode.strength](https://developer.apple.com/documentation/spritekit/skfieldnode/1520152-strength)Added [SKFieldNode.texture](https://developer.apple.com/documentation/spritekit/skfieldnode/1519928-texture)Added [+[SKFieldNode turbulenceFieldWithSmoothness:animationSpeed:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520018-turbulencefieldwithsmoothness)Added [+[SKFieldNode velocityFieldWithTexture:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519778-velocityfieldwithtexture)Added [+[SKFieldNode velocityFieldWithVector:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520271-velocityfieldwithvector)Added [+[SKFieldNode vortexField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520157-vortexfield)Added [SKFieldForceEvaluator](https://developer.apple.com/documentation/spritekit/skfieldforceevaluator)SKKeyframeSequence.hAdded [-[SKKeyframeSequence initWithCoder:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390892-init)Modified [-[SKKeyframeSequence initWithKeyframeValues:times:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390896-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [SKKeyframeSequence.interpolationMode](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390914-interpolationmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) SKInterpolationMode interpolationMode ``` |
| To | ``` @property(nonatomic) SKInterpolationMode interpolationMode ``` |

Modified [SKKeyframeSequence.repeatMode](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390900-repeatmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) SKRepeatMode repeatMode ``` |
| To | ``` @property(nonatomic) SKRepeatMode repeatMode ``` |

SKLabelNode.hAdded [+[SKLabelNode labelNodeWithText:]](https://developer.apple.com/documentation/spritekit/sklabelnode/1519612-labelnodewithtext)Modified [SKLabelNode.blendMode](https://developer.apple.com/documentation/spritekit/sklabelnode/1519598-blendmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) SKBlendMode blendMode ``` |
| To | ``` @property(nonatomic) SKBlendMode blendMode ``` |

Modified [SKLabelNode.color](https://developer.apple.com/documentation/spritekit/sklabelnode/1519938-color)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) NSColor *color ``` |
| To | ``` @property(nonatomic, retain) NSColor *color ``` |

Modified [SKLabelNode.colorBlendFactor](https://developer.apple.com/documentation/spritekit/sklabelnode/1519724-colorblendfactor)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat colorBlendFactor ``` |
| To | ``` @property(nonatomic) CGFloat colorBlendFactor ``` |

Modified [SKLabelNode.fontColor](https://developer.apple.com/documentation/spritekit/sklabelnode/1520057-fontcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) NSColor *fontColor ``` |
| To | ``` @property(nonatomic, retain) NSColor *fontColor ``` |

Modified [SKLabelNode.fontName](https://developer.apple.com/documentation/spritekit/sklabelnode/1520129-fontname)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) NSString *fontName ``` |
| To | ``` @property(nonatomic, copy) NSString *fontName ``` |

Modified [SKLabelNode.fontSize](https://developer.apple.com/documentation/spritekit/sklabelnode/1520208-fontsize)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat fontSize ``` |
| To | ``` @property(nonatomic) CGFloat fontSize ``` |

Modified [SKLabelNode.horizontalAlignmentMode](https://developer.apple.com/documentation/spritekit/sklabelnode/1519711-horizontalalignmentmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) SKLabelHorizontalAlignmentMode horizontalAlignmentMode ``` |
| To | ``` @property(nonatomic) SKLabelHorizontalAlignmentMode horizontalAlignmentMode ``` |

Modified [SKLabelNode.text](https://developer.apple.com/documentation/spritekit/sklabelnode/1519788-text)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) NSString *text ``` |
| To | ``` @property(nonatomic, copy) NSString *text ``` |

Modified [SKLabelNode.verticalAlignmentMode](https://developer.apple.com/documentation/spritekit/sklabelnode/1519933-verticalalignmentmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) SKLabelVerticalAlignmentMode verticalAlignmentMode ``` |
| To | ``` @property(nonatomic) SKLabelVerticalAlignmentMode verticalAlignmentMode ``` |

SKLightNode.h (Added)Added [SKLightNode](https://developer.apple.com/documentation/spritekit/sklightnode)Added [SKLightNode.ambientColor](https://developer.apple.com/documentation/spritekit/sklightnode/1520139-ambientcolor)Added [SKLightNode.categoryBitMask](https://developer.apple.com/documentation/spritekit/sklightnode/1519940-categorybitmask)Added [SKLightNode.enabled](https://developer.apple.com/documentation/spritekit/sklightnode/1519826-enabled)Added [SKLightNode.falloff](https://developer.apple.com/documentation/spritekit/sklightnode/1519776-falloff)Added [SKLightNode.lightColor](https://developer.apple.com/documentation/spritekit/sklightnode/1520244-lightcolor)Added [SKLightNode.shadowColor](https://developer.apple.com/documentation/spritekit/sklightnode/1519844-shadowcolor)SKMutableTexture.h (Added)Added [SKMutableTexture](https://developer.apple.com/documentation/spritekit/skmutabletexture)Added [-[SKMutableTexture initWithSize:]](https://developer.apple.com/documentation/spritekit/skmutabletexture/1397883-init)Added [-[SKMutableTexture initWithSize:pixelFormat:]](https://developer.apple.com/documentation/spritekit/skmutabletexture/1397879-init)Added [-[SKMutableTexture modifyPixelDataWithBlock:]](https://developer.apple.com/documentation/spritekit/skmutabletexture/1397881-modifypixeldatawithblock)Added [+[SKMutableTexture mutableTextureWithSize:]](https://developer.apple.com/documentation/spritekit/skmutabletexture/1397874-mutabletexturewithsize)SKNode.hAdded [SKNode.constraints](https://developer.apple.com/documentation/spritekit/sknode/1483124-constraints)Added [-[SKNode init]](https://developer.apple.com/documentation/spritekit/sknode/1483097-init)Added [-[SKNode initWithCoder:]](https://developer.apple.com/documentation/spritekit/sknode/1483142-initwithcoder)Added [+[SKNode nodeWithFileNamed:]](https://developer.apple.com/documentation/spritekit/sknode/1483083-init)Added [-[SKNode objectForKeyedSubscript:]](https://developer.apple.com/documentation/spritekit/sknode/1483070-subscript)Added [SKNode.reachConstraints](https://developer.apple.com/documentation/spritekit/sknode/1483019-reachconstraints)Modified [SKNode.alpha](https://developer.apple.com/documentation/spritekit/sknode/1483023-alpha)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat alpha ``` |
| To | ``` @property(nonatomic) CGFloat alpha ``` |

Modified [SKNode.children](https://developer.apple.com/documentation/spritekit/sknode/1483028-children)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSArray *children ``` |
| To | ``` @property(nonatomic, readonly) NSArray *children ``` |

Modified [SKNode.frame](https://developer.apple.com/documentation/spritekit/sknode/1483026-frame)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) CGRect frame ``` |
| To | ``` @property(nonatomic, readonly) CGRect frame ``` |

Modified [SKNode.hidden](https://developer.apple.com/documentation/spritekit/sknode/1483048-hidden)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isHidden, atomic) BOOL hidden ``` |
| To | ``` @property(nonatomic, getter=isHidden) BOOL hidden ``` |

Modified [SKNode.name](https://developer.apple.com/documentation/spritekit/sknode/1483136-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) NSString *name ``` |
| To | ``` @property(nonatomic, copy) NSString *name ``` |

Modified [SKNode.parent](https://developer.apple.com/documentation/spritekit/sknode/1483080-parent)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) SKNode *parent ``` |
| To | ``` @property(nonatomic, readonly) SKNode *parent ``` |

Modified [SKNode.paused](https://developer.apple.com/documentation/spritekit/sknode/1483113-paused)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isPaused, atomic) BOOL paused ``` |
| To | ``` @property(nonatomic, getter=isPaused) BOOL paused ``` |

Modified [SKNode.physicsBody](https://developer.apple.com/documentation/spritekit/sknode/1483117-physicsbody)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) SKPhysicsBody *physicsBody ``` |
| To | ``` @property(nonatomic, retain) SKPhysicsBody *physicsBody ``` |

Modified [SKNode.position](https://developer.apple.com/documentation/spritekit/sknode/1483101-position)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGPoint position ``` |
| To | ``` @property(nonatomic) CGPoint position ``` |

Modified [SKNode.scene](https://developer.apple.com/documentation/spritekit/sknode/1483064-scene)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) SKScene *scene ``` |
| To | ``` @property(nonatomic, readonly) SKScene *scene ``` |

Modified [SKNode.speed](https://developer.apple.com/documentation/spritekit/sknode/1483036-speed)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat speed ``` |
| To | ``` @property(nonatomic) CGFloat speed ``` |

Modified [SKNode.userData](https://developer.apple.com/documentation/spritekit/sknode/1483121-userdata)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) NSMutableDictionary *userData ``` |
| To | ``` @property(nonatomic, retain) NSMutableDictionary *userData ``` |

Modified [SKNode.userInteractionEnabled](https://developer.apple.com/documentation/spritekit/sknode/1483109-userinteractionenabled)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isUserInteractionEnabled) BOOL userInteractionEnabled ``` |
| To | ``` @property(nonatomic, getter=isUserInteractionEnabled) BOOL userInteractionEnabled ``` |

Modified [SKNode.xScale](https://developer.apple.com/documentation/spritekit/sknode/1483087-xscale)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat xScale ``` |
| To | ``` @property(nonatomic) CGFloat xScale ``` |

Modified [SKNode.yScale](https://developer.apple.com/documentation/spritekit/sknode/1483046-yscale)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat yScale ``` |
| To | ``` @property(nonatomic) CGFloat yScale ``` |

Modified [SKNode.zPosition](https://developer.apple.com/documentation/spritekit/sknode/1483107-zposition)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat zPosition ``` |
| To | ``` @property(nonatomic) CGFloat zPosition ``` |

Modified [SKNode.zRotation](https://developer.apple.com/documentation/spritekit/sknode/1483089-zrotation)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat zRotation ``` |
| To | ``` @property(nonatomic) CGFloat zRotation ``` |

SKPhysicsBody.hAdded [+[SKPhysicsBody bodyWithBodies:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519736-bodywithbodies)Added [+[SKPhysicsBody bodyWithCircleOfRadius:center:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519692-init)Added [+[SKPhysicsBody bodyWithRectangleOfSize:center:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519936-bodywithrectangleofsize)Added [+[SKPhysicsBody bodyWithTexture:alphaThreshold:size:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519689-bodywithtexture)Added [+[SKPhysicsBody bodyWithTexture:size:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519690-bodywithtexture)Added [SKPhysicsBody.charge](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519881-charge)Added [SKPhysicsBody.fieldBitMask](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520280-fieldbitmask)Added [SKPhysicsBody.pinned](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520354-pinned)Modified [SKPhysicsBody.affectedByGravity](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519774-affectedbygravity)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) BOOL affectedByGravity ``` |
| To | ``` @property(nonatomic, assign) BOOL affectedByGravity ``` |

Modified [SKPhysicsBody.allowsRotation](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519986-allowsrotation)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL allowsRotation ``` |
| To | ``` @property(nonatomic) BOOL allowsRotation ``` |

Modified [SKPhysicsBody.angularDamping](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519913-angulardamping)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) CGFloat angularDamping ``` |
| To | ``` @property(nonatomic, assign) CGFloat angularDamping ``` |

Modified [SKPhysicsBody.angularVelocity](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519766-angularvelocity)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat angularVelocity ``` |
| To | ``` @property(nonatomic) CGFloat angularVelocity ``` |

Modified [SKPhysicsBody.area](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520034-area)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) CGFloat area ``` |
| To | ``` @property(nonatomic, readonly) CGFloat area ``` |

Modified [SKPhysicsBody.categoryBitMask](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519869-categorybitmask)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) uint32_t categoryBitMask ``` |
| To | ``` @property(nonatomic, assign) uint32_t categoryBitMask ``` |

Modified [SKPhysicsBody.collisionBitMask](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520003-collisionbitmask)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) uint32_t collisionBitMask ``` |
| To | ``` @property(nonatomic, assign) uint32_t collisionBitMask ``` |

Modified [SKPhysicsBody.contactTestBitMask](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519781-contacttestbitmask)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) uint32_t contactTestBitMask ``` |
| To | ``` @property(nonatomic, assign) uint32_t contactTestBitMask ``` |

Modified [SKPhysicsBody.density](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519983-density)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat density ``` |
| To | ``` @property(nonatomic) CGFloat density ``` |

Modified [SKPhysicsBody.dynamic](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520132-isdynamic)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isDynamic, atomic) BOOL dynamic ``` |
| To | ``` @property(nonatomic, getter=isDynamic) BOOL dynamic ``` |

Modified [SKPhysicsBody.friction](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519840-friction)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat friction ``` |
| To | ``` @property(nonatomic) CGFloat friction ``` |

Modified [SKPhysicsBody.joints](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519849-joints)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSArray *joints ``` |
| To | ``` @property(nonatomic, readonly) NSArray *joints ``` |

Modified [SKPhysicsBody.linearDamping](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519796-lineardamping)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) CGFloat linearDamping ``` |
| To | ``` @property(nonatomic, assign) CGFloat linearDamping ``` |

Modified [SKPhysicsBody.mass](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519906-mass)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat mass ``` |
| To | ``` @property(nonatomic) CGFloat mass ``` |

Modified [SKPhysicsBody.node](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520049-node)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, weak, atomic) SKNode *node ``` |
| To | ``` @property(nonatomic, readonly, weak) SKNode *node ``` |

Modified [SKPhysicsBody.resting](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520256-resting)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isResting, atomic) BOOL resting ``` |
| To | ``` @property(nonatomic, getter=isResting) BOOL resting ``` |

Modified [SKPhysicsBody.restitution](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520447-restitution)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat restitution ``` |
| To | ``` @property(nonatomic) CGFloat restitution ``` |

Modified [SKPhysicsBody.usesPreciseCollisionDetection](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520014-usesprecisecollisiondetection)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL usesPreciseCollisionDetection ``` |
| To | ``` @property(nonatomic) BOOL usesPreciseCollisionDetection ``` |

Modified [SKPhysicsBody.velocity](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519635-velocity)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGVector velocity ``` |
| To | ``` @property(nonatomic) CGVector velocity ``` |

SKPhysicsContact.hAdded [SKPhysicsContact.contactNormal](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478528-contactnormal)Modified [SKPhysicsContact.bodyA](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478533-bodya)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) SKPhysicsBody *bodyA ``` |
| To | ``` @property(nonatomic, readonly) SKPhysicsBody *bodyA ``` |

Modified [SKPhysicsContact.bodyB](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478526-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) SKPhysicsBody *bodyB ``` |
| To | ``` @property(nonatomic, readonly) SKPhysicsBody *bodyB ``` |

Modified [SKPhysicsContact.collisionImpulse](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478523-collisionimpulse)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) CGFloat collisionImpulse ``` |
| To | ``` @property(nonatomic, readonly) CGFloat collisionImpulse ``` |

Modified [SKPhysicsContact.contactPoint](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478524-contactpoint)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) CGPoint contactPoint ``` |
| To | ``` @property(nonatomic, readonly) CGPoint contactPoint ``` |

SKPhysicsJoint.hAdded [SKPhysicsJoint.reactionForce](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1519866-reactionforce)Added [SKPhysicsJoint.reactionTorque](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1519682-reactiontorque)Added [SKPhysicsJointPin.rotationSpeed](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1520259-rotationspeed)Modified [SKPhysicsJoint.bodyA](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1520403-bodya)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) SKPhysicsBody *bodyA ``` |
| To | ``` @property(nonatomic, retain) SKPhysicsBody *bodyA ``` |

Modified [SKPhysicsJoint.bodyB](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1519693-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) SKPhysicsBody *bodyB ``` |
| To | ``` @property(nonatomic, retain) SKPhysicsBody *bodyB ``` |

Modified [SKPhysicsJointLimit.maxLength](https://developer.apple.com/documentation/spritekit/skphysicsjointlimit/1519978-maxlength)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat maxLength ``` |
| To | ``` @property(nonatomic) CGFloat maxLength ``` |

Modified [SKPhysicsJointPin.frictionTorque](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1520299-frictiontorque)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat frictionTorque ``` |
| To | ``` @property(nonatomic) CGFloat frictionTorque ``` |

Modified [SKPhysicsJointPin.lowerAngleLimit](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1520130-loweranglelimit)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat lowerAngleLimit ``` |
| To | ``` @property(nonatomic) CGFloat lowerAngleLimit ``` |

Modified [SKPhysicsJointPin.shouldEnableLimits](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1520292-shouldenablelimits)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL shouldEnableLimits ``` |
| To | ``` @property(nonatomic) BOOL shouldEnableLimits ``` |

Modified [SKPhysicsJointPin.upperAngleLimit](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1519967-upperanglelimit)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat upperAngleLimit ``` |
| To | ``` @property(nonatomic) CGFloat upperAngleLimit ``` |

Modified [SKPhysicsJointSliding.lowerDistanceLimit](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/1519969-lowerdistancelimit)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat lowerDistanceLimit ``` |
| To | ``` @property(nonatomic) CGFloat lowerDistanceLimit ``` |

Modified [SKPhysicsJointSliding.shouldEnableLimits](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/1520053-shouldenablelimits)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL shouldEnableLimits ``` |
| To | ``` @property(nonatomic) BOOL shouldEnableLimits ``` |

Modified [SKPhysicsJointSliding.upperDistanceLimit](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/1519836-upperdistancelimit)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat upperDistanceLimit ``` |
| To | ``` @property(nonatomic) CGFloat upperDistanceLimit ``` |

Modified [SKPhysicsJointSpring.damping](https://developer.apple.com/documentation/spritekit/skphysicsjointspring/1519709-damping)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat damping ``` |
| To | ``` @property(nonatomic) CGFloat damping ``` |

Modified [SKPhysicsJointSpring.frequency](https://developer.apple.com/documentation/spritekit/skphysicsjointspring/1519806-frequency)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat frequency ``` |
| To | ``` @property(nonatomic) CGFloat frequency ``` |

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
| From | ``` @property(assign, atomic) id<SKPhysicsContactDelegate> contactDelegate ``` |
| To | ``` @property(nonatomic, assign) id<SKPhysicsContactDelegate> contactDelegate ``` |

Modified [SKPhysicsWorld.gravity](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449623-gravity)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGVector gravity ``` |
| To | ``` @property(nonatomic) CGVector gravity ``` |

Modified [SKPhysicsWorld.speed](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449611-speed)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat speed ``` |
| To | ``` @property(nonatomic) CGFloat speed ``` |

SKReachConstraints.h (Added)Added [SKReachConstraints](https://developer.apple.com/documentation/spritekit/skreachconstraints)Added [-[SKReachConstraints initWithLowerAngleLimit:upperAngleLimit:]](https://developer.apple.com/documentation/spritekit/skreachconstraints/1520170-initwithloweranglelimit)Added [SKReachConstraints.lowerAngleLimit](https://developer.apple.com/documentation/spritekit/skreachconstraints/1519923-loweranglelimit)Added [SKReachConstraints.upperAngleLimit](https://developer.apple.com/documentation/spritekit/skreachconstraints/1519699-upperanglelimit)SKRegion.h (Added)Added [SKRegion](https://developer.apple.com/documentation/spritekit/skregion)Added [-[SKRegion containsPoint:]](https://developer.apple.com/documentation/spritekit/skregion/1519695-containspoint)Added [+[SKRegion infiniteRegion]](https://developer.apple.com/documentation/spritekit/skregion/1520061-infinite)Added [-[SKRegion initWithPath:]](https://developer.apple.com/documentation/spritekit/skregion/1519857-initwithpath)Added [-[SKRegion initWithRadius:]](https://developer.apple.com/documentation/spritekit/skregion/1520219-init)Added [-[SKRegion initWithSize:]](https://developer.apple.com/documentation/spritekit/skregion/1520385-initwithsize)Added [-[SKRegion inverseRegion]](https://developer.apple.com/documentation/spritekit/skregion/1519700-inverse)Added [SKRegion.path](https://developer.apple.com/documentation/spritekit/skregion/1520042-path)Added [-[SKRegion regionByDifferenceFromRegion:]](https://developer.apple.com/documentation/spritekit/skregion/1519879-bydifference)Added [-[SKRegion regionByIntersectionWithRegion:]](https://developer.apple.com/documentation/spritekit/skregion/1519646-regionbyintersectionwithregion)Added [-[SKRegion regionByUnionWithRegion:]](https://developer.apple.com/documentation/spritekit/skregion/1519702-regionbyunionwithregion)SKScene.hAdded [SKScene.delegate](https://developer.apple.com/documentation/spritekit/skscene/1520213-delegate)Added [-[SKScene didApplyConstraints]](https://developer.apple.com/documentation/spritekit/skscene/1520006-didapplyconstraints)Added [-[SKScene didFinishUpdate]](https://developer.apple.com/documentation/spritekit/skscene/1520269-didfinishupdate)Added [SKSceneDelegate](https://developer.apple.com/documentation/spritekit/skscenedelegate)Added [-[SKSceneDelegate didApplyConstraintsForScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1520375-didapplyconstraintsforscene)Added [-[SKSceneDelegate didEvaluateActionsForScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1520071-didevaluateactions)Added [-[SKSceneDelegate didFinishUpdateForScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1519814-didfinishupdate)Added [-[SKSceneDelegate didSimulatePhysicsForScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1520392-didsimulatephysicsforscene)Added [-[SKSceneDelegate update:forScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1519757-update)Modified [SKScene.anchorPoint](https://developer.apple.com/documentation/spritekit/skscene/1519864-anchorpoint)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGPoint anchorPoint ``` |
| To | ``` @property(nonatomic) CGPoint anchorPoint ``` |

Modified [SKScene.backgroundColor](https://developer.apple.com/documentation/spritekit/skscene/1520278-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) NSColor *backgroundColor ``` |
| To | ``` @property(nonatomic, retain) NSColor *backgroundColor ``` |

Modified [SKScene.physicsWorld](https://developer.apple.com/documentation/spritekit/skscene/1519584-physicsworld)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) SKPhysicsWorld *physicsWorld ``` |
| To | ``` @property(nonatomic, readonly) SKPhysicsWorld *physicsWorld ``` |

Modified [SKScene.scaleMode](https://developer.apple.com/documentation/spritekit/skscene/1519562-scalemode)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) SKSceneScaleMode scaleMode ``` |
| To | ``` @property(nonatomic) SKSceneScaleMode scaleMode ``` |

Modified [SKScene.size](https://developer.apple.com/documentation/spritekit/skscene/1519831-size)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGSize size ``` |
| To | ``` @property(nonatomic) CGSize size ``` |

Modified [SKScene.view](https://developer.apple.com/documentation/spritekit/skscene/1519726-view)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, readonly, atomic) SKView *view ``` |
| To | ``` @property(nonatomic, weak, readonly) SKView *view ``` |

SKShader.h (Added)Added [SKShader](https://developer.apple.com/documentation/spritekit/skshader)Added [-[SKShader addUniform:]](https://developer.apple.com/documentation/spritekit/skshader/1477561-adduniform)Added [-[SKShader initWithSource:]](https://developer.apple.com/documentation/spritekit/skshader/1477571-initwithsource)Added [-[SKShader initWithSource:uniforms:]](https://developer.apple.com/documentation/spritekit/skshader/1477555-initwithsource)Added [-[SKShader removeUniformNamed:]](https://developer.apple.com/documentation/spritekit/skshader/1477553-removeuniformnamed)Added [+[SKShader shader]](https://developer.apple.com/documentation/spritekit/skshader/1477559-shader)Added [+[SKShader shaderWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skshader/1477557-shaderwithfilenamed)Added [+[SKShader shaderWithSource:]](https://developer.apple.com/documentation/spritekit/skshader/1477563-shaderwithsource)Added [+[SKShader shaderWithSource:uniforms:]](https://developer.apple.com/documentation/spritekit/skshader/1477569-shaderwithsource)Added [SKShader.source](https://developer.apple.com/documentation/spritekit/skshader/1477544-source)Added [-[SKShader uniformNamed:]](https://developer.apple.com/documentation/spritekit/skshader/1477567-uniformnamed)Added [SKShader.uniforms](https://developer.apple.com/documentation/spritekit/skshader/1477565-uniforms)SKShapeNode.hAdded [SKShapeNode.fillShader](https://developer.apple.com/documentation/spritekit/skshapenode/1519629-fillshader)Added [SKShapeNode.fillTexture](https://developer.apple.com/documentation/spritekit/skshapenode/1519956-filltexture)Added [SKShapeNode.lineCap](https://developer.apple.com/documentation/spritekit/skshapenode/1520360-linecap)Added [SKShapeNode.lineJoin](https://developer.apple.com/documentation/spritekit/skshapenode/1520358-linejoin)Added [SKShapeNode.lineLength](https://developer.apple.com/documentation/spritekit/skshapenode/1520398-linelength)Added [SKShapeNode.miterLimit](https://developer.apple.com/documentation/spritekit/skshapenode/1520240-miterlimit)Added [+[SKShapeNode shapeNodeWithCircleOfRadius:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519570-shapenodewithcircleofradius)Added [+[SKShapeNode shapeNodeWithEllipseInRect:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520412-shapenodewithellipseinrect)Added [+[SKShapeNode shapeNodeWithEllipseOfSize:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519980-init)Added [+[SKShapeNode shapeNodeWithPath:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520022-shapenodewithpath)Added [+[SKShapeNode shapeNodeWithPath:centered:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519649-init)Added [+[SKShapeNode shapeNodeWithPoints:count:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520120-shapenodewithpoints)Added [+[SKShapeNode shapeNodeWithRect:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520047-init)Added [+[SKShapeNode shapeNodeWithRect:cornerRadius:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519769-init)Added [+[SKShapeNode shapeNodeWithRectOfSize:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520147-init)Added [+[SKShapeNode shapeNodeWithRectOfSize:cornerRadius:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519712-init)Added [+[SKShapeNode shapeNodeWithSplinePoints:count:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520140-init)Added [SKShapeNode.strokeShader](https://developer.apple.com/documentation/spritekit/skshapenode/1519784-strokeshader)Added [SKShapeNode.strokeTexture](https://developer.apple.com/documentation/spritekit/skshapenode/1519824-stroketexture)Modified [SKShapeNode.antialiased](https://developer.apple.com/documentation/spritekit/skshapenode/1519719-antialiased)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isAntialiased, atomic) BOOL antialiased ``` |
| To | ``` @property(nonatomic, getter=isAntialiased) BOOL antialiased ``` |

Modified [SKShapeNode.blendMode](https://developer.apple.com/documentation/spritekit/skshapenode/1520045-blendmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) SKBlendMode blendMode ``` |
| To | ``` @property(nonatomic) SKBlendMode blendMode ``` |

Modified [SKShapeNode.fillColor](https://developer.apple.com/documentation/spritekit/skshapenode/1520154-fillcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) NSColor *fillColor ``` |
| To | ``` @property(nonatomic, retain) NSColor *fillColor ``` |

Modified [SKShapeNode.glowWidth](https://developer.apple.com/documentation/spritekit/skshapenode/1520116-glowwidth)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat glowWidth ``` |
| To | ``` @property(nonatomic) CGFloat glowWidth ``` |

Modified [SKShapeNode.lineWidth](https://developer.apple.com/documentation/spritekit/skshapenode/1519885-linewidth)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat lineWidth ``` |
| To | ``` @property(nonatomic) CGFloat lineWidth ``` |

Modified [SKShapeNode.path](https://developer.apple.com/documentation/spritekit/skshapenode/1519741-path)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGPathRef path ``` |
| To | ``` @property(nonatomic) CGPathRef path ``` |

Modified [SKShapeNode.strokeColor](https://developer.apple.com/documentation/spritekit/skshapenode/1519748-strokecolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) NSColor *strokeColor ``` |
| To | ``` @property(nonatomic, retain) NSColor *strokeColor ``` |

SKSpriteNode.hAdded [-[SKSpriteNode initWithCoder:]](https://developer.apple.com/documentation/spritekit/skspritenode/1520399-init)Added [SKSpriteNode.lightingBitMask](https://developer.apple.com/documentation/spritekit/skspritenode/1519637-lightingbitmask)Added [SKSpriteNode.normalTexture](https://developer.apple.com/documentation/spritekit/skspritenode/1519657-normaltexture)Added [SKSpriteNode.shader](https://developer.apple.com/documentation/spritekit/skspritenode/1519714-shader)Added [SKSpriteNode.shadowCastBitMask](https://developer.apple.com/documentation/spritekit/skspritenode/1520325-shadowcastbitmask)Added [SKSpriteNode.shadowedBitMask](https://developer.apple.com/documentation/spritekit/skspritenode/1519974-shadowedbitmask)Added [+[SKSpriteNode spriteNodeWithImageNamed:normalMapped:]](https://developer.apple.com/documentation/spritekit/skspritenode/1519721-init)Added [+[SKSpriteNode spriteNodeWithTexture:normalMap:]](https://developer.apple.com/documentation/spritekit/skspritenode/1520153-spritenodewithtexture)Modified [SKSpriteNode.anchorPoint](https://developer.apple.com/documentation/spritekit/skspritenode/1519877-anchorpoint)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGPoint anchorPoint ``` |
| To | ``` @property(nonatomic) CGPoint anchorPoint ``` |

Modified [SKSpriteNode.blendMode](https://developer.apple.com/documentation/spritekit/skspritenode/1519931-blendmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) SKBlendMode blendMode ``` |
| To | ``` @property(nonatomic) SKBlendMode blendMode ``` |

Modified [SKSpriteNode.centerRect](https://developer.apple.com/documentation/spritekit/skspritenode/1520119-centerrect)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGRect centerRect ``` |
| To | ``` @property(nonatomic) CGRect centerRect ``` |

Modified [SKSpriteNode.color](https://developer.apple.com/documentation/spritekit/skspritenode/1519639-color)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) NSColor *color ``` |
| To | ``` @property(nonatomic, retain) NSColor *color ``` |

Modified [SKSpriteNode.colorBlendFactor](https://developer.apple.com/documentation/spritekit/skspritenode/1519780-colorblendfactor)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGFloat colorBlendFactor ``` |
| To | ``` @property(nonatomic) CGFloat colorBlendFactor ``` |

Modified [-[SKSpriteNode initWithTexture:color:size:]](https://developer.apple.com/documentation/spritekit/skspritenode/1520029-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [SKSpriteNode.size](https://developer.apple.com/documentation/spritekit/skspritenode/1519668-size)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGSize size ``` |
| To | ``` @property(nonatomic) CGSize size ``` |

Modified [SKSpriteNode.texture](https://developer.apple.com/documentation/spritekit/skspritenode/1520011-texture)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) SKTexture *texture ``` |
| To | ``` @property(nonatomic, retain) SKTexture *texture ``` |

SKTexture.hAdded [-[SKTexture textureByGeneratingNormalMap]](https://developer.apple.com/documentation/spritekit/sktexture/1519687-texturebygeneratingnormalmap)Added [-[SKTexture textureByGeneratingNormalMapWithSmoothness:contrast:]](https://developer.apple.com/documentation/spritekit/sktexture/1520441-texturebygeneratingnormalmapwith)Added [+[SKTexture textureNoiseWithSmoothness:size:grayscale:]](https://developer.apple.com/documentation/spritekit/sktexture/1519971-texturenoisewithsmoothness)Added [+[SKTexture textureVectorNoiseWithSmoothness:size:]](https://developer.apple.com/documentation/spritekit/sktexture/1520393-texturevectornoisewithsmoothness)Added [+[SKTexture textureWithData:size:flipped:]](https://developer.apple.com/documentation/spritekit/sktexture/1519674-texturewithdata)Modified [SKTexture.filteringMode](https://developer.apple.com/documentation/spritekit/sktexture/1519659-filteringmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) SKTextureFilteringMode filteringMode ``` |
| To | ``` @property(nonatomic) SKTextureFilteringMode filteringMode ``` |

Modified [-[SKTexture textureByApplyingCIFilter:]](https://developer.apple.com/documentation/spritekit/sktexture/1520388-texturebyapplyingcifilter)

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
| From | ``` + (SKTexture *)textureWithImage:(NSImage *)image ``` |
| To | ``` + (instancetype)textureWithImage:(NSImage *)image ``` |

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

Modified [SKTexture.usesMipmaps](https://developer.apple.com/documentation/spritekit/sktexture/1519960-usesmipmaps)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL usesMipmaps ``` |
| To | ``` @property(nonatomic) BOOL usesMipmaps ``` |

SKTextureAtlas.hAdded [+[SKTextureAtlas atlasWithDictionary:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427383-atlaswithdictionary)Modified [+[SKTextureAtlas atlasNamed:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427381-atlasnamed)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTextureAtlas *)atlasNamed:(NSString *)name ``` |
| To | ``` + (instancetype)atlasNamed:(NSString *)name ``` |

Modified [SKTextureAtlas.textureNames](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427373-texturenames)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSArray *textureNames ``` |
| To | ``` @property(nonatomic, readonly) NSArray *textureNames ``` |

SKTransition.hModified [SKTransition.pausesIncomingScene](https://developer.apple.com/documentation/spritekit/sktransition/1395883-pausesincomingscene)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL pausesIncomingScene ``` |
| To | ``` @property(nonatomic) BOOL pausesIncomingScene ``` |

Modified [SKTransition.pausesOutgoingScene](https://developer.apple.com/documentation/spritekit/sktransition/1395877-pausesoutgoingscene)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL pausesOutgoingScene ``` |
| To | ``` @property(nonatomic) BOOL pausesOutgoingScene ``` |

SKUniform.h (Added)Added [SKUniform](https://developer.apple.com/documentation/spritekit/skuniform)Added [SKUniform.floatMatrix2Value](https://developer.apple.com/documentation/spritekit/skuniform/1455410-floatmatrix2value)Added [SKUniform.floatMatrix3Value](https://developer.apple.com/documentation/spritekit/skuniform/1455438-floatmatrix3value)Added [SKUniform.floatMatrix4Value](https://developer.apple.com/documentation/spritekit/skuniform/1455460-floatmatrix4value)Added [SKUniform.floatValue](https://developer.apple.com/documentation/spritekit/skuniform/1455406-floatvalue)Added [SKUniform.floatVector2Value](https://developer.apple.com/documentation/spritekit/skuniform/1455436-floatvector2value)Added [SKUniform.floatVector3Value](https://developer.apple.com/documentation/spritekit/skuniform/1455434-floatvector3value)Added [SKUniform.floatVector4Value](https://developer.apple.com/documentation/spritekit/skuniform/1455404-floatvector4value)Added [-[SKUniform initWithName:]](https://developer.apple.com/documentation/spritekit/skuniform/1455420-initwithname)Added [-[SKUniform initWithName:float:]](https://developer.apple.com/documentation/spritekit/skuniform/1455447-init)Added [-[SKUniform initWithName:floatMatrix2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455431-initwithname)Added [-[SKUniform initWithName:floatMatrix3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455462-init)Added [-[SKUniform initWithName:floatMatrix4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455429-init)Added [-[SKUniform initWithName:floatVector2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455444-initwithname)Added [-[SKUniform initWithName:floatVector3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455416-initwithname)Added [-[SKUniform initWithName:floatVector4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455418-initwithname)Added [-[SKUniform initWithName:texture:]](https://developer.apple.com/documentation/spritekit/skuniform/1455452-init)Added [SKUniform.name](https://developer.apple.com/documentation/spritekit/skuniform/1455442-name)Added [SKUniform.textureValue](https://developer.apple.com/documentation/spritekit/skuniform/1455449-texturevalue)Added [SKUniform.uniformType](https://developer.apple.com/documentation/spritekit/skuniform/1455440-uniformtype)Added [+[SKUniform uniformWithName:]](https://developer.apple.com/documentation/spritekit/skuniform/1455458-uniformwithname)Added [+[SKUniform uniformWithName:float:]](https://developer.apple.com/documentation/spritekit/skuniform/1455412-uniformwithname)Added [+[SKUniform uniformWithName:floatMatrix2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455463-uniformwithname)Added [+[SKUniform uniformWithName:floatMatrix3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455402-uniformwithname)Added [+[SKUniform uniformWithName:floatMatrix4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455446-uniformwithname)Added [+[SKUniform uniformWithName:floatVector2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455472-uniformwithname)Added [+[SKUniform uniformWithName:floatVector3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455414-uniformwithname)Added [+[SKUniform uniformWithName:floatVector4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455465-uniformwithname)Added [+[SKUniform uniformWithName:texture:]](https://developer.apple.com/documentation/spritekit/skuniform/1455470-uniformwithname)Added [SKUniformType](https://developer.apple.com/documentation/spritekit/skuniformtype)Added [SKUniformTypeFloat](https://developer.apple.com/documentation/spritekit/skuniformtype/float)Added [SKUniformTypeFloatMatrix2](https://developer.apple.com/documentation/spritekit/skuniformtype/floatmatrix2)Added [SKUniformTypeFloatMatrix3](https://developer.apple.com/documentation/spritekit/skuniformtype/floatmatrix3)Added [SKUniformTypeFloatMatrix4](https://developer.apple.com/documentation/spritekit/skuniformtype/floatmatrix4)Added [SKUniformTypeFloatVector2](https://developer.apple.com/documentation/spritekit/skuniformtype/skuniformtypefloatvector2)Added [SKUniformTypeFloatVector3](https://developer.apple.com/documentation/spritekit/skuniformtype/floatvector3)Added [SKUniformTypeFloatVector4](https://developer.apple.com/documentation/spritekit/skuniformtype/skuniformtypefloatvector4)Added [SKUniformTypeNone](https://developer.apple.com/documentation/spritekit/skuniformtype/skuniformtypenone)Added [SKUniformTypeTexture](https://developer.apple.com/documentation/spritekit/skuniformtype/texture)SKVideoNode.hAdded [-[SKVideoNode initWithCoder:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407907-initwithcoder)Modified [SKVideoNode.anchorPoint](https://developer.apple.com/documentation/spritekit/skvideonode/1407904-anchorpoint)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGPoint anchorPoint ``` |
| To | ``` @property(nonatomic) CGPoint anchorPoint ``` |

Modified [-[SKVideoNode initWithAVPlayer:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407900-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[SKVideoNode initWithVideoFileNamed:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407918-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[SKVideoNode initWithVideoURL:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407908-initwithvideourl)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [SKVideoNode.size](https://developer.apple.com/documentation/spritekit/skvideonode/1407916-size)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) CGSize size ``` |
| To | ``` @property(nonatomic) CGSize size ``` |

SKView.hAdded [SKView.allowsTransparency](https://developer.apple.com/documentation/spritekit/skview/1519697-allowstransparency)Added [SKView.shouldCullNonVisibleNodes](https://developer.apple.com/documentation/spritekit/skview/1519683-shouldcullnonvisiblenodes)Added [SKView.showsFields](https://developer.apple.com/documentation/spritekit/skview/1520443-showsfields)Added [SKView.showsPhysics](https://developer.apple.com/documentation/spritekit/skview/1520389-showsphysics)Added [SKView.showsQuadCount](https://developer.apple.com/documentation/spritekit/skview/1519652-showsquadcount)Added [-[SKView textureFromNode:crop:]](https://developer.apple.com/documentation/spritekit/skview/1519994-texturefromnode)Modified [SKView.asynchronous](https://developer.apple.com/documentation/spritekit/skview/1520229-asynchronous)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isAsynchronous, atomic) BOOL asynchronous ``` |
| To | ``` @property(nonatomic, getter=isAsynchronous) BOOL asynchronous ``` |

Modified [SKView.frameInterval](https://developer.apple.com/documentation/spritekit/skview/1520008-frameinterval)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) NSInteger frameInterval ``` |
| To | ``` @property(nonatomic) NSInteger frameInterval ``` |

Modified [SKView.ignoresSiblingOrder](https://developer.apple.com/documentation/spritekit/skview/1520215-ignoressiblingorder)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL ignoresSiblingOrder ``` |
| To | ``` @property(nonatomic) BOOL ignoresSiblingOrder ``` |

Modified [SKView.paused](https://developer.apple.com/documentation/spritekit/skview/1519654-ispaused)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=isPaused, atomic) BOOL paused ``` |
| To | ``` @property(nonatomic, getter=isPaused) BOOL paused ``` |

Modified [SKView.scene](https://developer.apple.com/documentation/spritekit/skview/1520084-scene)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) SKScene *scene ``` |
| To | ``` @property(nonatomic, readonly) SKScene *scene ``` |

Modified [SKView.showsDrawCount](https://developer.apple.com/documentation/spritekit/skview/1520112-showsdrawcount)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL showsDrawCount ``` |
| To | ``` @property(nonatomic) BOOL showsDrawCount ``` |

Modified [SKView.showsFPS](https://developer.apple.com/documentation/spritekit/skview/1519590-showsfps)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL showsFPS ``` |
| To | ``` @property(nonatomic) BOOL showsFPS ``` |

Modified [SKView.showsNodeCount](https://developer.apple.com/documentation/spritekit/skview/1520156-showsnodecount)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic) BOOL showsNodeCount ``` |
| To | ``` @property(nonatomic) BOOL showsNodeCount ``` |

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
