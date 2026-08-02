---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Swift/SceneKit.html
archived_at: '2026-07-18T02:58:06.483564Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# SceneKit Changes for Swift

### SceneKit

Added [MDLAsset.init(SCNScene: SCNScene)](https://developer.apple.com/documentation/modelio/mdlasset/1419847-init)Added [MDLCamera.init(SCNCamera: SCNCamera)](https://developer.apple.com/documentation/modelio/mdlcamera/1419832-init)Added [MDLLight.init(SCNLight: SCNLight)](https://developer.apple.com/documentation/modelio/mdllight/1419830-init)Added [MDLMaterial.init(SCNMaterial: SCNMaterial)](https://developer.apple.com/documentation/modelio/mdlmaterial/1419851-materialwithscnmaterial)Added [MDLMesh.init(SCNGeometry: SCNGeometry)](https://developer.apple.com/documentation/modelio/mdlmesh/1419853-meshwithscngeometry)Added [MDLObject.init(SCNNode: SCNNode)](https://developer.apple.com/documentation/modelio/mdlobject/1419855-init)Added [MDLSubmesh.init(SCNGeometryElement: SCNGeometryElement)](https://developer.apple.com/documentation/modelio/mdlsubmesh/1419837-submeshwithscngeometryelement)Added [SCNCamera.init(MDLCamera: MDLCamera)](https://developer.apple.com/documentation/scenekit/scncamera/1419839-init)Added [SCNGeometry.init(MDLMesh: MDLMesh)](https://developer.apple.com/documentation/scenekit/scngeometry/1419845-geometrywithmdlmesh)Added [SCNGeometryElement.init(MDLSubmesh: MDLSubmesh)](https://developer.apple.com/documentation/scenekit/scngeometryelement/1419843-init)Added [SCNLight.init(MDLLight: MDLLight)](https://developer.apple.com/documentation/scenekit/scnlight/1419849-init)Added [SCNMaterial.init(MDLMaterial: MDLMaterial)](https://developer.apple.com/documentation/scenekit/scnmaterial/1419835-materialwithmdlmaterial)Added [SCNNode.init(MDLObject: MDLObject)](https://developer.apple.com/documentation/scenekit/scnnode/1419841-nodewithmdlobject)Added [SCNScene.init(MDLAsset: MDLAsset)](https://developer.apple.com/documentation/scenekit/scnscene/1419833-scenewithmdlasset)Modified [SCNCamera](https://developer.apple.com/documentation/scenekit/scncamera)

|  | Declaration |
| --- | --- |
| From | ``` class SCNCamera : NSObject, SCNAnimatable, SCNTechniqueSupport, NSCopying, NSSecureCoding {     convenience init()     class func camera() -> Self     var name: String?     var xFov: Double     var yFov: Double     var zNear: Double     var zFar: Double     var automaticallyAdjustsZRange: Bool     var usesOrthographicProjection: Bool     var orthographicScale: Double     func projectionTransform() -> SCNMatrix4     func setProjectionTransform(_ projectionTransform: SCNMatrix4)     var focalDistance: CGFloat     var focalSize: CGFloat     var focalBlurRadius: CGFloat     var aperture: CGFloat     var categoryBitMask: Int } ``` |
| To | ``` class SCNCamera : NSObject, SCNAnimatable, SCNTechniqueSupport, NSCopying, NSSecureCoding {     convenience init()     class func camera() -> Self     var name: String?     var xFov: Double     var yFov: Double     var zNear: Double     var zFar: Double     var automaticallyAdjustsZRange: Bool     var usesOrthographicProjection: Bool     var orthographicScale: Double     func projectionTransform() -> SCNMatrix4     func setProjectionTransform(_ projectionTransform: SCNMatrix4)     var focalDistance: CGFloat     var focalSize: CGFloat     var focalBlurRadius: CGFloat     var aperture: CGFloat     var categoryBitMask: Int } extension SCNCamera {     convenience init(MDLCamera mdlCamera: MDLCamera)     class func cameraWithMDLCamera(_ mdlCamera: MDLCamera) -> Self } ``` |

Modified [SCNGeometry](https://developer.apple.com/documentation/scenekit/scngeometry)

|  | Declaration |
| --- | --- |
| From | ``` class SCNGeometry : NSObject, SCNAnimatable, SCNBoundingVolume, SCNShadable, NSCopying, NSSecureCoding {     convenience init()     class func geometry() -> Self     var name: String?     var materials: [SCNMaterial]     var firstMaterial: SCNMaterial?     func insertMaterial(_ material: SCNMaterial, atIndex index: Int)     func removeMaterialAtIndex(_ index: Int)     func replaceMaterialAtIndex(_ index: Int, withMaterial material: SCNMaterial)     func materialWithName(_ name: String) -> SCNMaterial?     convenience init(sources sources: [SCNGeometrySource], elements elements: [SCNGeometryElement])     class func geometryWithSources(_ sources: [SCNGeometrySource], elements elements: [SCNGeometryElement]) -> Self     var geometrySources: [SCNGeometrySource] { get }     func geometrySourcesForSemantic(_ semantic: String) -> [SCNGeometrySource]     var geometryElements: [SCNGeometryElement] { get }     var geometryElementCount: Int { get }     func geometryElementAtIndex(_ elementIndex: Int) -> SCNGeometryElement     var levelsOfDetail: [SCNLevelOfDetail]?     var subdivisionLevel: Int     var edgeCreasesElement: SCNGeometryElement?     var edgeCreasesSource: SCNGeometrySource? } ``` |
| To | ``` class SCNGeometry : NSObject, SCNAnimatable, SCNBoundingVolume, SCNShadable, NSCopying, NSSecureCoding {     convenience init()     class func geometry() -> Self     var name: String?     var materials: [SCNMaterial]     var firstMaterial: SCNMaterial?     func insertMaterial(_ material: SCNMaterial, atIndex index: Int)     func removeMaterialAtIndex(_ index: Int)     func replaceMaterialAtIndex(_ index: Int, withMaterial material: SCNMaterial)     func materialWithName(_ name: String) -> SCNMaterial?     convenience init(sources sources: [SCNGeometrySource], elements elements: [SCNGeometryElement])     class func geometryWithSources(_ sources: [SCNGeometrySource], elements elements: [SCNGeometryElement]) -> Self     var geometrySources: [SCNGeometrySource] { get }     func geometrySourcesForSemantic(_ semantic: String) -> [SCNGeometrySource]     var geometryElements: [SCNGeometryElement] { get }     var geometryElementCount: Int { get }     func geometryElementAtIndex(_ elementIndex: Int) -> SCNGeometryElement     var levelsOfDetail: [SCNLevelOfDetail]?     var subdivisionLevel: Int     var edgeCreasesElement: SCNGeometryElement?     var edgeCreasesSource: SCNGeometrySource? } extension SCNGeometry {     convenience init(MDLMesh mdlMesh: MDLMesh)     class func geometryWithMDLMesh(_ mdlMesh: MDLMesh) -> Self } ``` |

Modified [SCNGeometryElement](https://developer.apple.com/documentation/scenekit/scngeometryelement)

|  | Declaration |
| --- | --- |
| From | ``` class SCNGeometryElement : NSObject, NSSecureCoding {     convenience init(data data: NSData?, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int)     class func geometryElementWithData(_ data: NSData?, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int) -> Self     var data: NSData { get }     var primitiveType: SCNGeometryPrimitiveType { get }     var primitiveCount: Int { get }     var bytesPerIndex: Int { get } } extension SCNGeometryElement {     convenience init<IndexType : IntegerType>(indices indices: [IndexType], primitiveType primitiveType: SCNGeometryPrimitiveType) } extension SCNGeometryElement {     convenience init<IndexType : IntegerType>(indices indices: [IndexType], primitiveType primitiveType: SCNGeometryPrimitiveType) } ``` |
| To | ``` class SCNGeometryElement : NSObject, NSSecureCoding {     convenience init(data data: NSData?, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int)     class func geometryElementWithData(_ data: NSData?, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int) -> Self     var data: NSData { get }     var primitiveType: SCNGeometryPrimitiveType { get }     var primitiveCount: Int { get }     var bytesPerIndex: Int { get } } extension SCNGeometryElement {     convenience init(MDLSubmesh mdlSubMesh: MDLSubmesh)     class func geometryElementWithMDLSubmesh(_ mdlSubMesh: MDLSubmesh) -> Self } extension SCNGeometryElement {     convenience init<IndexType : IntegerType>(indices indices: [IndexType], primitiveType primitiveType: SCNGeometryPrimitiveType) } extension SCNGeometryElement {     convenience init<IndexType : IntegerType>(indices indices: [IndexType], primitiveType primitiveType: SCNGeometryPrimitiveType) } ``` |

Modified [SCNLight](https://developer.apple.com/documentation/scenekit/scnlight)

|  | Declaration |
| --- | --- |
| From | ``` class SCNLight : NSObject, SCNAnimatable, SCNTechniqueSupport, NSCopying, NSSecureCoding {     convenience init()     class func light() -> Self     var type: String     var color: AnyObject     var name: String?     var castsShadow: Bool     var shadowColor: AnyObject     var shadowRadius: CGFloat     var shadowMapSize: CGSize     var shadowSampleCount: Int     var shadowMode: SCNShadowMode     var shadowBias: CGFloat     var orthographicScale: CGFloat     var zNear: CGFloat     var zFar: CGFloat     var attenuationStartDistance: CGFloat     var attenuationEndDistance: CGFloat     var attenuationFalloffExponent: CGFloat     var spotInnerAngle: CGFloat     var spotOuterAngle: CGFloat     var gobo: SCNMaterialProperty? { get }     var categoryBitMask: Int } ``` |
| To | ``` class SCNLight : NSObject, SCNAnimatable, SCNTechniqueSupport, NSCopying, NSSecureCoding {     convenience init()     class func light() -> Self     var type: String     var color: AnyObject     var name: String?     var castsShadow: Bool     var shadowColor: AnyObject     var shadowRadius: CGFloat     var shadowMapSize: CGSize     var shadowSampleCount: Int     var shadowMode: SCNShadowMode     var shadowBias: CGFloat     var orthographicScale: CGFloat     var zNear: CGFloat     var zFar: CGFloat     var attenuationStartDistance: CGFloat     var attenuationEndDistance: CGFloat     var attenuationFalloffExponent: CGFloat     var spotInnerAngle: CGFloat     var spotOuterAngle: CGFloat     var gobo: SCNMaterialProperty? { get }     var categoryBitMask: Int } extension SCNLight {     convenience init(MDLLight mdlLight: MDLLight)     class func lightWithMDLLight(_ mdlLight: MDLLight) -> Self } ``` |

Modified [SCNMaterial](https://developer.apple.com/documentation/scenekit/scnmaterial)

|  | Declaration |
| --- | --- |
| From | ``` class SCNMaterial : NSObject, SCNAnimatable, SCNShadable, NSCopying, NSSecureCoding {     convenience init()     class func material() -> Self     var name: String?     var diffuse: SCNMaterialProperty { get }     var ambient: SCNMaterialProperty { get }     var specular: SCNMaterialProperty { get }     var emission: SCNMaterialProperty { get }     var transparent: SCNMaterialProperty { get }     var reflective: SCNMaterialProperty { get }     var multiply: SCNMaterialProperty { get }     var normal: SCNMaterialProperty { get }     var ambientOcclusion: SCNMaterialProperty { get }     var selfIllumination: SCNMaterialProperty { get }     var shininess: CGFloat     var transparency: CGFloat     var lightingModelName: String     var litPerPixel: Bool     var doubleSided: Bool     var cullMode: SCNCullMode     var transparencyMode: SCNTransparencyMode     var locksAmbientWithDiffuse: Bool     var writesToDepthBuffer: Bool     var readsFromDepthBuffer: Bool     var fresnelExponent: CGFloat     var blendMode: SCNBlendMode } ``` |
| To | ``` class SCNMaterial : NSObject, SCNAnimatable, SCNShadable, NSCopying, NSSecureCoding {     convenience init()     class func material() -> Self     var name: String?     var diffuse: SCNMaterialProperty { get }     var ambient: SCNMaterialProperty { get }     var specular: SCNMaterialProperty { get }     var emission: SCNMaterialProperty { get }     var transparent: SCNMaterialProperty { get }     var reflective: SCNMaterialProperty { get }     var multiply: SCNMaterialProperty { get }     var normal: SCNMaterialProperty { get }     var ambientOcclusion: SCNMaterialProperty { get }     var selfIllumination: SCNMaterialProperty { get }     var shininess: CGFloat     var transparency: CGFloat     var lightingModelName: String     var litPerPixel: Bool     var doubleSided: Bool     var cullMode: SCNCullMode     var transparencyMode: SCNTransparencyMode     var locksAmbientWithDiffuse: Bool     var writesToDepthBuffer: Bool     var readsFromDepthBuffer: Bool     var fresnelExponent: CGFloat     var blendMode: SCNBlendMode } extension SCNMaterial {     convenience init(MDLMaterial mdlMaterial: MDLMaterial)     class func materialWithMDLMaterial(_ mdlMaterial: MDLMaterial) -> Self } ``` |

Modified [SCNNode](https://developer.apple.com/documentation/scenekit/scnnode)

|  | Declaration |
| --- | --- |
| From | ``` class SCNNode : NSObject, NSCopying, NSSecureCoding, SCNAnimatable, SCNActionable, SCNBoundingVolume {     convenience init()     class func node() -> Self      init(geometry geometry: SCNGeometry?)     class func nodeWithGeometry(_ geometry: SCNGeometry?) -> SCNNode     func clone() -> Self     func flattenedClone() -> Self     var name: String?     var light: SCNLight?     var camera: SCNCamera?     var geometry: SCNGeometry?     var skinner: SCNSkinner?     var morpher: SCNMorpher?     var transform: SCNMatrix4     var position: SCNVector3     var rotation: SCNVector4     var orientation: SCNQuaternion     var eulerAngles: SCNVector3     var scale: SCNVector3     var pivot: SCNMatrix4     var worldTransform: SCNMatrix4 { get }     var hidden: Bool     var opacity: CGFloat     var renderingOrder: Int     var castsShadow: Bool     var parentNode: SCNNode? { get }     var childNodes: [SCNNode] { get }     func addChildNode(_ child: SCNNode)     func insertChildNode(_ child: SCNNode, atIndex index: Int)     func removeFromParentNode()     func replaceChildNode(_ oldChild: SCNNode, with newChild: SCNNode)     func childNodeWithName(_ name: String, recursively recursively: Bool) -> SCNNode?     func childNodesPassingTest(_ predicate: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]     func enumerateChildNodesUsingBlock(_ block: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)     func convertPosition(_ position: SCNVector3, toNode node: SCNNode?) -> SCNVector3     func convertPosition(_ position: SCNVector3, fromNode node: SCNNode?) -> SCNVector3     func convertTransform(_ transform: SCNMatrix4, toNode node: SCNNode?) -> SCNMatrix4     func convertTransform(_ transform: SCNMatrix4, fromNode node: SCNNode?) -> SCNMatrix4     var physicsBody: SCNPhysicsBody?     var physicsField: SCNPhysicsField?     var constraints: [SCNConstraint]?     var filters: [CIFilter]?     var presentationNode: SCNNode { get }     var paused: Bool     unowned(unsafe) var rendererDelegate: SCNNodeRendererDelegate?     func hitTestWithSegmentFromPoint(_ pointA: SCNVector3, toPoint pointB: SCNVector3, options options: [String : AnyObject]?) -> [SCNHitTestResult]     var categoryBitMask: Int } extension SCNNode {     func addAudioPlayer(_ player: SCNAudioPlayer)     func removeAllAudioPlayers()     func removeAudioPlayer(_ player: SCNAudioPlayer)     var audioPlayers: [SCNAudioPlayer] { get } } extension SCNNode {     func addParticleSystem(_ system: SCNParticleSystem)     func removeAllParticleSystems()     func removeParticleSystem(_ system: SCNParticleSystem)     var particleSystems: [SCNParticleSystem]? { get } } ``` |
| To | ``` class SCNNode : NSObject, NSCopying, NSSecureCoding, SCNAnimatable, SCNActionable, SCNBoundingVolume {     convenience init()     class func node() -> Self      init(geometry geometry: SCNGeometry?)     class func nodeWithGeometry(_ geometry: SCNGeometry?) -> SCNNode     func clone() -> Self     func flattenedClone() -> Self     var name: String?     var light: SCNLight?     var camera: SCNCamera?     var geometry: SCNGeometry?     var skinner: SCNSkinner?     var morpher: SCNMorpher?     var transform: SCNMatrix4     var position: SCNVector3     var rotation: SCNVector4     var orientation: SCNQuaternion     var eulerAngles: SCNVector3     var scale: SCNVector3     var pivot: SCNMatrix4     var worldTransform: SCNMatrix4 { get }     var hidden: Bool     var opacity: CGFloat     var renderingOrder: Int     var castsShadow: Bool     var parentNode: SCNNode? { get }     var childNodes: [SCNNode] { get }     func addChildNode(_ child: SCNNode)     func insertChildNode(_ child: SCNNode, atIndex index: Int)     func removeFromParentNode()     func replaceChildNode(_ oldChild: SCNNode, with newChild: SCNNode)     func childNodeWithName(_ name: String, recursively recursively: Bool) -> SCNNode?     func childNodesPassingTest(_ predicate: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]     func enumerateChildNodesUsingBlock(_ block: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)     func convertPosition(_ position: SCNVector3, toNode node: SCNNode?) -> SCNVector3     func convertPosition(_ position: SCNVector3, fromNode node: SCNNode?) -> SCNVector3     func convertTransform(_ transform: SCNMatrix4, toNode node: SCNNode?) -> SCNMatrix4     func convertTransform(_ transform: SCNMatrix4, fromNode node: SCNNode?) -> SCNMatrix4     var physicsBody: SCNPhysicsBody?     var physicsField: SCNPhysicsField?     var constraints: [SCNConstraint]?     var filters: [CIFilter]?     var presentationNode: SCNNode { get }     var paused: Bool     unowned(unsafe) var rendererDelegate: SCNNodeRendererDelegate?     func hitTestWithSegmentFromPoint(_ pointA: SCNVector3, toPoint pointB: SCNVector3, options options: [String : AnyObject]?) -> [SCNHitTestResult]     var categoryBitMask: Int } extension SCNNode {     convenience init(MDLObject mdlObject: MDLObject)     class func nodeWithMDLObject(_ mdlObject: MDLObject) -> Self } extension SCNNode {     func addAudioPlayer(_ player: SCNAudioPlayer)     func removeAllAudioPlayers()     func removeAudioPlayer(_ player: SCNAudioPlayer)     var audioPlayers: [SCNAudioPlayer] { get } } extension SCNNode {     func addParticleSystem(_ system: SCNParticleSystem)     func removeAllParticleSystems()     func removeParticleSystem(_ system: SCNParticleSystem)     var particleSystems: [SCNParticleSystem]? { get } } ``` |

Modified [SCNScene](https://developer.apple.com/documentation/scenekit/scnscene)

|  | Declaration |
| --- | --- |
| From | ``` class SCNScene : NSObject, NSSecureCoding {     convenience init()     class func scene() -> Self     var rootNode: SCNNode { get }     var physicsWorld: SCNPhysicsWorld { get }     func attributeForKey(_ key: String) -> AnyObject?     func setAttribute(_ attribute: AnyObject?, forKey key: String)     var background: SCNMaterialProperty { get }     convenience init?(named name: String)     class func sceneNamed(_ name: String) -> Self?     convenience init?(named name: String, inDirectory directory: String?, options options: [String : AnyObject]?)     class func sceneNamed(_ name: String, inDirectory directory: String?, options options: [String : AnyObject]?) -> Self?     convenience init(URL url: NSURL, options options: [String : AnyObject]?) throws     class func sceneWithURL(_ url: NSURL, options options: [String : AnyObject]?) throws -> Self     var fogStartDistance: CGFloat     var fogEndDistance: CGFloat     var fogDensityExponent: CGFloat     var fogColor: AnyObject     var paused: Bool } extension SCNScene {     func addParticleSystem(_ system: SCNParticleSystem, withTransform transform: SCNMatrix4)     func removeAllParticleSystems()     func removeParticleSystem(_ system: SCNParticleSystem)     var particleSystems: [SCNParticleSystem]? { get } } ``` |
| To | ``` class SCNScene : NSObject, NSSecureCoding {     convenience init()     class func scene() -> Self     var rootNode: SCNNode { get }     var physicsWorld: SCNPhysicsWorld { get }     func attributeForKey(_ key: String) -> AnyObject?     func setAttribute(_ attribute: AnyObject?, forKey key: String)     var background: SCNMaterialProperty { get }     convenience init?(named name: String)     class func sceneNamed(_ name: String) -> Self?     convenience init?(named name: String, inDirectory directory: String?, options options: [String : AnyObject]?)     class func sceneNamed(_ name: String, inDirectory directory: String?, options options: [String : AnyObject]?) -> Self?     convenience init(URL url: NSURL, options options: [String : AnyObject]?) throws     class func sceneWithURL(_ url: NSURL, options options: [String : AnyObject]?) throws -> Self     var fogStartDistance: CGFloat     var fogEndDistance: CGFloat     var fogDensityExponent: CGFloat     var fogColor: AnyObject     var paused: Bool } extension SCNScene {     convenience init(MDLAsset mdlAsset: MDLAsset)     class func sceneWithMDLAsset(_ mdlAsset: MDLAsset) -> Self } extension SCNScene {     func addParticleSystem(_ system: SCNParticleSystem, withTransform transform: SCNMatrix4)     func removeAllParticleSystems()     func removeParticleSystem(_ system: SCNParticleSystem)     var particleSystems: [SCNParticleSystem]? { get } } ``` |

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
