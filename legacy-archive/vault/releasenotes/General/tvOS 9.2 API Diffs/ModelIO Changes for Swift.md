---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Swift/ModelIO.html
archived_at: '2026-07-18T02:58:06.364808Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# ModelIO Changes for Swift

### ModelIO

Removed MDLMeshBuffer.zone() -> MDLMeshBufferZoneModified [MDLAsset](https://developer.apple.com/documentation/modelio/mdlasset)

|  | Declaration |
| --- | --- |
| From | ``` class MDLAsset : NSObject, NSCopying, NSFastEnumeration {     init(URL URL: NSURL)     init(URL URL: NSURL, vertexDescriptor vertexDescriptor: MDLVertexDescriptor?, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?)     init(URL URL: NSURL, vertexDescriptor vertexDescriptor: MDLVertexDescriptor?, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?, preserveTopology preserveTopology: Bool, error error: NSErrorPointer)     func exportAssetToURL(_ URL: NSURL) -> Bool     func exportAssetToURL(_ URL: NSURL, error error: ()) throws     class func canImportFileExtension(_ `extension`: String) -> Bool     class func canExportFileExtension(_ `extension`: String) -> Bool     func boundingBoxAtTime(_ time: NSTimeInterval) -> MDLAxisAlignedBoundingBox     var boundingBox: MDLAxisAlignedBoundingBox { get }     var frameInterval: NSTimeInterval     var startTime: NSTimeInterval     var endTime: NSTimeInterval     var URL: NSURL? { get }     var bufferAllocator: MDLMeshBufferAllocator { get }     var vertexDescriptor: MDLVertexDescriptor? { get }     func addObject(_ object: MDLObject)     func removeObject(_ object: MDLObject)     var count: Int { get }     subscript (_ index: Int) -> MDLObject? { get }     func objectAtIndexedSubscript(_ index: Int) -> MDLObject?     func objectAtIndex(_ index: Int) -> MDLObject } ``` |
| To | ``` class MDLAsset : NSObject, NSCopying, NSFastEnumeration {     init(URL URL: NSURL)     init(URL URL: NSURL, vertexDescriptor vertexDescriptor: MDLVertexDescriptor?, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?)     init(URL URL: NSURL, vertexDescriptor vertexDescriptor: MDLVertexDescriptor?, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?, preserveTopology preserveTopology: Bool, error error: NSErrorPointer)     func exportAssetToURL(_ URL: NSURL) -> Bool     func exportAssetToURL(_ URL: NSURL, error error: ()) throws     class func canImportFileExtension(_ extension: String) -> Bool     class func canExportFileExtension(_ extension: String) -> Bool     func boundingBoxAtTime(_ time: NSTimeInterval) -> MDLAxisAlignedBoundingBox     var boundingBox: MDLAxisAlignedBoundingBox { get }     var frameInterval: NSTimeInterval     var startTime: NSTimeInterval     var endTime: NSTimeInterval     var URL: NSURL? { get }     var bufferAllocator: MDLMeshBufferAllocator { get }     var vertexDescriptor: MDLVertexDescriptor? { get }     func addObject(_ object: MDLObject)     func removeObject(_ object: MDLObject)     var count: Int { get }     subscript (_ index: Int) -> MDLObject? { get }     func objectAtIndexedSubscript(_ index: Int) -> MDLObject?     func objectAtIndex(_ index: Int) -> MDLObject } extension MDLAsset {     convenience init(SCNScene scnScene: SCNScene)     class func assetWithSCNScene(_ scnScene: SCNScene) -> Self } ``` |

Modified [MDLAsset.canExportFileExtension(_: String) -> Bool [class]](https://developer.apple.com/documentation/modelio/mdlasset/1391708-canexportfileextension)

|  | Declaration |
| --- | --- |
| From | ``` class func canExportFileExtension(_ `extension`: String) -> Bool ``` |
| To | ``` class func canExportFileExtension(_ extension: String) -> Bool ``` |

Modified [MDLAsset.canImportFileExtension(_: String) -> Bool [class]](https://developer.apple.com/documentation/modelio/mdlasset/1391813-canimportfileextension)

|  | Declaration |
| --- | --- |
| From | ``` class func canImportFileExtension(_ `extension`: String) -> Bool ``` |
| To | ``` class func canImportFileExtension(_ extension: String) -> Bool ``` |

Modified [MDLCamera](https://developer.apple.com/documentation/modelio/mdlcamera)

|  | Declaration |
| --- | --- |
| From | ``` class MDLCamera : MDLObject {     var projectionMatrix: matrix_float4x4 { get }     func frameBoundingBox(_ boundingBox: MDLAxisAlignedBoundingBox, setNearAndFar setNearAndFar: Bool)     func lookAt(_ focusPosition: vector_float3)     func lookAt(_ focusPosition: vector_float3, from cameraPosition: vector_float3)     func rayTo(_ pixel: vector_int2, forViewPort size: vector_int2) -> vector_float3     var nearVisibilityDistance: Float     var farVisibilityDistance: Float     var worldToMetersConversionScale: Float     var barrelDistortion: Float     var fisheyeDistortion: Float     var opticalVignetting: Float     var chromaticAberration: Float     var focalLength: Float     var focusDistance: Float     var fieldOfView: Float     var fStop: Float     var apertureBladeCount: Int     var maximumCircleOfConfusion: Float     func bokehKernelWithSize(_ size: vector_int2) -> MDLTexture     var shutterOpenInterval: NSTimeInterval     var sensorVerticalAperture: Float     var sensorAspect: Float     var sensorEnlargement: vector_float2     var sensorShift: vector_float2     var flash: vector_float3     var exposureCompression: vector_float2     var exposure: vector_float3 } ``` |
| To | ``` class MDLCamera : MDLObject {     var projectionMatrix: matrix_float4x4 { get }     func frameBoundingBox(_ boundingBox: MDLAxisAlignedBoundingBox, setNearAndFar setNearAndFar: Bool)     func lookAt(_ focusPosition: vector_float3)     func lookAt(_ focusPosition: vector_float3, from cameraPosition: vector_float3)     func rayTo(_ pixel: vector_int2, forViewPort size: vector_int2) -> vector_float3     var nearVisibilityDistance: Float     var farVisibilityDistance: Float     var worldToMetersConversionScale: Float     var barrelDistortion: Float     var fisheyeDistortion: Float     var opticalVignetting: Float     var chromaticAberration: Float     var focalLength: Float     var focusDistance: Float     var fieldOfView: Float     var fStop: Float     var apertureBladeCount: Int     var maximumCircleOfConfusion: Float     func bokehKernelWithSize(_ size: vector_int2) -> MDLTexture     var shutterOpenInterval: NSTimeInterval     var sensorVerticalAperture: Float     var sensorAspect: Float     var sensorEnlargement: vector_float2     var sensorShift: vector_float2     var flash: vector_float3     var exposureCompression: vector_float2     var exposure: vector_float3 } extension MDLCamera {     convenience init(SCNCamera scnCamera: SCNCamera)     class func cameraWithSCNCamera(_ scnCamera: SCNCamera) -> Self } ``` |

Modified [MDLLight](https://developer.apple.com/documentation/modelio/mdllight)

|  | Declaration |
| --- | --- |
| From | ``` class MDLLight : MDLObject {     func irradianceAtPoint(_ point: vector_float3) -> Unmanaged<CGColor>     func irradianceAtPoint(_ point: vector_float3, colorSpace colorSpace: CGColorSpace) -> Unmanaged<CGColor>     var lightType: MDLLightType } ``` |
| To | ``` class MDLLight : MDLObject {     func irradianceAtPoint(_ point: vector_float3) -> Unmanaged<CGColor>     func irradianceAtPoint(_ point: vector_float3, colorSpace colorSpace: CGColorSpace) -> Unmanaged<CGColor>     var lightType: MDLLightType } extension MDLLight {     convenience init(SCNLight scnLight: SCNLight)     class func lightWithSCNLight(_ scnLight: SCNLight) -> Self } ``` |

Modified [MDLMaterial](https://developer.apple.com/documentation/modelio/mdlmaterial)

|  | Declaration |
| --- | --- |
| From | ``` class MDLMaterial : NSObject, MDLNamed, NSFastEnumeration {     init(name name: String, scatteringFunction scatteringFunction: MDLScatteringFunction)     func setProperty(_ property: MDLMaterialProperty)     func removeProperty(_ property: MDLMaterialProperty)     func propertyNamed(_ name: String) -> MDLMaterialProperty?     func propertyWithSemantic(_ semantic: MDLMaterialSemantic) -> MDLMaterialProperty?     func removeAllProperties()     var scatteringFunction: MDLScatteringFunction { get }     var name: String     var baseMaterial: MDLMaterial?     subscript (_ idx: Int) -> MDLMaterialProperty? { get }     func objectAtIndexedSubscript(_ idx: Int) -> MDLMaterialProperty?     subscript (_ name: String) -> MDLMaterialProperty? { get }     func objectForKeyedSubscript(_ name: String) -> MDLMaterialProperty?     var count: Int { get } } ``` |
| To | ``` class MDLMaterial : NSObject, MDLNamed, NSFastEnumeration {     init(name name: String, scatteringFunction scatteringFunction: MDLScatteringFunction)     func setProperty(_ property: MDLMaterialProperty)     func removeProperty(_ property: MDLMaterialProperty)     func propertyNamed(_ name: String) -> MDLMaterialProperty?     func propertyWithSemantic(_ semantic: MDLMaterialSemantic) -> MDLMaterialProperty?     func removeAllProperties()     var scatteringFunction: MDLScatteringFunction { get }     var name: String     var baseMaterial: MDLMaterial?     subscript (_ idx: Int) -> MDLMaterialProperty? { get }     func objectAtIndexedSubscript(_ idx: Int) -> MDLMaterialProperty?     subscript (_ name: String) -> MDLMaterialProperty? { get }     func objectForKeyedSubscript(_ name: String) -> MDLMaterialProperty?     var count: Int { get } } extension MDLMaterial {     convenience init(SCNMaterial scnMaterial: SCNMaterial)     class func materialWithSCNMaterial(_ scnMaterial: SCNMaterial) -> Self } ``` |

Modified [MDLMesh](https://developer.apple.com/documentation/modelio/mdlmesh)

|  | Declaration |
| --- | --- |
| From | ``` class MDLMesh : MDLObject {     init(vertexBuffer vertexBuffer: MDLMeshBuffer, vertexCount vertexCount: Int, descriptor descriptor: MDLVertexDescriptor, submeshes submeshes: [MDLSubmesh])     init(vertexBuffers vertexBuffers: [MDLMeshBuffer], vertexCount vertexCount: Int, descriptor descriptor: MDLVertexDescriptor, submeshes submeshes: [MDLSubmesh])     func vertexAttributeDataForAttributeNamed(_ name: String) -> MDLVertexAttributeData?     var boundingBox: MDLAxisAlignedBoundingBox { get }     @NSCopying var vertexDescriptor: MDLVertexDescriptor     var vertexCount: Int { get }     var vertexBuffers: [MDLMeshBuffer] { get }     var submeshes: NSMutableArray { get } } extension MDLMesh {     func addAttributeWithName(_ name: String, format format: MDLVertexFormat)     func addNormalsWithAttributeNamed(_ attributeName: String?, creaseThreshold creaseThreshold: Float)     func addTangentBasisForTextureCoordinateAttributeNamed(_ textureCoordinateAttributeName: String, tangentAttributeNamed tangentAttributeName: String, bitangentAttributeNamed bitangentAttributeName: String?)     func addTangentBasisForTextureCoordinateAttributeNamed(_ textureCoordinateAttributeName: String, normalAttributeNamed normalAttributeName: String, tangentAttributeNamed tangentAttributeName: String)     func makeVerticesUnique() } extension MDLMesh {     class func newEllipsoidWithRadii(_ radii: vector_float3, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, hemisphere hemisphere: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newCylinderWithHeight(_ height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newEllipticalConeWithHeight(_ height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newIcosahedronWithRadius(_ radius: Float, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newSubdividedMesh(_ mesh: MDLMesh, submeshIndex submeshIndex: Int, subdivisionLevels subdivisionLevels: Int) -> Self? } extension MDLMesh {     func generateAmbientOcclusionTextureWithSize(_ textureSize: vector_int2, raysPerSample raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateAmbientOcclusionTextureWithQuality(_ bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateAmbientOcclusionVertexColorsWithRaysPerSample(_ raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool     func generateAmbientOcclusionVertexColorsWithQuality(_ bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool     func generateLightMapTextureWithTextureSize(_ textureSize: vector_int2, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateLightMapTextureWithQuality(_ bakeQuality: Float, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateLightMapVertexColorsWithLightsToConsider(_ lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool } ``` |
| To | ``` class MDLMesh : MDLObject {     init(vertexBuffer vertexBuffer: MDLMeshBuffer, vertexCount vertexCount: Int, descriptor descriptor: MDLVertexDescriptor, submeshes submeshes: [MDLSubmesh])     init(vertexBuffers vertexBuffers: [MDLMeshBuffer], vertexCount vertexCount: Int, descriptor descriptor: MDLVertexDescriptor, submeshes submeshes: [MDLSubmesh])     func vertexAttributeDataForAttributeNamed(_ name: String) -> MDLVertexAttributeData?     var boundingBox: MDLAxisAlignedBoundingBox { get }     @NSCopying var vertexDescriptor: MDLVertexDescriptor     var vertexCount: Int { get }     var vertexBuffers: [MDLMeshBuffer] { get }     var submeshes: NSMutableArray { get } } extension MDLMesh {     func addAttributeWithName(_ name: String, format format: MDLVertexFormat)     func addNormalsWithAttributeNamed(_ attributeName: String?, creaseThreshold creaseThreshold: Float)     func addTangentBasisForTextureCoordinateAttributeNamed(_ textureCoordinateAttributeName: String, tangentAttributeNamed tangentAttributeName: String, bitangentAttributeNamed bitangentAttributeName: String?)     func addTangentBasisForTextureCoordinateAttributeNamed(_ textureCoordinateAttributeName: String, normalAttributeNamed normalAttributeName: String, tangentAttributeNamed tangentAttributeName: String)     func makeVerticesUnique() } extension MDLMesh {     class func newEllipsoidWithRadii(_ radii: vector_float3, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, hemisphere hemisphere: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newCylinderWithHeight(_ height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newEllipticalConeWithHeight(_ height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newIcosahedronWithRadius(_ radius: Float, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newSubdividedMesh(_ mesh: MDLMesh, submeshIndex submeshIndex: Int, subdivisionLevels subdivisionLevels: Int) -> Self? } extension MDLMesh {     func generateAmbientOcclusionTextureWithSize(_ textureSize: vector_int2, raysPerSample raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateAmbientOcclusionTextureWithQuality(_ bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateAmbientOcclusionVertexColorsWithRaysPerSample(_ raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool     func generateAmbientOcclusionVertexColorsWithQuality(_ bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool     func generateLightMapTextureWithTextureSize(_ textureSize: vector_int2, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateLightMapTextureWithQuality(_ bakeQuality: Float, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateLightMapVertexColorsWithLightsToConsider(_ lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool } extension MDLMesh {     convenience init(SCNGeometry scnGeometry: SCNGeometry)     class func meshWithSCNGeometry(_ scnGeometry: SCNGeometry) -> Self } ``` |

Modified [MDLMeshBuffer](https://developer.apple.com/documentation/modelio/mdlmeshbuffer)

|  | Declaration |
| --- | --- |
| From | ``` protocol MDLMeshBuffer : NSObjectProtocol, NSCopying {     func fillData(_ data: NSData, offset offset: Int)     func map() -> MDLMeshBufferMap     var length: Int { get }     var allocator: MDLMeshBufferAllocator { get }     var type: MDLMeshBufferType { get }     func zone() -> MDLMeshBufferZone } ``` |
| To | ``` protocol MDLMeshBuffer : NSObjectProtocol, NSCopying {     func fillData(_ data: NSData, offset offset: Int)     func map() -> MDLMeshBufferMap     var length: Int { get }     var allocator: MDLMeshBufferAllocator { get }     var type: MDLMeshBufferType { get } } ``` |

Modified [MDLObject](https://developer.apple.com/documentation/modelio/mdlobject)

|  | Declaration |
| --- | --- |
| From | ``` class MDLObject : NSObject, MDLNamed {     func setComponent(_ component: MDLComponent, forProtocol `protocol`: Protocol)     func componentConformingToProtocol(_ `protocol`: Protocol) -> MDLComponent?     weak var parent: MDLObject?     var transform: MDLTransformComponent?     var children: MDLObjectContainerComponent     func addChild(_ child: MDLObject)     func boundingBoxAtTime(_ time: NSTimeInterval) -> MDLAxisAlignedBoundingBox } ``` |
| To | ``` class MDLObject : NSObject, MDLNamed {     func setComponent(_ component: MDLComponent, forProtocol protocol: Protocol)     func componentConformingToProtocol(_ protocol: Protocol) -> MDLComponent?     weak var parent: MDLObject?     var transform: MDLTransformComponent?     var children: MDLObjectContainerComponent     func addChild(_ child: MDLObject)     func boundingBoxAtTime(_ time: NSTimeInterval) -> MDLAxisAlignedBoundingBox } extension MDLObject {     convenience init(SCNNode scnNode: SCNNode)     class func objectWithSCNNode(_ scnNode: SCNNode) -> Self } ``` |

Modified [MDLObject.componentConformingToProtocol(_: Protocol) -> MDLComponent?](https://developer.apple.com/documentation/modelio/mdlobject/1391664-componentconforming)

|  | Declaration |
| --- | --- |
| From | ``` func componentConformingToProtocol(_ `protocol`: Protocol) -> MDLComponent? ``` |
| To | ``` func componentConformingToProtocol(_ protocol: Protocol) -> MDLComponent? ``` |

Modified [MDLObject.setComponent(_: MDLComponent, forProtocol: Protocol)](https://developer.apple.com/documentation/modelio/mdlobject/1391974-setcomponent)

|  | Declaration |
| --- | --- |
| From | ``` func setComponent(_ component: MDLComponent, forProtocol `protocol`: Protocol) ``` |
| To | ``` func setComponent(_ component: MDLComponent, forProtocol protocol: Protocol) ``` |

Modified [MDLSubmesh](https://developer.apple.com/documentation/modelio/mdlsubmesh)

|  | Declaration |
| --- | --- |
| From | ``` class MDLSubmesh : NSObject, MDLNamed {     init(name name: String, indexBuffer indexBuffer: MDLMeshBuffer, indexCount indexCount: Int, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType, material material: MDLMaterial?)     init(indexBuffer indexBuffer: MDLMeshBuffer, indexCount indexCount: Int, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType, material material: MDLMaterial?)     init(name name: String, indexBuffer indexBuffer: MDLMeshBuffer, indexCount indexCount: Int, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType, material material: MDLMaterial?, topology topology: MDLSubmeshTopology?)     init?(MDLSubmesh submesh: MDLSubmesh, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType)     var indexBuffer: MDLMeshBuffer { get }     var indexCount: Int { get }     var indexType: MDLIndexBitDepth { get }     var geometryType: MDLGeometryType { get }     var material: MDLMaterial?     var topology: MDLSubmeshTopology? { get }     var name: String } ``` |
| To | ``` class MDLSubmesh : NSObject, MDLNamed {     init(name name: String, indexBuffer indexBuffer: MDLMeshBuffer, indexCount indexCount: Int, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType, material material: MDLMaterial?)     init(indexBuffer indexBuffer: MDLMeshBuffer, indexCount indexCount: Int, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType, material material: MDLMaterial?)     init(name name: String, indexBuffer indexBuffer: MDLMeshBuffer, indexCount indexCount: Int, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType, material material: MDLMaterial?, topology topology: MDLSubmeshTopology?)     init?(MDLSubmesh submesh: MDLSubmesh, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType)     var indexBuffer: MDLMeshBuffer { get }     var indexCount: Int { get }     var indexType: MDLIndexBitDepth { get }     var geometryType: MDLGeometryType { get }     var material: MDLMaterial?     var topology: MDLSubmeshTopology? { get }     var name: String } extension MDLSubmesh {     convenience init(SCNGeometryElement scnGeometryElement: SCNGeometryElement)     class func submeshWithSCNGeometryElement(_ scnGeometryElement: SCNGeometryElement) -> Self } ``` |

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
