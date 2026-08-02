---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/SceneKit.html
archived_at: '2026-07-18T02:56:36.487830Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# SceneKit Changes for Objective-C

### SceneKit

#### ModelIO.h (Added)

Added [+[MDLAsset assetWithSCNScene:]](https://developer.apple.com/documentation/modelio/mdlasset/1419847-init)Added [+[MDLCamera cameraWithSCNCamera:]](https://developer.apple.com/documentation/modelio/mdlcamera/1419832-camerawithscncamera)Added [+[MDLLight lightWithSCNLight:]](https://developer.apple.com/documentation/modelio/mdllight/1419830-lightwithscnlight)Added [+[MDLMaterial materialWithSCNMaterial:]](https://developer.apple.com/documentation/modelio/mdlmaterial/1419851-init)Added [+[MDLMesh meshWithSCNGeometry:]](https://developer.apple.com/documentation/modelio/mdlmesh/1419853-init)Added [+[MDLObject objectWithSCNNode:]](https://developer.apple.com/documentation/modelio/mdlobject/1419855-objectwithscnnode)Added [+[MDLSubmesh submeshWithSCNGeometryElement:]](https://developer.apple.com/documentation/modelio/mdlsubmesh/1419837-init)Added [+[SCNCamera cameraWithMDLCamera:]](https://developer.apple.com/documentation/scenekit/scncamera/1419839-init)Added [+[SCNGeometry geometryWithMDLMesh:]](https://developer.apple.com/documentation/scenekit/scngeometry/1419845-geometrywithmdlmesh)Added [+[SCNGeometryElement geometryElementWithMDLSubmesh:]](https://developer.apple.com/documentation/scenekit/scngeometryelement/1419843-geometryelementwithmdlsubmesh)Added [+[SCNLight lightWithMDLLight:]](https://developer.apple.com/documentation/scenekit/scnlight/1419849-lightwithmdllight)Added [+[SCNMaterial materialWithMDLMaterial:]](https://developer.apple.com/documentation/scenekit/scnmaterial/1419835-materialwithmdlmaterial)Added [+[SCNNode nodeWithMDLObject:]](https://developer.apple.com/documentation/scenekit/scnnode/1419841-init)Added [+[SCNScene sceneWithMDLAsset:]](https://developer.apple.com/documentation/scenekit/scnscene/1419833-scenewithmdlasset)Added MDLAsset(SCNModelIO)Added MDLCamera(SCNModelIO)Added MDLLight(SCNModelIO)Added MDLMaterial(SCNModelIO)Added MDLMesh(SCNModelIO)Added MDLObject(SCNModelIO)Added MDLSubmesh(SCNModelIO)Added SCNCamera(SCNModelIO)Added SCNGeometry(SCNModelIO)Added SCNGeometryElement(SCNModelIO)Added SCNLight(SCNModelIO)Added SCNMaterial(SCNModelIO)Added SCNNode(SCNModelIO)Added SCNScene(SCNModelIO)

#### SceneKitTypes.h

Added #def SCN_ENABLE_METALModified [NSValue.SCNMatrix4Value](https://developer.apple.com/documentation/foundation/nsvalue/1409684-scnmatrix4value)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SCNMatrix4 SCNMatrix4Value ``` |
| To | ``` @property(nonatomic, readonly) SCNMatrix4 SCNMatrix4Value ``` |

Modified [NSValue.SCNVector3Value](https://developer.apple.com/documentation/foundation/nsvalue/1409669-scnvector3value)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SCNVector3 SCNVector3Value ``` |
| To | ``` @property(nonatomic, readonly) SCNVector3 SCNVector3Value ``` |

Modified [NSValue.SCNVector4Value](https://developer.apple.com/documentation/foundation/nsvalue/1409725-scnvector4value)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SCNVector4 SCNVector4Value ``` |
| To | ``` @property(nonatomic, readonly) SCNVector4 SCNVector4Value ``` |

#### SCNAction.h

Removed [-[SCNActionable hasActions]](https://developer.apple.com/documentation/scenekit/scnactionable/1523794-hasactions)Removed SCNAction(SCNActions)Added [+[SCNAction hide]](https://developer.apple.com/documentation/scenekit/scnaction/1523487-hide)Added [+[SCNAction playAudioSource:waitForCompletion:]](https://developer.apple.com/documentation/scenekit/scnaction/1523651-playaudio)Added [+[SCNAction unhide]](https://developer.apple.com/documentation/scenekit/scnaction/1524205-unhide)Added [SCNActionable.actionKeys](https://developer.apple.com/documentation/scenekit/scnactionable/1523036-actionkeys)Added [SCNActionable.hasActions](https://developer.apple.com/documentation/scenekit/scnactionable/1523794-hasactions)Modified [+[SCNAction group:]](https://developer.apple.com/documentation/scenekit/scnaction/1522779-group)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)group:(NSArray *)actions ``` |
| To | ``` + (SCNAction * _Nonnull)group:(NSArray<SCNAction *> * _Nonnull)actions ``` |

Modified [+[SCNAction sequence:]](https://developer.apple.com/documentation/scenekit/scnaction/1522793-sequence)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)sequence:(NSArray *)actions ``` |
| To | ``` + (SCNAction * _Nonnull)sequence:(NSArray<SCNAction *> * _Nonnull)actions ``` |

#### SCNAnimation.h

Removed [-[SCNAnimatable animationKeys]](https://developer.apple.com/documentation/scenekit/scnanimatable/1523610-animationkeys)Added [SCNAnimatable.animationKeys](https://developer.apple.com/documentation/scenekit/scnanimatable/1523610-animationkeys)Modified [CAAnimation.animationEvents](https://developer.apple.com/documentation/quartzcore/caanimation/1523940-animationevents)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSArray *animationEvents ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<SCNAnimationEvent *> *animationEvents ``` |

#### SCNAudioSource.h (Added)

Added [SCNAudioPlayer](https://developer.apple.com/documentation/scenekit/scnaudioplayer)Added [SCNAudioPlayer.audioNode](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1522747-audionode)Added [+[SCNAudioPlayer audioPlayerWithAVAudioNode:]](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1533927-audioplayerwithavaudionode)Added [+[SCNAudioPlayer audioPlayerWithSource:]](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1533919-audioplayerwithsource)Added [SCNAudioPlayer.audioSource](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1523059-audiosource)Added [SCNAudioPlayer.didFinishPlayback](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1522818-didfinishplayback)Added [-[SCNAudioPlayer initWithAVAudioNode:]](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1523010-init)Added [-[SCNAudioPlayer initWithSource:]](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1522736-init)Added [SCNAudioPlayer.willStartPlayback](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1524115-willstartplayback)Added [SCNAudioSource](https://developer.apple.com/documentation/scenekit/scnaudiosource)Added [+[SCNAudioSource audioSourceNamed:]](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524138-audiosourcenamed)Added [-[SCNAudioSource initWithFileNamed:]](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524225-init)Added [-[SCNAudioSource initWithURL:]](https://developer.apple.com/documentation/scenekit/scnaudiosource/1523264-initwithurl)Added [-[SCNAudioSource load]](https://developer.apple.com/documentation/scenekit/scnaudiosource/1523399-load)Added [SCNAudioSource.loops](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524183-loops)Added [SCNAudioSource.positional](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524185-positional)Added [SCNAudioSource.rate](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524189-rate)Added [SCNAudioSource.reverbBlend](https://developer.apple.com/documentation/scenekit/scnaudiosource/1523450-reverbblend)Added [SCNAudioSource.shouldStream](https://developer.apple.com/documentation/scenekit/scnaudiosource/1523475-shouldstream)Added [SCNAudioSource.volume](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524106-volume)Added [-[SCNNode addAudioPlayer:]](https://developer.apple.com/documentation/scenekit/scnnode/1523464-addaudioplayer)Added [SCNNode.audioPlayers](https://developer.apple.com/documentation/scenekit/scnnode/1523244-audioplayers)Added [-[SCNNode removeAllAudioPlayers]](https://developer.apple.com/documentation/scenekit/scnnode/1523570-removeallaudioplayers)Added [-[SCNNode removeAudioPlayer:]](https://developer.apple.com/documentation/scenekit/scnnode/1522767-removeaudioplayer)Added SCNNode(SCNAudioSupport)

#### SCNConstraint.h

Added [SCNBillboardConstraint](https://developer.apple.com/documentation/scenekit/scnbillboardconstraint)Added [+[SCNBillboardConstraint billboardConstraint]](https://developer.apple.com/documentation/scenekit/scnbillboardconstraint/1468673-billboardconstraint)Added [SCNBillboardConstraint.freeAxes](https://developer.apple.com/documentation/scenekit/scnbillboardconstraint/1468685-freeaxes)Added [-[SCNIKConstraint initWithChainRootNode:]](https://developer.apple.com/documentation/scenekit/scnikconstraint/1468694-init)Added [SCNBillboardAxis](https://developer.apple.com/documentation/scenekit/scnbillboardaxis)Added [SCNBillboardAxisAll](https://developer.apple.com/documentation/scenekit/scnbillboardaxis/1468666-all)Added [SCNBillboardAxisX](https://developer.apple.com/documentation/scenekit/scnbillboardaxis/scnbillboardaxisx)Added [SCNBillboardAxisY](https://developer.apple.com/documentation/scenekit/scnbillboardaxis/scnbillboardaxisy)Added [SCNBillboardAxisZ](https://developer.apple.com/documentation/scenekit/scnbillboardaxis/scnbillboardaxisz)

#### SCNGeometry.h

Added [SCNGeometry.geometryElements](https://developer.apple.com/documentation/scenekit/scngeometry/1523046-geometryelements)Added [SCNGeometry.geometrySources](https://developer.apple.com/documentation/scenekit/scngeometry/1523662-sources)Added [+[SCNGeometrySource geometrySourceWithBuffer:vertexFormat:semantic:vertexCount:dataOffset:dataStride:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1522873-init)Modified [-[SCNGeometry geometrySourcesForSemantic:]](https://developer.apple.com/documentation/scenekit/scngeometry/1522926-geometrysourcesforsemantic)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)geometrySourcesForSemantic:(NSString *)semantic ``` |
| To | ``` - (NSArray<SCNGeometrySource *> * _Nonnull)geometrySourcesForSemantic:(NSString * _Nonnull)semantic ``` |

Modified [+[SCNGeometry geometryWithSources:elements:]](https://developer.apple.com/documentation/scenekit/scngeometry/1522803-geometrywithsources)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)geometryWithSources:(NSArray *)sources elements:(NSArray *)elements ``` |
| To | ``` + (instancetype _Nonnull)geometryWithSources:(NSArray<SCNGeometrySource *> * _Nonnull)sources elements:(NSArray<SCNGeometryElement *> * _Nonnull)elements ``` |

Modified [SCNGeometry.levelsOfDetail](https://developer.apple.com/documentation/scenekit/scngeometry/1523745-levelsofdetail)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *levelsOfDetail ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<SCNLevelOfDetail *> *levelsOfDetail ``` |

Modified [SCNGeometry.materials](https://developer.apple.com/documentation/scenekit/scngeometry/1523472-materials)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *materials ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<SCNMaterial *> *materials ``` |

#### SCNMaterial.h

Added [SCNMaterial.ambientOcclusion](https://developer.apple.com/documentation/scenekit/scnmaterial/1462579-ambientocclusion)Added [SCNMaterial.blendMode](https://developer.apple.com/documentation/scenekit/scnmaterial/1462585-blendmode)Added [SCNMaterial.selfIllumination](https://developer.apple.com/documentation/scenekit/scnmaterial/1462524-selfillumination)Added [SCNBlendMode](https://developer.apple.com/documentation/scenekit/scnblendmode)Added [SCNBlendModeAdd](https://developer.apple.com/documentation/scenekit/scnblendmode/scnblendmodeadd)Added [SCNBlendModeAlpha](https://developer.apple.com/documentation/scenekit/scnblendmode/alpha)Added [SCNBlendModeMultiply](https://developer.apple.com/documentation/scenekit/scnblendmode/scnblendmodemultiply)Added [SCNBlendModeReplace](https://developer.apple.com/documentation/scenekit/scnblendmode/replace)Added [SCNBlendModeScreen](https://developer.apple.com/documentation/scenekit/scnblendmode/screen)Added [SCNBlendModeSubtract](https://developer.apple.com/documentation/scenekit/scnblendmode/scnblendmodesubtract)

#### SCNMaterialProperty.h

Added [SCNWrapModeClampToBorder](https://developer.apple.com/documentation/scenekit/scnwrapmode/scnwrapmodeclamptoborder)

#### SCNMorpher.h

Modified [SCNMorpher.targets](https://developer.apple.com/documentation/scenekit/scnmorpher/1523572-targets)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *targets ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<SCNGeometry *> *targets ``` |

#### SCNNode.h

Modified [SCNNode.childNodes](https://developer.apple.com/documentation/scenekit/scnnode/1407984-childnodes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *childNodes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<SCNNode *> *childNodes ``` |

Modified [-[SCNNode childNodesPassingTest:]](https://developer.apple.com/documentation/scenekit/scnnode/1407982-childnodes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)childNodesPassingTest:(BOOL (^)(SCNNode *child, BOOL *stop))predicate ``` |
| To | ``` - (NSArray<SCNNode *> * _Nonnull)childNodesPassingTest:(BOOL (^ _Nonnull)(SCNNode * _Nonnull child, BOOL * _Nonnull stop))predicate ``` |

Modified [-[SCNNode clone]](https://developer.apple.com/documentation/scenekit/scnnode/1408046-clone)

|  | Declaration |
| --- | --- |
| From | ``` - (id)clone ``` |
| To | ``` - (instancetype _Nonnull)clone ``` |

Modified [SCNNode.constraints](https://developer.apple.com/documentation/scenekit/scnnode/1408016-constraints)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *constraints ``` |
| To | ``` @property(copy, nullable) NSArray<SCNConstraint *> *constraints ``` |

Modified [SCNNode.filters](https://developer.apple.com/documentation/scenekit/scnnode/1407949-filters)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *filters ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<CIFilter *> *filters ``` |

Modified [-[SCNNode flattenedClone]](https://developer.apple.com/documentation/scenekit/scnnode/1407960-flattenedclone)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNNode *)flattenedClone ``` |
| To | ``` - (instancetype _Nonnull)flattenedClone ``` |

Modified [-[SCNNode hitTestWithSegmentFromPoint:toPoint:options:]](https://developer.apple.com/documentation/scenekit/scnnode/1407998-hittestwithsegment)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)hitTestWithSegmentFromPoint:(SCNVector3)pointA toPoint:(SCNVector3)pointB options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNHitTestResult *> * _Nonnull)hitTestWithSegmentFromPoint:(SCNVector3)pointA toPoint:(SCNVector3)pointB options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [SCNNode.presentationNode](https://developer.apple.com/documentation/scenekit/scnnode/1408030-presentation)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNNode *)presentationNode ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNNode *presentationNode ``` |

Modified [-[SCNNodeRendererDelegate renderNode:renderer:arguments:]](https://developer.apple.com/documentation/scenekit/scnnoderendererdelegate/1407993-rendernode)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderNode:(SCNNode *)node renderer:(SCNRenderer *)renderer arguments:(NSDictionary *)arguments ``` |
| To | ``` - (void)renderNode:(SCNNode * _Nonnull)node renderer:(SCNRenderer * _Nonnull)renderer arguments:(NSDictionary<NSString *,NSValue *> * _Nonnull)arguments ``` |

#### SCNParticleSystem.h

Modified [SCNNode.particleSystems](https://developer.apple.com/documentation/scenekit/scnnode/1522705-particlesystems)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *particleSystems ``` |
| To | ``` @property(readonly, nullable) NSArray<SCNParticleSystem *> *particleSystems ``` |

Modified [-[SCNParticleSystem addModifierForProperties:atStage:withBlock:]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522635-addmodifierforproperties)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addModifierForProperties:(NSArray *)properties atStage:(SCNParticleModifierStage)stage withBlock:(SCNParticleModifierBlock)block ``` |
| To | ``` - (void)addModifierForProperties:(NSArray<NSString *> * _Nonnull)properties atStage:(SCNParticleModifierStage)stage withBlock:(SCNParticleModifierBlock _Nonnull)block ``` |

Modified [SCNParticleSystem.colliderNodes](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523516-collidernodes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *colliderNodes ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<SCNNode *> *colliderNodes ``` |

Modified [-[SCNParticleSystem handleEvent:forProperties:withBlock:]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523251-handleevent)

|  | Declaration |
| --- | --- |
| From | ``` - (void)handleEvent:(SCNParticleEvent)event forProperties:(NSArray *)properties withBlock:(SCNParticleEventBlock)block ``` |
| To | ``` - (void)handleEvent:(SCNParticleEvent)event forProperties:(NSArray<NSString *> * _Nonnull)properties withBlock:(SCNParticleEventBlock _Nonnull)block ``` |

Modified [SCNParticleSystem.propertyControllers](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522775-propertycontrollers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDictionary *propertyControllers ``` |
| To | ``` @property(nonatomic, copy, nullable) NSDictionary<NSString *,SCNParticlePropertyController *> *propertyControllers ``` |

Modified [SCNScene.particleSystems](https://developer.apple.com/documentation/scenekit/scnscene/1522787-particlesystems)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *particleSystems ``` |
| To | ``` @property(readonly, nullable) NSArray<SCNParticleSystem *> *particleSystems ``` |

#### SCNPhysicsBehavior.h

Modified [+[SCNPhysicsVehicle vehicleWithChassisBody:wheels:]](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387943-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)vehicleWithChassisBody:(SCNPhysicsBody *)chassisBody wheels:(NSArray *)wheels ``` |
| To | ``` + (instancetype _Nonnull)vehicleWithChassisBody:(SCNPhysicsBody * _Nonnull)chassisBody wheels:(NSArray<SCNPhysicsVehicleWheel *> * _Nonnull)wheels ``` |

Modified [SCNPhysicsVehicle.wheels](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387906-wheels)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *wheels ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<SCNPhysicsVehicleWheel *> *wheels ``` |

#### SCNPhysicsBody.h

Added [SCNPhysicsBody.affectedByGravity](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514738-affectedbygravity)Added [SCNPhysicsBody.contactTestBitMask](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514746-contacttestbitmask)Added [SCNPhysicsBody.momentOfInertia](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514777-momentofinertia)Added [SCNPhysicsBody.usesDefaultMomentOfInertia](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514761-usesdefaultmomentofinertia)Modified [SCNPhysicsBody.categoryBitMask](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514768-categorybitmask)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) NSUInteger categoryBitMask ``` |
| To | ``` @property(nonatomic) NSUInteger categoryBitMask ``` |

Modified [SCNPhysicsBody.collisionBitMask](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514772-collisionbitmask)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) NSUInteger collisionBitMask ``` |
| To | ``` @property(nonatomic) NSUInteger collisionBitMask ``` |

#### SCNPhysicsShape.h

Added [SCNPhysicsShape.options](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508904-options)Added [SCNPhysicsShape.sourceObject](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508888-sourceobject)Added [SCNPhysicsShape.transforms](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508898-transforms)Modified [+[SCNPhysicsShape shapeWithGeometry:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508897-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeWithGeometry:(SCNGeometry *)geometry options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nonnull)shapeWithGeometry:(SCNGeometry * _Nonnull)geometry options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[SCNPhysicsShape shapeWithNode:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508889-shapewithnode)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeWithNode:(SCNNode *)node options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nonnull)shapeWithNode:(SCNNode * _Nonnull)node options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[SCNPhysicsShape shapeWithShapes:transforms:]](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508886-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeWithShapes:(NSArray *)shapes transforms:(NSArray *)transforms ``` |
| To | ``` + (instancetype _Nonnull)shapeWithShapes:(NSArray<SCNPhysicsShape *> * _Nonnull)shapes transforms:(NSArray<NSValue *> * _Nullable)transforms ``` |

#### SCNPhysicsWorld.h

Modified [SCNPhysicsWorld.allBehaviors](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512853-allbehaviors)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)allBehaviors ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<SCNPhysicsBehavior *> *allBehaviors ``` |

Modified [-[SCNPhysicsWorld contactTestBetweenBody:andBody:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512875-contacttestbetween)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)contactTestBetweenBody:(SCNPhysicsBody *)bodyA andBody:(SCNPhysicsBody *)bodyB options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNPhysicsContact *> * _Nonnull)contactTestBetweenBody:(SCNPhysicsBody * _Nonnull)bodyA andBody:(SCNPhysicsBody * _Nonnull)bodyB options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNPhysicsWorld contactTestWithBody:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512841-contacttestwithbody)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)contactTestWithBody:(SCNPhysicsBody *)body options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNPhysicsContact *> * _Nonnull)contactTestWithBody:(SCNPhysicsBody * _Nonnull)body options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNPhysicsWorld convexSweepTestWithShape:fromTransform:toTransform:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512859-convexsweeptest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)convexSweepTestWithShape:(SCNPhysicsShape *)shape fromTransform:(SCNMatrix4)from toTransform:(SCNMatrix4)to options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNPhysicsContact *> * _Nonnull)convexSweepTestWithShape:(SCNPhysicsShape * _Nonnull)shape fromTransform:(SCNMatrix4)from toTransform:(SCNMatrix4)to options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNPhysicsWorld rayTestWithSegmentFromPoint:toPoint:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512857-raytestwithsegmentfrompoint)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)rayTestWithSegmentFromPoint:(SCNVector3)origin toPoint:(SCNVector3)dest options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNHitTestResult *> * _Nonnull)rayTestWithSegmentFromPoint:(SCNVector3)origin toPoint:(SCNVector3)dest options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

#### SCNReferenceNode.h (Added)

Added [SCNReferenceNode](https://developer.apple.com/documentation/scenekit/scnreferencenode)Added [-[SCNReferenceNode initWithCoder:]](https://developer.apple.com/documentation/scenekit/scnreferencenode/1524061-init)Added [-[SCNReferenceNode initWithURL:]](https://developer.apple.com/documentation/scenekit/scnreferencenode/1523967-init)Added [-[SCNReferenceNode load]](https://developer.apple.com/documentation/scenekit/scnreferencenode/1523204-load)Added [SCNReferenceNode.loaded](https://developer.apple.com/documentation/scenekit/scnreferencenode/1523906-loaded)Added [SCNReferenceNode.loadingPolicy](https://developer.apple.com/documentation/scenekit/scnreferencenode/1522996-loadingpolicy)Added [+[SCNReferenceNode referenceNodeWithURL:]](https://developer.apple.com/documentation/scenekit/scnreferencenode/1551036-referencenodewithurl)Added [SCNReferenceNode.referenceURL](https://developer.apple.com/documentation/scenekit/scnreferencenode/1522733-referenceurl)Added [-[SCNReferenceNode unload]](https://developer.apple.com/documentation/scenekit/scnreferencenode/1523566-unload)Added [SCNReferenceLoadingPolicy](https://developer.apple.com/documentation/scenekit/scnreferenceloadingpolicy)Added [SCNReferenceLoadingPolicyImmediate](https://developer.apple.com/documentation/scenekit/scnreferenceloadingpolicy/scnreferenceloadingpolicyimmediate)Added [SCNReferenceLoadingPolicyOnDemand](https://developer.apple.com/documentation/scenekit/scnreferenceloadingpolicy/scnreferenceloadingpolicyondemand)

#### SCNRenderer.h

Added [-[SCNRenderer renderAtTime:viewport:commandBuffer:passDescriptor:]](https://developer.apple.com/documentation/scenekit/scnrenderer/1518401-renderattime)Added [+[SCNRenderer rendererWithDevice:options:]](https://developer.apple.com/documentation/scenekit/scnrenderer/1518404-rendererwithdevice)Modified [-[SCNRenderer render]](https://developer.apple.com/documentation/scenekit/scnrenderer/1518403-render)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [+[SCNRenderer rendererWithContext:options:]](https://developer.apple.com/documentation/scenekit/scnrenderer/1518408-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)rendererWithContext:(void *)context options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nonnull)rendererWithContext:(EAGLContext * _Nonnull)context options:(NSDictionary * _Nullable)options ``` |

#### SCNScene.h

Modified [+[SCNScene sceneNamed:inDirectory:options:]](https://developer.apple.com/documentation/scenekit/scnscene/1522851-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneNamed:(NSString *)name inDirectory:(NSString *)directory options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nullable)sceneNamed:(NSString * _Nonnull)name inDirectory:(NSString * _Nullable)directory options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[SCNScene sceneWithURL:options:error:]](https://developer.apple.com/documentation/scenekit/scnscene/1522660-scenewithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneWithURL:(NSURL *)url options:(NSDictionary *)options error:(NSError **)error ``` |
| To | ``` + (instancetype _Nullable)sceneWithURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,id> * _Nullable)options error:(NSError * _Nullable * _Nullable)error ``` |

#### SCNSceneRenderer.h

Added [SCNSceneRenderer.audioEngine](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522686-audioengine)Added [SCNSceneRenderer.audioEnvironmentNode](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523582-audioenvironmentnode)Added [SCNSceneRenderer.audioListener](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523747-audiolistener)Added [SCNSceneRenderer.colorPixelFormat](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523701-colorpixelformat)Added [SCNSceneRenderer.commandQueue](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523974-commandqueue)Added [SCNSceneRenderer.currentRenderCommandEncoder](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522609-currentrendercommandencoder)Added [SCNSceneRenderer.debugOptions](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523281-debugoptions)Added [SCNSceneRenderer.depthPixelFormat](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523780-depthpixelformat)Added [SCNSceneRenderer.device](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523935-device)Added [-[SCNSceneRenderer nodesInsideFrustumWithPointOfView:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522942-nodesinsidefrustum)Added [-[SCNSceneRenderer presentScene:withTransition:incomingPointOfView:completionHandler:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523028-presentscene)Added [SCNSceneRenderer.renderingAPI](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522616-renderingapi)Added [SCNSceneRenderer.stencilPixelFormat](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523315-stencilpixelformat)Added [SCNDebugOptionNone](https://developer.apple.com/documentation/scenekit/scndebugoptions/scndebugoptionnone)Added [SCNDebugOptions](https://developer.apple.com/documentation/scenekit/scndebugoptions)Added [SCNDebugOptionShowBoundingBoxes](https://developer.apple.com/documentation/scenekit/scndebugoptions/scndebugoptionshowboundingboxes)Added [SCNDebugOptionShowLightExtents](https://developer.apple.com/documentation/scenekit/scndebugoptions/scndebugoptionshowlightextents)Added [SCNDebugOptionShowLightInfluences](https://developer.apple.com/documentation/scenekit/scndebugoptions/1522606-showlightinfluences)Added [SCNDebugOptionShowPhysicsFields](https://developer.apple.com/documentation/scenekit/scndebugoptions/1523589-showphysicsfields)Added [SCNDebugOptionShowPhysicsShapes](https://developer.apple.com/documentation/scenekit/scndebugoptions/1522896-showphysicsshapes)Added [SCNDebugOptionShowWireframe](https://developer.apple.com/documentation/scenekit/scndebugoptions/1523384-showwireframe)Added [SCNRenderingAPI](https://developer.apple.com/documentation/scenekit/scnrenderingapi)Added [SCNRenderingAPIMetal](https://developer.apple.com/documentation/scenekit/scnrenderingapi/metal)Added [SCNRenderingAPIOpenGLES2](https://developer.apple.com/documentation/scenekit/scnrenderingapi/scnrenderingapiopengles2)Modified [-[SCNSceneRenderer hitTest:options:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522929-hittest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)hitTest:(CGPoint)thePoint options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNHitTestResult *> * _Nonnull)hitTest:(CGPoint)point options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNSceneRendererDelegate renderer:didApplyAnimationsAtTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1523038-renderer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderer:(id<SCNSceneRenderer>)aRenderer didApplyAnimationsAtTime:(NSTimeInterval)time ``` |
| To | ``` - (void)renderer:(id<SCNSceneRenderer> _Nonnull)renderer didApplyAnimationsAtTime:(NSTimeInterval)time ``` |

Modified [-[SCNSceneRendererDelegate renderer:didRenderScene:atTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1524233-renderer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderer:(id<SCNSceneRenderer>)aRenderer didRenderScene:(SCNScene *)scene atTime:(NSTimeInterval)time ``` |
| To | ``` - (void)renderer:(id<SCNSceneRenderer> _Nonnull)renderer didRenderScene:(SCNScene * _Nonnull)scene atTime:(NSTimeInterval)time ``` |

Modified [-[SCNSceneRendererDelegate renderer:didSimulatePhysicsAtTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1522738-renderer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderer:(id<SCNSceneRenderer>)aRenderer didSimulatePhysicsAtTime:(NSTimeInterval)time ``` |
| To | ``` - (void)renderer:(id<SCNSceneRenderer> _Nonnull)renderer didSimulatePhysicsAtTime:(NSTimeInterval)time ``` |

Modified [-[SCNSceneRendererDelegate renderer:updateAtTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1522937-renderer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderer:(id<SCNSceneRenderer>)aRenderer updateAtTime:(NSTimeInterval)time ``` |
| To | ``` - (void)renderer:(id<SCNSceneRenderer> _Nonnull)renderer updateAtTime:(NSTimeInterval)time ``` |

Modified [-[SCNSceneRendererDelegate renderer:willRenderScene:atTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1523483-renderer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderer:(id<SCNSceneRenderer>)aRenderer willRenderScene:(SCNScene *)scene atTime:(NSTimeInterval)time ``` |
| To | ``` - (void)renderer:(id<SCNSceneRenderer> _Nonnull)renderer willRenderScene:(SCNScene * _Nonnull)scene atTime:(NSTimeInterval)time ``` |

#### SCNSceneSource.h

Modified [-[SCNSceneSource entriesPassingTest:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523055-entries)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)entriesPassingTest:(BOOL (^)(id entry, NSString *identifier, BOOL *stop))predicate ``` |
| To | ``` - (NSArray<id> * _Nonnull)entriesPassingTest:(BOOL (^ _Nonnull)(id _Nonnull entry, NSString * _Nonnull identifier, BOOL * _Nonnull stop))predicate ``` |

Modified [-[SCNSceneSource identifiersOfEntriesWithClass:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523656-identifiersofentrieswithclass)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)identifiersOfEntriesWithClass:(Class)entryClass ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)identifiersOfEntriesWithClass:(Class _Nonnull)entryClass ``` |

Modified [-[SCNSceneSource initWithData:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523500-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data options:(NSDictionary *)options ``` |
| To | ``` - (instancetype _Nullable)initWithData:(NSData * _Nonnull)data options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNSceneSource initWithURL:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1522629-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url options:(NSDictionary *)options ``` |
| To | ``` - (instancetype _Nullable)initWithURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[SCNSceneSource sceneSourceWithData:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1573764-scenesourcewithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneSourceWithData:(NSData *)data options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nullable)sceneSourceWithData:(NSData * _Nonnull)data options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[SCNSceneSource sceneSourceWithURL:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1573763-scenesourcewithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneSourceWithURL:(NSURL *)url options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nullable)sceneSourceWithURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNSceneSource sceneWithOptions:error:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523962-scenewithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNScene *)sceneWithOptions:(NSDictionary *)options error:(NSError **)error ``` |
| To | ``` - (SCNScene * _Nullable)sceneWithOptions:(NSDictionary<NSString *,id> * _Nullable)options error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[SCNSceneSource sceneWithOptions:statusHandler:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1522887-scene)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNScene *)sceneWithOptions:(NSDictionary *)options statusHandler:(SCNSceneSourceStatusHandler)statusHandler ``` |
| To | ``` - (SCNScene * _Nullable)sceneWithOptions:(NSDictionary<NSString *,id> * _Nullable)options statusHandler:(SCNSceneSourceStatusHandler _Nullable)statusHandler ``` |

#### SCNShadable.h

Added [SCNBufferStream](https://developer.apple.com/documentation/scenekit/scnbufferstream)Added [-[SCNBufferStream writeBytes:length:]](https://developer.apple.com/documentation/scenekit/scnbufferstream/1523175-writebytes)Added [SCNProgram.fragmentFunctionName](https://developer.apple.com/documentation/scenekit/scnprogram/1524012-fragmentfunctionname)Added [-[SCNProgram handleBindingOfBufferNamed:frequency:usingBlock:]](https://developer.apple.com/documentation/scenekit/scnprogram/1524047-handlebindingofbuffernamed)Added [SCNProgram.library](https://developer.apple.com/documentation/scenekit/scnprogram/1522934-library)Added [SCNProgram.vertexFunctionName](https://developer.apple.com/documentation/scenekit/scnprogram/1522799-vertexfunctionname)Added [SCNBufferBindingBlock](https://developer.apple.com/documentation/scenekit/scnbufferbindingblock)Added [SCNBufferFrequency](https://developer.apple.com/documentation/scenekit/scnbufferfrequency)Added [SCNBufferFrequencyPerFrame](https://developer.apple.com/documentation/scenekit/scnbufferfrequency/scnbufferfrequencyperframe)Added [SCNBufferFrequencyPerNode](https://developer.apple.com/documentation/scenekit/scnbufferfrequency/scnbufferfrequencypernode)Added [SCNBufferFrequencyPerShadable](https://developer.apple.com/documentation/scenekit/scnbufferfrequency/scnbufferfrequencypershadable)Modified [-[SCNProgram setSemantic:forSymbol:options:]](https://developer.apple.com/documentation/scenekit/scnprogram/1522730-setsemantic)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setSemantic:(NSString *)semantic forSymbol:(NSString *)symbol options:(NSDictionary *)options ``` |
| To | ``` - (void)setSemantic:(NSString * _Nullable)semantic forSymbol:(NSString * _Nonnull)symbol options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [SCNShadable.shaderModifiers](https://developer.apple.com/documentation/scenekit/scnshadable/1523348-shadermodifiers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDictionary *shaderModifiers ``` |
| To | ``` @property(nonatomic, copy, nullable) NSDictionary<NSString *,NSString *> *shaderModifiers ``` |

#### SCNSkinner.h

Modified [SCNSkinner.boneInverseBindTransforms](https://developer.apple.com/documentation/scenekit/scnskinner/1523802-boneinversebindtransforms)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *boneInverseBindTransforms ``` |
| To | ``` @property(readonly, nonatomic, nullable) NSArray<NSValue *> *boneInverseBindTransforms ``` |

Modified [SCNSkinner.bones](https://developer.apple.com/documentation/scenekit/scnskinner/1522732-bones)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *bones ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSArray<SCNNode *> *bones ``` |

Modified [+[SCNSkinner skinnerWithBaseGeometry:bones:boneInverseBindTransforms:boneWeights:boneIndices:]](https://developer.apple.com/documentation/scenekit/scnskinner/1523964-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)skinnerWithBaseGeometry:(SCNGeometry *)baseGeometry bones:(NSArray *)bones boneInverseBindTransforms:(NSArray *)boneInverseBindTransforms boneWeights:(SCNGeometrySource *)boneWeights boneIndices:(SCNGeometrySource *)boneIndices ``` |
| To | ``` + (instancetype _Nonnull)skinnerWithBaseGeometry:(SCNGeometry * _Nullable)baseGeometry bones:(NSArray<SCNNode *> * _Nonnull)bones boneInverseBindTransforms:(NSArray<NSValue *> * _Nullable)boneInverseBindTransforms boneWeights:(SCNGeometrySource * _Nonnull)boneWeights boneIndices:(SCNGeometrySource * _Nonnull)boneIndices ``` |

#### SCNTechnique.h

Added [-[SCNTechnique objectForKeyedSubscript:]](https://developer.apple.com/documentation/scenekit/scntechnique/1520493-objectforkeyedsubscript)Added [-[SCNTechnique setObject:forKeyedSubscript:]](https://developer.apple.com/documentation/scenekit/scntechnique/1520495-setobject)Modified [SCNTechnique.dictionaryRepresentation](https://developer.apple.com/documentation/scenekit/scntechnique/1520492-dictionaryrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDictionary *dictionaryRepresentation ``` |
| To | ``` @property(readonly, nonnull) NSDictionary<NSString *,id> *dictionaryRepresentation ``` |

Modified [+[SCNTechnique techniqueBySequencingTechniques:]](https://developer.apple.com/documentation/scenekit/scntechnique/1520497-techniquebysequencingtechniques)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNTechnique *)techniqueBySequencingTechniques:(NSArray *)techniques ``` |
| To | ``` + (SCNTechnique * _Nullable)techniqueBySequencingTechniques:(NSArray<SCNTechnique *> * _Nonnull)techniques ``` |

Modified [+[SCNTechnique techniqueWithDictionary:]](https://developer.apple.com/documentation/scenekit/scntechnique/1520494-init)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNTechnique *)techniqueWithDictionary:(NSDictionary *)dictionary ``` |
| To | ``` + (SCNTechnique * _Nullable)techniqueWithDictionary:(NSDictionary<NSString *,id> * _Nonnull)dictionary ``` |

#### SCNTransaction.h

Modified +[SCNTransaction setAnimationTimingFunction:]

|  | Declaration |
| --- | --- |
| From | ``` + (void)setAnimationTimingFunction:(CAMediaTimingFunction *)function ``` |
| To | ``` + (void)setAnimationTimingFunction:(CAMediaTimingFunction * _Nullable)animationTimingFunction ``` |

Modified [+[SCNTransaction setValue:forKey:]](https://developer.apple.com/documentation/scenekit/scntransaction/1524124-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setValue:(id)anObject forKey:(NSString *)key ``` |
| To | ``` + (void)setValue:(id _Nullable)value forKey:(NSString * _Nonnull)key ``` |

#### SCNView.h

Added [SCNPreferLowPowerDeviceKey](https://developer.apple.com/documentation/scenekit/scnview/option/1522859-preferlowpowerdevice)Added [SCNPreferredDeviceKey](https://developer.apple.com/documentation/scenekit/scnview/option/1523209-preferreddevice)Added [SCNPreferredRenderingAPIKey](https://developer.apple.com/documentation/scenekit/scnpreferredrenderingapikey)Modified [-[SCNView initWithFrame:options:]](https://developer.apple.com/documentation/scenekit/scnview/1524215-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(CGRect)frame options:(NSDictionary *)options ``` |
| To | ``` - (instancetype _Nonnull)initWithFrame:(CGRect)frame options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

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
