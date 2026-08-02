---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/SceneKit.html
archived_at: '2026-07-15T07:34:47.225401Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# SceneKit Changes

## SceneKit

SCNAction.h (Added)Added [SCNAction](https://developer.apple.com/documentation/scenekit/scnaction)Added [+[SCNAction customActionWithDuration:actionBlock:]](https://developer.apple.com/documentation/scenekit/scnaction/1523692-customactionwithduration)Added [SCNAction.duration](https://developer.apple.com/documentation/scenekit/scnaction/1524162-duration)Added [+[SCNAction fadeInWithDuration:]](https://developer.apple.com/documentation/scenekit/scnaction/1522777-fadein)Added [+[SCNAction fadeOpacityBy:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523595-fadeopacityby)Added [+[SCNAction fadeOpacityTo:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523875-fadeopacityto)Added [+[SCNAction fadeOutWithDuration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523922-fadeoutwithduration)Added [+[SCNAction group:]](https://developer.apple.com/documentation/scenekit/scnaction/1522779-group)Added [+[SCNAction javaScriptActionWithScript:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523984-javascriptaction)Added [+[SCNAction moveBy:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1522605-move)Added [+[SCNAction moveByX:y:z:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523238-moveby)Added [+[SCNAction moveTo:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1522826-move)Added [+[SCNAction removeFromParentNode]](https://developer.apple.com/documentation/scenekit/scnaction/1522966-removefromparentnode)Added [+[SCNAction repeatAction:count:]](https://developer.apple.com/documentation/scenekit/scnaction/1522764-repeat)Added [+[SCNAction repeatActionForever:]](https://developer.apple.com/documentation/scenekit/scnaction/1522908-repeatactionforever)Added [-[SCNAction reversedAction]](https://developer.apple.com/documentation/scenekit/scnaction/1522815-reversed)Added [+[SCNAction rotateByAngle:aroundAxis:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523805-rotate)Added [+[SCNAction rotateByX:y:z:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523522-rotatebyx)Added [+[SCNAction rotateToAxisAngle:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1524191-rotatetoaxisangle)Added [+[SCNAction rotateToX:y:z:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1524044-rotateto)Added [+[SCNAction rotateToX:y:z:duration:shortestUnitArc:]](https://developer.apple.com/documentation/scenekit/scnaction/1522808-rotatetox)Added [+[SCNAction runBlock:]](https://developer.apple.com/documentation/scenekit/scnaction/1523637-runblock)Added [+[SCNAction runBlock:queue:]](https://developer.apple.com/documentation/scenekit/scnaction/1522875-run)Added [+[SCNAction scaleBy:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523129-scaleby)Added [+[SCNAction scaleTo:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523322-scale)Added [+[SCNAction sequence:]](https://developer.apple.com/documentation/scenekit/scnaction/1522793-sequence)Added [SCNAction.speed](https://developer.apple.com/documentation/scenekit/scnaction/1522811-speed)Added [SCNAction.timingFunction](https://developer.apple.com/documentation/scenekit/scnaction/1524130-timingfunction)Added [SCNAction.timingMode](https://developer.apple.com/documentation/scenekit/scnaction/1524055-timingmode)Added [+[SCNAction waitForDuration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523915-wait)Added [+[SCNAction waitForDuration:withRange:]](https://developer.apple.com/documentation/scenekit/scnaction/1523086-wait)Added [SCNActionable](https://developer.apple.com/documentation/scenekit/scnactionable)Added [-[SCNActionable actionForKey:]](https://developer.apple.com/documentation/scenekit/scnactionable/1523287-action)Added [-[SCNActionable hasActions]](https://developer.apple.com/documentation/scenekit/scnactionable/1523794-hasactions)Added [-[SCNActionable removeActionForKey:]](https://developer.apple.com/documentation/scenekit/scnactionable/1523617-removeactionforkey)Added [-[SCNActionable removeAllActions]](https://developer.apple.com/documentation/scenekit/scnactionable/1524181-removeallactions)Added [-[SCNActionable runAction:]](https://developer.apple.com/documentation/scenekit/scnactionable/1523164-runaction)Added [-[SCNActionable runAction:completionHandler:]](https://developer.apple.com/documentation/scenekit/scnactionable/1524219-runaction)Added [-[SCNActionable runAction:forKey:]](https://developer.apple.com/documentation/scenekit/scnactionable/1524222-runaction)Added [-[SCNActionable runAction:forKey:completionHandler:]](https://developer.apple.com/documentation/scenekit/scnactionable/1522791-runaction)Added SCNAction(SCNActions)Added [SCNActionTimingFunction](https://developer.apple.com/documentation/scenekit/scnactiontimingfunction)Added [SCNActionTimingMode](https://developer.apple.com/documentation/scenekit/scnactiontimingmode)Added [SCNActionTimingModeEaseIn](https://developer.apple.com/documentation/scenekit/scnactiontimingmode/scnactiontimingmodeeasein)Added [SCNActionTimingModeEaseInEaseOut](https://developer.apple.com/documentation/scenekit/scnactiontimingmode/easeineaseout)Added [SCNActionTimingModeEaseOut](https://developer.apple.com/documentation/scenekit/scnactiontimingmode/easeout)Added [SCNActionTimingModeLinear](https://developer.apple.com/documentation/scenekit/scnactiontimingmode/scnactiontimingmodelinear)SCNAnimation.hAdded [-[SCNAnimatable removeAnimationForKey:fadeOutDuration:]](https://developer.apple.com/documentation/scenekit/scnanimatable/1522841-removeanimation)Modified [SCNAnimatable](https://developer.apple.com/documentation/scenekit/scnanimatable)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSObject |

SCNBoundingVolume.hModified [SCNBoundingVolume](https://developer.apple.com/documentation/scenekit/scnboundingvolume)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSObject |

SCNCamera.hAdded [SCNCamera.categoryBitMask](https://developer.apple.com/documentation/scenekit/scncamera/1436625-categorybitmask)Modified [SCNCamera](https://developer.apple.com/documentation/scenekit/scncamera)

|  | Protocols |
| --- | --- |
| From | NSCopying, SCNAnimatable |
| To | NSCopying, NSSecureCoding, SCNAnimatable, SCNTechniqueSupport |

Modified [-[SCNCamera projectionTransform]](https://developer.apple.com/documentation/scenekit/scncamera/1436619-projectiontransform)

|  | Declaration |
| --- | --- |
| From | ``` - (CATransform3D)projectionTransform ``` |
| To | ``` - (SCNMatrix4)projectionTransform ``` |

Modified [-[SCNCamera setProjectionTransform:]](https://developer.apple.com/documentation/scenekit/scncamera/1436590-setprojectiontransform)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setProjectionTransform:(CATransform3D)projectionTransform ``` |
| To | ``` - (void)setProjectionTransform:(SCNMatrix4)projectionTransform ``` |

SCNConstraint.hAdded [SCNConstraint.influenceFactor](https://developer.apple.com/documentation/scenekit/scnconstraint/1468692-influencefactor)Added [SCNIKConstraint](https://developer.apple.com/documentation/scenekit/scnikconstraint)Added [SCNIKConstraint.chainRootNode](https://developer.apple.com/documentation/scenekit/scnikconstraint/1468690-chainrootnode)Added [+[SCNIKConstraint inverseKinematicsConstraintWithChainRootNode:]](https://developer.apple.com/documentation/scenekit/scnikconstraint/1468653-inversekinematicsconstraintwithc)Added [-[SCNIKConstraint maxAllowedRotationAngleForJoint:]](https://developer.apple.com/documentation/scenekit/scnikconstraint/1468681-maxallowedrotationangle)Added [-[SCNIKConstraint setMaxAllowedRotationAngle:forJoint:]](https://developer.apple.com/documentation/scenekit/scnikconstraint/1468649-setmaxallowedrotationangle)Added [SCNIKConstraint.targetPosition](https://developer.apple.com/documentation/scenekit/scnikconstraint/1468651-targetposition)Modified [SCNConstraint](https://developer.apple.com/documentation/scenekit/scnconstraint)

|  | Protocols |
| --- | --- |
| From | NSCopying, SCNAnimatable |
| To | NSCopying, NSSecureCoding, SCNAnimatable |

Modified [+[SCNTransformConstraint transformConstraintInWorldSpace:withBlock:]](https://developer.apple.com/documentation/scenekit/scntransformconstraint/1468679-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)transformConstraintInWorldSpace:(BOOL)world withBlock:(CATransform3D (^)(SCNNode *node, CATransform3D transform))block ``` |
| To | ``` + (instancetype)transformConstraintInWorldSpace:(BOOL)world withBlock:(SCNMatrix4 (^)(SCNNode *node, SCNMatrix4 transform))block ``` |

SCNGeometry.hAdded [SCNGeometry.edgeCreasesElement](https://developer.apple.com/documentation/scenekit/scngeometry/1523246-edgecreaseselement)Added [SCNGeometry.edgeCreasesSource](https://developer.apple.com/documentation/scenekit/scngeometry/1523479-edgecreasessource)Added [SCNGeometry.subdivisionLevel](https://developer.apple.com/documentation/scenekit/scngeometry/1524177-subdivisionlevel)Added [SCNGeometrySourceSemanticBoneIndices](https://developer.apple.com/documentation/scenekit/scngeometrysourcesemanticboneindices)Added [SCNGeometrySourceSemanticBoneWeights](https://developer.apple.com/documentation/scenekit/scngeometrysourcesemanticboneweights)Added [SCNGeometrySourceSemanticEdgeCrease](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic/1523285-edgecrease)Added [SCNGeometrySourceSemanticVertexCrease](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic/1523206-vertexcrease)Modified [SCNGeometry](https://developer.apple.com/documentation/scenekit/scngeometry)

|  | Protocols |
| --- | --- |
| From | NSCopying, SCNAnimatable, SCNBoundingVolume, SCNShadable |
| To | NSCopying, NSSecureCoding, SCNAnimatable, SCNBoundingVolume, SCNShadable |

Modified [SCNGeometryElement](https://developer.apple.com/documentation/scenekit/scngeometryelement)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSSecureCoding |

Modified [SCNGeometrySource](https://developer.apple.com/documentation/scenekit/scngeometrysource)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSSecureCoding |

Modified [+[SCNGeometrySource geometrySourceWithNormals:count:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1522882-geometrysourcewithnormals)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)geometrySourceWithNormals:(SCNVector3 *)normals count:(NSInteger)count ``` |
| To | ``` + (instancetype)geometrySourceWithNormals:(const SCNVector3 *)normals count:(NSInteger)count ``` |

Modified [+[SCNGeometrySource geometrySourceWithTextureCoordinates:count:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1522718-geometrysourcewithtexturecoordin)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)geometrySourceWithTextureCoordinates:(CGPoint *)texcoord count:(NSInteger)count ``` |
| To | ``` + (instancetype)geometrySourceWithTextureCoordinates:(const CGPoint *)texcoord count:(NSInteger)count ``` |

Modified [+[SCNGeometrySource geometrySourceWithVertices:count:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1523882-geometrysourcewithvertices)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)geometrySourceWithVertices:(SCNVector3 *)vertices count:(NSInteger)count ``` |
| To | ``` + (instancetype)geometrySourceWithVertices:(const SCNVector3 *)vertices count:(NSInteger)count ``` |

SCNJavascript.h (Added)Added [SCNExportJavaScriptModule()](https://developer.apple.com/documentation/scenekit/1524164-scnexportjavascriptmodule)SCNLayer.hModified [SCNLayer](https://developer.apple.com/documentation/scenekit/scnlayer)

|  | Protocols |
| --- | --- |
| From | SCNSceneRenderer |
| To | SCNSceneRenderer, SCNTechniqueSupport |

SCNLevelOfDetail.hModified [SCNLevelOfDetail](https://developer.apple.com/documentation/scenekit/scnlevelofdetail)

|  | Protocols |
| --- | --- |
| From | NSCopying |
| To | NSCopying, NSSecureCoding |

SCNLight.hAdded [SCNLight.attenuationEndDistance](https://developer.apple.com/documentation/scenekit/scnlight/1524140-attenuationenddistance)Added [SCNLight.attenuationFalloffExponent](https://developer.apple.com/documentation/scenekit/scnlight/1522879-attenuationfalloffexponent)Added [SCNLight.attenuationStartDistance](https://developer.apple.com/documentation/scenekit/scnlight/1524223-attenuationstartdistance)Added [SCNLight.categoryBitMask](https://developer.apple.com/documentation/scenekit/scnlight/1523669-categorybitmask)Added [SCNLight.orthographicScale](https://developer.apple.com/documentation/scenekit/scnlight/1523951-orthographicscale)Added [SCNLight.shadowBias](https://developer.apple.com/documentation/scenekit/scnlight/1522849-shadowbias)Added [SCNLight.shadowMapSize](https://developer.apple.com/documentation/scenekit/scnlight/1524127-shadowmapsize)Added [SCNLight.shadowMode](https://developer.apple.com/documentation/scenekit/scnlight/1522847-shadowmode)Added [SCNLight.shadowSampleCount](https://developer.apple.com/documentation/scenekit/scnlight/1523300-shadowsamplecount)Added [SCNLight.spotInnerAngle](https://developer.apple.com/documentation/scenekit/scnlight/1522797-spotinnerangle)Added [SCNLight.spotOuterAngle](https://developer.apple.com/documentation/scenekit/scnlight/1523382-spotouterangle)Added [SCNLight.zFar](https://developer.apple.com/documentation/scenekit/scnlight/1522845-zfar)Added [SCNLight.zNear](https://developer.apple.com/documentation/scenekit/scnlight/1522630-znear)Added [SCNShadowMode](https://developer.apple.com/documentation/scenekit/scnshadowmode)Added [SCNShadowModeDeferred](https://developer.apple.com/documentation/scenekit/scnshadowmode/scnshadowmodedeferred)Added [SCNShadowModeForward](https://developer.apple.com/documentation/scenekit/scnshadowmode/scnshadowmodeforward)Added [SCNShadowModeModulated](https://developer.apple.com/documentation/scenekit/scnshadowmode/scnshadowmodemodulated)Modified [SCNLight](https://developer.apple.com/documentation/scenekit/scnlight)

|  | Protocols |
| --- | --- |
| From | NSCopying, SCNAnimatable |
| To | NSCopying, NSSecureCoding, SCNAnimatable, SCNTechniqueSupport |

Modified [-[SCNLight attributeForKey:]](https://developer.apple.com/documentation/scenekit/scnlight/1523345-attribute)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[SCNLight setAttribute:forKey:]](https://developer.apple.com/documentation/scenekit/scnlight/1523148-setattribute)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [SCNLightAttenuationEndKey](https://developer.apple.com/documentation/scenekit/scnlightattenuationendkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [SCNLightAttenuationFalloffExponentKey](https://developer.apple.com/documentation/scenekit/scnlightattenuationfalloffexponentkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [SCNLightAttenuationStartKey](https://developer.apple.com/documentation/scenekit/scnlightattenuationstartkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [SCNLightShadowFarClippingKey](https://developer.apple.com/documentation/scenekit/scnlightshadowfarclippingkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [SCNLightShadowNearClippingKey](https://developer.apple.com/documentation/scenekit/scnlightshadownearclippingkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [SCNLightSpotInnerAngleKey](https://developer.apple.com/documentation/scenekit/scnlightspotinneranglekey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [SCNLightSpotOuterAngleKey](https://developer.apple.com/documentation/scenekit/scnlightspotouteranglekey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

SCNMaterial.hModified [SCNMaterial](https://developer.apple.com/documentation/scenekit/scnmaterial)

|  | Protocols |
| --- | --- |
| From | NSCopying, SCNAnimatable, SCNShadable |
| To | NSCopying, NSSecureCoding, SCNAnimatable, SCNShadable |

SCNMaterialProperty.hModified [SCNMaterialProperty](https://developer.apple.com/documentation/scenekit/scnmaterialproperty)

|  | Protocols |
| --- | --- |
| From | SCNAnimatable |
| To | NSSecureCoding, SCNAnimatable |

Modified [SCNMaterialProperty.contentsTransform](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/1395388-contentstransform)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) CATransform3D contentsTransform ``` |
| To | ``` @property(nonatomic) SCNMatrix4 contentsTransform ``` |

SCNMorpher.hModified [SCNMorpher](https://developer.apple.com/documentation/scenekit/scnmorpher)

|  | Protocols |
| --- | --- |
| From | SCNAnimatable |
| To | NSSecureCoding, SCNAnimatable |

SCNNode.hAdded [SCNNode.castsShadow](https://developer.apple.com/documentation/scenekit/scnnode/1407955-castsshadow)Added [SCNNode.categoryBitMask](https://developer.apple.com/documentation/scenekit/scnnode/1407994-categorybitmask)Added [-[SCNNode enumerateChildNodesUsingBlock:]](https://developer.apple.com/documentation/scenekit/scnnode/1408032-enumeratechildnodesusingblock)Added [SCNNode.eulerAngles](https://developer.apple.com/documentation/scenekit/scnnode/1407980-eulerangles)Added [SCNNode.orientation](https://developer.apple.com/documentation/scenekit/scnnode/1408048-orientation)Added [SCNNode.paused](https://developer.apple.com/documentation/scenekit/scnnode/1407962-ispaused)Added [SCNNode.physicsBody](https://developer.apple.com/documentation/scenekit/scnnode/1407988-physicsbody)Added [SCNNode.physicsField](https://developer.apple.com/documentation/scenekit/scnnode/1408006-physicsfield)Modified [SCNNode](https://developer.apple.com/documentation/scenekit/scnnode)

|  | Protocols |
| --- | --- |
| From | NSCopying, SCNAnimatable, SCNBoundingVolume |
| To | NSCopying, NSSecureCoding, SCNActionable, SCNAnimatable, SCNBoundingVolume |

Modified [-[SCNNode convertTransform:fromNode:]](https://developer.apple.com/documentation/scenekit/scnnode/1407996-converttransform)

|  | Declaration |
| --- | --- |
| From | ``` - (CATransform3D)convertTransform:(CATransform3D)transform fromNode:(SCNNode *)node ``` |
| To | ``` - (SCNMatrix4)convertTransform:(SCNMatrix4)transform fromNode:(SCNNode *)node ``` |

Modified [-[SCNNode convertTransform:toNode:]](https://developer.apple.com/documentation/scenekit/scnnode/1407986-converttransform)

|  | Declaration |
| --- | --- |
| From | ``` - (CATransform3D)convertTransform:(CATransform3D)transform toNode:(SCNNode *)node ``` |
| To | ``` - (SCNMatrix4)convertTransform:(SCNMatrix4)transform toNode:(SCNNode *)node ``` |

Modified [SCNNode.pivot](https://developer.apple.com/documentation/scenekit/scnnode/1408044-pivot)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) CATransform3D pivot ``` |
| To | ``` @property(nonatomic) SCNMatrix4 pivot ``` |

Modified [SCNNode.transform](https://developer.apple.com/documentation/scenekit/scnnode/1407964-transform)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) CATransform3D transform ``` |
| To | ``` @property(nonatomic) SCNMatrix4 transform ``` |

Modified [SCNNode.worldTransform](https://developer.apple.com/documentation/scenekit/scnnode/1407970-worldtransform)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) CATransform3D worldTransform ``` |
| To | ``` @property(nonatomic, readonly) SCNMatrix4 worldTransform ``` |

Modified [-[SCNNodeRendererDelegate renderNode:renderer:arguments:]](https://developer.apple.com/documentation/scenekit/scnnoderendererdelegate/1407993-rendernode)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

SCNParametricGeometry.hAdded [SCNFloor.reflectionResolutionScaleFactor](https://developer.apple.com/documentation/scenekit/scnfloor/1522809-reflectionresolutionscalefactor)SCNParticleSystem.h (Added)Added [-[SCNNode addParticleSystem:]](https://developer.apple.com/documentation/scenekit/scnnode/1523123-addparticlesystem)Added [SCNNode.particleSystems](https://developer.apple.com/documentation/scenekit/scnnode/1522705-particlesystems)Added [-[SCNNode removeAllParticleSystems]](https://developer.apple.com/documentation/scenekit/scnnode/1522801-removeallparticlesystems)Added [-[SCNNode removeParticleSystem:]](https://developer.apple.com/documentation/scenekit/scnnode/1524014-removeparticlesystem)Added [SCNParticlePropertyController](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller)Added [SCNParticlePropertyController.animation](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1523707-animation)Added [+[SCNParticlePropertyController controllerWithAnimation:]](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1523579-controllerwithanimation)Added [SCNParticlePropertyController.inputBias](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1523994-inputbias)Added [SCNParticlePropertyController.inputMode](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1522852-inputmode)Added [SCNParticlePropertyController.inputOrigin](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1522895-inputorigin)Added [SCNParticlePropertyController.inputProperty](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1522973-inputproperty)Added [SCNParticlePropertyController.inputScale](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1522903-inputscale)Added [SCNParticleSystem](https://developer.apple.com/documentation/scenekit/scnparticlesystem)Added [SCNParticleSystem.acceleration](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522766-acceleration)Added [-[SCNParticleSystem addModifierForProperties:atStage:withBlock:]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522635-addmodifierforproperties)Added [SCNParticleSystem.affectedByGravity](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523452-isaffectedbygravity)Added [SCNParticleSystem.affectedByPhysicsFields](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523353-affectedbyphysicsfields)Added [SCNParticleSystem.birthDirection](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523361-birthdirection)Added [SCNParticleSystem.birthLocation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522899-birthlocation)Added [SCNParticleSystem.birthRate](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522857-birthrate)Added [SCNParticleSystem.birthRateVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524147-birthratevariation)Added [SCNParticleSystem.blackPassEnabled](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523901-blackpassenabled)Added [SCNParticleSystem.blendMode](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523728-blendmode)Added [SCNParticleSystem.colliderNodes](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523516-collidernodes)Added [SCNParticleSystem.dampingFactor](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522931-dampingfactor)Added [SCNParticleSystem.emissionDuration](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523998-emissionduration)Added [SCNParticleSystem.emissionDurationVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523842-emissiondurationvariation)Added [SCNParticleSystem.emitterShape](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522737-emittershape)Added [SCNParticleSystem.emittingDirection](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523600-emittingdirection)Added [SCNParticleSystem.fresnelExponent](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523317-fresnelexponent)Added [-[SCNParticleSystem handleEvent:forProperties:withBlock:]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523251-handleevent)Added [SCNParticleSystem.idleDuration](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522998-idleduration)Added [SCNParticleSystem.idleDurationVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523018-idledurationvariation)Added [SCNParticleSystem.imageSequenceAnimationMode](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522816-imagesequenceanimationmode)Added [SCNParticleSystem.imageSequenceColumnCount](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523462-imagesequencecolumncount)Added [SCNParticleSystem.imageSequenceFrameRate](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524075-imagesequenceframerate)Added [SCNParticleSystem.imageSequenceFrameRateVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523667-imagesequenceframeratevariation)Added [SCNParticleSystem.imageSequenceInitialFrame](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523511-imagesequenceinitialframe)Added [SCNParticleSystem.imageSequenceInitialFrameVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523821-imagesequenceinitialframevariati)Added [SCNParticleSystem.imageSequenceRowCount](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523340-imagesequencerowcount)Added [SCNParticleSystem.lightingEnabled](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522794-islightingenabled)Added [SCNParticleSystem.local](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522855-local)Added [SCNParticleSystem.loops](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522618-loops)Added [SCNParticleSystem.orientationMode](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523131-orientationmode)Added [SCNParticleSystem.particleAngle](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523896-particleangle)Added [SCNParticleSystem.particleAngleVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522828-particleanglevariation)Added [SCNParticleSystem.particleAngularVelocity](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522757-particleangularvelocity)Added [SCNParticleSystem.particleAngularVelocityVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523590-particleangularvelocityvariation)Added [SCNParticleSystem.particleBounce](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522637-particlebounce)Added [SCNParticleSystem.particleBounceVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522662-particlebouncevariation)Added [SCNParticleSystem.particleCharge](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523156-particlecharge)Added [SCNParticleSystem.particleChargeVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523377-particlechargevariation)Added [SCNParticleSystem.particleColor](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523248-particlecolor)Added [SCNParticleSystem.particleColorVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523639-particlecolorvariation)Added [SCNParticleSystem.particleDiesOnCollision](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523357-particlediesoncollision)Added [SCNParticleSystem.particleFriction](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524010-particlefriction)Added [SCNParticleSystem.particleFrictionVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522868-particlefrictionvariation)Added [SCNParticleSystem.particleImage](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524153-particleimage)Added [SCNParticleSystem.particleLifeSpan](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523575-particlelifespan)Added [SCNParticleSystem.particleLifeSpanVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523567-particlelifespanvariation)Added [SCNParticleSystem.particleMass](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522607-particlemass)Added [SCNParticleSystem.particleMassVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523408-particlemassvariation)Added [SCNParticleSystem.particleSize](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523508-particlesize)Added [SCNParticleSystem.particleSizeVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522716-particlesizevariation)Added [+[SCNParticleSystem particleSystem]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1564486-particlesystem)Added [+[SCNParticleSystem particleSystemNamed:inDirectory:]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522772-particlesystemnamed)Added [SCNParticleSystem.particleVelocity](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523946-particlevelocity)Added [SCNParticleSystem.particleVelocityVariation](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524157-particlevelocityvariation)Added [SCNParticleSystem.propertyControllers](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522775-propertycontrollers)Added [-[SCNParticleSystem removeAllModifiers]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523614-removeallmodifiers)Added [-[SCNParticleSystem removeModifiersOfStage:]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524077-removemodifiersofstage)Added [-[SCNParticleSystem reset]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522968-reset)Added [SCNParticleSystem.sortingMode](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522795-sortingmode)Added [SCNParticleSystem.speedFactor](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522988-speedfactor)Added [SCNParticleSystem.spreadingAngle](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522862-spreadingangle)Added [SCNParticleSystem.stretchFactor](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523338-stretchfactor)Added [SCNParticleSystem.systemSpawnedOnCollision](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524068-systemspawnedoncollision)Added [SCNParticleSystem.systemSpawnedOnDying](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524091-systemspawnedondying)Added [SCNParticleSystem.systemSpawnedOnLiving](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522751-systemspawnedonliving)Added [SCNParticleSystem.warmupDuration](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522597-warmupduration)Added [-[SCNScene addParticleSystem:withTransform:]](https://developer.apple.com/documentation/scenekit/scnscene/1523359-addparticlesystem)Added [SCNScene.particleSystems](https://developer.apple.com/documentation/scenekit/scnscene/1522787-particlesystems)Added [-[SCNScene removeAllParticleSystems]](https://developer.apple.com/documentation/scenekit/scnscene/1522786-removeallparticlesystems)Added [-[SCNScene removeParticleSystem:]](https://developer.apple.com/documentation/scenekit/scnscene/1523498-removeparticlesystem)Added SCNNode(SCNParticleSystemSupport)Added [SCNParticleBirthDirection](https://developer.apple.com/documentation/scenekit/scnparticlebirthdirection)Added [SCNParticleBirthDirectionConstant](https://developer.apple.com/documentation/scenekit/scnparticlebirthdirection/constant)Added [SCNParticleBirthDirectionRandom](https://developer.apple.com/documentation/scenekit/scnparticlebirthdirection/scnparticlebirthdirectionrandom)Added [SCNParticleBirthDirectionSurfaceNormal](https://developer.apple.com/documentation/scenekit/scnparticlebirthdirection/scnparticlebirthdirectionsurfacenormal)Added [SCNParticleBirthLocation](https://developer.apple.com/documentation/scenekit/scnparticlebirthlocation)Added [SCNParticleBirthLocationSurface](https://developer.apple.com/documentation/scenekit/scnparticlebirthlocation/surface)Added [SCNParticleBirthLocationVertex](https://developer.apple.com/documentation/scenekit/scnparticlebirthlocation/vertex)Added [SCNParticleBirthLocationVolume](https://developer.apple.com/documentation/scenekit/scnparticlebirthlocation/volume)Added [SCNParticleBlendMode](https://developer.apple.com/documentation/scenekit/scnparticleblendmode)Added [SCNParticleBlendModeAdditive](https://developer.apple.com/documentation/scenekit/scnparticleblendmode/additive)Added [SCNParticleBlendModeAlpha](https://developer.apple.com/documentation/scenekit/scnparticleblendmode/alpha)Added [SCNParticleBlendModeMultiply](https://developer.apple.com/documentation/scenekit/scnparticleblendmode/multiply)Added [SCNParticleBlendModeReplace](https://developer.apple.com/documentation/scenekit/scnparticleblendmode/replace)Added [SCNParticleBlendModeScreen](https://developer.apple.com/documentation/scenekit/scnparticleblendmode/screen)Added [SCNParticleBlendModeSubtract](https://developer.apple.com/documentation/scenekit/scnparticleblendmode/scnparticleblendmodesubtract)Added [SCNParticleEvent](https://developer.apple.com/documentation/scenekit/scnparticleevent)Added [SCNParticleEventBirth](https://developer.apple.com/documentation/scenekit/scnparticleevent/scnparticleeventbirth)Added [SCNParticleEventBlock](https://developer.apple.com/documentation/scenekit/scnparticleeventblock)Added [SCNParticleEventCollision](https://developer.apple.com/documentation/scenekit/scnparticleevent/collision)Added [SCNParticleEventDeath](https://developer.apple.com/documentation/scenekit/scnparticleevent/death)Added [SCNParticleImageSequenceAnimationMode](https://developer.apple.com/documentation/scenekit/scnparticleimagesequenceanimationmode)Added [SCNParticleImageSequenceAnimationModeAutoReverse](https://developer.apple.com/documentation/scenekit/scnparticleimagesequenceanimationmode/autoreverse)Added [SCNParticleImageSequenceAnimationModeClamp](https://developer.apple.com/documentation/scenekit/scnparticleimagesequenceanimationmode/scnparticleimagesequenceanimationmodeclamp)Added [SCNParticleImageSequenceAnimationModeRepeat](https://developer.apple.com/documentation/scenekit/scnparticleimagesequenceanimationmode/scnparticleimagesequenceanimationmoderepeat)Added [SCNParticleInputMode](https://developer.apple.com/documentation/scenekit/scnparticleinputmode)Added [SCNParticleInputModeOverDistance](https://developer.apple.com/documentation/scenekit/scnparticleinputmode/scnparticleinputmodeoverdistance)Added [SCNParticleInputModeOverLife](https://developer.apple.com/documentation/scenekit/scnparticleinputmode/scnparticleinputmodeoverlife)Added [SCNParticleInputModeOverOtherProperty](https://developer.apple.com/documentation/scenekit/scnparticleinputmode/scnparticleinputmodeoverotherproperty)Added [SCNParticleModifierBlock](https://developer.apple.com/documentation/scenekit/scnparticlemodifierblock)Added [SCNParticleModifierStage](https://developer.apple.com/documentation/scenekit/scnparticlemodifierstage)Added [SCNParticleModifierStagePostCollision](https://developer.apple.com/documentation/scenekit/scnparticlemodifierstage/postcollision)Added [SCNParticleModifierStagePostDynamics](https://developer.apple.com/documentation/scenekit/scnparticlemodifierstage/scnparticlemodifierstagepostdynamics)Added [SCNParticleModifierStagePreCollision](https://developer.apple.com/documentation/scenekit/scnparticlemodifierstage/scnparticlemodifierstageprecollision)Added [SCNParticleModifierStagePreDynamics](https://developer.apple.com/documentation/scenekit/scnparticlemodifierstage/predynamics)Added [SCNParticleOrientationMode](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode)Added [SCNParticleOrientationModeBillboardScreenAligned](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode/scnparticleorientationmodebillboardscreenaligned)Added [SCNParticleOrientationModeBillboardViewAligned](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode/billboardviewaligned)Added [SCNParticleOrientationModeBillboardYAligned](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode/scnparticleorientationmodebillboardyaligned)Added [SCNParticleOrientationModeFree](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode/scnparticleorientationmodefree)Added [SCNParticlePropertyAngle](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/1522778-angle)Added [SCNParticlePropertyAngularVelocity](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/1523211-angularvelocity)Added [SCNParticlePropertyBounce](https://developer.apple.com/documentation/scenekit/scnparticlepropertybounce)Added [SCNParticlePropertyCharge](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/1523372-charge)Added [SCNParticlePropertyColor](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/1523749-color)Added [SCNParticlePropertyContactNormal](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/1523709-contactnormal)Added [SCNParticlePropertyContactPoint](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/1522768-contactpoint)Added [SCNParticlePropertyFrame](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/1524217-frame)Added [SCNParticlePropertyFrameRate](https://developer.apple.com/documentation/scenekit/scnparticlepropertyframerate)Added [SCNParticlePropertyFriction](https://developer.apple.com/documentation/scenekit/scnparticlepropertyfriction)Added [SCNParticlePropertyLife](https://developer.apple.com/documentation/scenekit/scnparticlepropertylife)Added [SCNParticlePropertyOpacity](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/1522831-opacity)Added [SCNParticlePropertyPosition](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/1524136-position)Added [SCNParticlePropertyRotationAxis](https://developer.apple.com/documentation/scenekit/scnparticlepropertyrotationaxis)Added [SCNParticlePropertySize](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/1523860-size)Added [SCNParticlePropertyVelocity](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/1522760-velocity)Added [SCNParticleSortingMode](https://developer.apple.com/documentation/scenekit/scnparticlesortingmode)Added [SCNParticleSortingModeDistance](https://developer.apple.com/documentation/scenekit/scnparticlesortingmode/scnparticlesortingmodedistance)Added [SCNParticleSortingModeNone](https://developer.apple.com/documentation/scenekit/scnparticlesortingmode/none)Added [SCNParticleSortingModeOldestFirst](https://developer.apple.com/documentation/scenekit/scnparticlesortingmode/oldestfirst)Added [SCNParticleSortingModeProjectedDepth](https://developer.apple.com/documentation/scenekit/scnparticlesortingmode/projecteddepth)Added [SCNParticleSortingModeYoungestFirst](https://developer.apple.com/documentation/scenekit/scnparticlesortingmode/youngestfirst)Added SCNScene(SCNParticleSystemSupport)SCNPhysicsBehavior.h (Added)Added [SCNPhysicsBallSocketJoint](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint)Added [SCNPhysicsBallSocketJoint.anchorA](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387956-anchora)Added [SCNPhysicsBallSocketJoint.anchorB](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387965-anchorb)Added [SCNPhysicsBallSocketJoint.bodyA](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387981-bodya)Added [SCNPhysicsBallSocketJoint.bodyB](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387902-bodyb)Added [+[SCNPhysicsBallSocketJoint jointWithBody:anchor:]](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387975-init)Added [+[SCNPhysicsBallSocketJoint jointWithBodyA:anchorA:bodyB:anchorB:]](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387926-jointwithbodya)Added [SCNPhysicsBehavior](https://developer.apple.com/documentation/scenekit/scnphysicsbehavior)Added [SCNPhysicsHingeJoint](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint)Added [SCNPhysicsHingeJoint.anchorA](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387936-anchora)Added [SCNPhysicsHingeJoint.anchorB](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387979-anchorb)Added [SCNPhysicsHingeJoint.axisA](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387888-axisa)Added [SCNPhysicsHingeJoint.axisB](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387914-axisb)Added [SCNPhysicsHingeJoint.bodyA](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387973-bodya)Added [SCNPhysicsHingeJoint.bodyB](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387918-bodyb)Added [+[SCNPhysicsHingeJoint jointWithBody:axis:anchor:]](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387977-jointwithbody)Added [+[SCNPhysicsHingeJoint jointWithBodyA:axisA:anchorA:bodyB:axisB:anchorB:]](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387898-jointwithbodya)Added [SCNPhysicsSliderJoint](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint)Added [SCNPhysicsSliderJoint.anchorA](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387958-anchora)Added [SCNPhysicsSliderJoint.anchorB](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387916-anchorb)Added [SCNPhysicsSliderJoint.axisA](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387900-axisa)Added [SCNPhysicsSliderJoint.axisB](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387948-axisb)Added [SCNPhysicsSliderJoint.bodyA](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387987-bodya)Added [SCNPhysicsSliderJoint.bodyB](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387896-bodyb)Added [+[SCNPhysicsSliderJoint jointWithBody:axis:anchor:]](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387932-init)Added [+[SCNPhysicsSliderJoint jointWithBodyA:axisA:anchorA:bodyB:axisB:anchorB:]](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387922-jointwithbodya)Added [SCNPhysicsSliderJoint.maximumAngularLimit](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387924-maximumangularlimit)Added [SCNPhysicsSliderJoint.maximumLinearLimit](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387890-maximumlinearlimit)Added [SCNPhysicsSliderJoint.minimumAngularLimit](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387967-minimumangularlimit)Added [SCNPhysicsSliderJoint.minimumLinearLimit](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387920-minimumlinearlimit)Added [SCNPhysicsSliderJoint.motorMaximumForce](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387954-motormaximumforce)Added [SCNPhysicsSliderJoint.motorMaximumTorque](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387961-motormaximumtorque)Added [SCNPhysicsSliderJoint.motorTargetAngularVelocity](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387908-motortargetangularvelocity)Added [SCNPhysicsSliderJoint.motorTargetLinearVelocity](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387938-motortargetlinearvelocity)Added [SCNPhysicsVehicle](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle)Added [-[SCNPhysicsVehicle applyBrakingForce:forWheelAtIndex:]](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387894-applybrakingforce)Added [-[SCNPhysicsVehicle applyEngineForce:forWheelAtIndex:]](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387963-applyengineforce)Added [SCNPhysicsVehicle.chassisBody](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387985-chassisbody)Added [-[SCNPhysicsVehicle setSteeringAngle:forWheelAtIndex:]](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387952-setsteeringangle)Added [SCNPhysicsVehicle.speedInKilometersPerHour](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387910-speedinkilometersperhour)Added [+[SCNPhysicsVehicle vehicleWithChassisBody:wheels:]](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387943-init)Added [SCNPhysicsVehicle.wheels](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387906-wheels)Added [SCNPhysicsVehicleWheel](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel)Added [SCNPhysicsVehicleWheel.axle](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387969-axle)Added [SCNPhysicsVehicleWheel.connectionPosition](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387959-connectionposition)Added [SCNPhysicsVehicleWheel.frictionSlip](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387904-frictionslip)Added [SCNPhysicsVehicleWheel.maximumSuspensionForce](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387934-maximumsuspensionforce)Added [SCNPhysicsVehicleWheel.maximumSuspensionTravel](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387928-maximumsuspensiontravel)Added [SCNPhysicsVehicleWheel.node](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387892-node)Added [SCNPhysicsVehicleWheel.radius](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387991-radius)Added [SCNPhysicsVehicleWheel.steeringAxis](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387882-steeringaxis)Added [SCNPhysicsVehicleWheel.suspensionCompression](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387971-suspensioncompression)Added [SCNPhysicsVehicleWheel.suspensionDamping](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387886-suspensiondamping)Added [SCNPhysicsVehicleWheel.suspensionRestLength](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387880-suspensionrestlength)Added [SCNPhysicsVehicleWheel.suspensionStiffness](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387983-suspensionstiffness)Added [+[SCNPhysicsVehicleWheel wheelWithNode:]](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387989-init)SCNPhysicsBody.h (Added)Added [SCNPhysicsBody](https://developer.apple.com/documentation/scenekit/scnphysicsbody)Added [SCNPhysicsBody.allowsResting](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514742-allowsresting)Added [SCNPhysicsBody.angularDamping](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514792-angulardamping)Added [SCNPhysicsBody.angularVelocity](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514770-angularvelocity)Added [SCNPhysicsBody.angularVelocityFactor](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514748-angularvelocityfactor)Added [-[SCNPhysicsBody applyForce:atPosition:impulse:]](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514750-applyforce)Added [-[SCNPhysicsBody applyForce:impulse:]](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514801-applyforce)Added [-[SCNPhysicsBody applyTorque:impulse:]](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514752-applytorque)Added [+[SCNPhysicsBody bodyWithType:shape:]](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514797-init)Added [SCNPhysicsBody.categoryBitMask](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514768-categorybitmask)Added [SCNPhysicsBody.charge](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514786-charge)Added [-[SCNPhysicsBody clearAllForces]](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514735-clearallforces)Added [SCNPhysicsBody.collisionBitMask](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514772-collisionbitmask)Added [SCNPhysicsBody.damping](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514763-damping)Added [+[SCNPhysicsBody dynamicBody]](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514766-dynamicbody)Added [SCNPhysicsBody.friction](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514794-friction)Added [SCNPhysicsBody.isResting](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514795-isresting)Added [+[SCNPhysicsBody kinematicBody]](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514776-kinematicbody)Added [SCNPhysicsBody.mass](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514755-mass)Added [SCNPhysicsBody.physicsShape](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514789-physicsshape)Added [-[SCNPhysicsBody resetTransform]](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514782-resettransform)Added [SCNPhysicsBody.restitution](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514740-restitution)Added [SCNPhysicsBody.rollingFriction](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514737-rollingfriction)Added [+[SCNPhysicsBody staticBody]](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514791-staticbody)Added [SCNPhysicsBody.type](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514787-type)Added [SCNPhysicsBody.velocity](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514757-velocity)Added [SCNPhysicsBody.velocityFactor](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514753-velocityfactor)Added [SCNPhysicsBodyType](https://developer.apple.com/documentation/scenekit/scnphysicsbodytype)Added [SCNPhysicsBodyTypeDynamic](https://developer.apple.com/documentation/scenekit/scnphysicsbodytype/dynamic)Added [SCNPhysicsBodyTypeKinematic](https://developer.apple.com/documentation/scenekit/scnphysicsbodytype/kinematic)Added [SCNPhysicsBodyTypeStatic](https://developer.apple.com/documentation/scenekit/scnphysicsbodytype/static)Added [SCNPhysicsCollisionCategory](https://developer.apple.com/documentation/scenekit/scnphysicscollisioncategory)Added [SCNPhysicsCollisionCategoryAll](https://developer.apple.com/documentation/scenekit/scnphysicscollisioncategory/1514784-all)Added [SCNPhysicsCollisionCategoryDefault](https://developer.apple.com/documentation/scenekit/scnphysicscollisioncategory/scnphysicscollisioncategorydefault)Added [SCNPhysicsCollisionCategoryStatic](https://developer.apple.com/documentation/scenekit/scnphysicscollisioncategory/scnphysicscollisioncategorystatic)SCNPhysicsContact.h (Added)Added [SCNPhysicsContact](https://developer.apple.com/documentation/scenekit/scnphysicscontact)Added [SCNPhysicsContact.collisionImpulse](https://developer.apple.com/documentation/scenekit/scnphysicscontact/1523944-collisionimpulse)Added [SCNPhysicsContact.contactNormal](https://developer.apple.com/documentation/scenekit/scnphysicscontact/1522833-contactnormal)Added [SCNPhysicsContact.contactPoint](https://developer.apple.com/documentation/scenekit/scnphysicscontact/1523810-contactpoint)Added [SCNPhysicsContact.nodeA](https://developer.apple.com/documentation/scenekit/scnphysicscontact/1523445-nodea)Added [SCNPhysicsContact.nodeB](https://developer.apple.com/documentation/scenekit/scnphysicscontact/1524232-nodeb)Added [SCNPhysicsContact.penetrationDistance](https://developer.apple.com/documentation/scenekit/scnphysicscontact/1522870-penetrationdistance)SCNPhysicsField.h (Added)Added [SCNPhysicsField](https://developer.apple.com/documentation/scenekit/scnphysicsfield)Added [SCNPhysicsField.active](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388117-isactive)Added [SCNPhysicsField.categoryBitMask](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388119-categorybitmask)Added [+[SCNPhysicsField customFieldWithEvaluationBlock:]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388140-customfieldwithevaluationblock)Added [SCNPhysicsField.direction](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388128-direction)Added [+[SCNPhysicsField dragField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388164-drag)Added [+[SCNPhysicsField electricField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388152-electricfield)Added [SCNPhysicsField.exclusive](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388126-exclusive)Added [SCNPhysicsField.falloffExponent](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388146-falloffexponent)Added [SCNPhysicsField.halfExtent](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388138-halfextent)Added [+[SCNPhysicsField linearGravityField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388130-lineargravity)Added [+[SCNPhysicsField magneticField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388168-magneticfield)Added [SCNPhysicsField.minimumDistance](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388148-minimumdistance)Added [+[SCNPhysicsField noiseFieldWithSmoothness:animationSpeed:]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388150-noisefieldwithsmoothness)Added [SCNPhysicsField.offset](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388154-offset)Added [+[SCNPhysicsField radialGravityField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388115-radialgravity)Added [SCNPhysicsField.scope](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388136-scope)Added [+[SCNPhysicsField springField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388134-spring)Added [SCNPhysicsField.strength](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388132-strength)Added [+[SCNPhysicsField turbulenceFieldWithSmoothness:animationSpeed:]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388162-turbulencefield)Added [SCNPhysicsField.usesEllipsoidalExtent](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388158-usesellipsoidalextent)Added [+[SCNPhysicsField vortexField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388160-vortex)Added [SCNFieldForceEvaluator](https://developer.apple.com/documentation/scenekit/scnfieldforceevaluator)Added [SCNPhysicsFieldScope](https://developer.apple.com/documentation/scenekit/scnphysicsfieldscope)Added [SCNPhysicsFieldScopeInsideExtent](https://developer.apple.com/documentation/scenekit/scnphysicsfieldscope/insideextent)Added [SCNPhysicsFieldScopeOutsideExtent](https://developer.apple.com/documentation/scenekit/scnphysicsfieldscope/outsideextent)SCNPhysicsShape.h (Added)Added [SCNPhysicsShape](https://developer.apple.com/documentation/scenekit/scnphysicsshape)Added [+[SCNPhysicsShape shapeWithGeometry:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508897-init)Added [+[SCNPhysicsShape shapeWithNode:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508889-shapewithnode)Added [+[SCNPhysicsShape shapeWithShapes:transforms:]](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508886-init)Added [SCNPhysicsShapeKeepAsCompoundKey](https://developer.apple.com/documentation/scenekit/scnphysicsshape/option/1508892-keepascompound)Added [SCNPhysicsShapeScaleKey](https://developer.apple.com/documentation/scenekit/scnphysicsshapescalekey)Added [SCNPhysicsShapeTypeBoundingBox](https://developer.apple.com/documentation/scenekit/scnphysicsshapetypeboundingbox)Added [SCNPhysicsShapeTypeConcavePolyhedron](https://developer.apple.com/documentation/scenekit/scnphysicsshapetypeconcavepolyhedron)Added [SCNPhysicsShapeTypeConvexHull](https://developer.apple.com/documentation/scenekit/scnphysicsshapetypeconvexhull)Added [SCNPhysicsShapeTypeKey](https://developer.apple.com/documentation/scenekit/scnphysicsshapetypekey)SCNPhysicsWorld.h (Added)Added [SCNPhysicsContactDelegate](https://developer.apple.com/documentation/scenekit/scnphysicscontactdelegate)Added [-[SCNPhysicsContactDelegate physicsWorld:didBeginContact:]](https://developer.apple.com/documentation/scenekit/scnphysicscontactdelegate/1512835-physicsworld)Added [-[SCNPhysicsContactDelegate physicsWorld:didEndContact:]](https://developer.apple.com/documentation/scenekit/scnphysicscontactdelegate/1512883-physicsworld)Added [-[SCNPhysicsContactDelegate physicsWorld:didUpdateContact:]](https://developer.apple.com/documentation/scenekit/scnphysicscontactdelegate/1512865-physicsworld)Added [SCNPhysicsWorld](https://developer.apple.com/documentation/scenekit/scnphysicsworld)Added [-[SCNPhysicsWorld addBehavior:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512839-addbehavior)Added [-[SCNPhysicsWorld allBehaviors]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512853-allbehaviors)Added [SCNPhysicsWorld.contactDelegate](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512843-contactdelegate)Added [-[SCNPhysicsWorld contactTestBetweenBody:andBody:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512875-contacttestbetween)Added [-[SCNPhysicsWorld contactTestWithBody:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512841-contacttestwithbody)Added [-[SCNPhysicsWorld convexSweepTestWithShape:fromTransform:toTransform:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512859-convexsweeptest)Added [SCNPhysicsWorld.gravity](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512855-gravity)Added [-[SCNPhysicsWorld rayTestWithSegmentFromPoint:toPoint:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512857-raytestwithsegmentfrompoint)Added [-[SCNPhysicsWorld removeAllBehaviors]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512849-removeallbehaviors)Added [-[SCNPhysicsWorld removeBehavior:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512870-removebehavior)Added [SCNPhysicsWorld.speed](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512851-speed)Added [SCNPhysicsWorld.timeStep](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512881-timestep)Added [-[SCNPhysicsWorld updateCollisionPairs]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512877-updatecollisionpairs)Added [SCNPhysicsTestBackfaceCullingKey](https://developer.apple.com/documentation/scenekit/scnphysicstestbackfacecullingkey)Added [SCNPhysicsTestCollisionBitMaskKey](https://developer.apple.com/documentation/scenekit/scnphysicsworld/testoption/1512845-collisionbitmask)Added [SCNPhysicsTestSearchModeAll](https://developer.apple.com/documentation/scenekit/scnphysicstestsearchmodeall)Added [SCNPhysicsTestSearchModeAny](https://developer.apple.com/documentation/scenekit/scnphysicstestsearchmodeany)Added [SCNPhysicsTestSearchModeClosest](https://developer.apple.com/documentation/scenekit/scnphysicstestsearchmodeclosest)Added [SCNPhysicsTestSearchModeKey](https://developer.apple.com/documentation/scenekit/scnphysicstestsearchmodekey)SCNRenderer.hAdded [SCNRenderer.nextFrameTime](https://developer.apple.com/documentation/scenekit/scnrenderer/1518410-nextframetime)Added [-[SCNRenderer renderAtTime:]](https://developer.apple.com/documentation/scenekit/scnrenderer/1518402-renderattime)Modified [SCNRenderer](https://developer.apple.com/documentation/scenekit/scnrenderer)

|  | Protocols |
| --- | --- |
| From | SCNSceneRenderer |
| To | SCNSceneRenderer, SCNTechniqueSupport |

SCNScene.hAdded [SCNScene.fogColor](https://developer.apple.com/documentation/scenekit/scnscene/1522774-fogcolor)Added [SCNScene.fogDensityExponent](https://developer.apple.com/documentation/scenekit/scnscene/1523776-fogdensityexponent)Added [SCNScene.fogEndDistance](https://developer.apple.com/documentation/scenekit/scnscene/1523836-fogenddistance)Added [SCNScene.fogStartDistance](https://developer.apple.com/documentation/scenekit/scnscene/1522790-fogstartdistance)Added [SCNScene.paused](https://developer.apple.com/documentation/scenekit/scnscene/1523604-ispaused)Added [SCNScene.physicsWorld](https://developer.apple.com/documentation/scenekit/scnscene/1522643-physicsworld)Added [+[SCNScene sceneNamed:inDirectory:options:]](https://developer.apple.com/documentation/scenekit/scnscene/1522851-init)Added [SCNSceneUpAxisAttributeKey](https://developer.apple.com/documentation/scenekit/scnscene/attribute/1524016-upaxis)Modified [SCNScene](https://developer.apple.com/documentation/scenekit/scnscene)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSSecureCoding |

Modified [SCNSceneExportDelegate](https://developer.apple.com/documentation/scenekit/scnsceneexportdelegate)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSObject |

Modified [-[SCNSceneExportDelegate writeImage:withSceneDocumentURL:originalImageURL:]](https://developer.apple.com/documentation/scenekit/scnsceneexportdelegate/1524221-write)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

SCNSceneRenderer.hAdded [SCNSceneRenderer.overlaySKScene](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1524051-overlayskscene)Added [-[SCNSceneRenderer prepareObjects:withCompletionHandler:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523375-prepareobjects)Added [SCNSceneRenderer.scene](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523956-scene)Added [SCNSceneRenderer.sceneTime](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522680-scenetime)Added [-[SCNSceneRendererDelegate renderer:didApplyAnimationsAtTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1523038-renderer)Added [-[SCNSceneRendererDelegate renderer:didSimulatePhysicsAtTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1522738-renderer)Added [-[SCNSceneRendererDelegate renderer:updateAtTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1522937-renderer)Modified [SCNHitTestResult.modelTransform](https://developer.apple.com/documentation/scenekit/scnhittestresult/1523496-modeltransform)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) CATransform3D modelTransform ``` |
| To | ``` @property(nonatomic, readonly) SCNMatrix4 modelTransform ``` |

Modified [SCNSceneRenderer.currentTime](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522854-currenttime)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[SCNSceneRendererDelegate renderer:didRenderScene:atTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1524233-renderer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[SCNSceneRendererDelegate renderer:willRenderScene:atTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1523483-renderer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

SCNSceneSource.hAdded [SCNSceneSourceAnimationImportPolicyDoNotPlay](https://developer.apple.com/documentation/scenekit/scnscenesourceanimationimportpolicydonotplay)Added [SCNSceneSourceAnimationImportPolicyKey](https://developer.apple.com/documentation/scenekit/scnscenesourceanimationimportpolicykey)Added [SCNSceneSourceAnimationImportPolicyPlay](https://developer.apple.com/documentation/scenekit/scnscenesource/animationimportpolicy/1523908-play)Added [SCNSceneSourceAnimationImportPolicyPlayRepeatedly](https://developer.apple.com/documentation/scenekit/scnscenesourceanimationimportpolicyplayrepeatedly)Added [SCNSceneSourceAnimationImportPolicyPlayUsingSceneTimeBase](https://developer.apple.com/documentation/scenekit/scnscenesourceanimationimportpolicyplayusingscenetimebase)Added [SCNSceneSourceConvertToYUpKey](https://developer.apple.com/documentation/scenekit/scnscenesourceconverttoyupkey)Added [SCNSceneSourceConvertUnitsToMetersKey](https://developer.apple.com/documentation/scenekit/scnscenesource/loadingoption/1523784-convertunitstometers)SCNShadable.hAdded [SCNProgram.geometryShader](https://developer.apple.com/documentation/scenekit/scnprogram/1524049-geometryshader)Added [SCNProgram.opaque](https://developer.apple.com/documentation/scenekit/scnprogram/1522844-opaque)Added [SCNProgram.tessellationControlShader](https://developer.apple.com/documentation/scenekit/scnprogram/1523852-tessellationcontrolshader)Added [SCNProgram.tessellationEvaluationShader](https://developer.apple.com/documentation/scenekit/scnprogram/1523760-tessellationevaluationshader)Modified [SCNProgram](https://developer.apple.com/documentation/scenekit/scnprogram)

|  | Protocols |
| --- | --- |
| From | NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [-[SCNProgramDelegate program:bindValueForSymbol:atLocation:programID:renderer:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1524155-program)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified [-[SCNProgramDelegate program:handleError:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1523007-program)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[SCNProgramDelegate program:unbindValueForSymbol:atLocation:programID:renderer:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1523857-program)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified [-[SCNProgramDelegate programIsOpaque:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1523068-programisopaque)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified [SCNShadable](https://developer.apple.com/documentation/scenekit/scnshadable)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSObject |

Modified [-[SCNShadable handleBindingOfSymbol:usingBlock:]](https://developer.apple.com/documentation/scenekit/scnshadable/1523063-handlebindingofsymbol)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[SCNShadable handleUnbindingOfSymbol:usingBlock:]](https://developer.apple.com/documentation/scenekit/scnshadable/1522783-handleunbinding)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [SCNProgramMappingChannelKey](https://developer.apple.com/documentation/scenekit/scnprogrammappingchannelkey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

SCNSkinner.hAdded [SCNSkinner.baseGeometry](https://developer.apple.com/documentation/scenekit/scnskinner/1522823-basegeometry)Added [SCNSkinner.baseGeometryBindTransform](https://developer.apple.com/documentation/scenekit/scnskinner/1523160-basegeometrybindtransform)Added [SCNSkinner.boneIndices](https://developer.apple.com/documentation/scenekit/scnskinner/1524117-boneindices)Added [SCNSkinner.boneInverseBindTransforms](https://developer.apple.com/documentation/scenekit/scnskinner/1523802-boneinversebindtransforms)Added [SCNSkinner.boneWeights](https://developer.apple.com/documentation/scenekit/scnskinner/1522986-boneweights)Added [SCNSkinner.bones](https://developer.apple.com/documentation/scenekit/scnskinner/1522732-bones)Added [+[SCNSkinner skinnerWithBaseGeometry:bones:boneInverseBindTransforms:boneWeights:boneIndices:]](https://developer.apple.com/documentation/scenekit/scnskinner/1523964-init)Modified [SCNSkinner](https://developer.apple.com/documentation/scenekit/scnskinner)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSSecureCoding |

SCNTechnique.h (Added)Added [SCNTechnique](https://developer.apple.com/documentation/scenekit/scntechnique)Added [SCNTechnique.dictionaryRepresentation](https://developer.apple.com/documentation/scenekit/scntechnique/1520492-dictionaryrepresentation)Added [-[SCNTechnique handleBindingOfSymbol:usingBlock:]](https://developer.apple.com/documentation/scenekit/scntechnique/1520490-handlebindingofsymbol)Added [+[SCNTechnique techniqueBySequencingTechniques:]](https://developer.apple.com/documentation/scenekit/scntechnique/1520497-techniquebysequencingtechniques)Added [+[SCNTechnique techniqueWithDictionary:]](https://developer.apple.com/documentation/scenekit/scntechnique/1520494-init)Added [SCNTechniqueSupport](https://developer.apple.com/documentation/scenekit/scntechniquesupport)Added [SCNTechniqueSupport.technique](https://developer.apple.com/documentation/scenekit/scntechniquesupport/1520496-technique)SCNTransaction.hModified [+[SCNTransaction completionBlock]](https://developer.apple.com/documentation/scenekit/scntransaction/1523660-completionblock)

|  | Declaration |
| --- | --- |
| From | ``` + (void (^)())completionBlock ``` |
| To | ``` + (void (^)(void))completionBlock ``` |

SCNView.hAdded [SCNView.antialiasingMode](https://developer.apple.com/documentation/scenekit/scnview/1524085-antialiasingmode)Added [-[SCNView snapshot]](https://developer.apple.com/documentation/scenekit/scnview/1524031-snapshot)Added [SCNAntialiasingMode](https://developer.apple.com/documentation/scenekit/scnantialiasingmode)Added [SCNAntialiasingModeMultisampling16X](https://developer.apple.com/documentation/scenekit/scnantialiasingmode/multisampling16x)Added [SCNAntialiasingModeMultisampling2X](https://developer.apple.com/documentation/scenekit/scnantialiasingmode/multisampling2x)Added [SCNAntialiasingModeMultisampling4X](https://developer.apple.com/documentation/scenekit/scnantialiasingmode/scnantialiasingmodemultisampling4x)Added [SCNAntialiasingModeMultisampling8X](https://developer.apple.com/documentation/scenekit/scnantialiasingmode/multisampling8x)Added [SCNAntialiasingModeNone](https://developer.apple.com/documentation/scenekit/scnantialiasingmode/none)Modified [SCNView](https://developer.apple.com/documentation/scenekit/scnview)

|  | Protocols |
| --- | --- |
| From | SCNSceneRenderer |
| To | SCNSceneRenderer, SCNTechniqueSupport |

Modified [-[SCNView pause:]](https://developer.apple.com/documentation/scenekit/scnview/1522825-pause)

|  | Declaration |
| --- | --- |
| From | ``` - (void)pause:(id)sender ``` |
| To | ``` - (IBAction)pause:(id)sender ``` |

Modified [-[SCNView play:]](https://developer.apple.com/documentation/scenekit/scnview/1523699-play)

|  | Declaration |
| --- | --- |
| From | ``` - (void)play:(id)sender ``` |
| To | ``` - (IBAction)play:(id)sender ``` |

Modified [-[SCNView stop:]](https://developer.apple.com/documentation/scenekit/scnview/1524132-stop)

|  | Declaration |
| --- | --- |
| From | ``` - (void)stop:(id)sender ``` |
| To | ``` - (IBAction)stop:(id)sender ``` |

SceneKitTypes.hRemoved [-[NSValue SCNVector3Value]](https://developer.apple.com/documentation/foundation/nsvalue/1409669-scnvector3value)Removed [-[NSValue SCNVector4Value]](https://developer.apple.com/documentation/foundation/nsvalue/1409725-scnvector4value)Added [NSValue.SCNMatrix4Value](https://developer.apple.com/documentation/foundation/nsvalue/1409684-scnmatrix4value)Added [NSValue.SCNVector3Value](https://developer.apple.com/documentation/foundation/nsvalue/1409669-scnvector3value)Added [NSValue.SCNVector4Value](https://developer.apple.com/documentation/foundation/nsvalue/1409725-scnvector4value)Added [+[NSValue valueWithSCNMatrix4:]](https://developer.apple.com/documentation/foundation/nsvalue/1409680-valuewithscnmatrix4)Added [SCNMatrix4](https://developer.apple.com/documentation/scenekit/scnmatrix4)Added [SCNMatrix4EqualToMatrix4()](https://developer.apple.com/documentation/scenekit/1409665-scnmatrix4equaltomatrix4)Added [SCNMatrix4FromGLKMatrix4()](https://developer.apple.com/documentation/scenekit/1409699-scnmatrix4fromglkmatrix4)Added [SCNMatrix4Identity](https://developer.apple.com/documentation/scenekit/scnmatrix4identity)Added [SCNMatrix4Invert()](https://developer.apple.com/documentation/scenekit/1409682-scnmatrix4invert)Added [SCNMatrix4IsIdentity()](https://developer.apple.com/documentation/scenekit/1409715-scnmatrix4isidentity)Added [SCNMatrix4MakeRotation()](https://developer.apple.com/documentation/scenekit/1409686-scnmatrix4makerotation)Added [SCNMatrix4MakeScale()](https://developer.apple.com/documentation/scenekit/1409681-scnmatrix4makescale)Added [SCNMatrix4MakeTranslation()](https://developer.apple.com/documentation/scenekit/1409679-scnmatrix4maketranslation)Added [SCNMatrix4Mult()](https://developer.apple.com/documentation/scenekit/1409697-scnmatrix4mult)Added [SCNMatrix4Rotate()](https://developer.apple.com/documentation/scenekit/1409659-scnmatrix4rotate)Added [SCNMatrix4Scale()](https://developer.apple.com/documentation/scenekit/1409653-scnmatrix4scale)Added [SCNMatrix4ToGLKMatrix4()](https://developer.apple.com/documentation/scenekit/1409703-scnmatrix4toglkmatrix4)Added [SCNMatrix4Translate()](https://developer.apple.com/documentation/scenekit/1409717-scnmatrix4translate)Added [SCNQuaternion](https://developer.apple.com/documentation/scenekit/scnquaternion)Added [SCNVector3Zero](https://developer.apple.com/documentation/scenekit/scnvector3zero)Added [SCNVector4Zero](https://developer.apple.com/documentation/scenekit/scnvector4zero)SceneKit_simd.h (Added)Added [SCNMatrix4FromMat4()](https://developer.apple.com/documentation/scenekit/1522632-scnmatrix4frommat4)Added [SCNMatrix4ToMat4()](https://developer.apple.com/documentation/scenekit/1523928-scnmatrix4tomat4)Added [SCNVector3FromFloat3()](https://developer.apple.com/documentation/scenekit/1524143-scnvector3fromfloat3)Added [SCNVector3ToFloat3()](https://developer.apple.com/documentation/scenekit/1523448-scnvector3tofloat3)Added [SCNVector4FromFloat4()](https://developer.apple.com/documentation/scenekit/1523606-scnvector4fromfloat4)Added [SCNVector4ToFloat4()](https://developer.apple.com/documentation/scenekit/1523001-scnvector4tofloat4)

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
