---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/SceneKit.html
archived_at: '2026-07-18T02:57:10.764384Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# SceneKit Changes for Swift

### SceneKit

Modified [SCNAction](https://developer.apple.com/documentation/scenekit/scnaction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNAction : NSObject, NSCopying, NSSecureCoding, NSCoding {     var duration: NSTimeInterval     var timingMode: SCNActionTimingMode     var timingFunction: SCNActionTimingFunction?     var speed: CGFloat     func reversedAction() -> SCNAction     class func moveByX(_ deltaX: CGFloat, y deltaY: CGFloat, z deltaZ: CGFloat, duration duration: NSTimeInterval) -> SCNAction     class func moveBy(_ delta: SCNVector3, duration duration: NSTimeInterval) -> SCNAction     class func moveTo(_ location: SCNVector3, duration duration: NSTimeInterval) -> SCNAction     class func rotateByX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval) -> SCNAction     class func rotateToX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval) -> SCNAction     class func rotateToX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SCNAction     class func rotateByAngle(_ angle: CGFloat, aroundAxis axis: SCNVector3, duration duration: NSTimeInterval) -> SCNAction     class func rotateToAxisAngle(_ axisAngle: SCNVector4, duration duration: NSTimeInterval) -> SCNAction     class func scaleBy(_ scale: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func scaleTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func sequence(_ actions: [SCNAction]) -> SCNAction     class func group(_ actions: [SCNAction]) -> SCNAction     class func repeatAction(_ action: SCNAction, count count: Int) -> SCNAction     class func repeatActionForever(_ action: SCNAction) -> SCNAction     class func fadeInWithDuration(_ sec: NSTimeInterval) -> SCNAction     class func fadeOutWithDuration(_ sec: NSTimeInterval) -> SCNAction     class func fadeOpacityBy(_ factor: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func fadeOpacityTo(_ opacity: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func hide() -> SCNAction     class func unhide() -> SCNAction     class func waitForDuration(_ sec: NSTimeInterval) -> SCNAction     class func waitForDuration(_ sec: NSTimeInterval, withRange durationRange: NSTimeInterval) -> SCNAction     class func removeFromParentNode() -> SCNAction     class func runBlock(_ block: (SCNNode) -> Void) -> SCNAction     class func runBlock(_ block: (SCNNode) -> Void, queue queue: dispatch_queue_t) -> SCNAction     class func javaScriptActionWithScript(_ script: String, duration seconds: NSTimeInterval) -> SCNAction     class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SCNNode, CGFloat) -> Void) -> SCNAction     class func playAudioSource(_ source: SCNAudioSource, waitForCompletion wait: Bool) -> SCNAction } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class SCNAction : NSObject, NSCopying, NSSecureCoding {     var duration: NSTimeInterval     var timingMode: SCNActionTimingMode     var timingFunction: SCNActionTimingFunction?     var speed: CGFloat     func reversedAction() -> SCNAction     class func moveByX(_ deltaX: CGFloat, y deltaY: CGFloat, z deltaZ: CGFloat, duration duration: NSTimeInterval) -> SCNAction     class func moveBy(_ delta: SCNVector3, duration duration: NSTimeInterval) -> SCNAction     class func moveTo(_ location: SCNVector3, duration duration: NSTimeInterval) -> SCNAction     class func rotateByX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval) -> SCNAction     class func rotateToX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval) -> SCNAction     class func rotateToX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SCNAction     class func rotateByAngle(_ angle: CGFloat, aroundAxis axis: SCNVector3, duration duration: NSTimeInterval) -> SCNAction     class func rotateToAxisAngle(_ axisAngle: SCNVector4, duration duration: NSTimeInterval) -> SCNAction     class func scaleBy(_ scale: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func scaleTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func sequence(_ actions: [SCNAction]) -> SCNAction     class func group(_ actions: [SCNAction]) -> SCNAction     class func repeatAction(_ action: SCNAction, count count: Int) -> SCNAction     class func repeatActionForever(_ action: SCNAction) -> SCNAction     class func fadeInWithDuration(_ sec: NSTimeInterval) -> SCNAction     class func fadeOutWithDuration(_ sec: NSTimeInterval) -> SCNAction     class func fadeOpacityBy(_ factor: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func fadeOpacityTo(_ opacity: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func hide() -> SCNAction     class func unhide() -> SCNAction     class func waitForDuration(_ sec: NSTimeInterval) -> SCNAction     class func waitForDuration(_ sec: NSTimeInterval, withRange durationRange: NSTimeInterval) -> SCNAction     class func removeFromParentNode() -> SCNAction     class func runBlock(_ block: (SCNNode) -> Void) -> SCNAction     class func runBlock(_ block: (SCNNode) -> Void, queue queue: dispatch_queue_t) -> SCNAction     class func javaScriptActionWithScript(_ script: String, duration seconds: NSTimeInterval) -> SCNAction     class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SCNNode, CGFloat) -> Void) -> SCNAction     class func playAudioSource(_ source: SCNAudioSource, waitForCompletion wait: Bool) -> SCNAction } ``` | NSCopying, NSSecureCoding |

Modified [SCNActionTimingMode [enum]](https://developer.apple.com/documentation/scenekit/scnactiontimingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNAnimationEvent](https://developer.apple.com/documentation/scenekit/scnanimationevent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNAntialiasingMode [enum]](https://developer.apple.com/documentation/scenekit/scnantialiasingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNAudioPlayer](https://developer.apple.com/documentation/scenekit/scnaudioplayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNAudioSource](https://developer.apple.com/documentation/scenekit/scnaudiosource)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNAudioSource : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init?(fileNamed name: String)     init?(URL url: NSURL)     convenience init?(named fileName: String)     class func audioSourceNamed(_ fileName: String) -> Self?     var positional: Bool     var volume: Float     var rate: Float     var reverbBlend: Float     var loops: Bool     var shouldStream: Bool     func load() } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class SCNAudioSource : NSObject, NSCopying, NSSecureCoding {     convenience init?(fileNamed name: String)     init?(URL url: NSURL)     convenience init?(named fileName: String)     class func audioSourceNamed(_ fileName: String) -> Self?     var positional: Bool     var volume: Float     var rate: Float     var reverbBlend: Float     var loops: Bool     var shouldStream: Bool     func load() } ``` | NSCopying, NSSecureCoding |

Modified [SCNBillboardConstraint](https://developer.apple.com/documentation/scenekit/scnbillboardconstraint)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNBlendMode [enum]](https://developer.apple.com/documentation/scenekit/scnblendmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNBox](https://developer.apple.com/documentation/scenekit/scnbox)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNBufferFrequency [enum]](https://developer.apple.com/documentation/scenekit/scnbufferfrequency)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNCamera](https://developer.apple.com/documentation/scenekit/scncamera)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNCamera : NSObject, SCNAnimatable, SCNTechniqueSupport, NSCopying, NSSecureCoding, NSCoding {     convenience init()     class func camera() -> Self     var name: String?     var xFov: Double     var yFov: Double     var zNear: Double     var zFar: Double     var automaticallyAdjustsZRange: Bool     var usesOrthographicProjection: Bool     var orthographicScale: Double     func projectionTransform() -> SCNMatrix4     func setProjectionTransform(_ projectionTransform: SCNMatrix4)     var focalDistance: CGFloat     var focalSize: CGFloat     var focalBlurRadius: CGFloat     var aperture: CGFloat     var categoryBitMask: Int } ``` | AnyObject, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, SCNAnimatable, SCNTechniqueSupport |
| To | ``` class SCNCamera : NSObject, SCNAnimatable, SCNTechniqueSupport, NSCopying, NSSecureCoding {     convenience init()     class func camera() -> Self     var name: String?     var xFov: Double     var yFov: Double     var zNear: Double     var zFar: Double     var automaticallyAdjustsZRange: Bool     var usesOrthographicProjection: Bool     var orthographicScale: Double     func projectionTransform() -> SCNMatrix4     func setProjectionTransform(_ projectionTransform: SCNMatrix4)     var focalDistance: CGFloat     var focalSize: CGFloat     var focalBlurRadius: CGFloat     var aperture: CGFloat     var categoryBitMask: Int } ``` | NSCopying, NSSecureCoding, SCNAnimatable, SCNTechniqueSupport |

Modified [SCNCapsule](https://developer.apple.com/documentation/scenekit/scncapsule)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNChamferMode [enum]](https://developer.apple.com/documentation/scenekit/scnchamfermode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNCone](https://developer.apple.com/documentation/scenekit/scncone)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNConstraint](https://developer.apple.com/documentation/scenekit/scnconstraint)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNConstraint : NSObject, NSCopying, NSSecureCoding, NSCoding, SCNAnimatable {     var influenceFactor: CGFloat } ``` | AnyObject, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, SCNAnimatable |
| To | ``` class SCNConstraint : NSObject, NSCopying, NSSecureCoding, SCNAnimatable {     var influenceFactor: CGFloat } ``` | NSCopying, NSSecureCoding, SCNAnimatable |

Modified [SCNCullMode [enum]](https://developer.apple.com/documentation/scenekit/scncullmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNCylinder](https://developer.apple.com/documentation/scenekit/scncylinder)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNFilterMode [enum]](https://developer.apple.com/documentation/scenekit/scnfiltermode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNFloor](https://developer.apple.com/documentation/scenekit/scnfloor)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNGeometry](https://developer.apple.com/documentation/scenekit/scngeometry)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNGeometry : NSObject, SCNAnimatable, SCNBoundingVolume, SCNShadable, NSCopying, NSSecureCoding, NSCoding {     convenience init()     class func geometry() -> Self     var name: String?     var materials: [SCNMaterial]     var firstMaterial: SCNMaterial?     func insertMaterial(_ material: SCNMaterial, atIndex index: Int)     func removeMaterialAtIndex(_ index: Int)     func replaceMaterialAtIndex(_ index: Int, withMaterial material: SCNMaterial)     func materialWithName(_ name: String) -> SCNMaterial?     convenience init(sources sources: [SCNGeometrySource], elements elements: [SCNGeometryElement])     class func geometryWithSources(_ sources: [SCNGeometrySource], elements elements: [SCNGeometryElement]) -> Self     var geometrySources: [SCNGeometrySource] { get }     func geometrySourcesForSemantic(_ semantic: String) -> [SCNGeometrySource]     var geometryElements: [SCNGeometryElement] { get }     var geometryElementCount: Int { get }     func geometryElementAtIndex(_ elementIndex: Int) -> SCNGeometryElement     var levelsOfDetail: [SCNLevelOfDetail]?     var subdivisionLevel: Int     var edgeCreasesElement: SCNGeometryElement?     var edgeCreasesSource: SCNGeometrySource? } ``` | AnyObject, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, SCNAnimatable, SCNBoundingVolume, SCNShadable |
| To | ``` class SCNGeometry : NSObject, SCNAnimatable, SCNBoundingVolume, SCNShadable, NSCopying, NSSecureCoding {     convenience init()     class func geometry() -> Self     var name: String?     var materials: [SCNMaterial]     var firstMaterial: SCNMaterial?     func insertMaterial(_ material: SCNMaterial, atIndex index: Int)     func removeMaterialAtIndex(_ index: Int)     func replaceMaterialAtIndex(_ index: Int, withMaterial material: SCNMaterial)     func materialWithName(_ name: String) -> SCNMaterial?     convenience init(sources sources: [SCNGeometrySource], elements elements: [SCNGeometryElement])     class func geometryWithSources(_ sources: [SCNGeometrySource], elements elements: [SCNGeometryElement]) -> Self     var geometrySources: [SCNGeometrySource] { get }     func geometrySourcesForSemantic(_ semantic: String) -> [SCNGeometrySource]     var geometryElements: [SCNGeometryElement] { get }     var geometryElementCount: Int { get }     func geometryElementAtIndex(_ elementIndex: Int) -> SCNGeometryElement     var levelsOfDetail: [SCNLevelOfDetail]?     var subdivisionLevel: Int     var edgeCreasesElement: SCNGeometryElement?     var edgeCreasesSource: SCNGeometrySource? } ``` | NSCopying, NSSecureCoding, SCNAnimatable, SCNBoundingVolume, SCNShadable |

Modified [SCNGeometryElement](https://developer.apple.com/documentation/scenekit/scngeometryelement)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNGeometryElement : NSObject, NSSecureCoding, NSCoding {     convenience init(data data: NSData?, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int)     class func geometryElementWithData(_ data: NSData?, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int) -> Self     var data: NSData { get }     var primitiveType: SCNGeometryPrimitiveType { get }     var primitiveCount: Int { get }     var bytesPerIndex: Int { get } } extension SCNGeometryElement {     convenience init<IndexType : IntegerType>(indices indices: [IndexType], primitiveType primitiveType: SCNGeometryPrimitiveType) } extension SCNGeometryElement {     convenience init<IndexType : IntegerType>(indices indices: [IndexType], primitiveType primitiveType: SCNGeometryPrimitiveType) } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class SCNGeometryElement : NSObject, NSSecureCoding {     convenience init(data data: NSData?, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int)     class func geometryElementWithData(_ data: NSData?, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int) -> Self     var data: NSData { get }     var primitiveType: SCNGeometryPrimitiveType { get }     var primitiveCount: Int { get }     var bytesPerIndex: Int { get } } extension SCNGeometryElement {     convenience init<IndexType : IntegerType>(indices indices: [IndexType], primitiveType primitiveType: SCNGeometryPrimitiveType) } extension SCNGeometryElement {     convenience init<IndexType : IntegerType>(indices indices: [IndexType], primitiveType primitiveType: SCNGeometryPrimitiveType) } ``` | NSSecureCoding |

Modified [SCNGeometryPrimitiveType [enum]](https://developer.apple.com/documentation/scenekit/scngeometryprimitivetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNGeometrySource](https://developer.apple.com/documentation/scenekit/scngeometrysource)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNGeometrySource : NSObject, NSSecureCoding, NSCoding {     convenience init(data data: NSData, semantic semantic: String, vectorCount vectorCount: Int, floatComponents floatComponents: Bool, componentsPerVector componentsPerVector: Int, bytesPerComponent bytesPerComponent: Int, dataOffset offset: Int, dataStride stride: Int)     class func geometrySourceWithData(_ data: NSData, semantic semantic: String, vectorCount vectorCount: Int, floatComponents floatComponents: Bool, componentsPerVector componentsPerVector: Int, bytesPerComponent bytesPerComponent: Int, dataOffset offset: Int, dataStride stride: Int) -> Self     convenience init(vertices vertices: UnsafePointer<SCNVector3>, count count: Int)     class func geometrySourceWithVertices(_ vertices: UnsafePointer<SCNVector3>, count count: Int) -> Self     convenience init(normals normals: UnsafePointer<SCNVector3>, count count: Int)     class func geometrySourceWithNormals(_ normals: UnsafePointer<SCNVector3>, count count: Int) -> Self     convenience init(textureCoordinates texcoord: UnsafePointer<CGPoint>, count count: Int)     class func geometrySourceWithTextureCoordinates(_ texcoord: UnsafePointer<CGPoint>, count count: Int) -> Self     convenience init(buffer mtlBuffer: MTLBuffer, vertexFormat vertexFormat: MTLVertexFormat, semantic semantic: String, vertexCount vertexCount: Int, dataOffset offset: Int, dataStride stride: Int)     class func geometrySourceWithBuffer(_ mtlBuffer: MTLBuffer, vertexFormat vertexFormat: MTLVertexFormat, semantic semantic: String, vertexCount vertexCount: Int, dataOffset offset: Int, dataStride stride: Int) -> Self     var data: NSData { get }     var semantic: String { get }     var vectorCount: Int { get }     var floatComponents: Bool { get }     var componentsPerVector: Int { get }     var bytesPerComponent: Int { get }     var dataOffset: Int { get }     var dataStride: Int { get } } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class SCNGeometrySource : NSObject, NSSecureCoding {     convenience init(data data: NSData, semantic semantic: String, vectorCount vectorCount: Int, floatComponents floatComponents: Bool, componentsPerVector componentsPerVector: Int, bytesPerComponent bytesPerComponent: Int, dataOffset offset: Int, dataStride stride: Int)     class func geometrySourceWithData(_ data: NSData, semantic semantic: String, vectorCount vectorCount: Int, floatComponents floatComponents: Bool, componentsPerVector componentsPerVector: Int, bytesPerComponent bytesPerComponent: Int, dataOffset offset: Int, dataStride stride: Int) -> Self     convenience init(vertices vertices: UnsafePointer<SCNVector3>, count count: Int)     class func geometrySourceWithVertices(_ vertices: UnsafePointer<SCNVector3>, count count: Int) -> Self     convenience init(normals normals: UnsafePointer<SCNVector3>, count count: Int)     class func geometrySourceWithNormals(_ normals: UnsafePointer<SCNVector3>, count count: Int) -> Self     convenience init(textureCoordinates texcoord: UnsafePointer<CGPoint>, count count: Int)     class func geometrySourceWithTextureCoordinates(_ texcoord: UnsafePointer<CGPoint>, count count: Int) -> Self     convenience init(buffer mtlBuffer: MTLBuffer, vertexFormat vertexFormat: MTLVertexFormat, semantic semantic: String, vertexCount vertexCount: Int, dataOffset offset: Int, dataStride stride: Int)     class func geometrySourceWithBuffer(_ mtlBuffer: MTLBuffer, vertexFormat vertexFormat: MTLVertexFormat, semantic semantic: String, vertexCount vertexCount: Int, dataOffset offset: Int, dataStride stride: Int) -> Self     var data: NSData { get }     var semantic: String { get }     var vectorCount: Int { get }     var floatComponents: Bool { get }     var componentsPerVector: Int { get }     var bytesPerComponent: Int { get }     var dataOffset: Int { get }     var dataStride: Int { get } } ``` | NSSecureCoding |

Modified [SCNHitTestResult](https://developer.apple.com/documentation/scenekit/scnhittestresult)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNIKConstraint](https://developer.apple.com/documentation/scenekit/scnikconstraint)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNLevelOfDetail](https://developer.apple.com/documentation/scenekit/scnlevelofdetail)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNLevelOfDetail : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(geometry geometry: SCNGeometry?, screenSpaceRadius radius: CGFloat)     class func levelOfDetailWithGeometry(_ geometry: SCNGeometry?, screenSpaceRadius radius: CGFloat) -> Self     convenience init(geometry geometry: SCNGeometry?, worldSpaceDistance distance: CGFloat)     class func levelOfDetailWithGeometry(_ geometry: SCNGeometry?, worldSpaceDistance distance: CGFloat) -> Self     var geometry: SCNGeometry? { get }     var screenSpaceRadius: CGFloat { get }     var worldSpaceDistance: CGFloat { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class SCNLevelOfDetail : NSObject, NSCopying, NSSecureCoding {     convenience init(geometry geometry: SCNGeometry?, screenSpaceRadius radius: CGFloat)     class func levelOfDetailWithGeometry(_ geometry: SCNGeometry?, screenSpaceRadius radius: CGFloat) -> Self     convenience init(geometry geometry: SCNGeometry?, worldSpaceDistance distance: CGFloat)     class func levelOfDetailWithGeometry(_ geometry: SCNGeometry?, worldSpaceDistance distance: CGFloat) -> Self     var geometry: SCNGeometry? { get }     var screenSpaceRadius: CGFloat { get }     var worldSpaceDistance: CGFloat { get } } ``` | NSCopying, NSSecureCoding |

Modified [SCNLight](https://developer.apple.com/documentation/scenekit/scnlight)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNLight : NSObject, SCNAnimatable, SCNTechniqueSupport, NSCopying, NSSecureCoding, NSCoding {     convenience init()     class func light() -> Self     var type: String     var color: AnyObject     var name: String?     var castsShadow: Bool     var shadowColor: AnyObject     var shadowRadius: CGFloat     var shadowMapSize: CGSize     var shadowSampleCount: Int     var shadowMode: SCNShadowMode     var shadowBias: CGFloat     var orthographicScale: CGFloat     var zNear: CGFloat     var zFar: CGFloat     var attenuationStartDistance: CGFloat     var attenuationEndDistance: CGFloat     var attenuationFalloffExponent: CGFloat     var spotInnerAngle: CGFloat     var spotOuterAngle: CGFloat     var gobo: SCNMaterialProperty? { get }     var categoryBitMask: Int } ``` | AnyObject, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, SCNAnimatable, SCNTechniqueSupport |
| To | ``` class SCNLight : NSObject, SCNAnimatable, SCNTechniqueSupport, NSCopying, NSSecureCoding {     convenience init()     class func light() -> Self     var type: String     var color: AnyObject     var name: String?     var castsShadow: Bool     var shadowColor: AnyObject     var shadowRadius: CGFloat     var shadowMapSize: CGSize     var shadowSampleCount: Int     var shadowMode: SCNShadowMode     var shadowBias: CGFloat     var orthographicScale: CGFloat     var zNear: CGFloat     var zFar: CGFloat     var attenuationStartDistance: CGFloat     var attenuationEndDistance: CGFloat     var attenuationFalloffExponent: CGFloat     var spotInnerAngle: CGFloat     var spotOuterAngle: CGFloat     var gobo: SCNMaterialProperty? { get }     var categoryBitMask: Int } ``` | NSCopying, NSSecureCoding, SCNAnimatable, SCNTechniqueSupport |

Modified [SCNLookAtConstraint](https://developer.apple.com/documentation/scenekit/scnlookatconstraint)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNMaterial](https://developer.apple.com/documentation/scenekit/scnmaterial)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNMaterial : NSObject, SCNAnimatable, SCNShadable, NSCopying, NSSecureCoding, NSCoding {     convenience init()     class func material() -> Self     var name: String?     var diffuse: SCNMaterialProperty { get }     var ambient: SCNMaterialProperty { get }     var specular: SCNMaterialProperty { get }     var emission: SCNMaterialProperty { get }     var transparent: SCNMaterialProperty { get }     var reflective: SCNMaterialProperty { get }     var multiply: SCNMaterialProperty { get }     var normal: SCNMaterialProperty { get }     var ambientOcclusion: SCNMaterialProperty { get }     var selfIllumination: SCNMaterialProperty { get }     var shininess: CGFloat     var transparency: CGFloat     var lightingModelName: String     var litPerPixel: Bool     var doubleSided: Bool     var cullMode: SCNCullMode     var transparencyMode: SCNTransparencyMode     var locksAmbientWithDiffuse: Bool     var writesToDepthBuffer: Bool     var readsFromDepthBuffer: Bool     var fresnelExponent: CGFloat     var blendMode: SCNBlendMode } ``` | AnyObject, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, SCNAnimatable, SCNShadable |
| To | ``` class SCNMaterial : NSObject, SCNAnimatable, SCNShadable, NSCopying, NSSecureCoding {     convenience init()     class func material() -> Self     var name: String?     var diffuse: SCNMaterialProperty { get }     var ambient: SCNMaterialProperty { get }     var specular: SCNMaterialProperty { get }     var emission: SCNMaterialProperty { get }     var transparent: SCNMaterialProperty { get }     var reflective: SCNMaterialProperty { get }     var multiply: SCNMaterialProperty { get }     var normal: SCNMaterialProperty { get }     var ambientOcclusion: SCNMaterialProperty { get }     var selfIllumination: SCNMaterialProperty { get }     var shininess: CGFloat     var transparency: CGFloat     var lightingModelName: String     var litPerPixel: Bool     var doubleSided: Bool     var cullMode: SCNCullMode     var transparencyMode: SCNTransparencyMode     var locksAmbientWithDiffuse: Bool     var writesToDepthBuffer: Bool     var readsFromDepthBuffer: Bool     var fresnelExponent: CGFloat     var blendMode: SCNBlendMode } ``` | NSCopying, NSSecureCoding, SCNAnimatable, SCNShadable |

Modified [SCNMaterialProperty](https://developer.apple.com/documentation/scenekit/scnmaterialproperty)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNMaterialProperty : NSObject, SCNAnimatable, NSSecureCoding, NSCoding {     convenience init(contents contents: AnyObject)     class func materialPropertyWithContents(_ contents: AnyObject) -> Self     var contents: AnyObject?     var intensity: CGFloat     var minificationFilter: SCNFilterMode     var magnificationFilter: SCNFilterMode     var mipFilter: SCNFilterMode     var contentsTransform: SCNMatrix4     var wrapS: SCNWrapMode     var wrapT: SCNWrapMode     var borderColor: AnyObject?     var mappingChannel: Int     var maxAnisotropy: CGFloat } ``` | AnyObject, NSCoding, NSObjectProtocol, NSSecureCoding, SCNAnimatable |
| To | ``` class SCNMaterialProperty : NSObject, SCNAnimatable, NSSecureCoding {     convenience init(contents contents: AnyObject)     class func materialPropertyWithContents(_ contents: AnyObject) -> Self     var contents: AnyObject?     var intensity: CGFloat     var minificationFilter: SCNFilterMode     var magnificationFilter: SCNFilterMode     var mipFilter: SCNFilterMode     var contentsTransform: SCNMatrix4     var wrapS: SCNWrapMode     var wrapT: SCNWrapMode     var borderColor: AnyObject?     var mappingChannel: Int     var maxAnisotropy: CGFloat } ``` | NSSecureCoding, SCNAnimatable |

Modified [SCNMorpher](https://developer.apple.com/documentation/scenekit/scnmorpher)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNMorpher : NSObject, SCNAnimatable, NSSecureCoding, NSCoding {     var targets: [SCNGeometry]     func setWeight(_ weight: CGFloat, forTargetAtIndex targetIndex: Int)     func weightForTargetAtIndex(_ targetIndex: Int) -> CGFloat     var calculationMode: SCNMorpherCalculationMode } ``` | AnyObject, NSCoding, NSObjectProtocol, NSSecureCoding, SCNAnimatable |
| To | ``` class SCNMorpher : NSObject, SCNAnimatable, NSSecureCoding {     var targets: [SCNGeometry]     func setWeight(_ weight: CGFloat, forTargetAtIndex targetIndex: Int)     func weightForTargetAtIndex(_ targetIndex: Int) -> CGFloat     var calculationMode: SCNMorpherCalculationMode } ``` | NSSecureCoding, SCNAnimatable |

Modified [SCNMorpherCalculationMode [enum]](https://developer.apple.com/documentation/scenekit/scnmorphercalculationmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNNode](https://developer.apple.com/documentation/scenekit/scnnode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNNode : NSObject, NSCopying, NSSecureCoding, NSCoding, SCNAnimatable, SCNActionable, SCNBoundingVolume {     convenience init()     class func node() -> Self      init(geometry geometry: SCNGeometry?)     class func nodeWithGeometry(_ geometry: SCNGeometry?) -> SCNNode     func clone() -> Self     func flattenedClone() -> Self     var name: String?     var light: SCNLight?     var camera: SCNCamera?     var geometry: SCNGeometry?     var skinner: SCNSkinner?     var morpher: SCNMorpher?     var transform: SCNMatrix4     var position: SCNVector3     var rotation: SCNVector4     var orientation: SCNQuaternion     var eulerAngles: SCNVector3     var scale: SCNVector3     var pivot: SCNMatrix4     var worldTransform: SCNMatrix4 { get }     var hidden: Bool     var opacity: CGFloat     var renderingOrder: Int     var castsShadow: Bool     var parentNode: SCNNode? { get }     var childNodes: [SCNNode] { get }     func addChildNode(_ child: SCNNode)     func insertChildNode(_ child: SCNNode, atIndex index: Int)     func removeFromParentNode()     func replaceChildNode(_ oldChild: SCNNode, with newChild: SCNNode)     func childNodeWithName(_ name: String, recursively recursively: Bool) -> SCNNode?     func childNodesPassingTest(_ predicate: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]     func enumerateChildNodesUsingBlock(_ block: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)     func convertPosition(_ position: SCNVector3, toNode node: SCNNode?) -> SCNVector3     func convertPosition(_ position: SCNVector3, fromNode node: SCNNode?) -> SCNVector3     func convertTransform(_ transform: SCNMatrix4, toNode node: SCNNode?) -> SCNMatrix4     func convertTransform(_ transform: SCNMatrix4, fromNode node: SCNNode?) -> SCNMatrix4     var physicsBody: SCNPhysicsBody?     var physicsField: SCNPhysicsField?     var constraints: [SCNConstraint]?     var filters: [CIFilter]?     var presentationNode: SCNNode { get }     var paused: Bool     unowned(unsafe) var rendererDelegate: SCNNodeRendererDelegate?     func hitTestWithSegmentFromPoint(_ pointA: SCNVector3, toPoint pointB: SCNVector3, options options: [String : AnyObject]?) -> [SCNHitTestResult]     var categoryBitMask: Int } extension SCNNode {     func addAudioPlayer(_ player: SCNAudioPlayer)     func removeAllAudioPlayers()     func removeAudioPlayer(_ player: SCNAudioPlayer)     var audioPlayers: [SCNAudioPlayer] { get } } extension SCNNode {     func addParticleSystem(_ system: SCNParticleSystem)     func removeAllParticleSystems()     func removeParticleSystem(_ system: SCNParticleSystem)     var particleSystems: [SCNParticleSystem]? { get } } ``` | AnyObject, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, SCNActionable, SCNAnimatable, SCNBoundingVolume |
| To | ``` class SCNNode : NSObject, NSCopying, NSSecureCoding, SCNAnimatable, SCNActionable, SCNBoundingVolume {     convenience init()     class func node() -> Self      init(geometry geometry: SCNGeometry?)     class func nodeWithGeometry(_ geometry: SCNGeometry?) -> SCNNode     func clone() -> Self     func flattenedClone() -> Self     var name: String?     var light: SCNLight?     var camera: SCNCamera?     var geometry: SCNGeometry?     var skinner: SCNSkinner?     var morpher: SCNMorpher?     var transform: SCNMatrix4     var position: SCNVector3     var rotation: SCNVector4     var orientation: SCNQuaternion     var eulerAngles: SCNVector3     var scale: SCNVector3     var pivot: SCNMatrix4     var worldTransform: SCNMatrix4 { get }     var hidden: Bool     var opacity: CGFloat     var renderingOrder: Int     var castsShadow: Bool     var parentNode: SCNNode? { get }     var childNodes: [SCNNode] { get }     func addChildNode(_ child: SCNNode)     func insertChildNode(_ child: SCNNode, atIndex index: Int)     func removeFromParentNode()     func replaceChildNode(_ oldChild: SCNNode, with newChild: SCNNode)     func childNodeWithName(_ name: String, recursively recursively: Bool) -> SCNNode?     func childNodesPassingTest(_ predicate: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]     func enumerateChildNodesUsingBlock(_ block: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)     func convertPosition(_ position: SCNVector3, toNode node: SCNNode?) -> SCNVector3     func convertPosition(_ position: SCNVector3, fromNode node: SCNNode?) -> SCNVector3     func convertTransform(_ transform: SCNMatrix4, toNode node: SCNNode?) -> SCNMatrix4     func convertTransform(_ transform: SCNMatrix4, fromNode node: SCNNode?) -> SCNMatrix4     var physicsBody: SCNPhysicsBody?     var physicsField: SCNPhysicsField?     var constraints: [SCNConstraint]?     var filters: [CIFilter]?     var presentationNode: SCNNode { get }     var paused: Bool     unowned(unsafe) var rendererDelegate: SCNNodeRendererDelegate?     func hitTestWithSegmentFromPoint(_ pointA: SCNVector3, toPoint pointB: SCNVector3, options options: [String : AnyObject]?) -> [SCNHitTestResult]     var categoryBitMask: Int } extension SCNNode {     func addAudioPlayer(_ player: SCNAudioPlayer)     func removeAllAudioPlayers()     func removeAudioPlayer(_ player: SCNAudioPlayer)     var audioPlayers: [SCNAudioPlayer] { get } } extension SCNNode {     func addParticleSystem(_ system: SCNParticleSystem)     func removeAllParticleSystems()     func removeParticleSystem(_ system: SCNParticleSystem)     var particleSystems: [SCNParticleSystem]? { get } } ``` | NSCopying, NSSecureCoding, SCNActionable, SCNAnimatable, SCNBoundingVolume |

Modified [SCNParticleBirthDirection [enum]](https://developer.apple.com/documentation/scenekit/scnparticlebirthdirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNParticleBirthLocation [enum]](https://developer.apple.com/documentation/scenekit/scnparticlebirthlocation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNParticleBlendMode [enum]](https://developer.apple.com/documentation/scenekit/scnparticleblendmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNParticleEvent [enum]](https://developer.apple.com/documentation/scenekit/scnparticleevent)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNParticleImageSequenceAnimationMode [enum]](https://developer.apple.com/documentation/scenekit/scnparticleimagesequenceanimationmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNParticleInputMode [enum]](https://developer.apple.com/documentation/scenekit/scnparticleinputmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNParticleModifierStage [enum]](https://developer.apple.com/documentation/scenekit/scnparticlemodifierstage)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNParticleOrientationMode [enum]](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNParticlePropertyController](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNParticlePropertyController : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init(animation animation: CAAnimation)     class func controllerWithAnimation(_ animation: CAAnimation) -> Self     var animation: CAAnimation     var inputMode: SCNParticleInputMode     var inputScale: CGFloat     var inputBias: CGFloat     weak var inputOrigin: SCNNode?     var inputProperty: String? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class SCNParticlePropertyController : NSObject, NSSecureCoding, NSCopying {     convenience init(animation animation: CAAnimation)     class func controllerWithAnimation(_ animation: CAAnimation) -> Self     var animation: CAAnimation     var inputMode: SCNParticleInputMode     var inputScale: CGFloat     var inputBias: CGFloat     weak var inputOrigin: SCNNode?     var inputProperty: String? } ``` | NSCopying, NSSecureCoding |

Modified [SCNParticleSortingMode [enum]](https://developer.apple.com/documentation/scenekit/scnparticlesortingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNParticleSystem](https://developer.apple.com/documentation/scenekit/scnparticlesystem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNParticleSystem : NSObject, NSCopying, NSSecureCoding, NSCoding, SCNAnimatable {     convenience init()     class func particleSystem() -> Self     convenience init?(named name: String, inDirectory directory: String?)     class func particleSystemNamed(_ name: String, inDirectory directory: String?) -> Self?     var emissionDuration: CGFloat     var emissionDurationVariation: CGFloat     var idleDuration: CGFloat     var idleDurationVariation: CGFloat     var loops: Bool     var birthRate: CGFloat     var birthRateVariation: CGFloat     var warmupDuration: CGFloat     var emitterShape: SCNGeometry?     var birthLocation: SCNParticleBirthLocation     var birthDirection: SCNParticleBirthDirection     var spreadingAngle: CGFloat     var emittingDirection: SCNVector3     var acceleration: SCNVector3     var local: Bool     var particleAngle: CGFloat     var particleAngleVariation: CGFloat     var particleVelocity: CGFloat     var particleVelocityVariation: CGFloat     var particleAngularVelocity: CGFloat     var particleAngularVelocityVariation: CGFloat     var particleLifeSpan: CGFloat     var particleLifeSpanVariation: CGFloat     var systemSpawnedOnDying: SCNParticleSystem?     var systemSpawnedOnCollision: SCNParticleSystem?     var systemSpawnedOnLiving: SCNParticleSystem?     var particleImage: AnyObject?     var imageSequenceColumnCount: Int     var imageSequenceRowCount: Int     var imageSequenceInitialFrame: CGFloat     var imageSequenceInitialFrameVariation: CGFloat     var imageSequenceFrameRate: CGFloat     var imageSequenceFrameRateVariation: CGFloat     var imageSequenceAnimationMode: SCNParticleImageSequenceAnimationMode     var particleColor: UIColor     var particleColorVariation: SCNVector4     var particleSize: CGFloat     var particleSizeVariation: CGFloat     var blendMode: SCNParticleBlendMode     var blackPassEnabled: Bool     var orientationMode: SCNParticleOrientationMode     var sortingMode: SCNParticleSortingMode     var lightingEnabled: Bool     var affectedByGravity: Bool     var affectedByPhysicsFields: Bool     var particleDiesOnCollision: Bool     var colliderNodes: [SCNNode]?     var particleMass: CGFloat     var particleMassVariation: CGFloat     var particleBounce: CGFloat     var particleBounceVariation: CGFloat     var particleFriction: CGFloat     var particleFrictionVariation: CGFloat     var particleCharge: CGFloat     var particleChargeVariation: CGFloat     var dampingFactor: CGFloat     var speedFactor: CGFloat     var stretchFactor: CGFloat     var fresnelExponent: CGFloat     var propertyControllers: [String : SCNParticlePropertyController]?     func reset()     func handleEvent(_ event: SCNParticleEvent, forProperties properties: [String], withBlock block: SCNParticleEventBlock)     func addModifierForProperties(_ properties: [String], atStage stage: SCNParticleModifierStage, withBlock block: SCNParticleModifierBlock)     func removeModifiersOfStage(_ stage: SCNParticleModifierStage)     func removeAllModifiers() } ``` | AnyObject, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, SCNAnimatable |
| To | ``` class SCNParticleSystem : NSObject, NSCopying, NSSecureCoding, SCNAnimatable {     convenience init()     class func particleSystem() -> Self     convenience init?(named name: String, inDirectory directory: String?)     class func particleSystemNamed(_ name: String, inDirectory directory: String?) -> Self?     var emissionDuration: CGFloat     var emissionDurationVariation: CGFloat     var idleDuration: CGFloat     var idleDurationVariation: CGFloat     var loops: Bool     var birthRate: CGFloat     var birthRateVariation: CGFloat     var warmupDuration: CGFloat     var emitterShape: SCNGeometry?     var birthLocation: SCNParticleBirthLocation     var birthDirection: SCNParticleBirthDirection     var spreadingAngle: CGFloat     var emittingDirection: SCNVector3     var acceleration: SCNVector3     var local: Bool     var particleAngle: CGFloat     var particleAngleVariation: CGFloat     var particleVelocity: CGFloat     var particleVelocityVariation: CGFloat     var particleAngularVelocity: CGFloat     var particleAngularVelocityVariation: CGFloat     var particleLifeSpan: CGFloat     var particleLifeSpanVariation: CGFloat     var systemSpawnedOnDying: SCNParticleSystem?     var systemSpawnedOnCollision: SCNParticleSystem?     var systemSpawnedOnLiving: SCNParticleSystem?     var particleImage: AnyObject?     var imageSequenceColumnCount: Int     var imageSequenceRowCount: Int     var imageSequenceInitialFrame: CGFloat     var imageSequenceInitialFrameVariation: CGFloat     var imageSequenceFrameRate: CGFloat     var imageSequenceFrameRateVariation: CGFloat     var imageSequenceAnimationMode: SCNParticleImageSequenceAnimationMode     var particleColor: UIColor     var particleColorVariation: SCNVector4     var particleSize: CGFloat     var particleSizeVariation: CGFloat     var blendMode: SCNParticleBlendMode     var blackPassEnabled: Bool     var orientationMode: SCNParticleOrientationMode     var sortingMode: SCNParticleSortingMode     var lightingEnabled: Bool     var affectedByGravity: Bool     var affectedByPhysicsFields: Bool     var particleDiesOnCollision: Bool     var colliderNodes: [SCNNode]?     var particleMass: CGFloat     var particleMassVariation: CGFloat     var particleBounce: CGFloat     var particleBounceVariation: CGFloat     var particleFriction: CGFloat     var particleFrictionVariation: CGFloat     var particleCharge: CGFloat     var particleChargeVariation: CGFloat     var dampingFactor: CGFloat     var speedFactor: CGFloat     var stretchFactor: CGFloat     var fresnelExponent: CGFloat     var propertyControllers: [String : SCNParticlePropertyController]?     func reset()     func handleEvent(_ event: SCNParticleEvent, forProperties properties: [String], withBlock block: SCNParticleEventBlock)     func addModifierForProperties(_ properties: [String], atStage stage: SCNParticleModifierStage, withBlock block: SCNParticleModifierBlock)     func removeModifiersOfStage(_ stage: SCNParticleModifierStage)     func removeAllModifiers() } ``` | NSCopying, NSSecureCoding, SCNAnimatable |

Modified [SCNPhysicsBallSocketJoint](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNPhysicsBehavior](https://developer.apple.com/documentation/scenekit/scnphysicsbehavior)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNPhysicsBehavior : NSObject, NSSecureCoding, NSCoding { } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class SCNPhysicsBehavior : NSObject, NSSecureCoding { } ``` | NSSecureCoding |

Modified [SCNPhysicsBody](https://developer.apple.com/documentation/scenekit/scnphysicsbody)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNPhysicsBody : NSObject, NSCopying, NSSecureCoding, NSCoding {     class func staticBody() -> Self     class func dynamicBody() -> Self     class func kinematicBody() -> Self     convenience init(type type: SCNPhysicsBodyType, shape shape: SCNPhysicsShape?)     class func bodyWithType(_ type: SCNPhysicsBodyType, shape shape: SCNPhysicsShape?) -> Self     var type: SCNPhysicsBodyType     var mass: CGFloat     var momentOfInertia: SCNVector3     var usesDefaultMomentOfInertia: Bool     var charge: CGFloat     var friction: CGFloat     var restitution: CGFloat     var rollingFriction: CGFloat     var physicsShape: SCNPhysicsShape?     var isResting: Bool { get }     var allowsResting: Bool     var velocity: SCNVector3     var angularVelocity: SCNVector4     var damping: CGFloat     var angularDamping: CGFloat     var velocityFactor: SCNVector3     var angularVelocityFactor: SCNVector3     var categoryBitMask: Int     var collisionBitMask: Int     var contactTestBitMask: Int     var affectedByGravity: Bool     func applyForce(_ direction: SCNVector3, impulse impulse: Bool)     func applyForce(_ direction: SCNVector3, atPosition position: SCNVector3, impulse impulse: Bool)     func applyTorque(_ torque: SCNVector4, impulse impulse: Bool)     func clearAllForces()     func resetTransform() } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class SCNPhysicsBody : NSObject, NSCopying, NSSecureCoding {     class func staticBody() -> Self     class func dynamicBody() -> Self     class func kinematicBody() -> Self     convenience init(type type: SCNPhysicsBodyType, shape shape: SCNPhysicsShape?)     class func bodyWithType(_ type: SCNPhysicsBodyType, shape shape: SCNPhysicsShape?) -> Self     var type: SCNPhysicsBodyType     var mass: CGFloat     var momentOfInertia: SCNVector3     var usesDefaultMomentOfInertia: Bool     var charge: CGFloat     var friction: CGFloat     var restitution: CGFloat     var rollingFriction: CGFloat     var physicsShape: SCNPhysicsShape?     var isResting: Bool { get }     var allowsResting: Bool     var velocity: SCNVector3     var angularVelocity: SCNVector4     var damping: CGFloat     var angularDamping: CGFloat     var velocityFactor: SCNVector3     var angularVelocityFactor: SCNVector3     var categoryBitMask: Int     var collisionBitMask: Int     var contactTestBitMask: Int     var affectedByGravity: Bool     func applyForce(_ direction: SCNVector3, impulse impulse: Bool)     func applyForce(_ direction: SCNVector3, atPosition position: SCNVector3, impulse impulse: Bool)     func applyTorque(_ torque: SCNVector4, impulse impulse: Bool)     func clearAllForces()     func resetTransform() } ``` | NSCopying, NSSecureCoding |

Modified [SCNPhysicsBodyType [enum]](https://developer.apple.com/documentation/scenekit/scnphysicsbodytype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNPhysicsContact](https://developer.apple.com/documentation/scenekit/scnphysicscontact)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNPhysicsField](https://developer.apple.com/documentation/scenekit/scnphysicsfield)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNPhysicsField : NSObject, NSCopying, NSSecureCoding, NSCoding {     var strength: CGFloat     var falloffExponent: CGFloat     var minimumDistance: CGFloat     var active: Bool     var exclusive: Bool     var halfExtent: SCNVector3     var usesEllipsoidalExtent: Bool     var scope: SCNPhysicsFieldScope     var offset: SCNVector3     var direction: SCNVector3     var categoryBitMask: Int     class func dragField() -> SCNPhysicsField     class func vortexField() -> SCNPhysicsField     class func radialGravityField() -> SCNPhysicsField     class func linearGravityField() -> SCNPhysicsField     class func noiseFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SCNPhysicsField     class func turbulenceFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SCNPhysicsField     class func springField() -> SCNPhysicsField     class func electricField() -> SCNPhysicsField     class func magneticField() -> SCNPhysicsField     class func customFieldWithEvaluationBlock(_ block: SCNFieldForceEvaluator) -> SCNPhysicsField } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class SCNPhysicsField : NSObject, NSCopying, NSSecureCoding {     var strength: CGFloat     var falloffExponent: CGFloat     var minimumDistance: CGFloat     var active: Bool     var exclusive: Bool     var halfExtent: SCNVector3     var usesEllipsoidalExtent: Bool     var scope: SCNPhysicsFieldScope     var offset: SCNVector3     var direction: SCNVector3     var categoryBitMask: Int     class func dragField() -> SCNPhysicsField     class func vortexField() -> SCNPhysicsField     class func radialGravityField() -> SCNPhysicsField     class func linearGravityField() -> SCNPhysicsField     class func noiseFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SCNPhysicsField     class func turbulenceFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SCNPhysicsField     class func springField() -> SCNPhysicsField     class func electricField() -> SCNPhysicsField     class func magneticField() -> SCNPhysicsField     class func customFieldWithEvaluationBlock(_ block: SCNFieldForceEvaluator) -> SCNPhysicsField } ``` | NSCopying, NSSecureCoding |

Modified [SCNPhysicsFieldScope [enum]](https://developer.apple.com/documentation/scenekit/scnphysicsfieldscope)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNPhysicsHingeJoint](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNPhysicsShape](https://developer.apple.com/documentation/scenekit/scnphysicsshape)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNPhysicsShape : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(geometry geometry: SCNGeometry, options options: [String : AnyObject]?)     class func shapeWithGeometry(_ geometry: SCNGeometry, options options: [String : AnyObject]?) -> Self     convenience init(node node: SCNNode, options options: [String : AnyObject]?)     class func shapeWithNode(_ node: SCNNode, options options: [String : AnyObject]?) -> Self     convenience init(shapes shapes: [SCNPhysicsShape], transforms transforms: [NSValue]?)     class func shapeWithShapes(_ shapes: [SCNPhysicsShape], transforms transforms: [NSValue]?) -> Self     var options: [String : AnyObject]? { get }     var sourceObject: AnyObject { get }     var transforms: [NSValue]? { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class SCNPhysicsShape : NSObject, NSCopying, NSSecureCoding {     convenience init(geometry geometry: SCNGeometry, options options: [String : AnyObject]?)     class func shapeWithGeometry(_ geometry: SCNGeometry, options options: [String : AnyObject]?) -> Self     convenience init(node node: SCNNode, options options: [String : AnyObject]?)     class func shapeWithNode(_ node: SCNNode, options options: [String : AnyObject]?) -> Self     convenience init(shapes shapes: [SCNPhysicsShape], transforms transforms: [NSValue]?)     class func shapeWithShapes(_ shapes: [SCNPhysicsShape], transforms transforms: [NSValue]?) -> Self     var options: [String : AnyObject]? { get }     var sourceObject: AnyObject { get }     var transforms: [NSValue]? { get } } ``` | NSCopying, NSSecureCoding |

Modified [SCNPhysicsSliderJoint](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNPhysicsVehicle](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNPhysicsVehicleWheel](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNPhysicsVehicleWheel : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(node node: SCNNode)     class func wheelWithNode(_ node: SCNNode) -> Self     var node: SCNNode { get }     var suspensionStiffness: CGFloat     var suspensionCompression: CGFloat     var suspensionDamping: CGFloat     var maximumSuspensionTravel: CGFloat     var frictionSlip: CGFloat     var maximumSuspensionForce: CGFloat     var connectionPosition: SCNVector3     var steeringAxis: SCNVector3     var axle: SCNVector3     var radius: CGFloat     var suspensionRestLength: CGFloat } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class SCNPhysicsVehicleWheel : NSObject, NSCopying, NSSecureCoding {     convenience init(node node: SCNNode)     class func wheelWithNode(_ node: SCNNode) -> Self     var node: SCNNode { get }     var suspensionStiffness: CGFloat     var suspensionCompression: CGFloat     var suspensionDamping: CGFloat     var maximumSuspensionTravel: CGFloat     var frictionSlip: CGFloat     var maximumSuspensionForce: CGFloat     var connectionPosition: SCNVector3     var steeringAxis: SCNVector3     var axle: SCNVector3     var radius: CGFloat     var suspensionRestLength: CGFloat } ``` | NSCopying, NSSecureCoding |

Modified [SCNPhysicsWorld](https://developer.apple.com/documentation/scenekit/scnphysicsworld)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNPhysicsWorld : NSObject, NSSecureCoding, NSCoding {     var gravity: SCNVector3     var speed: CGFloat     var timeStep: NSTimeInterval     unowned(unsafe) var contactDelegate: SCNPhysicsContactDelegate?     func addBehavior(_ behavior: SCNPhysicsBehavior)     func removeBehavior(_ behavior: SCNPhysicsBehavior)     func removeAllBehaviors()     var allBehaviors: [SCNPhysicsBehavior] { get }     func rayTestWithSegmentFromPoint(_ origin: SCNVector3, toPoint dest: SCNVector3, options options: [String : AnyObject]?) -> [SCNHitTestResult]     func contactTestBetweenBody(_ bodyA: SCNPhysicsBody, andBody bodyB: SCNPhysicsBody, options options: [String : AnyObject]?) -> [SCNPhysicsContact]     func contactTestWithBody(_ body: SCNPhysicsBody, options options: [String : AnyObject]?) -> [SCNPhysicsContact]     func convexSweepTestWithShape(_ shape: SCNPhysicsShape, fromTransform from: SCNMatrix4, toTransform to: SCNMatrix4, options options: [String : AnyObject]?) -> [SCNPhysicsContact]     func updateCollisionPairs() } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class SCNPhysicsWorld : NSObject, NSSecureCoding {     var gravity: SCNVector3     var speed: CGFloat     var timeStep: NSTimeInterval     unowned(unsafe) var contactDelegate: SCNPhysicsContactDelegate?     func addBehavior(_ behavior: SCNPhysicsBehavior)     func removeBehavior(_ behavior: SCNPhysicsBehavior)     func removeAllBehaviors()     var allBehaviors: [SCNPhysicsBehavior] { get }     func rayTestWithSegmentFromPoint(_ origin: SCNVector3, toPoint dest: SCNVector3, options options: [String : AnyObject]?) -> [SCNHitTestResult]     func contactTestBetweenBody(_ bodyA: SCNPhysicsBody, andBody bodyB: SCNPhysicsBody, options options: [String : AnyObject]?) -> [SCNPhysicsContact]     func contactTestWithBody(_ body: SCNPhysicsBody, options options: [String : AnyObject]?) -> [SCNPhysicsContact]     func convexSweepTestWithShape(_ shape: SCNPhysicsShape, fromTransform from: SCNMatrix4, toTransform to: SCNMatrix4, options options: [String : AnyObject]?) -> [SCNPhysicsContact]     func updateCollisionPairs() } ``` | NSSecureCoding |

Modified [SCNPlane](https://developer.apple.com/documentation/scenekit/scnplane)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNProgram](https://developer.apple.com/documentation/scenekit/scnprogram)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNProgram : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init()     class func program() -> Self     var vertexShader: String?     var fragmentShader: String?     var vertexFunctionName: String?     var fragmentFunctionName: String?     func handleBindingOfBufferNamed(_ name: String, frequency frequency: SCNBufferFrequency, usingBlock block: SCNBufferBindingBlock)     var opaque: Bool     func setSemantic(_ semantic: String?, forSymbol symbol: String, options options: [String : AnyObject]?)     func semanticForSymbol(_ symbol: String) -> String?     unowned(unsafe) var delegate: SCNProgramDelegate?     var library: MTLLibrary? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class SCNProgram : NSObject, NSCopying, NSSecureCoding {     convenience init()     class func program() -> Self     var vertexShader: String?     var fragmentShader: String?     var vertexFunctionName: String?     var fragmentFunctionName: String?     func handleBindingOfBufferNamed(_ name: String, frequency frequency: SCNBufferFrequency, usingBlock block: SCNBufferBindingBlock)     var opaque: Bool     func setSemantic(_ semantic: String?, forSymbol symbol: String, options options: [String : AnyObject]?)     func semanticForSymbol(_ symbol: String) -> String?     unowned(unsafe) var delegate: SCNProgramDelegate?     var library: MTLLibrary? } ``` | NSCopying, NSSecureCoding |

Modified [SCNPyramid](https://developer.apple.com/documentation/scenekit/scnpyramid)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNReferenceLoadingPolicy [enum]](https://developer.apple.com/documentation/scenekit/scnreferenceloadingpolicy)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNReferenceNode](https://developer.apple.com/documentation/scenekit/scnreferencenode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNRenderer](https://developer.apple.com/documentation/scenekit/scnrenderer)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, SCNSceneRenderer, SCNTechniqueSupport |
| To | SCNSceneRenderer, SCNTechniqueSupport |

Modified [SCNRenderingAPI [enum]](https://developer.apple.com/documentation/scenekit/scnrenderingapi)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNScene](https://developer.apple.com/documentation/scenekit/scnscene)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNScene : NSObject, NSSecureCoding, NSCoding {     convenience init()     class func scene() -> Self     var rootNode: SCNNode { get }     var physicsWorld: SCNPhysicsWorld { get }     func attributeForKey(_ key: String) -> AnyObject?     func setAttribute(_ attribute: AnyObject?, forKey key: String)     var background: SCNMaterialProperty { get }     convenience init?(named name: String)     class func sceneNamed(_ name: String) -> Self?     convenience init?(named name: String, inDirectory directory: String?, options options: [String : AnyObject]?)     class func sceneNamed(_ name: String, inDirectory directory: String?, options options: [String : AnyObject]?) -> Self?     convenience init(URL url: NSURL, options options: [String : AnyObject]?) throws     class func sceneWithURL(_ url: NSURL, options options: [String : AnyObject]?) throws -> Self     var fogStartDistance: CGFloat     var fogEndDistance: CGFloat     var fogDensityExponent: CGFloat     var fogColor: AnyObject     var paused: Bool } extension SCNScene {     func addParticleSystem(_ system: SCNParticleSystem, withTransform transform: SCNMatrix4)     func removeAllParticleSystems()     func removeParticleSystem(_ system: SCNParticleSystem)     var particleSystems: [SCNParticleSystem]? { get } } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class SCNScene : NSObject, NSSecureCoding {     convenience init()     class func scene() -> Self     var rootNode: SCNNode { get }     var physicsWorld: SCNPhysicsWorld { get }     func attributeForKey(_ key: String) -> AnyObject?     func setAttribute(_ attribute: AnyObject?, forKey key: String)     var background: SCNMaterialProperty { get }     convenience init?(named name: String)     class func sceneNamed(_ name: String) -> Self?     convenience init?(named name: String, inDirectory directory: String?, options options: [String : AnyObject]?)     class func sceneNamed(_ name: String, inDirectory directory: String?, options options: [String : AnyObject]?) -> Self?     convenience init(URL url: NSURL, options options: [String : AnyObject]?) throws     class func sceneWithURL(_ url: NSURL, options options: [String : AnyObject]?) throws -> Self     var fogStartDistance: CGFloat     var fogEndDistance: CGFloat     var fogDensityExponent: CGFloat     var fogColor: AnyObject     var paused: Bool } extension SCNScene {     func addParticleSystem(_ system: SCNParticleSystem, withTransform transform: SCNMatrix4)     func removeAllParticleSystems()     func removeParticleSystem(_ system: SCNParticleSystem)     var particleSystems: [SCNParticleSystem]? { get } } ``` | NSSecureCoding |

Modified [SCNSceneSource](https://developer.apple.com/documentation/scenekit/scnscenesource)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNSceneSourceStatus [enum]](https://developer.apple.com/documentation/scenekit/scnscenesourcestatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNShadowMode [enum]](https://developer.apple.com/documentation/scenekit/scnshadowmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNShape](https://developer.apple.com/documentation/scenekit/scnshape)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNSkinner](https://developer.apple.com/documentation/scenekit/scnskinner)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNSkinner : NSObject, NSSecureCoding, NSCoding {     var skeleton: SCNNode?     convenience init(baseGeometry baseGeometry: SCNGeometry?, bones bones: [SCNNode], boneInverseBindTransforms boneInverseBindTransforms: [NSValue]?, boneWeights boneWeights: SCNGeometrySource, boneIndices boneIndices: SCNGeometrySource)     class func skinnerWithBaseGeometry(_ baseGeometry: SCNGeometry?, bones bones: [SCNNode], boneInverseBindTransforms boneInverseBindTransforms: [NSValue]?, boneWeights boneWeights: SCNGeometrySource, boneIndices boneIndices: SCNGeometrySource) -> Self     var baseGeometry: SCNGeometry?     var baseGeometryBindTransform: SCNMatrix4     var boneInverseBindTransforms: [NSValue]? { get }     var bones: [SCNNode] { get }     var boneWeights: SCNGeometrySource { get }     var boneIndices: SCNGeometrySource { get } } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class SCNSkinner : NSObject, NSSecureCoding {     var skeleton: SCNNode?     convenience init(baseGeometry baseGeometry: SCNGeometry?, bones bones: [SCNNode], boneInverseBindTransforms boneInverseBindTransforms: [NSValue]?, boneWeights boneWeights: SCNGeometrySource, boneIndices boneIndices: SCNGeometrySource)     class func skinnerWithBaseGeometry(_ baseGeometry: SCNGeometry?, bones bones: [SCNNode], boneInverseBindTransforms boneInverseBindTransforms: [NSValue]?, boneWeights boneWeights: SCNGeometrySource, boneIndices boneIndices: SCNGeometrySource) -> Self     var baseGeometry: SCNGeometry?     var baseGeometryBindTransform: SCNMatrix4     var boneInverseBindTransforms: [NSValue]? { get }     var bones: [SCNNode] { get }     var boneWeights: SCNGeometrySource { get }     var boneIndices: SCNGeometrySource { get } } ``` | NSSecureCoding |

Modified [SCNSphere](https://developer.apple.com/documentation/scenekit/scnsphere)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNTechnique](https://developer.apple.com/documentation/scenekit/scntechnique)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SCNTechnique : NSObject, SCNAnimatable, NSCopying, NSSecureCoding, NSCoding {      init?(dictionary dictionary: [String : AnyObject])     class func techniqueWithDictionary(_ dictionary: [String : AnyObject]) -> SCNTechnique?      init?(bySequencingTechniques techniques: [SCNTechnique])     class func techniqueBySequencingTechniques(_ techniques: [SCNTechnique]) -> SCNTechnique?     func handleBindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock?)     var dictionaryRepresentation: [String : AnyObject] { get }     subscript (_ key: AnyObject) -> AnyObject? { get }     func objectForKeyedSubscript(_ key: AnyObject) -> AnyObject?     func setObject(_ obj: AnyObject?, forKeyedSubscript key: NSCopying) } ``` | AnyObject, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding, SCNAnimatable |
| To | ``` class SCNTechnique : NSObject, SCNAnimatable, NSCopying, NSSecureCoding {      init?(dictionary dictionary: [String : AnyObject])     class func techniqueWithDictionary(_ dictionary: [String : AnyObject]) -> SCNTechnique?      init?(bySequencingTechniques techniques: [SCNTechnique])     class func techniqueBySequencingTechniques(_ techniques: [SCNTechnique]) -> SCNTechnique?     func handleBindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock?)     var dictionaryRepresentation: [String : AnyObject] { get }     subscript (_ key: AnyObject) -> AnyObject? { get }     func objectForKeyedSubscript(_ key: AnyObject) -> AnyObject?     func setObject(_ obj: AnyObject?, forKeyedSubscript key: NSCopying) } ``` | NSCopying, NSSecureCoding, SCNAnimatable |

Modified [SCNText](https://developer.apple.com/documentation/scenekit/scntext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNTorus](https://developer.apple.com/documentation/scenekit/scntorus)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNTransaction](https://developer.apple.com/documentation/scenekit/scntransaction)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNTransformConstraint](https://developer.apple.com/documentation/scenekit/scntransformconstraint)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNTransparencyMode [enum]](https://developer.apple.com/documentation/scenekit/scntransparencymode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SCNTube](https://developer.apple.com/documentation/scenekit/scntube)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SCNView](https://developer.apple.com/documentation/scenekit/scnview)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, SCNSceneRenderer, SCNTechniqueSupport |
| To | SCNSceneRenderer, SCNTechniqueSupport |

Modified [SCNWrapMode [enum]](https://developer.apple.com/documentation/scenekit/scnwrapmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
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
