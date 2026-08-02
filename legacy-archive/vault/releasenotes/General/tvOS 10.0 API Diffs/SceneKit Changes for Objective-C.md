---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Objective-C/SceneKit.html
archived_at: '2026-07-18T02:57:27.707007Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# SceneKit Changes for Objective-C

### SceneKit

#### ModelIO.h

Added [+[MDLAsset assetWithSCNScene:bufferAllocator:]](https://developer.apple.com/documentation/modelio/mdlasset/1643661-assetwithscnscene)Added [+[MDLMesh meshWithSCNGeometry:bufferAllocator:]](https://developer.apple.com/documentation/modelio/mdlmesh/1643663-init)Added [+[MDLObject objectWithSCNNode:bufferAllocator:]](https://developer.apple.com/documentation/modelio/mdlobject/1643660-init)Added [+[MDLSubmesh submeshWithSCNGeometryElement:bufferAllocator:]](https://developer.apple.com/documentation/modelio/mdlsubmesh/1643662-submeshwithscngeometryelement)

#### SceneKit_simd.h (Removed)

Modified [SCNMatrix4FromMat4()](https://developer.apple.com/documentation/scenekit/1522632-scnmatrix4frommat4)

|  | Header |
| --- | --- |
| From | SceneKit/SceneKit_simd.h |
| To | SceneKit/SceneKitTypes.h |

Modified [SCNMatrix4ToMat4()](https://developer.apple.com/documentation/scenekit/1523928-scnmatrix4tomat4)

|  | Header |
| --- | --- |
| From | SceneKit/SceneKit_simd.h |
| To | SceneKit/SceneKitTypes.h |

Modified [SCNVector3FromFloat3()](https://developer.apple.com/documentation/scenekit/1524143-scnvector3fromfloat3)

|  | Header |
| --- | --- |
| From | SceneKit/SceneKit_simd.h |
| To | SceneKit/SceneKitTypes.h |

Modified [SCNVector3ToFloat3()](https://developer.apple.com/documentation/scenekit/1523448-scnvector3tofloat3)

|  | Header |
| --- | --- |
| From | SceneKit/SceneKit_simd.h |
| To | SceneKit/SceneKitTypes.h |

Modified [SCNVector4FromFloat4()](https://developer.apple.com/documentation/scenekit/1523606-scnvector4fromfloat4)

|  | Header |
| --- | --- |
| From | SceneKit/SceneKit_simd.h |
| To | SceneKit/SceneKitTypes.h |

Modified [SCNVector4ToFloat4()](https://developer.apple.com/documentation/scenekit/1523001-scnvector4tofloat4)

|  | Header |
| --- | --- |
| From | SceneKit/SceneKit_simd.h |
| To | SceneKit/SceneKitTypes.h |

#### SceneKitTypes.h

Modified [SCNMatrix4EqualToMatrix4()](https://developer.apple.com/documentation/scenekit/1409665-scnmatrix4equaltomatrix4)

|  | Declaration |
| --- | --- |
| From | ``` bool SCNMatrix4EqualToMatrix4 (     SCNMatrix4 matA,     SCNMatrix4 matB ); ``` |
| To | ``` bool SCNMatrix4EqualToMatrix4 (     SCNMatrix4 a,     SCNMatrix4 b ); ``` |

Modified [SCNMatrix4FromMat4()](https://developer.apple.com/documentation/scenekit/1522632-scnmatrix4frommat4)

|  | Header |
| --- | --- |
| From | SceneKit/SceneKit_simd.h |
| To | SceneKit/SceneKitTypes.h |

Modified [SCNMatrix4Invert()](https://developer.apple.com/documentation/scenekit/1409682-scnmatrix4invert)

|  | Declaration |
| --- | --- |
| From | ``` SCNMatrix4 SCNMatrix4Invert (     SCNMatrix4 mat ); ``` |
| To | ``` SCNMatrix4 SCNMatrix4Invert (     SCNMatrix4 m ); ``` |

Modified [SCNMatrix4IsIdentity()](https://developer.apple.com/documentation/scenekit/1409715-scnmatrix4isidentity)

|  | Declaration |
| --- | --- |
| From | ``` bool SCNMatrix4IsIdentity (     SCNMatrix4 mat ); ``` |
| To | ``` bool SCNMatrix4IsIdentity (     SCNMatrix4 m ); ``` |

Modified [SCNMatrix4MakeTranslation()](https://developer.apple.com/documentation/scenekit/1409679-scnmatrix4maketranslation)

|  | Declaration |
| --- | --- |
| From | ``` SCNMatrix4 SCNMatrix4MakeTranslation (     float x,     float y,     float z ); ``` |
| To | ``` SCNMatrix4 SCNMatrix4MakeTranslation (     float tx,     float ty,     float tz ); ``` |

Modified [SCNMatrix4Mult()](https://developer.apple.com/documentation/scenekit/1409697-scnmatrix4mult)

|  | Declaration |
| --- | --- |
| From | ``` SCNMatrix4 SCNMatrix4Mult (     SCNMatrix4 matA,     SCNMatrix4 matB ); ``` |
| To | ``` SCNMatrix4 SCNMatrix4Mult (     SCNMatrix4 a,     SCNMatrix4 b ); ``` |

Modified [SCNMatrix4Rotate()](https://developer.apple.com/documentation/scenekit/1409659-scnmatrix4rotate)

|  | Declaration |
| --- | --- |
| From | ``` SCNMatrix4 SCNMatrix4Rotate (     SCNMatrix4 mat,     float angle,     float x,     float y,     float z ); ``` |
| To | ``` SCNMatrix4 SCNMatrix4Rotate (     SCNMatrix4 m,     float angle,     float x,     float y,     float z ); ``` |

Modified [SCNMatrix4Scale()](https://developer.apple.com/documentation/scenekit/1409653-scnmatrix4scale)

|  | Declaration |
| --- | --- |
| From | ``` SCNMatrix4 SCNMatrix4Scale (     SCNMatrix4 mat,     float x,     float y,     float z ); ``` |
| To | ``` SCNMatrix4 SCNMatrix4Scale (     SCNMatrix4 m,     float sx,     float sy,     float sz ); ``` |

Modified [SCNMatrix4ToMat4()](https://developer.apple.com/documentation/scenekit/1523928-scnmatrix4tomat4)

|  | Header |
| --- | --- |
| From | SceneKit/SceneKit_simd.h |
| To | SceneKit/SceneKitTypes.h |

Modified [SCNMatrix4Translate()](https://developer.apple.com/documentation/scenekit/1409717-scnmatrix4translate)

|  | Declaration |
| --- | --- |
| From | ``` SCNMatrix4 SCNMatrix4Translate (     SCNMatrix4 mat,     float x,     float y,     float z ); ``` |
| To | ``` SCNMatrix4 SCNMatrix4Translate (     SCNMatrix4 m,     float tx,     float ty,     float tz ); ``` |

Modified [SCNVector3FromFloat3()](https://developer.apple.com/documentation/scenekit/1524143-scnvector3fromfloat3)

|  | Header |
| --- | --- |
| From | SceneKit/SceneKit_simd.h |
| To | SceneKit/SceneKitTypes.h |

Modified [SCNVector3ToFloat3()](https://developer.apple.com/documentation/scenekit/1523448-scnvector3tofloat3)

|  | Header |
| --- | --- |
| From | SceneKit/SceneKit_simd.h |
| To | SceneKit/SceneKitTypes.h |

Modified [SCNVector4FromFloat4()](https://developer.apple.com/documentation/scenekit/1523606-scnvector4fromfloat4)

|  | Header |
| --- | --- |
| From | SceneKit/SceneKit_simd.h |
| To | SceneKit/SceneKitTypes.h |

Modified [SCNVector4ToFloat4()](https://developer.apple.com/documentation/scenekit/1523001-scnvector4tofloat4)

|  | Header |
| --- | --- |
| From | SceneKit/SceneKit_simd.h |
| To | SceneKit/SceneKitTypes.h |

#### SCNAnimation.h

Added [-[SCNAnimatable setSpeed:forAnimationKey:]](https://developer.apple.com/documentation/scenekit/scnanimatable/1778343-setspeed)

#### SCNCamera.h

Removed [-[SCNCamera setProjectionTransform:]](https://developer.apple.com/documentation/scenekit/scncamera/1436590-setprojectiontransform)Added [SCNCamera.averageGray](https://developer.apple.com/documentation/scenekit/scncamera/1644097-averagegray)Added [SCNCamera.bloomBlurRadius](https://developer.apple.com/documentation/scenekit/scncamera/1644096-bloomblurradius)Added [SCNCamera.bloomIntensity](https://developer.apple.com/documentation/scenekit/scncamera/1644104-bloomintensity)Added [SCNCamera.bloomThreshold](https://developer.apple.com/documentation/scenekit/scncamera/1644098-bloomthreshold)Added [SCNCamera.colorFringeIntensity](https://developer.apple.com/documentation/scenekit/scncamera/1644108-colorfringeintensity)Added [SCNCamera.colorFringeStrength](https://developer.apple.com/documentation/scenekit/scncamera/1644113-colorfringestrength)Added [SCNCamera.colorGrading](https://developer.apple.com/documentation/scenekit/scncamera/1644114-colorgrading)Added [SCNCamera.contrast](https://developer.apple.com/documentation/scenekit/scncamera/1644112-contrast)Added [SCNCamera.exposureAdaptationBrighteningSpeedFactor](https://developer.apple.com/documentation/scenekit/scncamera/1644093-exposureadaptationbrighteningspe)Added [SCNCamera.exposureAdaptationDarkeningSpeedFactor](https://developer.apple.com/documentation/scenekit/scncamera/1644094-exposureadaptationdarkeningspeed)Added [SCNCamera.exposureOffset](https://developer.apple.com/documentation/scenekit/scncamera/1644105-exposureoffset)Added [SCNCamera.maximumExposure](https://developer.apple.com/documentation/scenekit/scncamera/1644120-maximumexposure)Added [SCNCamera.minimumExposure](https://developer.apple.com/documentation/scenekit/scncamera/1644103-minimumexposure)Added [SCNCamera.motionBlurIntensity](https://developer.apple.com/documentation/scenekit/scncamera/1644099-motionblurintensity)Added [SCNCamera.saturation](https://developer.apple.com/documentation/scenekit/scncamera/1644100-saturation)Added [SCNCamera.vignettingIntensity](https://developer.apple.com/documentation/scenekit/scncamera/1644106-vignettingintensity)Added [SCNCamera.vignettingPower](https://developer.apple.com/documentation/scenekit/scncamera/1644118-vignettingpower)Added [SCNCamera.wantsExposureAdaptation](https://developer.apple.com/documentation/scenekit/scncamera/1644117-wantsexposureadaptation)Added [SCNCamera.wantsHDR](https://developer.apple.com/documentation/scenekit/scncamera/1644101-wantshdr)Added [SCNCamera.whitePoint](https://developer.apple.com/documentation/scenekit/scncamera/1644110-whitepoint)Modified [SCNCamera.projectionTransform](https://developer.apple.com/documentation/scenekit/scncamera/1690501-projectiontransform)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNMatrix4)projectionTransform ``` |
| To | ``` @property(nonatomic) SCNMatrix4 projectionTransform ``` |

#### SCNConstraint.h

Added [-[SCNLookAtConstraint setTarget:]](https://developer.apple.com/documentation/scenekit/scnlookatconstraint/1644027-settarget)Added [-[SCNLookAtConstraint target]](https://developer.apple.com/documentation/scenekit/scnlookatconstraint/1468677-target)Modified [SCNLookAtConstraint.target](https://developer.apple.com/documentation/scenekit/scnlookatconstraint/1468677-target)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` @property(nonatomic, readonly) SCNNode *target ``` | yes |
| To | ``` @property(nonatomic, retain) SCNNode *target ``` | -- |

#### SCNGeometry.h

Added #def SCNGeometryPrimitiveTypePolygonAdded [SCNGeometrySourceSemantic](https://developer.apple.com/documentation/scenekit/scngeometrysourcesemantic)Added [SCNGeometrySourceSemanticTangent](https://developer.apple.com/documentation/scenekit/scngeometrysourcesemantictangent)Modified [-[SCNGeometry geometrySourcesForSemantic:]](https://developer.apple.com/documentation/scenekit/scngeometry/1522926-geometrysourcesforsemantic)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray<SCNGeometrySource *> *)geometrySourcesForSemantic:(NSString *)semantic ``` |
| To | ``` - (NSArray<SCNGeometrySource *> *)geometrySourcesForSemantic:(SCNGeometrySourceSemantic)semantic ``` |

Modified [+[SCNGeometrySource geometrySourceWithBuffer:vertexFormat:semantic:vertexCount:dataOffset:dataStride:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1522873-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)geometrySourceWithBuffer:(id<MTLBuffer>)mtlBuffer vertexFormat:(MTLVertexFormat)vertexFormat semantic:(NSString *)semantic vertexCount:(NSInteger)vertexCount dataOffset:(NSInteger)offset dataStride:(NSInteger)stride ``` |
| To | ``` + (instancetype)geometrySourceWithBuffer:(id<MTLBuffer>)mtlBuffer vertexFormat:(MTLVertexFormat)vertexFormat semantic:(SCNGeometrySourceSemantic)semantic vertexCount:(NSInteger)vertexCount dataOffset:(NSInteger)offset dataStride:(NSInteger)stride ``` |

Modified [+[SCNGeometrySource geometrySourceWithData:semantic:vectorCount:floatComponents:componentsPerVector:bytesPerComponent:dataOffset:dataStride:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1523320-geometrysourcewithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)geometrySourceWithData:(NSData *)data semantic:(NSString *)semantic vectorCount:(NSInteger)vectorCount floatComponents:(BOOL)floatComponents componentsPerVector:(NSInteger)componentsPerVector bytesPerComponent:(NSInteger)bytesPerComponent dataOffset:(NSInteger)offset dataStride:(NSInteger)stride ``` |
| To | ``` + (instancetype)geometrySourceWithData:(NSData *)data semantic:(SCNGeometrySourceSemantic)semantic vectorCount:(NSInteger)vectorCount floatComponents:(BOOL)floatComponents componentsPerVector:(NSInteger)componentsPerVector bytesPerComponent:(NSInteger)bytesPerComponent dataOffset:(NSInteger)offset dataStride:(NSInteger)stride ``` |

Modified [SCNGeometrySource.semantic](https://developer.apple.com/documentation/scenekit/scngeometrysource/1523071-semantic)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *semantic ``` |
| To | ``` @property(nonatomic, readonly) SCNGeometrySourceSemantic semantic ``` |

#### SCNHitTest.h (Added)

Added [SCNHitTestResult.boneNode](https://developer.apple.com/documentation/scenekit/scnhittestresult/1823463-bonenode)Added [SCNHitTestOption](https://developer.apple.com/documentation/scenekit/scnhittestoption)Added #def SCNHitTestOptionBackFaceCullingAdded #def SCNHitTestOptionBoundingBoxOnlyAdded [SCNHitTestOptionCategoryBitMask](https://developer.apple.com/documentation/scenekit/scnhittestoptioncategorybitmask)Added #def SCNHitTestOptionClipToZRangeAdded #def SCNHitTestOptionFirstFoundOnlyAdded #def SCNHitTestOptionIgnoreChildNodesAdded #def SCNHitTestOptionIgnoreHiddenNodesAdded #def SCNHitTestOptionRootNodeAdded #def SCNHitTestOptionSortResultsModified [SCNHitTestResult](https://developer.apple.com/documentation/scenekit/scnhittestresult)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.faceIndex](https://developer.apple.com/documentation/scenekit/scnhittestresult/1522888-faceindex)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.geometryIndex](https://developer.apple.com/documentation/scenekit/scnhittestresult/1522625-geometryindex)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.localCoordinates](https://developer.apple.com/documentation/scenekit/scnhittestresult/1523032-localcoordinates)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.localNormal](https://developer.apple.com/documentation/scenekit/scnhittestresult/1523953-localnormal)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.modelTransform](https://developer.apple.com/documentation/scenekit/scnhittestresult/1523496-modeltransform)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.node](https://developer.apple.com/documentation/scenekit/scnhittestresult/1523256-node)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [-[SCNHitTestResult textureCoordinatesWithMappingChannel:]](https://developer.apple.com/documentation/scenekit/scnhittestresult/1522771-texturecoordinateswithmappingcha)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.worldCoordinates](https://developer.apple.com/documentation/scenekit/scnhittestresult/1523058-worldcoordinates)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.worldNormal](https://developer.apple.com/documentation/scenekit/scnhittestresult/1524066-worldnormal)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestBackFaceCullingKey](https://developer.apple.com/documentation/scenekit/scnhittestbackfacecullingkey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestBoundingBoxOnlyKey](https://developer.apple.com/documentation/scenekit/scnhittestboundingboxonlykey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestClipToZRangeKey](https://developer.apple.com/documentation/scenekit/scnhittestcliptozrangekey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestFirstFoundOnlyKey](https://developer.apple.com/documentation/scenekit/scnhittestfirstfoundonlykey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestIgnoreChildNodesKey](https://developer.apple.com/documentation/scenekit/scnhittestignorechildnodeskey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestIgnoreHiddenNodesKey](https://developer.apple.com/documentation/scenekit/scnhittestignorehiddennodeskey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestRootNodeKey](https://developer.apple.com/documentation/scenekit/scnhittestrootnodekey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestSortResultsKey](https://developer.apple.com/documentation/scenekit/scnhittestsortresultskey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

#### SCNLight.h

Added [SCNLight.IESProfileURL](https://developer.apple.com/documentation/scenekit/scnlight/1640546-iesprofileurl)Added [SCNLight.intensity](https://developer.apple.com/documentation/scenekit/scnlight/1640548-intensity)Added [SCNLight.temperature](https://developer.apple.com/documentation/scenekit/scnlight/1640545-temperature)Added [SCNLightType](https://developer.apple.com/documentation/scenekit/scnlight/lighttype)Added [SCNLightTypeIES](https://developer.apple.com/documentation/scenekit/scnlighttypeies)Added [SCNLightTypeProbe](https://developer.apple.com/documentation/scenekit/scnlight/lighttype/1778346-probe)Modified [SCNLight.type](https://developer.apple.com/documentation/scenekit/scnlight/1522919-type)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *type ``` |
| To | ``` @property(nonatomic, copy) SCNLightType type ``` |

#### SCNMaterial.h

Removed [SCNCullBack](https://developer.apple.com/documentation/scenekit/scncullback)Removed [SCNCullFront](https://developer.apple.com/documentation/scenekit/scncullfront)Added [SCNMaterial.metalness](https://developer.apple.com/documentation/scenekit/scnmaterial/1640554-metalness)Added [SCNMaterial.roughness](https://developer.apple.com/documentation/scenekit/scnmaterial/1640555-roughness)Added [#def SCNCullBack](https://developer.apple.com/documentation/scenekit/scncullback)Added [#def SCNCullFront](https://developer.apple.com/documentation/scenekit/scncullfront)Added [SCNCullModeBack](https://developer.apple.com/documentation/scenekit/scncullmode/scncullmodeback)Added [SCNCullModeFront](https://developer.apple.com/documentation/scenekit/scncullmode/scncullmodefront)Added [SCNLightingModel](https://developer.apple.com/documentation/scenekit/scnlightingmodel)Added [SCNLightingModelPhysicallyBased](https://developer.apple.com/documentation/scenekit/scnmaterial/lightingmodel/1640553-physicallybased)Modified [SCNMaterial.lightingModelName](https://developer.apple.com/documentation/scenekit/scnmaterial/1462518-lightingmodelname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *lightingModelName ``` |
| To | ``` @property(nonatomic, copy) SCNLightingModel lightingModelName ``` |

#### SCNMaterialProperty.h

Removed [SCNMaterialProperty.borderColor](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/1395376-bordercolor)

#### SCNNode.h

Added [-[SCNNode enumerateHierarchyUsingBlock:]](https://developer.apple.com/documentation/scenekit/scnnode/1642248-enumeratehierarchyusingblock)Added [SCNNode.movabilityHint](https://developer.apple.com/documentation/scenekit/scnnode/1690499-movabilityhint)Added [SCNMovabilityHint](https://developer.apple.com/documentation/scenekit/scnmovabilityhint)Added [SCNMovabilityHintFixed](https://developer.apple.com/documentation/scenekit/scnmovabilityhint/fixed)Added [SCNMovabilityHintMovable](https://developer.apple.com/documentation/scenekit/scnmovabilityhint/movable)Modified [-[SCNNodeRendererDelegate renderNode:renderer:arguments:]](https://developer.apple.com/documentation/scenekit/scnnoderendererdelegate/1407993-rendernode)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderNode:(SCNNode *)node renderer:(SCNRenderer *)renderer arguments:(NSDictionary<NSString *,NSValue *> *)arguments ``` |
| To | ``` - (void)renderNode:(SCNNode *)node renderer:(SCNRenderer *)renderer arguments:(NSDictionary<NSString *,id> *)arguments ``` |

#### SCNParametricGeometry.h

Added [SCNFloor.length](https://developer.apple.com/documentation/scenekit/scnfloor/2091890-length)Added [SCNFloor.reflectionCategoryBitMask](https://developer.apple.com/documentation/scenekit/scnfloor/1845281-reflectioncategorybitmask)Added [SCNFloor.width](https://developer.apple.com/documentation/scenekit/scnfloor/1845280-width)

#### SCNParticleSystem.h

Added [SCNParticleProperty](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty)Modified [SCNParticlePropertyController.inputProperty](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1522973-inputproperty)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *inputProperty ``` |
| To | ``` @property(nonatomic, copy) SCNParticleProperty inputProperty ``` |

Modified [-[SCNParticleSystem addModifierForProperties:atStage:withBlock:]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522635-addmodifierforproperties)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addModifierForProperties:(NSArray<NSString *> *)properties atStage:(SCNParticleModifierStage)stage withBlock:(SCNParticleModifierBlock)block ``` |
| To | ``` - (void)addModifierForProperties:(NSArray<SCNParticleProperty> *)properties atStage:(SCNParticleModifierStage)stage withBlock:(SCNParticleModifierBlock)block ``` |

Modified [-[SCNParticleSystem handleEvent:forProperties:withBlock:]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523251-handleevent)

|  | Declaration |
| --- | --- |
| From | ``` - (void)handleEvent:(SCNParticleEvent)event forProperties:(NSArray<NSString *> *)properties withBlock:(SCNParticleEventBlock)block ``` |
| To | ``` - (void)handleEvent:(SCNParticleEvent)event forProperties:(NSArray<SCNParticleProperty> *)properties withBlock:(SCNParticleEventBlock)block ``` |

Modified [SCNParticleSystem.propertyControllers](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522775-propertycontrollers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDictionary<NSString *,SCNParticlePropertyController *> *propertyControllers ``` |
| To | ``` @property(nonatomic, copy) NSDictionary<SCNParticleProperty,SCNParticlePropertyController *> *propertyControllers ``` |

#### SCNPhysicsShape.h

Added [SCNPhysicsShapeOption](https://developer.apple.com/documentation/scenekit/scnphysicsshapeoption)Added [SCNPhysicsShapeOptionCollisionMargin](https://developer.apple.com/documentation/scenekit/scnphysicsshape/option/1778254-collisionmargin)Added #def SCNPhysicsShapeOptionKeepAsCompoundAdded #def SCNPhysicsShapeOptionScaleAdded #def SCNPhysicsShapeOptionTypeAdded [SCNPhysicsShapeType](https://developer.apple.com/documentation/scenekit/scnphysicsshapetype)Modified [SCNPhysicsShape.options](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508904-options)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSDictionary<NSString *,id> *options ``` |
| To | ``` @property(readonly, nonatomic) NSDictionary<SCNPhysicsShapeOption, id> *options ``` |

Modified [+[SCNPhysicsShape shapeWithGeometry:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508897-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeWithGeometry:(SCNGeometry *)geometry options:(NSDictionary<NSString *,id> *)options ``` |
| To | ``` + (instancetype)shapeWithGeometry:(SCNGeometry *)geometry options:(NSDictionary<SCNPhysicsShapeOption,id> *)options ``` |

Modified [+[SCNPhysicsShape shapeWithNode:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508889-shapewithnode)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeWithNode:(SCNNode *)node options:(NSDictionary<NSString *,id> *)options ``` |
| To | ``` + (instancetype)shapeWithNode:(SCNNode *)node options:(NSDictionary<SCNPhysicsShapeOption,id> *)options ``` |

#### SCNPhysicsWorld.h

Added [SCNPhysicsTestOption](https://developer.apple.com/documentation/scenekit/scnphysicstestoption)Added #def SCNPhysicsTestOptionBackfaceCullingAdded #def SCNPhysicsTestOptionCollisionBitMaskAdded #def SCNPhysicsTestOptionSearchModeAdded [SCNPhysicsTestSearchMode](https://developer.apple.com/documentation/scenekit/scnphysicstestsearchmode)Modified [-[SCNPhysicsWorld contactTestBetweenBody:andBody:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512875-contacttestbetween)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray<SCNPhysicsContact *> *)contactTestBetweenBody:(SCNPhysicsBody *)bodyA andBody:(SCNPhysicsBody *)bodyB options:(NSDictionary<NSString *,id> *)options ``` |
| To | ``` - (NSArray<SCNPhysicsContact *> *)contactTestBetweenBody:(SCNPhysicsBody *)bodyA andBody:(SCNPhysicsBody *)bodyB options:(NSDictionary<SCNPhysicsTestOption,id> *)options ``` |

Modified [-[SCNPhysicsWorld contactTestWithBody:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512841-contacttestwithbody)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray<SCNPhysicsContact *> *)contactTestWithBody:(SCNPhysicsBody *)body options:(NSDictionary<NSString *,id> *)options ``` |
| To | ``` - (NSArray<SCNPhysicsContact *> *)contactTestWithBody:(SCNPhysicsBody *)body options:(NSDictionary<SCNPhysicsTestOption,id> *)options ``` |

Modified [-[SCNPhysicsWorld convexSweepTestWithShape:fromTransform:toTransform:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512859-convexsweeptest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray<SCNPhysicsContact *> *)convexSweepTestWithShape:(SCNPhysicsShape *)shape fromTransform:(SCNMatrix4)from toTransform:(SCNMatrix4)to options:(NSDictionary<NSString *,id> *)options ``` |
| To | ``` - (NSArray<SCNPhysicsContact *> *)convexSweepTestWithShape:(SCNPhysicsShape *)shape fromTransform:(SCNMatrix4)from toTransform:(SCNMatrix4)to options:(NSDictionary<SCNPhysicsTestOption,id> *)options ``` |

Modified [-[SCNPhysicsWorld rayTestWithSegmentFromPoint:toPoint:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512857-raytestwithsegmentfrompoint)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray<SCNHitTestResult *> *)rayTestWithSegmentFromPoint:(SCNVector3)origin toPoint:(SCNVector3)dest options:(NSDictionary<NSString *,id> *)options ``` |
| To | ``` - (NSArray<SCNHitTestResult *> *)rayTestWithSegmentFromPoint:(SCNVector3)origin toPoint:(SCNVector3)dest options:(NSDictionary<SCNPhysicsTestOption,id> *)options ``` |

#### SCNRenderer.h

Removed [-[SCNRenderer render]](https://developer.apple.com/documentation/scenekit/scnrenderer/1518403-render)Added [-[SCNRenderer snapshotAtTime:withSize:antialiasingMode:]](https://developer.apple.com/documentation/scenekit/scnrenderer/1641767-snapshotattime)Added [-[SCNRenderer updateProbes:atTime:]](https://developer.apple.com/documentation/scenekit/scnrenderer/2097153-updateprobes)

#### SCNScene.h

Added [SCNScene.lightingEnvironment](https://developer.apple.com/documentation/scenekit/scnscene/1639532-lightingenvironment)Added [-[SCNScene writeToURL:options:delegate:progressHandler:]](https://developer.apple.com/documentation/scenekit/scnscene/1523577-write)Added [SCNSceneExportDelegate](https://developer.apple.com/documentation/scenekit/scnsceneexportdelegate)Added [-[SCNSceneExportDelegate writeImage:withSceneDocumentURL:originalImageURL:]](https://developer.apple.com/documentation/scenekit/scnsceneexportdelegate/1524221-write)Added [SCNSceneAttribute](https://developer.apple.com/documentation/scenekit/scnsceneattribute)Added #def SCNSceneAttributeEndTimeAdded #def SCNSceneAttributeFrameRateAdded #def SCNSceneAttributeStartTimeAdded #def SCNSceneAttributeUpAxisModified [+[SCNScene sceneNamed:inDirectory:options:]](https://developer.apple.com/documentation/scenekit/scnscene/1522851-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneNamed:(NSString *)name inDirectory:(NSString *)directory options:(NSDictionary<NSString *,id> *)options ``` |
| To | ``` + (instancetype)sceneNamed:(NSString *)name inDirectory:(NSString *)directory options:(NSDictionary<SCNSceneSourceLoadingOption,id> *)options ``` |

Modified [+[SCNScene sceneWithURL:options:error:]](https://developer.apple.com/documentation/scenekit/scnscene/1522660-scenewithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneWithURL:(NSURL *)url options:(NSDictionary<NSString *,id> *)options error:(NSError * _Nullable *)error ``` |
| To | ``` + (instancetype)sceneWithURL:(NSURL *)url options:(NSDictionary<SCNSceneSourceLoadingOption,id> *)options error:(NSError * _Nullable *)error ``` |

#### SCNSceneRenderer.h

Modified [SCNHitTestResult](https://developer.apple.com/documentation/scenekit/scnhittestresult)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.faceIndex](https://developer.apple.com/documentation/scenekit/scnhittestresult/1522888-faceindex)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.geometryIndex](https://developer.apple.com/documentation/scenekit/scnhittestresult/1522625-geometryindex)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.localCoordinates](https://developer.apple.com/documentation/scenekit/scnhittestresult/1523032-localcoordinates)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.localNormal](https://developer.apple.com/documentation/scenekit/scnhittestresult/1523953-localnormal)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.modelTransform](https://developer.apple.com/documentation/scenekit/scnhittestresult/1523496-modeltransform)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.node](https://developer.apple.com/documentation/scenekit/scnhittestresult/1523256-node)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [-[SCNHitTestResult textureCoordinatesWithMappingChannel:]](https://developer.apple.com/documentation/scenekit/scnhittestresult/1522771-texturecoordinateswithmappingcha)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.worldCoordinates](https://developer.apple.com/documentation/scenekit/scnhittestresult/1523058-worldcoordinates)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestResult.worldNormal](https://developer.apple.com/documentation/scenekit/scnhittestresult/1524066-worldnormal)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [-[SCNSceneRenderer hitTest:options:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522929-hittest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray<SCNHitTestResult *> *)hitTest:(CGPoint)point options:(NSDictionary<NSString *,id> *)options ``` |
| To | ``` - (NSArray<SCNHitTestResult *> *)hitTest:(CGPoint)point options:(NSDictionary<SCNHitTestOption,id> *)options ``` |

Modified [SCNAntialiasingMode](https://developer.apple.com/documentation/scenekit/scnantialiasingmode)

|  | Header |
| --- | --- |
| From | SceneKit/SCNView.h |
| To | SceneKit/SCNSceneRenderer.h |

Modified [SCNAntialiasingModeMultisampling2X](https://developer.apple.com/documentation/scenekit/scnantialiasingmode/multisampling2x)

|  | Header |
| --- | --- |
| From | SceneKit/SCNView.h |
| To | SceneKit/SCNSceneRenderer.h |

Modified [SCNAntialiasingModeMultisampling4X](https://developer.apple.com/documentation/scenekit/scnantialiasingmode/scnantialiasingmodemultisampling4x)

|  | Header |
| --- | --- |
| From | SceneKit/SCNView.h |
| To | SceneKit/SCNSceneRenderer.h |

Modified [SCNAntialiasingModeNone](https://developer.apple.com/documentation/scenekit/scnantialiasingmode/none)

|  | Header |
| --- | --- |
| From | SceneKit/SCNView.h |
| To | SceneKit/SCNSceneRenderer.h |

Modified [SCNHitTestBackFaceCullingKey](https://developer.apple.com/documentation/scenekit/scnhittestbackfacecullingkey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestBoundingBoxOnlyKey](https://developer.apple.com/documentation/scenekit/scnhittestboundingboxonlykey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestClipToZRangeKey](https://developer.apple.com/documentation/scenekit/scnhittestcliptozrangekey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestFirstFoundOnlyKey](https://developer.apple.com/documentation/scenekit/scnhittestfirstfoundonlykey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestIgnoreChildNodesKey](https://developer.apple.com/documentation/scenekit/scnhittestignorechildnodeskey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestIgnoreHiddenNodesKey](https://developer.apple.com/documentation/scenekit/scnhittestignorehiddennodeskey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestRootNodeKey](https://developer.apple.com/documentation/scenekit/scnhittestrootnodekey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

Modified [SCNHitTestSortResultsKey](https://developer.apple.com/documentation/scenekit/scnhittestsortresultskey)

|  | Header |
| --- | --- |
| From | SceneKit/SCNSceneRenderer.h |
| To | SceneKit/SCNHitTest.h |

#### SCNSceneSource.h

Added [SCNSceneSourceAnimationImportPolicy](https://developer.apple.com/documentation/scenekit/scnscenesource/animationimportpolicy)Added [SCNSceneSourceLoadingOption](https://developer.apple.com/documentation/scenekit/scnscenesource/loadingoption)Added #def SCNSceneSourceLoadingOptionAnimationImportPolicyAdded #def SCNSceneSourceLoadingOptionAssetDirectoryURLsAdded #def SCNSceneSourceLoadingOptionCheckConsistencyAdded #def SCNSceneSourceLoadingOptionConvertToYUpAdded #def SCNSceneSourceLoadingOptionConvertUnitsToMetersAdded #def SCNSceneSourceLoadingOptionCreateNormalsIfAbsentAdded #def SCNSceneSourceLoadingOptionFlattenSceneAdded #def SCNSceneSourceLoadingOptionOverrideAssetURLsAdded [SCNSceneSourceLoadingOptionPreserveOriginalTopology](https://developer.apple.com/documentation/scenekit/scnscenesource/loadingoption/1778185-preserveoriginaltopology)Added #def SCNSceneSourceLoadingOptionStrictConformanceAdded #def SCNSceneSourceLoadingOptionUseSafeModeModified [-[SCNSceneSource initWithData:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523500-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithData:(NSData *)data options:(NSDictionary<NSString *,id> *)options ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data options:(NSDictionary<SCNSceneSourceLoadingOption,id> *)options ``` |

Modified [-[SCNSceneSource initWithURL:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1522629-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithURL:(NSURL *)url options:(NSDictionary<NSString *,id> *)options ``` |
| To | ``` - (instancetype)initWithURL:(NSURL *)url options:(NSDictionary<SCNSceneSourceLoadingOption,id> *)options ``` |

Modified [+[SCNSceneSource sceneSourceWithData:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1573764-scenesourcewithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneSourceWithData:(NSData *)data options:(NSDictionary<NSString *,id> *)options ``` |
| To | ``` + (instancetype)sceneSourceWithData:(NSData *)data options:(NSDictionary<SCNSceneSourceLoadingOption,id> *)options ``` |

Modified [+[SCNSceneSource sceneSourceWithURL:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1573763-scenesourcewithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneSourceWithURL:(NSURL *)url options:(NSDictionary<NSString *,id> *)options ``` |
| To | ``` + (instancetype)sceneSourceWithURL:(NSURL *)url options:(NSDictionary<SCNSceneSourceLoadingOption,id> *)options ``` |

Modified [-[SCNSceneSource sceneWithOptions:error:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523962-scenewithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNScene *)sceneWithOptions:(NSDictionary<NSString *,id> *)options error:(NSError * _Nullable *)error ``` |
| To | ``` - (SCNScene *)sceneWithOptions:(NSDictionary<SCNSceneSourceLoadingOption,id> *)options error:(NSError * _Nullable *)error ``` |

Modified [-[SCNSceneSource sceneWithOptions:statusHandler:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1522887-scene)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNScene *)sceneWithOptions:(NSDictionary<NSString *,id> *)options statusHandler:(SCNSceneSourceStatusHandler)statusHandler ``` |
| To | ``` - (SCNScene *)sceneWithOptions:(NSDictionary<SCNSceneSourceLoadingOption,id> *)options statusHandler:(SCNSceneSourceStatusHandler)statusHandler ``` |

#### SCNShadable.h

Added [SCNShaderModifierEntryPoint](https://developer.apple.com/documentation/scenekit/scnshadermodifierentrypoint)Modified [SCNShadable.shaderModifiers](https://developer.apple.com/documentation/scenekit/scnshadable/1523348-shadermodifiers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDictionary<NSString *,NSString *> *shaderModifiers ``` |
| To | ``` @property(nonatomic, copy) NSDictionary<SCNShaderModifierEntryPoint,NSString *> *shaderModifiers ``` |

#### SCNTransaction.h

Added [SCNTransaction.animationDuration](https://developer.apple.com/documentation/scenekit/scntransaction/1523888-animationduration)Added [SCNTransaction.animationTimingFunction](https://developer.apple.com/documentation/scenekit/scntransaction/1522614-animationtimingfunction)Added [SCNTransaction.completionBlock](https://developer.apple.com/documentation/scenekit/scntransaction/1523660-completionblock)Added [SCNTransaction.disableActions](https://developer.apple.com/documentation/scenekit/scntransaction/1524238-disableactions)Modified +[SCNTransaction setAnimationDuration:]

|  | Declaration |
| --- | --- |
| From | ``` + (void)setAnimationDuration:(CFTimeInterval)duration ``` |
| To | ``` + (void)setAnimationDuration:(CFTimeInterval)animationDuration ``` |

Modified +[SCNTransaction setCompletionBlock:]

|  | Declaration |
| --- | --- |
| From | ``` + (void)setCompletionBlock:(void (^)(void))block ``` |
| To | ``` + (void)setCompletionBlock:(void (^)(void))completionBlock ``` |

Modified +[SCNTransaction setDisableActions:]

|  | Declaration |
| --- | --- |
| From | ``` + (void)setDisableActions:(BOOL)flag ``` |
| To | ``` + (void)setDisableActions:(BOOL)disableActions ``` |

#### SCNView.h

Added [SCNViewOption](https://developer.apple.com/documentation/scenekit/scnviewoption)Added #def SCNViewOptionPreferLowPowerDeviceAdded #def SCNViewOptionPreferredDeviceAdded #def SCNViewOptionPreferredRenderingAPIModified [SCNAntialiasingMode](https://developer.apple.com/documentation/scenekit/scnantialiasingmode)

|  | Header |
| --- | --- |
| From | SceneKit/SCNView.h |
| To | SceneKit/SCNSceneRenderer.h |

Modified [SCNAntialiasingModeMultisampling2X](https://developer.apple.com/documentation/scenekit/scnantialiasingmode/multisampling2x)

|  | Header |
| --- | --- |
| From | SceneKit/SCNView.h |
| To | SceneKit/SCNSceneRenderer.h |

Modified [SCNAntialiasingModeMultisampling4X](https://developer.apple.com/documentation/scenekit/scnantialiasingmode/scnantialiasingmodemultisampling4x)

|  | Header |
| --- | --- |
| From | SceneKit/SCNView.h |
| To | SceneKit/SCNSceneRenderer.h |

Modified [SCNAntialiasingModeNone](https://developer.apple.com/documentation/scenekit/scnantialiasingmode/none)

|  | Header |
| --- | --- |
| From | SceneKit/SCNView.h |
| To | SceneKit/SCNSceneRenderer.h |

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
