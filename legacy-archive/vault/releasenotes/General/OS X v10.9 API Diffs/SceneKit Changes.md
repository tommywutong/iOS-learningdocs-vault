---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/SceneKit.html
archived_at: '2026-07-18T02:54:21.513672Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# SceneKit Changes

## SceneKit

SCNAnimation.hAdded [CAAnimation.animationEvents](https://developer.apple.com/documentation/quartzcore/caanimation/1523940-animationevents)Added [CAAnimation.fadeInDuration](https://developer.apple.com/documentation/quartzcore/caanimation/1523370-fadeinduration)Added [CAAnimation.fadeOutDuration](https://developer.apple.com/documentation/quartzcore/caanimation/1522959-fadeoutduration)Added [-[SCNAnimatable isAnimationForKeyPaused:]](https://developer.apple.com/documentation/scenekit/scnanimatable/1523703-isanimationforkeypaused)Added [-[SCNAnimatable pauseAnimationForKey:]](https://developer.apple.com/documentation/scenekit/scnanimatable/1523592-pauseanimation)Added [-[SCNAnimatable resumeAnimationForKey:]](https://developer.apple.com/documentation/scenekit/scnanimatable/1523332-resumeanimationforkey)Added [SCNAnimationEvent](https://developer.apple.com/documentation/scenekit/scnanimationevent)Added [+[SCNAnimationEvent animationEventWithKeyTime:block:]](https://developer.apple.com/documentation/scenekit/scnanimationevent/1524004-init)Added [SCNAnimationEventBlock](https://developer.apple.com/documentation/scenekit/scnanimationeventblock)SCNBase.hRemoved #def SCENEKIT_DEPRECATEDRemoved #def SCENEKIT_EXTERNRemoved #def SCENEKIT_INLINERemoved #def SCENEKIT_UNUSEDAdded #def SCENEKIT_CLASS_AVAILABLEAdded #def SCENEKIT_ENUM_AVAILABLEAdded #def SCN_EXTERNSCNBoundingVolume.hAdded [-[SCNBoundingVolume setBoundingBoxMin:max:]](https://developer.apple.com/documentation/scenekit/scnboundingvolume/1522866-setboundingboxmin)SCNCamera.hAdded [SCNCamera.aperture](https://developer.apple.com/documentation/scenekit/scncamera/1436594-aperture)Added [SCNCamera.automaticallyAdjustsZRange](https://developer.apple.com/documentation/scenekit/scncamera/1436610-automaticallyadjustszrange)Added [SCNCamera.focalBlurRadius](https://developer.apple.com/documentation/scenekit/scncamera/1436606-focalblurradius)Added [SCNCamera.focalDistance](https://developer.apple.com/documentation/scenekit/scncamera/1436600-focaldistance)Added [SCNCamera.focalSize](https://developer.apple.com/documentation/scenekit/scncamera/1436604-focalsize)Added [SCNCamera.orthographicScale](https://developer.apple.com/documentation/scenekit/scncamera/1436612-orthographicscale)Added [-[SCNCamera setProjectionTransform:]](https://developer.apple.com/documentation/scenekit/scncamera/1436590-setprojectiontransform)Modified [+[SCNCamera camera]](https://developer.apple.com/documentation/scenekit/scncamera/1436602-camera)

|  | Declaration |
| --- | --- |
| From | + (SCNCamera \*)camera |
| To | + (instancetype)camera |

SCNConstraint.hAdded [SCNConstraint](https://developer.apple.com/documentation/scenekit/scnconstraint)Added [SCNLookAtConstraint](https://developer.apple.com/documentation/scenekit/scnlookatconstraint)Added [SCNLookAtConstraint.gimbalLockEnabled](https://developer.apple.com/documentation/scenekit/scnlookatconstraint/1468675-isgimballockenabled)Added [+[SCNLookAtConstraint lookAtConstraintWithTarget:]](https://developer.apple.com/documentation/scenekit/scnlookatconstraint/1468683-init)Added [SCNLookAtConstraint.target](https://developer.apple.com/documentation/scenekit/scnlookatconstraint/1468677-target)Added [SCNTransformConstraint](https://developer.apple.com/documentation/scenekit/scntransformconstraint)Added [+[SCNTransformConstraint transformConstraintInWorldSpace:withBlock:]](https://developer.apple.com/documentation/scenekit/scntransformconstraint/1468679-init)SCNGeometry.hAdded [+[SCNGeometry geometry]](https://developer.apple.com/documentation/scenekit/scngeometry/1585530-geometry)Added [SCNGeometry.levelsOfDetail](https://developer.apple.com/documentation/scenekit/scngeometry/1523745-levelsofdetail)Modified [SCNGeometry](https://developer.apple.com/documentation/scenekit/scngeometry)

|  | Protocols |
| --- | --- |
| From | NSCopying, SCNAnimatable, SCNBoundingVolume |
| To | NSCopying, SCNAnimatable, SCNBoundingVolume, SCNShadable |

Modified [+[SCNGeometry geometryWithSources:elements:]](https://developer.apple.com/documentation/scenekit/scngeometry/1522803-geometrywithsources)

|  | Declaration |
| --- | --- |
| From | + (id)geometryWithSources:(NSArray \*)sources elements:(NSArray \*)elements |
| To | + (instancetype)geometryWithSources:(NSArray \*)sources elements:(NSArray \*)elements |

Modified [+[SCNGeometryElement geometryElementWithData:primitiveType:primitiveCount:bytesPerIndex:]](https://developer.apple.com/documentation/scenekit/scngeometryelement/1522615-init)

|  | Declaration |
| --- | --- |
| From | + (id)geometryElementWithData:(NSData \*)data primitiveType:(SCNGeometryPrimitiveType)primitiveType primitiveCount:(NSInteger)primitiveCount bytesPerIndex:(NSInteger)bytesPerIndex |
| To | + (instancetype)geometryElementWithData:(NSData \*)data primitiveType:(SCNGeometryPrimitiveType)primitiveType primitiveCount:(NSInteger)primitiveCount bytesPerIndex:(NSInteger)bytesPerIndex |

Modified [+[SCNGeometrySource geometrySourceWithData:semantic:vectorCount:floatComponents:componentsPerVector:bytesPerComponent:dataOffset:dataStride:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1523320-geometrysourcewithdata)

|  | Declaration |
| --- | --- |
| From | + (id)geometrySourceWithData:(NSData \*)data semantic:(NSString \*)semantic vectorCount:(NSInteger)vectorCount floatComponents:(BOOL)floatComponents componentsPerVector:(NSInteger)componentsPerVector bytesPerComponent:(NSInteger)bytesPerComponent dataOffset:(NSInteger)offset dataStride:(NSInteger)stride |
| To | + (instancetype)geometrySourceWithData:(NSData \*)data semantic:(NSString \*)semantic vectorCount:(NSInteger)vectorCount floatComponents:(BOOL)floatComponents componentsPerVector:(NSInteger)componentsPerVector bytesPerComponent:(NSInteger)bytesPerComponent dataOffset:(NSInteger)offset dataStride:(NSInteger)stride |

Modified [+[SCNGeometrySource geometrySourceWithNormals:count:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1522882-geometrysourcewithnormals)

|  | Declaration |
| --- | --- |
| From | + (id)geometrySourceWithNormals:(SCNVector3 \*)normals count:(NSInteger)count |
| To | + (instancetype)geometrySourceWithNormals:(SCNVector3 \*)normals count:(NSInteger)count |

Modified [+[SCNGeometrySource geometrySourceWithTextureCoordinates:count:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1522718-geometrysourcewithtexturecoordin)

|  | Declaration |
| --- | --- |
| From | + (id)geometrySourceWithTextureCoordinates:(CGPoint \*)texcoord count:(NSInteger)count |
| To | + (instancetype)geometrySourceWithTextureCoordinates:(CGPoint \*)texcoord count:(NSInteger)count |

Modified [+[SCNGeometrySource geometrySourceWithVertices:count:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1523882-geometrysourcewithvertices)

|  | Declaration |
| --- | --- |
| From | + (id)geometrySourceWithVertices:(SCNVector3 \*)vertices count:(NSInteger)count |
| To | + (instancetype)geometrySourceWithVertices:(SCNVector3 \*)vertices count:(NSInteger)count |

SCNLevelOfDetail.hAdded [SCNLevelOfDetail](https://developer.apple.com/documentation/scenekit/scnlevelofdetail)Added [SCNLevelOfDetail.geometry](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/1522819-geometry)Added [+[SCNLevelOfDetail levelOfDetailWithGeometry:screenSpaceRadius:]](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/1523557-init)Added [+[SCNLevelOfDetail levelOfDetailWithGeometry:worldSpaceDistance:]](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/1522802-init)Added [SCNLevelOfDetail.screenSpaceRadius](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/1523554-screenspaceradius)Added [SCNLevelOfDetail.worldSpaceDistance](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/1524159-worldspacedistance)SCNLight.hAdded [SCNLight.gobo](https://developer.apple.com/documentation/scenekit/scnlight/1523524-gobo)Modified [+[SCNLight light]](https://developer.apple.com/documentation/scenekit/scnlight/1542979-light)

|  | Declaration |
| --- | --- |
| From | + (SCNLight \*)light |
| To | + (instancetype)light |

SCNMaterial.hRemoved SCNMaterial.programAdded [SCNMaterial.fresnelExponent](https://developer.apple.com/documentation/scenekit/scnmaterial/1462587-fresnelexponent)Added [SCNMaterial.readsFromDepthBuffer](https://developer.apple.com/documentation/scenekit/scnmaterial/1462562-readsfromdepthbuffer)Modified [SCNMaterial](https://developer.apple.com/documentation/scenekit/scnmaterial)

|  | Protocols |
| --- | --- |
| From | NSCopying, SCNAnimatable |
| To | NSCopying, SCNAnimatable, SCNShadable |

Modified [+[SCNMaterial material]](https://developer.apple.com/documentation/scenekit/scnmaterial/1462552-material)

|  | Declaration |
| --- | --- |
| From | + (SCNMaterial \*)material |
| To | + (instancetype)material |

Modified [SCNProgram](https://developer.apple.com/documentation/scenekit/scnprogram)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [SCNProgram.delegate](https://developer.apple.com/documentation/scenekit/scnprogram/1522611-delegate)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [SCNProgram.fragmentShader](https://developer.apple.com/documentation/scenekit/scnprogram/1523135-fragmentshader)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [+[SCNProgram program]](https://developer.apple.com/documentation/scenekit/scnprogram/1565076-program)

|  | Header | Declaration |
| --- | --- | --- |
| From | SceneKit/SCNMaterial.h | + (SCNProgram \*)program |
| To | SceneKit/SCNShadable.h | + (instancetype)program |

Modified [-[SCNProgram semanticForSymbol:]](https://developer.apple.com/documentation/scenekit/scnprogram/1523350-semantic)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [-[SCNProgram setSemantic:forSymbol:options:]](https://developer.apple.com/documentation/scenekit/scnprogram/1522730-setsemantic)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [SCNProgram.vertexShader](https://developer.apple.com/documentation/scenekit/scnprogram/1522891-vertexshader)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [SCNProgramDelegate](https://developer.apple.com/documentation/scenekit/scnprogramdelegate)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [-[SCNProgramDelegate program:bindValueForSymbol:atLocation:programID:renderer:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1524155-program)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [-[SCNProgramDelegate program:handleError:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1523007-program)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [-[SCNProgramDelegate program:unbindValueForSymbol:atLocation:programID:renderer:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1523857-program)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [-[SCNProgramDelegate programIsOpaque:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1523068-programisopaque)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

SCNMaterialProperty.hAdded [SCNMaterialProperty.intensity](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/1395407-intensity)Added [+[SCNMaterialProperty materialPropertyWithContents:]](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/1395386-init)Added [SCNMaterialProperty.maxAnisotropy](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/1395402-maxanisotropy)Added [SCNFilterModeLinear](https://developer.apple.com/documentation/scenekit/scnfiltermode/linear)Added [SCNFilterModeNearest](https://developer.apple.com/documentation/scenekit/scnfiltermode/scnfiltermodenearest)Added [SCNFilterModeNone](https://developer.apple.com/documentation/scenekit/scnfiltermode/scnfiltermodenone)Added [SCNWrapModeClamp](https://developer.apple.com/documentation/scenekit/scnwrapmode/clamp)Added [SCNWrapModeClampToBorder](https://developer.apple.com/documentation/scenekit/scnwrapmode/scnwrapmodeclamptoborder)Added [SCNWrapModeMirror](https://developer.apple.com/documentation/scenekit/scnwrapmode/scnwrapmodemirror)Added [SCNWrapModeRepeat](https://developer.apple.com/documentation/scenekit/scnwrapmode/scnwrapmoderepeat)SCNMorpher.hAdded [SCNMorpher](https://developer.apple.com/documentation/scenekit/scnmorpher)Added [SCNMorpher.calculationMode](https://developer.apple.com/documentation/scenekit/scnmorpher/1523754-calculationmode)Added [-[SCNMorpher setWeight:forTargetAtIndex:]](https://developer.apple.com/documentation/scenekit/scnmorpher/1522886-setweight)Added [SCNMorpher.targets](https://developer.apple.com/documentation/scenekit/scnmorpher/1523572-targets)Added [-[SCNMorpher weightForTargetAtIndex:]](https://developer.apple.com/documentation/scenekit/scnmorpher/1522940-weight)Added [SCNMorpherCalculationMode](https://developer.apple.com/documentation/scenekit/scnmorphercalculationmode)Added [SCNMorpherCalculationModeAdditive](https://developer.apple.com/documentation/scenekit/scnmorphercalculationmode/scnmorphercalculationmodeadditive)Added [SCNMorpherCalculationModeNormalized](https://developer.apple.com/documentation/scenekit/scnmorphercalculationmode/normalized)SCNNode.hAdded [SCNNode.constraints](https://developer.apple.com/documentation/scenekit/scnnode/1408016-constraints)Added [-[SCNNode convertPosition:fromNode:]](https://developer.apple.com/documentation/scenekit/scnnode/1408018-convertposition)Added [-[SCNNode convertPosition:toNode:]](https://developer.apple.com/documentation/scenekit/scnnode/1407990-convertposition)Added [-[SCNNode convertTransform:fromNode:]](https://developer.apple.com/documentation/scenekit/scnnode/1407996-converttransform)Added [-[SCNNode convertTransform:toNode:]](https://developer.apple.com/documentation/scenekit/scnnode/1407986-converttransform)Added [SCNNode.filters](https://developer.apple.com/documentation/scenekit/scnnode/1407949-filters)Added [-[SCNNode flattenedClone]](https://developer.apple.com/documentation/scenekit/scnnode/1407960-flattenedclone)Added [-[SCNNode hitTestWithSegmentFromPoint:toPoint:options:]](https://developer.apple.com/documentation/scenekit/scnnode/1407998-hittestwithsegment)Added [SCNNode.morpher](https://developer.apple.com/documentation/scenekit/scnnode/1408022-morpher)Added [SCNNode.skinner](https://developer.apple.com/documentation/scenekit/scnnode/1407953-skinner)Modified [SCNNode.childNodes](https://developer.apple.com/documentation/scenekit/scnnode/1407984-childnodes)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, copy) NSArray \*childNodes |
| To | @property(nonatomic, readonly) NSArray \*childNodes |

Modified [+[SCNNode node]](https://developer.apple.com/documentation/scenekit/scnnode/1407972-node)

|  | Declaration |
| --- | --- |
| From | + (SCNNode \*)node |
| To | + (instancetype)node |

Modified [-[SCNNode replaceChildNode:with:]](https://developer.apple.com/documentation/scenekit/scnnode/1408002-replacechildnode)

|  | Declaration |
| --- | --- |
| From | - (void)replaceChildNode:(SCNNode \*)child with:(SCNNode \*)child2 |
| To | - (void)replaceChildNode:(SCNNode \*)oldChild with:(SCNNode \*)newChild |

SCNParametricGeometry.hAdded [SCNPlane.cornerRadius](https://developer.apple.com/documentation/scenekit/scnplane/1523005-cornerradius)Added [SCNPlane.cornerSegmentCount](https://developer.apple.com/documentation/scenekit/scnplane/1524234-cornersegmentcount)Added [SCNShape](https://developer.apple.com/documentation/scenekit/scnshape)Added [SCNShape.chamferMode](https://developer.apple.com/documentation/scenekit/scnshape/1523989-chamfermode)Added [SCNShape.chamferProfile](https://developer.apple.com/documentation/scenekit/scnshape/1522865-chamferprofile)Added [SCNShape.chamferRadius](https://developer.apple.com/documentation/scenekit/scnshape/1524145-chamferradius)Added [SCNShape.extrusionDepth](https://developer.apple.com/documentation/scenekit/scnshape/1523365-extrusiondepth)Added [SCNShape.path](https://developer.apple.com/documentation/scenekit/scnshape/1523434-path)Added [+[SCNShape shapeWithPath:extrusionDepth:]](https://developer.apple.com/documentation/scenekit/scnshape/1523432-init)Added [SCNText.chamferProfile](https://developer.apple.com/documentation/scenekit/scntext/1523334-chamferprofile)Added [SCNText.flatness](https://developer.apple.com/documentation/scenekit/scntext/1524111-flatness)Added [SCNChamferMode](https://developer.apple.com/documentation/scenekit/scnchamfermode)Added [SCNChamferModeBack](https://developer.apple.com/documentation/scenekit/scnchamfermode/scnchamfermodeback)Added [SCNChamferModeBoth](https://developer.apple.com/documentation/scenekit/scnchamfermode/both)Added [SCNChamferModeFront](https://developer.apple.com/documentation/scenekit/scnchamfermode/front)Modified [+[SCNBox boxWithWidth:height:length:chamferRadius:]](https://developer.apple.com/documentation/scenekit/scnbox/1522620-boxwithwidth)

|  | Declaration |
| --- | --- |
| From | + (id)boxWithWidth:(CGFloat)width height:(CGFloat)height length:(CGFloat)length chamferRadius:(CGFloat)chamferRadius |
| To | + (instancetype)boxWithWidth:(CGFloat)width height:(CGFloat)height length:(CGFloat)length chamferRadius:(CGFloat)chamferRadius |

Modified [+[SCNCapsule capsuleWithCapRadius:height:]](https://developer.apple.com/documentation/scenekit/scncapsule/1523790-capsulewithcapradius)

|  | Declaration |
| --- | --- |
| From | + (id)capsuleWithCapRadius:(CGFloat)capRadius height:(CGFloat)height |
| To | + (instancetype)capsuleWithCapRadius:(CGFloat)capRadius height:(CGFloat)height |

Modified [+[SCNCone coneWithTopRadius:bottomRadius:height:]](https://developer.apple.com/documentation/scenekit/scncone/1522863-conewithtopradius)

|  | Declaration |
| --- | --- |
| From | + (id)coneWithTopRadius:(CGFloat)topRadius bottomRadius:(CGFloat)bottomRadius height:(CGFloat)height |
| To | + (instancetype)coneWithTopRadius:(CGFloat)topRadius bottomRadius:(CGFloat)bottomRadius height:(CGFloat)height |

Modified [+[SCNCylinder cylinderWithRadius:height:]](https://developer.apple.com/documentation/scenekit/scncylinder/1523685-init)

|  | Declaration |
| --- | --- |
| From | + (id)cylinderWithRadius:(CGFloat)radius height:(CGFloat)height |
| To | + (instancetype)cylinderWithRadius:(CGFloat)radius height:(CGFloat)height |

Modified [+[SCNFloor floor]](https://developer.apple.com/documentation/scenekit/scnfloor/1572698-floor)

|  | Declaration |
| --- | --- |
| From | + (id)floor |
| To | + (instancetype)floor |

Modified [+[SCNPlane planeWithWidth:height:]](https://developer.apple.com/documentation/scenekit/scnplane/1523631-planewithwidth)

|  | Declaration |
| --- | --- |
| From | + (id)planeWithWidth:(CGFloat)width height:(CGFloat)height |
| To | + (instancetype)planeWithWidth:(CGFloat)width height:(CGFloat)height |

Modified [+[SCNPyramid pyramidWithWidth:height:length:]](https://developer.apple.com/documentation/scenekit/scnpyramid/1523254-pyramidwithwidth)

|  | Declaration |
| --- | --- |
| From | + (id)pyramidWithWidth:(CGFloat)width height:(CGFloat)height length:(CGFloat)length |
| To | + (instancetype)pyramidWithWidth:(CGFloat)width height:(CGFloat)height length:(CGFloat)length |

Modified [+[SCNSphere sphereWithRadius:]](https://developer.apple.com/documentation/scenekit/scnsphere/1522601-init)

|  | Declaration |
| --- | --- |
| From | + (id)sphereWithRadius:(CGFloat)radius |
| To | + (instancetype)sphereWithRadius:(CGFloat)radius |

Modified [SCNText.chamferSegmentCount](https://developer.apple.com/documentation/scenekit/scntext/1572699-chamfersegmentcount)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [+[SCNText textWithString:extrusionDepth:]](https://developer.apple.com/documentation/scenekit/scntext/1522734-textwithstring)

|  | Declaration |
| --- | --- |
| From | + (id)textWithString:(id)string extrusionDepth:(CGFloat)extrusionDepth |
| To | + (instancetype)textWithString:(id)string extrusionDepth:(CGFloat)extrusionDepth |

Modified [+[SCNTorus torusWithRingRadius:pipeRadius:]](https://developer.apple.com/documentation/scenekit/scntorus/1523833-init)

|  | Declaration |
| --- | --- |
| From | + (id)torusWithRingRadius:(CGFloat)ringRadius pipeRadius:(CGFloat)pipeRadius |
| To | + (instancetype)torusWithRingRadius:(CGFloat)ringRadius pipeRadius:(CGFloat)pipeRadius |

Modified [+[SCNTube tubeWithInnerRadius:outerRadius:height:]](https://developer.apple.com/documentation/scenekit/scntube/1522843-init)

|  | Declaration |
| --- | --- |
| From | + (id)tubeWithInnerRadius:(CGFloat)innerRadius outerRadius:(CGFloat)outerRadius height:(CGFloat)height |
| To | + (instancetype)tubeWithInnerRadius:(CGFloat)innerRadius outerRadius:(CGFloat)outerRadius height:(CGFloat)height |

SCNRenderer.hModified [+[SCNRenderer rendererWithContext:options:]](https://developer.apple.com/documentation/scenekit/scnrenderer/1518408-init)

|  | Declaration |
| --- | --- |
| From | + (SCNRenderer \*)rendererWithContext:(void \*)context options:(NSDictionary \*)options |
| To | + (instancetype)rendererWithContext:(void \*)context options:(NSDictionary \*)options |

SCNScene.hAdded [SCNScene.background](https://developer.apple.com/documentation/scenekit/scnscene/1523665-background)Added [+[SCNScene sceneNamed:]](https://developer.apple.com/documentation/scenekit/scnscene/1523355-init)Added [-[SCNScene writeToURL:options:delegate:progressHandler:]](https://developer.apple.com/documentation/scenekit/scnscene/1523577-write)Added [SCNSceneExportDelegate](https://developer.apple.com/documentation/scenekit/scnsceneexportdelegate)Added [-[SCNSceneExportDelegate writeImage:withSceneDocumentURL:originalImageURL:]](https://developer.apple.com/documentation/scenekit/scnsceneexportdelegate/1524221-write)Added [SCNSceneExportDestinationURL](https://developer.apple.com/documentation/scenekit/scnsceneexportdestinationurl)Added [SCNSceneExportProgressHandler](https://developer.apple.com/documentation/scenekit/scnsceneexportprogresshandler)Modified [+[SCNScene scene]](https://developer.apple.com/documentation/scenekit/scnscene/1574179-scene)

|  | Declaration |
| --- | --- |
| From | + (SCNScene \*)scene |
| To | + (instancetype)scene |

Modified [+[SCNScene sceneWithURL:options:error:]](https://developer.apple.com/documentation/scenekit/scnscene/1522660-scenewithurl)

|  | Declaration |
| --- | --- |
| From | + (SCNScene \*)sceneWithURL:(NSURL \*)url options:(NSDictionary \*)options error:(NSError \*\*)error |
| To | + (instancetype)sceneWithURL:(NSURL \*)url options:(NSDictionary \*)options error:(NSError \*\*)error |

SCNSceneRenderer.hAdded [-[SCNSceneRenderer isNodeInsideFrustum:withPointOfView:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522647-isnode)Added [-[SCNSceneRenderer prepareObject:shouldAbortBlock:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522798-prepareobject)Added [-[SCNSceneRenderer projectPoint:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1524089-projectpoint)Added [SCNSceneRenderer.showsStatistics](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522763-showsstatistics)Added [-[SCNSceneRenderer unprojectPoint:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522631-unprojectpoint)Added [SCNHitTestIgnoreHiddenNodesKey](https://developer.apple.com/documentation/scenekit/scnhittestignorehiddennodeskey)SCNSceneSource.hAdded [-[SCNSceneSource entriesPassingTest:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523055-entries)Modified [+[SCNSceneSource sceneSourceWithData:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1573764-scenesourcewithdata)

|  | Declaration |
| --- | --- |
| From | + (id)sceneSourceWithData:(NSData \*)data options:(NSDictionary \*)options |
| To | + (instancetype)sceneSourceWithData:(NSData \*)data options:(NSDictionary \*)options |

Modified [+[SCNSceneSource sceneSourceWithURL:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1573763-scenesourcewithurl)

|  | Declaration |
| --- | --- |
| From | + (id)sceneSourceWithURL:(NSURL \*)url options:(NSDictionary \*)options |
| To | + (instancetype)sceneSourceWithURL:(NSURL \*)url options:(NSDictionary \*)options |

SCNShadable.hAdded [SCNShadable](https://developer.apple.com/documentation/scenekit/scnshadable)Added [-[SCNShadable handleBindingOfSymbol:usingBlock:]](https://developer.apple.com/documentation/scenekit/scnshadable/1523063-handlebindingofsymbol)Added [-[SCNShadable handleUnbindingOfSymbol:usingBlock:]](https://developer.apple.com/documentation/scenekit/scnshadable/1522783-handleunbinding)Added [SCNShadable.program](https://developer.apple.com/documentation/scenekit/scnshadable/1523689-program)Added [SCNShadable.shaderModifiers](https://developer.apple.com/documentation/scenekit/scnshadable/1523348-shadermodifiers)Added [SCNBindingBlock](https://developer.apple.com/documentation/scenekit/scnbindingblock)Added [SCNShaderModifierEntryPointFragment](https://developer.apple.com/documentation/scenekit/scnshadermodifierentrypointfragment)Added [SCNShaderModifierEntryPointGeometry](https://developer.apple.com/documentation/scenekit/scnshadermodifierentrypointgeometry)Added [SCNShaderModifierEntryPointLightingModel](https://developer.apple.com/documentation/scenekit/scnshadermodifierentrypointlightingmodel)Added [SCNShaderModifierEntryPointSurface](https://developer.apple.com/documentation/scenekit/scnshadermodifierentrypoint/1523791-surface)Modified [SCNProgram](https://developer.apple.com/documentation/scenekit/scnprogram)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [SCNProgram.delegate](https://developer.apple.com/documentation/scenekit/scnprogram/1522611-delegate)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [SCNProgram.fragmentShader](https://developer.apple.com/documentation/scenekit/scnprogram/1523135-fragmentshader)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [+[SCNProgram program]](https://developer.apple.com/documentation/scenekit/scnprogram/1565076-program)

|  | Header | Declaration |
| --- | --- | --- |
| From | SceneKit/SCNMaterial.h | + (SCNProgram \*)program |
| To | SceneKit/SCNShadable.h | + (instancetype)program |

Modified [-[SCNProgram semanticForSymbol:]](https://developer.apple.com/documentation/scenekit/scnprogram/1523350-semantic)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [-[SCNProgram setSemantic:forSymbol:options:]](https://developer.apple.com/documentation/scenekit/scnprogram/1522730-setsemantic)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [SCNProgram.vertexShader](https://developer.apple.com/documentation/scenekit/scnprogram/1522891-vertexshader)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [SCNProgramDelegate](https://developer.apple.com/documentation/scenekit/scnprogramdelegate)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [-[SCNProgramDelegate program:bindValueForSymbol:atLocation:programID:renderer:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1524155-program)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [-[SCNProgramDelegate program:handleError:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1523007-program)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [-[SCNProgramDelegate program:unbindValueForSymbol:atLocation:programID:renderer:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1523857-program)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

Modified [-[SCNProgramDelegate programIsOpaque:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1523068-programisopaque)

|  | Header |
| --- | --- |
| From | SceneKit/SCNMaterial.h |
| To | SceneKit/SCNShadable.h |

SCNSkinner.hAdded [SCNSkinner](https://developer.apple.com/documentation/scenekit/scnskinner)Added [SCNSkinner.skeleton](https://developer.apple.com/documentation/scenekit/scnskinner/1523048-skeleton)SceneKitTypes.hAdded #def GLKMatrix4FromCATransform3DAdded #def GLKMatrix4ToCATransform3DAdded [SCNVector3FromGLKVector3()](https://developer.apple.com/documentation/scenekit/1409692-scnvector3fromglkvector3)Added [SCNVector3ToGLKVector3()](https://developer.apple.com/documentation/scenekit/1409651-scnvector3toglkvector3)Added [SCNVector4FromGLKVector4()](https://developer.apple.com/documentation/scenekit/1409729-scnvector4fromglkvector4)Added [SCNVector4ToGLKVector4()](https://developer.apple.com/documentation/scenekit/1409663-scnvector4toglkvector4)

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
