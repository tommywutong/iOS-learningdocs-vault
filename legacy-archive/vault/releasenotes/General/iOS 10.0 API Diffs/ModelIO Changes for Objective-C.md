---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/ModelIO.html
archived_at: '2026-07-18T02:54:57.650391Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# ModelIO Changes for Objective-C

### ModelIO

#### MDLAsset.h

Added [-[MDLAsset childObjectsOfClass:]](https://developer.apple.com/documentation/modelio/mdlasset/1644589-childobjects)Added [-[MDLAsset initWithBufferAllocator:]](https://developer.apple.com/documentation/modelio/mdlasset/1644590-initwithbufferallocator)Added [MDLAsset.masters](https://developer.apple.com/documentation/modelio/mdlasset/2097126-masters)Added [+[MDLAsset placeLightProbesWithDensity:heuristic:usingIrradianceDataSource:]](https://developer.apple.com/documentation/modelio/mdlasset/1644588-placelightprobes)Added [MDLLightProbeIrradianceDataSource](https://developer.apple.com/documentation/modelio/mdllightprobeirradiancedatasource)Added [MDLLightProbeIrradianceDataSource.boundingBox](https://developer.apple.com/documentation/modelio/mdllightprobeirradiancedatasource/1644585-boundingbox)Added [-[MDLLightProbeIrradianceDataSource sphericalHarmonicsCoefficientsAtPosition:]](https://developer.apple.com/documentation/modelio/mdllightprobeirradiancedatasource/1644584-sphericalharmonicscoefficientsat)Added [MDLLightProbeIrradianceDataSource.sphericalHarmonicsLevel](https://developer.apple.com/documentation/modelio/mdllightprobeirradiancedatasource/1644586-sphericalharmonicslevel)Added MDLAsset(MDLLightBaking)

#### MDLCamera.h

Added [MDLCamera.projection](https://developer.apple.com/documentation/modelio/mdlcamera/1645841-projection)Added [MDLCameraProjection](https://developer.apple.com/documentation/modelio/mdlcameraprojection)Added [MDLCameraProjectionOrthographic](https://developer.apple.com/documentation/modelio/mdlcameraprojection/mdlcameraprojectionorthographic)Added [MDLCameraProjectionPerspective](https://developer.apple.com/documentation/modelio/mdlcameraprojection/mdlcameraprojectionperspective)

#### MDLLight.h

Added [MDLLight.colorSpace](https://developer.apple.com/documentation/modelio/mdllight/1823498-colorspace)

#### MDLMaterial.h

Added [MDLMaterial.materialFace](https://developer.apple.com/documentation/modelio/mdlmaterial/1642036-materialface)Added [MDLMaterialProperty.luminance](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/1642051-luminance)Added [MDLMaterialPropertyConnection](https://developer.apple.com/documentation/modelio/mdlmaterialpropertyconnection)Added [-[MDLMaterialPropertyConnection initWithOutput:input:]](https://developer.apple.com/documentation/modelio/mdlmaterialpropertyconnection/1642034-init)Added [MDLMaterialPropertyConnection.input](https://developer.apple.com/documentation/modelio/mdlmaterialpropertyconnection/1642037-input)Added [MDLMaterialPropertyConnection.output](https://developer.apple.com/documentation/modelio/mdlmaterialpropertyconnection/1642041-output)Added [MDLMaterialPropertyGraph](https://developer.apple.com/documentation/modelio/mdlmaterialpropertygraph)Added [MDLMaterialPropertyGraph.connections](https://developer.apple.com/documentation/modelio/mdlmaterialpropertygraph/1642040-connections)Added [-[MDLMaterialPropertyGraph evaluate]](https://developer.apple.com/documentation/modelio/mdlmaterialpropertygraph/1642044-evaluate)Added [-[MDLMaterialPropertyGraph initWithNodes:connections:]](https://developer.apple.com/documentation/modelio/mdlmaterialpropertygraph/1642048-init)Added [MDLMaterialPropertyGraph.nodes](https://developer.apple.com/documentation/modelio/mdlmaterialpropertygraph/1642043-nodes)Added [MDLMaterialPropertyNode](https://developer.apple.com/documentation/modelio/mdlmaterialpropertynode)Added [MDLMaterialPropertyNode.evaluationFunction](https://developer.apple.com/documentation/modelio/mdlmaterialpropertynode/1642039-evaluationfunction)Added [-[MDLMaterialPropertyNode initWithInputs:outputs:evaluationFunction:]](https://developer.apple.com/documentation/modelio/mdlmaterialpropertynode/1642053-init)Added [MDLMaterialPropertyNode.inputs](https://developer.apple.com/documentation/modelio/mdlmaterialpropertynode/1642052-inputs)Added [MDLMaterialPropertyNode.outputs](https://developer.apple.com/documentation/modelio/mdlmaterialpropertynode/1642049-outputs)Added [MDLMaterialFace](https://developer.apple.com/documentation/modelio/mdlmaterialface)Added [MDLMaterialFaceBack](https://developer.apple.com/documentation/modelio/mdlmaterialface/mdlmaterialfaceback)Added [MDLMaterialFaceDoubleSided](https://developer.apple.com/documentation/modelio/mdlmaterialface/doublesided)Added [MDLMaterialFaceFront](https://developer.apple.com/documentation/modelio/mdlmaterialface/mdlmaterialfacefront)Modified [MDLMaterialProperty](https://developer.apple.com/documentation/modelio/mdlmaterialproperty)

|  | Protocols |
| --- | --- |
| From | MDLNamed |
| To | MDLNamed, NSCopying |

#### MDLMesh.h

Added [-[MDLMesh addAttributeWithName:format:type:data:stride:]](https://developer.apple.com/documentation/modelio/mdlmesh/1823499-addattributewithname)Added [-[MDLMesh addAttributeWithName:format:type:data:stride:time:]](https://developer.apple.com/documentation/modelio/mdlmesh/2097115-addattribute)Added [-[MDLMesh addUnwrappedTextureCoordinatesForAttributeNamed:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644690-addunwrappedtexturecoordinatesfo)Added [MDLMesh.allocator](https://developer.apple.com/documentation/modelio/mdlmesh/1778158-allocator)Added [-[MDLMesh initBoxWithExtent:segments:inwardNormals:geometryType:allocator:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644689-init)Added [-[MDLMesh initCapsuleWithExtent:cylinderSegments:hemisphereSegments:inwardNormals:geometryType:allocator:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644680-initcapsulewithextent)Added [-[MDLMesh initConeWithExtent:segments:inwardNormals:cap:geometryType:allocator:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644688-init)Added [-[MDLMesh initCylinderWithExtent:segments:inwardNormals:topCap:bottomCap:geometryType:allocator:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644686-initcylinderwithextent)Added [-[MDLMesh initHemisphereWithExtent:segments:inwardNormals:cap:geometryType:allocator:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644685-init)Added [-[MDLMesh initIcosahedronWithExtent:inwardNormals:geometryType:allocator:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644682-init)Added [-[MDLMesh initMeshBySubdividingMesh:submeshIndex:subdivisionLevels:allocator:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644678-initmeshbysubdividingmesh)Added [-[MDLMesh initPlaneWithExtent:segments:geometryType:allocator:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644677-init)Added [-[MDLMesh initSphereWithExtent:segments:inwardNormals:geometryType:allocator:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644681-init)Added [-[MDLMesh initWithBufferAllocator:]](https://developer.apple.com/documentation/modelio/mdlmesh/1778157-init)Added [-[MDLMesh removeAttributeNamed:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644684-removeattributenamed)Added [-[MDLMesh replaceAttributeNamed:withData:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644679-replaceattributenamed)Added [-[MDLMesh updateAttributeNamed:withData:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644683-updateattributenamed)Added [-[MDLMesh vertexAttributeDataForAttributeNamed:asFormat:]](https://developer.apple.com/documentation/modelio/mdlmesh/1644687-vertexattributedata)Modified [-[MDLMesh addTangentBasisForTextureCoordinateAttributeNamed:normalAttributeNamed:tangentAttributeNamed:]](https://developer.apple.com/documentation/modelio/mdlmesh/1391237-addtangentbasis)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addTangentBasisForTextureCoordinateAttributeNamed:(NSString *)textureCoordinateAttributeName normalAttributeNamed:(NSString *)normalAttributeName tangentAttributeNamed:(NSString *)tangentAttributeName ``` |
| To | ``` - (void)addTangentBasisForTextureCoordinateAttributeNamed:(NSString *)textureCoordinateAttributeName normalAttributeNamed:(NSString *)normalAttributeNamed tangentAttributeNamed:(NSString *)tangentAttributeNamed ``` |

Modified [-[MDLMesh addTangentBasisForTextureCoordinateAttributeNamed:tangentAttributeNamed:bitangentAttributeNamed:]](https://developer.apple.com/documentation/modelio/mdlmesh/1391942-addtangentbasis)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addTangentBasisForTextureCoordinateAttributeNamed:(NSString *)textureCoordinateAttributeName tangentAttributeNamed:(NSString *)tangentAttributeName bitangentAttributeNamed:(NSString *)bitangentAttributeName ``` |
| To | ``` - (void)addTangentBasisForTextureCoordinateAttributeNamed:(NSString *)textureCoordinateAttributeName tangentAttributeNamed:(NSString *)tangentAttributeNamed bitangentAttributeNamed:(NSString *)bitangentAttributeName ``` |

Modified [MDLMesh.submeshes](https://developer.apple.com/documentation/modelio/mdlmesh/1390937-submeshes)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSMutableArray<MDLSubmesh *> *submeshes ``` | yes |
| To | ``` @property(nonatomic, copy) NSMutableArray<MDLSubmesh *> *submeshes ``` | -- |

Modified [MDLMesh.vertexCount](https://developer.apple.com/documentation/modelio/mdlmesh/1391411-vertexcount)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` @property(nonatomic, readonly) NSUInteger vertexCount ``` | yes |
| To | ``` @property(nonatomic, readwrite) NSUInteger vertexCount ``` | -- |

#### MDLObject.h

Added [MDLObject.hidden](https://developer.apple.com/documentation/modelio/mdlobject/2143069-hidden)Added [MDLObject.instance](https://developer.apple.com/documentation/modelio/mdlobject/2097123-instance)Added [-[MDLObject objectAtPath:]](https://developer.apple.com/documentation/modelio/mdlobject/2097124-atpath)Added [MDLObject.path](https://developer.apple.com/documentation/modelio/mdlobject/1642272-path)

#### MDLSubmesh.h

Added [-[MDLSubmesh indexBufferAsIndexType:]](https://developer.apple.com/documentation/modelio/mdlsubmesh/1644031-indexbuffer)

#### MDLTexture.h

Added [MDLTexture.hasAlphaValues](https://developer.apple.com/documentation/modelio/mdltexture/1644783-hasalphavalues)Added [-[MDLTexture init]](https://developer.apple.com/documentation/modelio/mdltexture/1644782-init)

#### MDLTransform.h

Added [-[MDLTransform initWithMatrix:resetsTransform:]](https://developer.apple.com/documentation/modelio/mdltransform/1643554-init)Added [-[MDLTransform initWithTransformComponent:resetsTransform:]](https://developer.apple.com/documentation/modelio/mdltransform/1643552-initwithtransformcomponent)Added [MDLTransformComponent.keyTimes](https://developer.apple.com/documentation/modelio/mdltransformcomponent/1823488-keytimes)Added [MDLTransformComponent.resetsTransform](https://developer.apple.com/documentation/modelio/mdltransformcomponent/1643553-resetstransform)Modified [MDLTransform](https://developer.apple.com/documentation/modelio/mdltransform)

|  | Protocols |
| --- | --- |
| From | MDLTransformComponent |
| To | MDLTransformComponent, NSCopying |

#### MDLTypes.h

Removed MDLGeometryKindLinesRemoved MDLGeometryKindPointsRemoved MDLGeometryKindQuadsRemoved MDLGeometryKindTrianglesRemoved MDLGeometryKindTriangleStripsAdded [kUTTypeUniversalSceneDescription](https://developer.apple.com/documentation/modelio/kuttypeuniversalscenedescription)Added [MDLProbePlacement](https://developer.apple.com/documentation/modelio/mdlprobeplacement)Added [MDLProbePlacementIrradianceDistribution](https://developer.apple.com/documentation/modelio/mdlprobeplacement/mdlprobeplacementirradiancedistribution)Added [MDLProbePlacementUniformGrid](https://developer.apple.com/documentation/modelio/mdlprobeplacement/uniformgrid)

#### MDLVertexDescriptor.h

Added [MDLVertexAttribute.time](https://developer.apple.com/documentation/modelio/mdlvertexattribute/2097127-time)Added [-[MDLVertexBufferLayout initWithStride:]](https://developer.apple.com/documentation/modelio/mdlvertexbufferlayout/2097125-init)Added [-[MDLVertexDescriptor removeAttributeNamed:]](https://developer.apple.com/documentation/modelio/mdlvertexdescriptor/1645007-removeattributenamed)

#### MDLVoxelArray.h

Removed [-[MDLVoxelArray initWithAsset:divisions:interiorNBWidth:exteriorNBWidth:patchRadius:]](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391981-init)Removed [-[MDLVoxelArray initWithAsset:divisions:interiorShells:exteriorShells:patchRadius:]](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391256-initwithasset)Removed [-[MDLVoxelArray setVoxelsForMesh:divisions:interiorNBWidth:exteriorNBWidth:patchRadius:]](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391241-setvoxelsfor)Removed [-[MDLVoxelArray setVoxelsForMesh:divisions:interiorShells:exteriorShells:patchRadius:]](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1392017-setvoxelsfor)Added [-[MDLVoxelArray coarseMesh]](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640656-coarsemesh)Added [-[MDLVoxelArray coarseMeshUsingAllocator:]](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1823497-coarsemeshusingallocator)Added [-[MDLVoxelArray convertToSignedShellField]](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640668-converttosignedshellfield)Added [-[MDLVoxelArray initWithAsset:divisions:patchRadius:]](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640657-initwithasset)Added [MDLVoxelArray.isValidSignedShellField](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640661-isvalidsignedshellfield)Added [-[MDLVoxelArray setVoxelsForMesh:divisions:patchRadius:]](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640666-setvoxelsformesh)Added [MDLVoxelArray.shellFieldExteriorThickness](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640670-shellfieldexteriorthickness)Added [MDLVoxelArray.shellFieldInteriorThickness](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640664-shellfieldinteriorthickness)Modified [MDLVoxelArray](https://developer.apple.com/documentation/modelio/mdlvoxelarray)

|  | Superclasses |
| --- | --- |
| From | NSObject |
| To | MDLObject |

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
