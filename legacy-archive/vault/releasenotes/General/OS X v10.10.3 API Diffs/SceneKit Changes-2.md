---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/SceneKit.html
archived_at: '2026-07-18T02:52:38.416586Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# SceneKit Changes

## SceneKit

Removed SCNPhysicsCollisionCategory.valueAdded CAAnimation.animationEventsAdded CAAnimation.fadeInDurationAdded CAAnimation.fadeOutDurationAdded CAAnimation.usesSceneTimeBaseAdded NSValue.init(SCNMatrix4: SCNMatrix4)Added NSValue.SCNMatrix4ValueAdded NSValue.init(SCNVector3: SCNVector3)Added NSValue.SCNVector3ValueAdded NSValue.init(SCNVector4: SCNVector4)Added NSValue.SCNVector4ValueAdded SCNPhysicsCollisionCategory.init(rawValue: UInt)Added SCNProgram.geometryShaderAdded SCNProgram.tessellationControlShaderAdded SCNProgram.tessellationEvaluationShaderAdded SCNSceneRenderer.overlaySKSceneAdded SCNVector3.init()Added SCNVector3.init(x: CGFloat, y: CGFloat, z: CGFloat)Added SCNVector4.init()Added SCNVector4.init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)Added SCNMatrix4FromGLKMatrix4(GLKMatrix4) -> SCNMatrix4Added SCNMatrix4ToGLKMatrix4(SCNMatrix4) -> GLKMatrix4Added SCNVector3FromGLKVector3(GLKVector3) -> SCNVector3Added SCNVector3ToGLKVector3(SCNVector3) -> GLKVector3Added SCNVector4FromGLKVector4(GLKVector4) -> SCNVector4Added SCNVector4ToGLKVector4(SCNVector4) -> GLKVector4Modified SCNAction.customActionWithDuration(NSTimeInterval, actionBlock:(SCNNode!, CGFloat) -> Void) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: ((SCNNode!, CGFloat) -> Void)!) -> SCNAction! ``` |
| To | ``` class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SCNNode!, CGFloat) -> Void) -> SCNAction ``` |

Modified SCNAction.fadeInWithDuration(NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fadeInWithDuration(_ sec: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func fadeInWithDuration(_ sec: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.fadeOpacityBy(CGFloat, duration: NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fadeOpacityBy(_ factor: CGFloat, duration sec: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func fadeOpacityBy(_ factor: CGFloat, duration sec: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.fadeOpacityTo(CGFloat, duration: NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fadeOpacityTo(_ opacity: CGFloat, duration sec: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func fadeOpacityTo(_ opacity: CGFloat, duration sec: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.fadeOutWithDuration(NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fadeOutWithDuration(_ sec: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func fadeOutWithDuration(_ sec: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.group([AnyObject]) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func group(_ actions: [AnyObject]!) -> SCNAction! ``` |
| To | ``` class func group(_ actions: [AnyObject]) -> SCNAction ``` |

Modified SCNAction.javaScriptActionWithScript(String, duration: NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func javaScriptActionWithScript(_ script: String!, duration seconds: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func javaScriptActionWithScript(_ script: String, duration seconds: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.moveBy(SCNVector3, duration: NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func moveBy(_ delta: SCNVector3, duration duration: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func moveBy(_ delta: SCNVector3, duration duration: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.moveByX(CGFloat, y: CGFloat, z: CGFloat, duration: NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func moveByX(_ deltaX: CGFloat, y deltaY: CGFloat, z deltaZ: CGFloat, duration duration: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func moveByX(_ deltaX: CGFloat, y deltaY: CGFloat, z deltaZ: CGFloat, duration duration: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.moveTo(SCNVector3, duration: NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func moveTo(_ location: SCNVector3, duration duration: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func moveTo(_ location: SCNVector3, duration duration: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.removeFromParentNode() -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func removeFromParentNode() -> SCNAction! ``` |
| To | ``` class func removeFromParentNode() -> SCNAction ``` |

Modified SCNAction.repeatAction(SCNAction, count: Int) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func repeatAction(_ action: SCNAction!, count count: Int) -> SCNAction! ``` |
| To | ``` class func repeatAction(_ action: SCNAction, count count: Int) -> SCNAction ``` |

Modified SCNAction.repeatActionForever(SCNAction) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func repeatActionForever(_ action: SCNAction!) -> SCNAction! ``` |
| To | ``` class func repeatActionForever(_ action: SCNAction) -> SCNAction ``` |

Modified SCNAction.reversedAction() -> SCNAction

|  | Declaration |
| --- | --- |
| From | ``` func reversedAction() -> SCNAction! ``` |
| To | ``` func reversedAction() -> SCNAction ``` |

Modified SCNAction.rotateByAngle(CGFloat, aroundAxis: SCNVector3, duration: NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func rotateByAngle(_ angle: CGFloat, aroundAxis axis: SCNVector3, duration duration: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func rotateByAngle(_ angle: CGFloat, aroundAxis axis: SCNVector3, duration duration: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.rotateByX(CGFloat, y: CGFloat, z: CGFloat, duration: NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func rotateByX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func rotateByX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.rotateToAxisAngle(SCNVector4, duration: NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func rotateToAxisAngle(_ axisAngle: SCNVector4, duration duration: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func rotateToAxisAngle(_ axisAngle: SCNVector4, duration duration: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.rotateToX(CGFloat, y: CGFloat, z: CGFloat, duration: NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func rotateToX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func rotateToX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.rotateToX(CGFloat, y: CGFloat, z: CGFloat, duration: NSTimeInterval, shortestUnitArc: Bool) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func rotateToX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SCNAction! ``` |
| To | ``` class func rotateToX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SCNAction ``` |

Modified SCNAction.runBlock((SCNNode!) -> Void) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func runBlock(_ block: ((SCNNode!) -> Void)!) -> SCNAction! ``` |
| To | ``` class func runBlock(_ block: (SCNNode!) -> Void) -> SCNAction ``` |

Modified SCNAction.runBlock((SCNNode!) -> Void, queue: dispatch_queue_t?) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func runBlock(_ block: ((SCNNode!) -> Void)!, queue queue: dispatch_queue_t!) -> SCNAction! ``` |
| To | ``` class func runBlock(_ block: (SCNNode!) -> Void, queue queue: dispatch_queue_t?) -> SCNAction ``` |

Modified SCNAction.scaleBy(CGFloat, duration: NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func scaleBy(_ scale: CGFloat, duration sec: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func scaleBy(_ scale: CGFloat, duration sec: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.scaleTo(CGFloat, duration: NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func scaleTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func scaleTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.sequence([AnyObject]) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func sequence(_ actions: [AnyObject]!) -> SCNAction! ``` |
| To | ``` class func sequence(_ actions: [AnyObject]) -> SCNAction ``` |

Modified SCNAction.timingFunction

|  | Declaration |
| --- | --- |
| From | ``` var timingFunction: SCNActionTimingFunction! ``` |
| To | ``` var timingFunction: SCNActionTimingFunction? ``` |

Modified SCNAction.waitForDuration(NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func waitForDuration(_ sec: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func waitForDuration(_ sec: NSTimeInterval) -> SCNAction ``` |

Modified SCNAction.waitForDuration(NSTimeInterval, withRange: NSTimeInterval) -> SCNAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func waitForDuration(_ sec: NSTimeInterval, withRange durationRange: NSTimeInterval) -> SCNAction! ``` |
| To | ``` class func waitForDuration(_ sec: NSTimeInterval, withRange durationRange: NSTimeInterval) -> SCNAction ``` |

Modified SCNActionable.actionForKey(String) -> SCNAction?

|  | Declaration |
| --- | --- |
| From | ``` func actionForKey(_ key: String!) -> SCNAction! ``` |
| To | ``` func actionForKey(_ key: String) -> SCNAction? ``` |

Modified SCNActionable.removeActionForKey(String)

|  | Declaration |
| --- | --- |
| From | ``` func removeActionForKey(_ key: String!) ``` |
| To | ``` func removeActionForKey(_ key: String) ``` |

Modified SCNActionable.runAction(SCNAction)

|  | Declaration |
| --- | --- |
| From | ``` func runAction(_ action: SCNAction!) ``` |
| To | ``` func runAction(_ action: SCNAction) ``` |

Modified SCNActionable.runAction(SCNAction, completionHandler:(() -> Void)?)

|  | Declaration |
| --- | --- |
| From | ``` func runAction(_ action: SCNAction!, completionHandler block: (() -> Void)!) ``` |
| To | ``` func runAction(_ action: SCNAction, completionHandler block: (() -> Void)?) ``` |

Modified SCNActionable.runAction(SCNAction, forKey: String?)

|  | Declaration |
| --- | --- |
| From | ``` func runAction(_ action: SCNAction!, forKey key: String!) ``` |
| To | ``` func runAction(_ action: SCNAction, forKey key: String?) ``` |

Modified SCNActionable.runAction(SCNAction, forKey: String?, completionHandler:(() -> Void)?)

|  | Declaration |
| --- | --- |
| From | ``` func runAction(_ action: SCNAction!, forKey key: String!, completionHandler block: (() -> Void)!) ``` |
| To | ``` func runAction(_ action: SCNAction, forKey key: String?, completionHandler block: (() -> Void)?) ``` |

Modified SCNAnimatable.addAnimation(CAAnimation, forKey: String?)

|  | Declaration |
| --- | --- |
| From | ``` func addAnimation(_ animation: CAAnimation!, forKey key: String!) ``` |
| To | ``` func addAnimation(_ animation: CAAnimation, forKey key: String?) ``` |

Modified SCNAnimatable.animationForKey(String) -> CAAnimation?

|  | Declaration |
| --- | --- |
| From | ``` func animationForKey(_ key: String!) -> CAAnimation! ``` |
| To | ``` func animationForKey(_ key: String) -> CAAnimation? ``` |

Modified SCNAnimatable.animationKeys() -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func animationKeys() -> [AnyObject]! ``` |
| To | ``` func animationKeys() -> [AnyObject]? ``` |

Modified SCNAnimatable.isAnimationForKeyPaused(String) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isAnimationForKeyPaused(_ key: String!) -> Bool ``` | OS X 10.10 |
| To | ``` func isAnimationForKeyPaused(_ key: String) -> Bool ``` | OS X 10.9 |

Modified SCNAnimatable.pauseAnimationForKey(String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func pauseAnimationForKey(_ key: String!) ``` | OS X 10.10 |
| To | ``` func pauseAnimationForKey(_ key: String) ``` | OS X 10.9 |

Modified SCNAnimatable.removeAnimationForKey(String)

|  | Declaration |
| --- | --- |
| From | ``` func removeAnimationForKey(_ key: String!) ``` |
| To | ``` func removeAnimationForKey(_ key: String) ``` |

Modified SCNAnimatable.removeAnimationForKey(String, fadeOutDuration: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` func removeAnimationForKey(_ key: String!, fadeOutDuration duration: CGFloat) ``` |
| To | ``` func removeAnimationForKey(_ key: String, fadeOutDuration duration: CGFloat) ``` |

Modified SCNAnimatable.resumeAnimationForKey(String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func resumeAnimationForKey(_ key: String!) ``` | OS X 10.10 |
| To | ``` func resumeAnimationForKey(_ key: String) ``` | OS X 10.9 |

Modified SCNAnimationEvent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNBoundingVolume.getBoundingBoxMin(UnsafeMutablePointer<SCNVector3>, max: UnsafeMutablePointer<SCNVector3>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getBoundingBoxMin(_ min: UnsafePointer<SCNVector3>, max max: UnsafePointer<SCNVector3>) -> Bool ``` |
| To | ``` func getBoundingBoxMin(_ min: UnsafeMutablePointer<SCNVector3>, max max: UnsafeMutablePointer<SCNVector3>) -> Bool ``` |

Modified SCNBoundingVolume.getBoundingSphereCenter(UnsafeMutablePointer<SCNVector3>, radius: UnsafeMutablePointer<CGFloat>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getBoundingSphereCenter(_ center: UnsafePointer<SCNVector3>, radius radius: UnsafePointer<CGFloat>) -> Bool ``` |
| To | ``` func getBoundingSphereCenter(_ center: UnsafeMutablePointer<SCNVector3>, radius radius: UnsafeMutablePointer<CGFloat>) -> Bool ``` |

Modified SCNBoundingVolume.setBoundingBoxMin(UnsafeMutablePointer<SCNVector3>, max: UnsafeMutablePointer<SCNVector3>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setBoundingBoxMin(_ min: UnsafePointer<SCNVector3>, max max: UnsafePointer<SCNVector3>) ``` | OS X 10.10 |
| To | ``` func setBoundingBoxMin(_ min: UnsafeMutablePointer<SCNVector3>, max max: UnsafeMutablePointer<SCNVector3>) ``` | OS X 10.9 |

Modified SCNBox

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNCamera

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNCamera.aperture

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNCamera.automaticallyAdjustsZRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNCamera.focalBlurRadius

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNCamera.focalDistance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNCamera.focalSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNCamera.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified SCNCamera.orthographicScale

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNCamera.setProjectionTransform(SCNMatrix4)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNCapsule

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNChamferMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNCone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNConstraint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNCylinder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNFilterMode.FilterModeLinear

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNFilterMode.FilterModeNearest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNFilterMode.FilterModeNone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNFloor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNGeometry

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNGeometry.edgeCreasesElement

|  | Declaration |
| --- | --- |
| From | ``` var edgeCreasesElement: SCNGeometryElement! ``` |
| To | ``` var edgeCreasesElement: SCNGeometryElement? ``` |

Modified SCNGeometry.edgeCreasesSource

|  | Declaration |
| --- | --- |
| From | ``` var edgeCreasesSource: SCNGeometrySource! ``` |
| To | ``` var edgeCreasesSource: SCNGeometrySource? ``` |

Modified SCNGeometry.firstMaterial

|  | Declaration |
| --- | --- |
| From | ``` var firstMaterial: SCNMaterial! ``` |
| To | ``` var firstMaterial: SCNMaterial? ``` |

Modified SCNGeometry.geometryElementAtIndex(Int) -> SCNGeometryElement?

|  | Declaration |
| --- | --- |
| From | ``` func geometryElementAtIndex(_ elementIndex: Int) -> SCNGeometryElement! ``` |
| To | ``` func geometryElementAtIndex(_ elementIndex: Int) -> SCNGeometryElement? ``` |

Modified SCNGeometry.geometrySourcesForSemantic(String) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func geometrySourcesForSemantic(_ semantic: String!) -> [AnyObject]! ``` |
| To | ``` func geometrySourcesForSemantic(_ semantic: String) -> [AnyObject]? ``` |

Modified SCNGeometry.insertMaterial(SCNMaterial, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertMaterial(_ material: SCNMaterial!, atIndex index: Int) ``` |
| To | ``` func insertMaterial(_ material: SCNMaterial, atIndex index: Int) ``` |

Modified SCNGeometry.levelsOfDetail

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var levelsOfDetail: [AnyObject]! ``` | OS X 10.10 |
| To | ``` var levelsOfDetail: [AnyObject]? ``` | OS X 10.9 |

Modified SCNGeometry.materialWithName(String) -> SCNMaterial?

|  | Declaration |
| --- | --- |
| From | ``` func materialWithName(_ name: String!) -> SCNMaterial! ``` |
| To | ``` func materialWithName(_ name: String) -> SCNMaterial? ``` |

Modified SCNGeometry.materials

|  | Declaration |
| --- | --- |
| From | ``` var materials: [AnyObject]! ``` |
| To | ``` var materials: [AnyObject]? ``` |

Modified SCNGeometry.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified SCNGeometry.replaceMaterialAtIndex(Int, withMaterial: SCNMaterial)

|  | Declaration |
| --- | --- |
| From | ``` func replaceMaterialAtIndex(_ index: Int, withMaterial material: SCNMaterial!) ``` |
| To | ``` func replaceMaterialAtIndex(_ index: Int, withMaterial material: SCNMaterial) ``` |

Modified SCNGeometry.init(sources: [AnyObject], elements:[AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(sources sources: [AnyObject]!, elements elements: [AnyObject]!) ``` |
| To | ``` convenience init(sources sources: [AnyObject], elements elements: [AnyObject]?) ``` |

Modified SCNGeometryElement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNGeometryElement.data

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` var data: NSData? { get } ``` |

Modified SCNGeometryElement.init(data: NSData, primitiveType: SCNGeometryPrimitiveType, primitiveCount: Int, bytesPerIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data data: NSData!, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int) ``` |
| To | ``` convenience init(data data: NSData, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int) ``` |

Modified SCNGeometrySource

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNGeometrySource.data

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` var data: NSData? { get } ``` |

Modified SCNGeometrySource.init(data: NSData, semantic: String, vectorCount: Int, floatComponents: Bool, componentsPerVector: Int, bytesPerComponent: Int, dataOffset: Int, dataStride: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data data: NSData!, semantic semantic: String!, vectorCount vectorCount: Int, floatComponents floatComponents: Bool, componentsPerVector componentsPerVector: Int, bytesPerComponent bytesPerComponent: Int, dataOffset offset: Int, dataStride stride: Int) ``` |
| To | ``` convenience init(data data: NSData, semantic semantic: String, vectorCount vectorCount: Int, floatComponents floatComponents: Bool, componentsPerVector componentsPerVector: Int, bytesPerComponent bytesPerComponent: Int, dataOffset offset: Int, dataStride stride: Int) ``` |

Modified SCNGeometrySource.init(normals: UnsafePointer<SCNVector3>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(normals normals: ConstUnsafePointer<SCNVector3>, count count: Int) ``` |
| To | ``` convenience init(normals normals: UnsafePointer<SCNVector3>, count count: Int) ``` |

Modified SCNGeometrySource.semantic

|  | Declaration |
| --- | --- |
| From | ``` var semantic: String! { get } ``` |
| To | ``` var semantic: String { get } ``` |

Modified SCNGeometrySource.init(textureCoordinates: UnsafePointer<CGPoint>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(textureCoordinates texcoord: ConstUnsafePointer<CGPoint>, count count: Int) ``` |
| To | ``` convenience init(textureCoordinates texcoord: UnsafePointer<CGPoint>, count count: Int) ``` |

Modified SCNGeometrySource.init(vertices: UnsafePointer<SCNVector3>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(vertices vertices: ConstUnsafePointer<SCNVector3>, count count: Int) ``` |
| To | ``` convenience init(vertices vertices: UnsafePointer<SCNVector3>, count count: Int) ``` |

Modified SCNHitTestResult

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNHitTestResult.node

|  | Declaration |
| --- | --- |
| From | ``` var node: SCNNode! { get } ``` |
| To | ``` var node: SCNNode { get } ``` |

Modified SCNIKConstraint.chainRootNode

|  | Declaration |
| --- | --- |
| From | ``` var chainRootNode: SCNNode! { get } ``` |
| To | ``` var chainRootNode: SCNNode { get } ``` |

Modified SCNIKConstraint.inverseKinematicsConstraintWithChainRootNode(SCNNode) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func inverseKinematicsConstraintWithChainRootNode(_ chainRootNode: SCNNode!) -> Self! ``` | OS X 10.10 |
| To | ``` class func inverseKinematicsConstraintWithChainRootNode(_ chainRootNode: SCNNode) -> Self ``` | OS X 10.10.3 |

Modified SCNIKConstraint.maxAllowedRotationAngleForJoint(SCNNode) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func maxAllowedRotationAngleForJoint(_ node: SCNNode!) -> CGFloat ``` |
| To | ``` func maxAllowedRotationAngleForJoint(_ node: SCNNode) -> CGFloat ``` |

Modified SCNIKConstraint.setMaxAllowedRotationAngle(CGFloat, forJoint: SCNNode)

|  | Declaration |
| --- | --- |
| From | ``` func setMaxAllowedRotationAngle(_ angle: CGFloat, forJoint node: SCNNode!) ``` |
| To | ``` func setMaxAllowedRotationAngle(_ angle: CGFloat, forJoint node: SCNNode) ``` |

Modified SCNLayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNLayer.scene

|  | Declaration |
| --- | --- |
| From | ``` var scene: SCNScene! ``` |
| To | ``` var scene: SCNScene? ``` |

Modified SCNLevelOfDetail

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNLevelOfDetail.geometry

|  | Declaration |
| --- | --- |
| From | ``` var geometry: SCNGeometry! { get } ``` |
| To | ``` var geometry: SCNGeometry? { get } ``` |

Modified SCNLevelOfDetail.init(geometry: SCNGeometry?, screenSpaceRadius: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(geometry geometry: SCNGeometry!, screenSpaceRadius radius: CGFloat) ``` |
| To | ``` convenience init(geometry geometry: SCNGeometry?, screenSpaceRadius radius: CGFloat) ``` |

Modified SCNLevelOfDetail.init(geometry: SCNGeometry?, worldSpaceDistance: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(geometry geometry: SCNGeometry!, worldSpaceDistance distance: CGFloat) ``` |
| To | ``` convenience init(geometry geometry: SCNGeometry?, worldSpaceDistance distance: CGFloat) ``` |

Modified SCNLight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNLight.attributeForKey(String) -> AnyObject?

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func attributeForKey(_ key: String!) -> AnyObject! ``` | OS X 10.10 | -- |
| To | ``` func attributeForKey(_ key: String) -> AnyObject? ``` | OS X 10.8 | OS X 10.10 |

Modified SCNLight.color

|  | Declaration |
| --- | --- |
| From | ``` var color: AnyObject! ``` |
| To | ``` var color: AnyObject ``` |

Modified SCNLight.gobo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var gobo: SCNMaterialProperty! { get } ``` | OS X 10.10 |
| To | ``` var gobo: SCNMaterialProperty { get } ``` | OS X 10.9 |

Modified SCNLight.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified SCNLight.setAttribute(AnyObject?, forKey: String)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func setAttribute(_ attribute: AnyObject!, forKey key: String!) ``` | OS X 10.10 | -- |
| To | ``` func setAttribute(_ attribute: AnyObject?, forKey key: String) ``` | OS X 10.8 | OS X 10.10 |

Modified SCNLight.shadowColor

|  | Declaration |
| --- | --- |
| From | ``` var shadowColor: AnyObject! ``` |
| To | ``` var shadowColor: AnyObject ``` |

Modified SCNLight.type

|  | Declaration |
| --- | --- |
| From | ``` var type: String! ``` |
| To | ``` var type: String ``` |

Modified SCNLookAtConstraint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNLookAtConstraint.target

|  | Declaration |
| --- | --- |
| From | ``` var target: SCNNode! { get } ``` |
| To | ``` var target: SCNNode? { get } ``` |

Modified SCNLookAtConstraint.init(target: SCNNode)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(target target: SCNNode!) ``` |
| To | ``` convenience init(target target: SCNNode) ``` |

Modified SCNMaterial

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNMaterial.ambient

|  | Declaration |
| --- | --- |
| From | ``` var ambient: SCNMaterialProperty! { get } ``` |
| To | ``` var ambient: SCNMaterialProperty { get } ``` |

Modified SCNMaterial.diffuse

|  | Declaration |
| --- | --- |
| From | ``` var diffuse: SCNMaterialProperty! { get } ``` |
| To | ``` var diffuse: SCNMaterialProperty { get } ``` |

Modified SCNMaterial.emission

|  | Declaration |
| --- | --- |
| From | ``` var emission: SCNMaterialProperty! { get } ``` |
| To | ``` var emission: SCNMaterialProperty { get } ``` |

Modified SCNMaterial.fresnelExponent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNMaterial.lightingModelName

|  | Declaration |
| --- | --- |
| From | ``` var lightingModelName: String! ``` |
| To | ``` var lightingModelName: String ``` |

Modified SCNMaterial.multiply

|  | Declaration |
| --- | --- |
| From | ``` var multiply: SCNMaterialProperty! { get } ``` |
| To | ``` var multiply: SCNMaterialProperty { get } ``` |

Modified SCNMaterial.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified SCNMaterial.normal

|  | Declaration |
| --- | --- |
| From | ``` var normal: SCNMaterialProperty! { get } ``` |
| To | ``` var normal: SCNMaterialProperty { get } ``` |

Modified SCNMaterial.readsFromDepthBuffer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNMaterial.reflective

|  | Declaration |
| --- | --- |
| From | ``` var reflective: SCNMaterialProperty! { get } ``` |
| To | ``` var reflective: SCNMaterialProperty { get } ``` |

Modified SCNMaterial.specular

|  | Declaration |
| --- | --- |
| From | ``` var specular: SCNMaterialProperty! { get } ``` |
| To | ``` var specular: SCNMaterialProperty { get } ``` |

Modified SCNMaterial.transparent

|  | Declaration |
| --- | --- |
| From | ``` var transparent: SCNMaterialProperty! { get } ``` |
| To | ``` var transparent: SCNMaterialProperty { get } ``` |

Modified SCNMaterialProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNMaterialProperty.borderColor

|  | Declaration |
| --- | --- |
| From | ``` var borderColor: AnyObject! ``` |
| To | ``` var borderColor: AnyObject ``` |

Modified SCNMaterialProperty.init(contents: AnyObject)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(contents contents: AnyObject!) ``` | OS X 10.10 |
| To | ``` convenience init(contents contents: AnyObject) ``` | OS X 10.9 |

Modified SCNMaterialProperty.intensity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNMaterialProperty.maxAnisotropy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNMorpher

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNMorpher.targets

|  | Declaration |
| --- | --- |
| From | ``` var targets: [AnyObject]! ``` |
| To | ``` var targets: [AnyObject]? ``` |

Modified SCNNode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNNode.addChildNode(SCNNode)

|  | Declaration |
| --- | --- |
| From | ``` func addChildNode(_ child: SCNNode!) ``` |
| To | ``` func addChildNode(_ child: SCNNode) ``` |

Modified SCNNode.addParticleSystem(SCNParticleSystem)

|  | Declaration |
| --- | --- |
| From | ``` func addParticleSystem(_ system: SCNParticleSystem!) ``` |
| To | ``` func addParticleSystem(_ system: SCNParticleSystem) ``` |

Modified SCNNode.camera

|  | Declaration |
| --- | --- |
| From | ``` var camera: SCNCamera! ``` |
| To | ``` var camera: SCNCamera? ``` |

Modified SCNNode.childNodeWithName(String, recursively: Bool) -> SCNNode?

|  | Declaration |
| --- | --- |
| From | ``` func childNodeWithName(_ name: String!, recursively recursively: Bool) -> SCNNode! ``` |
| To | ``` func childNodeWithName(_ name: String, recursively recursively: Bool) -> SCNNode? ``` |

Modified SCNNode.childNodes

|  | Declaration |
| --- | --- |
| From | ``` var childNodes: [AnyObject]! { get } ``` |
| To | ``` var childNodes: [AnyObject] { get } ``` |

Modified SCNNode.childNodesPassingTest((SCNNode!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func childNodesPassingTest(_ predicate: ((SCNNode!, UnsafePointer<ObjCBool>) -> Bool)!) -> [AnyObject]! ``` |
| To | ``` func childNodesPassingTest(_ predicate: (SCNNode!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AnyObject] ``` |

Modified SCNNode.clone() -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func clone() -> AnyObject! ``` |
| To | ``` func clone() -> AnyObject ``` |

Modified SCNNode.constraints

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var constraints: [AnyObject]! ``` | OS X 10.10 |
| To | ``` var constraints: [AnyObject]? ``` | OS X 10.9 |

Modified SCNNode.convertPosition(SCNVector3, fromNode: SCNNode?) -> SCNVector3

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func convertPosition(_ position: SCNVector3, fromNode node: SCNNode!) -> SCNVector3 ``` | OS X 10.10 |
| To | ``` func convertPosition(_ position: SCNVector3, fromNode node: SCNNode?) -> SCNVector3 ``` | OS X 10.9 |

Modified SCNNode.convertPosition(SCNVector3, toNode: SCNNode?) -> SCNVector3

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func convertPosition(_ position: SCNVector3, toNode node: SCNNode!) -> SCNVector3 ``` | OS X 10.10 |
| To | ``` func convertPosition(_ position: SCNVector3, toNode node: SCNNode?) -> SCNVector3 ``` | OS X 10.9 |

Modified SCNNode.convertTransform(SCNMatrix4, fromNode: SCNNode?) -> SCNMatrix4

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func convertTransform(_ transform: SCNMatrix4, fromNode node: SCNNode!) -> SCNMatrix4 ``` | OS X 10.10 |
| To | ``` func convertTransform(_ transform: SCNMatrix4, fromNode node: SCNNode?) -> SCNMatrix4 ``` | OS X 10.9 |

Modified SCNNode.convertTransform(SCNMatrix4, toNode: SCNNode?) -> SCNMatrix4

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func convertTransform(_ transform: SCNMatrix4, toNode node: SCNNode!) -> SCNMatrix4 ``` | OS X 10.10 |
| To | ``` func convertTransform(_ transform: SCNMatrix4, toNode node: SCNNode?) -> SCNMatrix4 ``` | OS X 10.9 |

Modified SCNNode.enumerateChildNodesUsingBlock((SCNNode!, UnsafeMutablePointer<ObjCBool>) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateChildNodesUsingBlock(_ block: ((SCNNode!, UnsafePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateChildNodesUsingBlock(_ block: (SCNNode!, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified SCNNode.filters

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var filters: [AnyObject]! ``` | OS X 10.10 |
| To | ``` var filters: [AnyObject]? ``` | OS X 10.9 |

Modified SCNNode.flattenedClone() -> SCNNode

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func flattenedClone() -> SCNNode! ``` | OS X 10.10 |
| To | ``` func flattenedClone() -> SCNNode ``` | OS X 10.9 |

Modified SCNNode.geometry

|  | Declaration |
| --- | --- |
| From | ``` var geometry: SCNGeometry! ``` |
| To | ``` var geometry: SCNGeometry? ``` |

Modified SCNNode.init(geometry: SCNGeometry)

|  | Declaration |
| --- | --- |
| From | ``` init(geometry geometry: SCNGeometry!) -> SCNNode ``` |
| To | ``` init(geometry geometry: SCNGeometry) -> SCNNode ``` |

Modified SCNNode.hitTestWithSegmentFromPoint(SCNVector3, toPoint: SCNVector3, options:[NSObject: AnyObject]?) -> [AnyObject]?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func hitTestWithSegmentFromPoint(_ pointA: SCNVector3, toPoint pointB: SCNVector3, options options: [NSObject : AnyObject]!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func hitTestWithSegmentFromPoint(_ pointA: SCNVector3, toPoint pointB: SCNVector3, options options: [NSObject : AnyObject]?) -> [AnyObject]? ``` | OS X 10.9 |

Modified SCNNode.insertChildNode(SCNNode, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insertChildNode(_ child: SCNNode!, atIndex index: Int) ``` |
| To | ``` func insertChildNode(_ child: SCNNode, atIndex index: Int) ``` |

Modified SCNNode.light

|  | Declaration |
| --- | --- |
| From | ``` var light: SCNLight! ``` |
| To | ``` var light: SCNLight? ``` |

Modified SCNNode.morpher

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var morpher: SCNMorpher! ``` | OS X 10.10 |
| To | ``` var morpher: SCNMorpher? ``` | OS X 10.9 |

Modified SCNNode.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified SCNNode.parentNode

|  | Declaration |
| --- | --- |
| From | ``` var parentNode: SCNNode! { get } ``` |
| To | ``` var parentNode: SCNNode? { get } ``` |

Modified SCNNode.particleSystems

|  | Declaration |
| --- | --- |
| From | ``` var particleSystems: [AnyObject]! { get } ``` |
| To | ``` var particleSystems: [AnyObject]? { get } ``` |

Modified SCNNode.physicsBody

|  | Declaration |
| --- | --- |
| From | ``` var physicsBody: SCNPhysicsBody! ``` |
| To | ``` var physicsBody: SCNPhysicsBody? ``` |

Modified SCNNode.physicsField

|  | Declaration |
| --- | --- |
| From | ``` var physicsField: SCNPhysicsField! ``` |
| To | ``` var physicsField: SCNPhysicsField? ``` |

Modified SCNNode.presentationNode() -> SCNNode

|  | Declaration |
| --- | --- |
| From | ``` func presentationNode() -> SCNNode! ``` |
| To | ``` func presentationNode() -> SCNNode ``` |

Modified SCNNode.removeParticleSystem(SCNParticleSystem)

|  | Declaration |
| --- | --- |
| From | ``` func removeParticleSystem(_ system: SCNParticleSystem!) ``` |
| To | ``` func removeParticleSystem(_ system: SCNParticleSystem) ``` |

Modified SCNNode.rendererDelegate

|  | Declaration |
| --- | --- |
| From | ``` var rendererDelegate: SCNNodeRendererDelegate! ``` |
| To | ``` unowned(unsafe) var rendererDelegate: SCNNodeRendererDelegate? ``` |

Modified SCNNode.replaceChildNode(SCNNode, with: SCNNode)

|  | Declaration |
| --- | --- |
| From | ``` func replaceChildNode(_ oldChild: SCNNode!, with newChild: SCNNode!) ``` |
| To | ``` func replaceChildNode(_ oldChild: SCNNode, with newChild: SCNNode) ``` |

Modified SCNNode.skinner

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var skinner: SCNSkinner! ``` | OS X 10.10 |
| To | ``` var skinner: SCNSkinner? ``` | OS X 10.9 |

Modified SCNNodeRendererDelegate.renderNode(SCNNode, renderer: SCNRenderer, arguments:[NSObject: AnyObject])

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func renderNode(_ node: SCNNode!, renderer renderer: SCNRenderer!, arguments arguments: [NSObject : AnyObject]!) ``` | -- |
| To | ``` optional func renderNode(_ node: SCNNode, renderer renderer: SCNRenderer, arguments arguments: [NSObject : AnyObject]) ``` | yes |

Modified SCNParticlePropertyController.init(animation: CAAnimation)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(animation animation: CAAnimation!) ``` |
| To | ``` convenience init(animation animation: CAAnimation) ``` |

Modified SCNParticlePropertyController.inputOrigin

|  | Declaration |
| --- | --- |
| From | ``` var inputOrigin: SCNNode! ``` |
| To | ``` weak var inputOrigin: SCNNode! ``` |

Modified SCNParticleSystem.addModifierForProperties([AnyObject], atStage: SCNParticleModifierStage, withBlock: SCNParticleModifierBlock)

|  | Declaration |
| --- | --- |
| From | ``` func addModifierForProperties(_ properties: [AnyObject]!, atStage stage: SCNParticleModifierStage, withBlock block: SCNParticleModifierBlock!) ``` |
| To | ``` func addModifierForProperties(_ properties: [AnyObject], atStage stage: SCNParticleModifierStage, withBlock block: SCNParticleModifierBlock) ``` |

Modified SCNParticleSystem.handleEvent(SCNParticleEvent, forProperties:[AnyObject], withBlock: SCNParticleEventBlock)

|  | Declaration |
| --- | --- |
| From | ``` func handleEvent(_ event: SCNParticleEvent, forProperties properties: [AnyObject]!, withBlock block: SCNParticleEventBlock!) ``` |
| To | ``` func handleEvent(_ event: SCNParticleEvent, forProperties properties: [AnyObject], withBlock block: SCNParticleEventBlock) ``` |

Modified SCNParticleSystem.init(named: String, inDirectory: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(named name: String!, inDirectory directory: String!) ``` |
| To | ``` convenience init!(named name: String, inDirectory directory: String!) ``` |

Modified SCNPhysicsBallSocketJoint.init(body: SCNPhysicsBody!, anchor: SCNVector3)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(body body: SCNPhysicsBody!, anchor anchor: SCNVector3) ``` |
| To | ``` convenience init!(body body: SCNPhysicsBody!, anchor anchor: SCNVector3) ``` |

Modified SCNPhysicsBallSocketJoint.init(bodyA: SCNPhysicsBody!, anchorA: SCNVector3, bodyB: SCNPhysicsBody!, anchorB: SCNVector3)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(bodyA bodyA: SCNPhysicsBody!, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, anchorB anchorB: SCNVector3) ``` |
| To | ``` convenience init!(bodyA bodyA: SCNPhysicsBody!, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, anchorB anchorB: SCNVector3) ``` |

Modified SCNPhysicsBody.dynamicBody() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func dynamicBody() -> Self! ``` | OS X 10.10 |
| To | ``` class func dynamicBody() -> Self ``` | OS X 10.10.3 |

Modified SCNPhysicsBody.kinematicBody() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func kinematicBody() -> Self! ``` | OS X 10.10 |
| To | ``` class func kinematicBody() -> Self ``` | OS X 10.10.3 |

Modified SCNPhysicsBody.physicsShape

|  | Declaration |
| --- | --- |
| From | ``` var physicsShape: SCNPhysicsShape! ``` |
| To | ``` var physicsShape: SCNPhysicsShape? ``` |

Modified SCNPhysicsBody.staticBody() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func staticBody() -> Self! ``` | OS X 10.10 |
| To | ``` class func staticBody() -> Self ``` | OS X 10.10.3 |

Modified SCNPhysicsBody.init(type: SCNPhysicsBodyType, shape: SCNPhysicsShape?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(type type: SCNPhysicsBodyType, shape shape: SCNPhysicsShape!) ``` |
| To | ``` convenience init(type type: SCNPhysicsBodyType, shape shape: SCNPhysicsShape?) ``` |

Modified SCNPhysicsCollisionCategory [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SCNPhysicsCollisionCategory : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Default: SCNPhysicsCollisionCategory { get }     static var Static: SCNPhysicsCollisionCategory { get }     static var All: SCNPhysicsCollisionCategory { get } } ``` | RawOptionSet |
| To | ``` struct SCNPhysicsCollisionCategory : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Default: SCNPhysicsCollisionCategory { get }     static var Static: SCNPhysicsCollisionCategory { get }     static var All: SCNPhysicsCollisionCategory { get } } ``` | RawOptionSetType |

Modified SCNPhysicsCollisionCategory.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified SCNPhysicsContact.nodeA

|  | Declaration |
| --- | --- |
| From | ``` var nodeA: SCNNode! { get } ``` |
| To | ``` var nodeA: SCNNode { get } ``` |

Modified SCNPhysicsContact.nodeB

|  | Declaration |
| --- | --- |
| From | ``` var nodeB: SCNNode! { get } ``` |
| To | ``` var nodeB: SCNNode { get } ``` |

Modified SCNPhysicsContactDelegate.physicsWorld(SCNPhysicsWorld, didBeginContact: SCNPhysicsContact)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func physicsWorld(_ world: SCNPhysicsWorld!, didBeginContact contact: SCNPhysicsContact!) ``` | -- |
| To | ``` optional func physicsWorld(_ world: SCNPhysicsWorld, didBeginContact contact: SCNPhysicsContact) ``` | yes |

Modified SCNPhysicsContactDelegate.physicsWorld(SCNPhysicsWorld, didEndContact: SCNPhysicsContact)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func physicsWorld(_ world: SCNPhysicsWorld!, didEndContact contact: SCNPhysicsContact!) ``` | -- |
| To | ``` optional func physicsWorld(_ world: SCNPhysicsWorld, didEndContact contact: SCNPhysicsContact) ``` | yes |

Modified SCNPhysicsContactDelegate.physicsWorld(SCNPhysicsWorld, didUpdateContact: SCNPhysicsContact)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func physicsWorld(_ world: SCNPhysicsWorld!, didUpdateContact contact: SCNPhysicsContact!) ``` | -- |
| To | ``` optional func physicsWorld(_ world: SCNPhysicsWorld, didUpdateContact contact: SCNPhysicsContact) ``` | yes |

Modified SCNPhysicsField.customFieldWithEvaluationBlock(SCNFieldForceEvaluator) -> SCNPhysicsField [class]

|  | Declaration |
| --- | --- |
| From | ``` class func customFieldWithEvaluationBlock(_ block: SCNFieldForceEvaluator!) -> SCNPhysicsField! ``` |
| To | ``` class func customFieldWithEvaluationBlock(_ block: SCNFieldForceEvaluator) -> SCNPhysicsField ``` |

Modified SCNPhysicsField.dragField() -> SCNPhysicsField [class]

|  | Declaration |
| --- | --- |
| From | ``` class func dragField() -> SCNPhysicsField! ``` |
| To | ``` class func dragField() -> SCNPhysicsField ``` |

Modified SCNPhysicsField.electricField() -> SCNPhysicsField [class]

|  | Declaration |
| --- | --- |
| From | ``` class func electricField() -> SCNPhysicsField! ``` |
| To | ``` class func electricField() -> SCNPhysicsField ``` |

Modified SCNPhysicsField.linearGravityField() -> SCNPhysicsField [class]

|  | Declaration |
| --- | --- |
| From | ``` class func linearGravityField() -> SCNPhysicsField! ``` |
| To | ``` class func linearGravityField() -> SCNPhysicsField ``` |

Modified SCNPhysicsField.magneticField() -> SCNPhysicsField [class]

|  | Declaration |
| --- | --- |
| From | ``` class func magneticField() -> SCNPhysicsField! ``` |
| To | ``` class func magneticField() -> SCNPhysicsField ``` |

Modified SCNPhysicsField.noiseFieldWithSmoothness(CGFloat, animationSpeed: CGFloat) -> SCNPhysicsField [class]

|  | Declaration |
| --- | --- |
| From | ``` class func noiseFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SCNPhysicsField! ``` |
| To | ``` class func noiseFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SCNPhysicsField ``` |

Modified SCNPhysicsField.radialGravityField() -> SCNPhysicsField [class]

|  | Declaration |
| --- | --- |
| From | ``` class func radialGravityField() -> SCNPhysicsField! ``` |
| To | ``` class func radialGravityField() -> SCNPhysicsField ``` |

Modified SCNPhysicsField.springField() -> SCNPhysicsField [class]

|  | Declaration |
| --- | --- |
| From | ``` class func springField() -> SCNPhysicsField! ``` |
| To | ``` class func springField() -> SCNPhysicsField ``` |

Modified SCNPhysicsField.turbulenceFieldWithSmoothness(CGFloat, animationSpeed: CGFloat) -> SCNPhysicsField [class]

|  | Declaration |
| --- | --- |
| From | ``` class func turbulenceFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SCNPhysicsField! ``` |
| To | ``` class func turbulenceFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SCNPhysicsField ``` |

Modified SCNPhysicsField.vortexField() -> SCNPhysicsField [class]

|  | Declaration |
| --- | --- |
| From | ``` class func vortexField() -> SCNPhysicsField! ``` |
| To | ``` class func vortexField() -> SCNPhysicsField ``` |

Modified SCNPhysicsHingeJoint.init(body: SCNPhysicsBody, axis: SCNVector3, anchor: SCNVector3)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(body body: SCNPhysicsBody!, axis axis: SCNVector3, anchor anchor: SCNVector3) ``` |
| To | ``` convenience init(body body: SCNPhysicsBody, axis axis: SCNVector3, anchor anchor: SCNVector3) ``` |

Modified SCNPhysicsHingeJoint.init(bodyA: SCNPhysicsBody, axisA: SCNVector3, anchorA: SCNVector3, bodyB: SCNPhysicsBody, axisB: SCNVector3, anchorB: SCNVector3)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(bodyA bodyA: SCNPhysicsBody!, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3) ``` |
| To | ``` convenience init(bodyA bodyA: SCNPhysicsBody, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3) ``` |

Modified SCNPhysicsShape.init(geometry: SCNGeometry, options:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(geometry geometry: SCNGeometry!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init(geometry geometry: SCNGeometry, options options: [NSObject : AnyObject]?) ``` |

Modified SCNPhysicsShape.init(node: SCNNode, options:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(node node: SCNNode!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init(node node: SCNNode, options options: [NSObject : AnyObject]?) ``` |

Modified SCNPhysicsShape.init(shapes: [AnyObject], transforms:[AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` convenience init(shapes shapes: [AnyObject]!, transforms transforms: [AnyObject]!) ``` |
| To | ``` convenience init(shapes shapes: [AnyObject], transforms transforms: [AnyObject]) ``` |

Modified SCNPhysicsSliderJoint.init(body: SCNPhysicsBody!, axis: SCNVector3, anchor: SCNVector3)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(body body: SCNPhysicsBody!, axis axis: SCNVector3, anchor anchor: SCNVector3) ``` |
| To | ``` convenience init!(body body: SCNPhysicsBody!, axis axis: SCNVector3, anchor anchor: SCNVector3) ``` |

Modified SCNPhysicsSliderJoint.init(bodyA: SCNPhysicsBody!, axisA: SCNVector3, anchorA: SCNVector3, bodyB: SCNPhysicsBody!, axisB: SCNVector3, anchorB: SCNVector3)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(bodyA bodyA: SCNPhysicsBody!, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3) ``` |
| To | ``` convenience init!(bodyA bodyA: SCNPhysicsBody!, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3) ``` |

Modified SCNPhysicsVehicle.init(chassisBody: SCNPhysicsBody!, wheels:[AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` convenience init(chassisBody chassisBody: SCNPhysicsBody!, wheels wheels: [AnyObject]!) ``` |
| To | ``` convenience init(chassisBody chassisBody: SCNPhysicsBody!, wheels wheels: [AnyObject]) ``` |

Modified SCNPhysicsWorld.contactDelegate

|  | Declaration |
| --- | --- |
| From | ``` var contactDelegate: SCNPhysicsContactDelegate! ``` |
| To | ``` unowned(unsafe) var contactDelegate: SCNPhysicsContactDelegate! ``` |

Modified SCNPlane

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNPlane.cornerRadius

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNPlane.cornerSegmentCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNProgram

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNProgram.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: SCNProgramDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: SCNProgramDelegate? ``` |

Modified SCNProgram.semanticForSymbol(String) -> String!

|  | Declaration |
| --- | --- |
| From | ``` func semanticForSymbol(_ symbol: String!) -> String! ``` |
| To | ``` func semanticForSymbol(_ symbol: String) -> String! ``` |

Modified SCNProgram.setSemantic(String!, forSymbol: String, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` func setSemantic(_ semantic: String!, forSymbol symbol: String!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` func setSemantic(_ semantic: String!, forSymbol symbol: String, options options: [NSObject : AnyObject]!) ``` |

Modified SCNProgramDelegate.program(SCNProgram, bindValueForSymbol: String, atLocation: UInt32, programID: UInt32, renderer: SCNRenderer) -> Bool

|  | Declaration | Introduction | Deprecation | Optional |
| --- | --- | --- | --- | --- |
| From | ``` optional func program(_ program: SCNProgram!, bindValueForSymbol symbol: String!, atLocation location: UInt32, programID programID: UInt32, renderer renderer: SCNRenderer!) -> Bool ``` | OS X 10.10 | -- | -- |
| To | ``` optional func program(_ program: SCNProgram, bindValueForSymbol symbol: String, atLocation location: UInt32, programID programID: UInt32, renderer renderer: SCNRenderer) -> Bool ``` | OS X 10.8 | OS X 10.10 | yes |

Modified SCNProgramDelegate.program(SCNProgram, handleError: NSError)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func program(_ program: SCNProgram!, handleError error: NSError!) ``` | -- |
| To | ``` optional func program(_ program: SCNProgram, handleError error: NSError) ``` | yes |

Modified SCNProgramDelegate.program(SCNProgram, unbindValueForSymbol: String, atLocation: UInt32, programID: UInt32, renderer: SCNRenderer)

|  | Declaration | Introduction | Deprecation | Optional |
| --- | --- | --- | --- | --- |
| From | ``` optional func program(_ program: SCNProgram!, unbindValueForSymbol symbol: String!, atLocation location: UInt32, programID programID: UInt32, renderer renderer: SCNRenderer!) ``` | OS X 10.10 | -- | -- |
| To | ``` optional func program(_ program: SCNProgram, unbindValueForSymbol symbol: String, atLocation location: UInt32, programID programID: UInt32, renderer renderer: SCNRenderer) ``` | OS X 10.8 | OS X 10.10 | yes |

Modified SCNProgramDelegate.programIsOpaque(SCNProgram) -> Bool

|  | Declaration | Introduction | Deprecation | Optional |
| --- | --- | --- | --- | --- |
| From | ``` optional func programIsOpaque(_ program: SCNProgram!) -> Bool ``` | OS X 10.10 | -- | -- |
| To | ``` optional func programIsOpaque(_ program: SCNProgram) -> Bool ``` | OS X 10.8 | OS X 10.10 | yes |

Modified SCNPyramid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNRenderer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNRenderer.init(context: UnsafeMutablePointer<Void>, options:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(context context: UnsafePointer<()>, options options: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init(context context: UnsafeMutablePointer<Void>, options options: [NSObject : AnyObject]?) ``` |

Modified SCNRenderer.scene

|  | Declaration |
| --- | --- |
| From | ``` var scene: SCNScene! ``` |
| To | ``` var scene: SCNScene? ``` |

Modified SCNScene

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNScene.init(URL: NSURL, options:[NSObject: AnyObject]?, error: NSErrorPointer)

|  | Name | Declaration |
| --- | --- | --- |
| From | sceneWithURL(_:options:error:) | ``` class func sceneWithURL(_ url: NSURL!, options options: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Self! ``` |
| To | init(URL:options:error:) | ``` convenience init?(URL url: NSURL, options options: [NSObject : AnyObject]?, error error: NSErrorPointer) ``` |

Modified SCNScene.addParticleSystem(SCNParticleSystem, withTransform: SCNMatrix4)

|  | Declaration |
| --- | --- |
| From | ``` func addParticleSystem(_ system: SCNParticleSystem!, withTransform transform: SCNMatrix4) ``` |
| To | ``` func addParticleSystem(_ system: SCNParticleSystem, withTransform transform: SCNMatrix4) ``` |

Modified SCNScene.attributeForKey(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func attributeForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func attributeForKey(_ key: String) -> AnyObject? ``` |

Modified SCNScene.background

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var background: SCNMaterialProperty! { get } ``` | OS X 10.10 |
| To | ``` var background: SCNMaterialProperty { get } ``` | OS X 10.9 |

Modified SCNScene.fogColor

|  | Declaration |
| --- | --- |
| From | ``` var fogColor: AnyObject! ``` |
| To | ``` var fogColor: AnyObject ``` |

Modified SCNScene.init(named: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(named name: String!) ``` | OS X 10.10 |
| To | ``` convenience init?(named name: String) ``` | OS X 10.9 |

Modified SCNScene.init(named: String, inDirectory: String?, options:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(named name: String!, inDirectory directory: String!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init?(named name: String, inDirectory directory: String?, options options: [NSObject : AnyObject]?) ``` |

Modified SCNScene.particleSystems

|  | Declaration |
| --- | --- |
| From | ``` var particleSystems: [AnyObject]! { get } ``` |
| To | ``` var particleSystems: [AnyObject]? { get } ``` |

Modified SCNScene.physicsWorld

|  | Declaration |
| --- | --- |
| From | ``` var physicsWorld: SCNPhysicsWorld! { get } ``` |
| To | ``` var physicsWorld: SCNPhysicsWorld { get } ``` |

Modified SCNScene.removeParticleSystem(SCNParticleSystem)

|  | Declaration |
| --- | --- |
| From | ``` func removeParticleSystem(_ system: SCNParticleSystem!) ``` |
| To | ``` func removeParticleSystem(_ system: SCNParticleSystem) ``` |

Modified SCNScene.rootNode

|  | Declaration |
| --- | --- |
| From | ``` var rootNode: SCNNode! { get } ``` |
| To | ``` var rootNode: SCNNode { get } ``` |

Modified SCNScene.setAttribute(AnyObject, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setAttribute(_ attribute: AnyObject!, forKey key: String!) ``` |
| To | ``` func setAttribute(_ attribute: AnyObject, forKey key: String) ``` |

Modified SCNScene.writeToURL(NSURL, options:[NSObject: AnyObject]?, delegate: SCNSceneExportDelegate?, progressHandler: SCNSceneExportProgressHandler?) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func writeToURL(_ url: NSURL!, options options: [NSObject : AnyObject]!, delegate delegate: SCNSceneExportDelegate!, progressHandler progressHandler: SCNSceneExportProgressHandler!) -> Bool ``` | OS X 10.10 |
| To | ``` func writeToURL(_ url: NSURL, options options: [NSObject : AnyObject]?, delegate delegate: SCNSceneExportDelegate?, progressHandler progressHandler: SCNSceneExportProgressHandler?) -> Bool ``` | OS X 10.9 |

Modified SCNSceneExportDelegate.writeImage(NSImage, withSceneDocumentURL: NSURL, originalImageURL: NSURL?) -> NSURL?

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func writeImage(_ image: NSImage!, withSceneDocumentURL documentURL: NSURL!, originalImageURL originalImageURL: NSURL!) -> NSURL! ``` | OS X 10.10 | -- |
| To | ``` optional func writeImage(_ image: NSImage, withSceneDocumentURL documentURL: NSURL, originalImageURL originalImageURL: NSURL?) -> NSURL? ``` | OS X 10.9 | yes |

Modified SCNSceneRenderer.context

|  | Declaration |
| --- | --- |
| From | ``` var context: UnsafePointer<()> { get } ``` |
| To | ``` var context: UnsafeMutablePointer<Void> { get } ``` |

Modified SCNSceneRenderer.currentTime

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified SCNSceneRenderer.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: SCNSceneRendererDelegate! { get set } ``` |
| To | ``` unowned(unsafe) var delegate: SCNSceneRendererDelegate? { get set } ``` |

Modified SCNSceneRenderer.hitTest(CGPoint, options:[NSObject: AnyObject]?) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func hitTest(_ thePoint: CGPoint, options options: [NSObject : AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func hitTest(_ thePoint: CGPoint, options options: [NSObject : AnyObject]?) -> [AnyObject]? ``` |

Modified SCNSceneRenderer.isNodeInsideFrustum(SCNNode, withPointOfView: SCNNode?) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isNodeInsideFrustum(_ node: SCNNode!, withPointOfView pointOfView: SCNNode!) -> Bool ``` | OS X 10.10 |
| To | ``` func isNodeInsideFrustum(_ node: SCNNode, withPointOfView pointOfView: SCNNode?) -> Bool ``` | OS X 10.9 |

Modified SCNSceneRenderer.pointOfView

|  | Declaration |
| --- | --- |
| From | ``` var pointOfView: SCNNode! { get set } ``` |
| To | ``` var pointOfView: SCNNode? { get set } ``` |

Modified SCNSceneRenderer.prepareObject(AnyObject, shouldAbortBlock:(() -> Bool)?) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func prepareObject(_ object: AnyObject!, shouldAbortBlock block: (() -> Bool)!) -> Bool ``` | OS X 10.10 |
| To | ``` func prepareObject(_ object: AnyObject, shouldAbortBlock block: (() -> Bool)?) -> Bool ``` | OS X 10.9 |

Modified SCNSceneRenderer.prepareObjects([AnyObject], withCompletionHandler:((Bool) -> Void)?)

|  | Declaration |
| --- | --- |
| From | ``` func prepareObjects(_ objects: [AnyObject]!, withCompletionHandler completionHandler: ((Bool) -> Void)!) ``` |
| To | ``` func prepareObjects(_ objects: [AnyObject], withCompletionHandler completionHandler: ((Bool) -> Void)?) ``` |

Modified SCNSceneRenderer.projectPoint(SCNVector3) -> SCNVector3

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNSceneRenderer.scene

|  | Declaration |
| --- | --- |
| From | ``` var scene: SCNScene! { get set } ``` |
| To | ``` var scene: SCNScene? { get set } ``` |

Modified SCNSceneRenderer.showsStatistics

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNSceneRenderer.unprojectPoint(SCNVector3) -> SCNVector3

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNSceneRendererDelegate.renderer(SCNSceneRenderer, didApplyAnimationsAtTime: NSTimeInterval)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func renderer(_ aRenderer: SCNSceneRenderer!, didApplyAnimationsAtTime time: NSTimeInterval) ``` | -- |
| To | ``` optional func renderer(_ aRenderer: SCNSceneRenderer, didApplyAnimationsAtTime time: NSTimeInterval) ``` | yes |

Modified SCNSceneRendererDelegate.renderer(SCNSceneRenderer, didRenderScene: SCNScene, atTime: NSTimeInterval)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func renderer(_ aRenderer: SCNSceneRenderer!, didRenderScene scene: SCNScene!, atTime time: NSTimeInterval) ``` | -- |
| To | ``` optional func renderer(_ aRenderer: SCNSceneRenderer, didRenderScene scene: SCNScene, atTime time: NSTimeInterval) ``` | yes |

Modified SCNSceneRendererDelegate.renderer(SCNSceneRenderer, didSimulatePhysicsAtTime: NSTimeInterval)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func renderer(_ aRenderer: SCNSceneRenderer!, didSimulatePhysicsAtTime time: NSTimeInterval) ``` | -- |
| To | ``` optional func renderer(_ aRenderer: SCNSceneRenderer, didSimulatePhysicsAtTime time: NSTimeInterval) ``` | yes |

Modified SCNSceneRendererDelegate.renderer(SCNSceneRenderer, updateAtTime: NSTimeInterval)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func renderer(_ aRenderer: SCNSceneRenderer!, updateAtTime time: NSTimeInterval) ``` | -- |
| To | ``` optional func renderer(_ aRenderer: SCNSceneRenderer, updateAtTime time: NSTimeInterval) ``` | yes |

Modified SCNSceneRendererDelegate.renderer(SCNSceneRenderer, willRenderScene: SCNScene, atTime: NSTimeInterval)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func renderer(_ aRenderer: SCNSceneRenderer!, willRenderScene scene: SCNScene!, atTime time: NSTimeInterval) ``` | -- |
| To | ``` optional func renderer(_ aRenderer: SCNSceneRenderer, willRenderScene scene: SCNScene, atTime time: NSTimeInterval) ``` | yes |

Modified SCNSceneSource

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNSceneSource.init(URL: NSURL, options:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` init?(URL url: NSURL, options options: [NSObject : AnyObject]?) ``` |

Modified SCNSceneSource.data

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` var data: NSData? { get } ``` |

Modified SCNSceneSource.init(data: NSData, options:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` init?(data data: NSData, options options: [NSObject : AnyObject]?) ``` |

Modified SCNSceneSource.entriesPassingTest((AnyObject!, String!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func entriesPassingTest(_ predicate: ((AnyObject!, String!, UnsafePointer<ObjCBool>) -> Bool)!) -> [AnyObject]! ``` | OS X 10.10 |
| To | ``` func entriesPassingTest(_ predicate: (AnyObject!, String!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AnyObject] ``` | OS X 10.9 |

Modified SCNSceneSource.entryWithIdentifier(String, withClass: AnyClass) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func entryWithIdentifier(_ uid: String!, withClass entryClass: AnyClass!) -> AnyObject! ``` |
| To | ``` func entryWithIdentifier(_ uid: String, withClass entryClass: AnyClass) -> AnyObject? ``` |

Modified SCNSceneSource.identifiersOfEntriesWithClass(AnyClass) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func identifiersOfEntriesWithClass(_ entryClass: AnyClass!) -> [AnyObject]! ``` |
| To | ``` func identifiersOfEntriesWithClass(_ entryClass: AnyClass) -> [AnyObject]? ``` |

Modified SCNSceneSource.propertyForKey(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func propertyForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func propertyForKey(_ key: String) -> AnyObject? ``` |

Modified SCNSceneSource.sceneWithOptions([NSObject: AnyObject]?, error: NSErrorPointer) -> SCNScene?

|  | Declaration |
| --- | --- |
| From | ``` func sceneWithOptions(_ options: [NSObject : AnyObject]!, error error: NSErrorPointer) -> SCNScene! ``` |
| To | ``` func sceneWithOptions(_ options: [NSObject : AnyObject]?, error error: NSErrorPointer) -> SCNScene? ``` |

Modified SCNSceneSource.sceneWithOptions([NSObject: AnyObject]?, statusHandler: SCNSceneSourceStatusHandler?) -> SCNScene?

|  | Declaration |
| --- | --- |
| From | ``` func sceneWithOptions(_ options: [NSObject : AnyObject]!, statusHandler statusHandler: SCNSceneSourceStatusHandler!) -> SCNScene! ``` |
| To | ``` func sceneWithOptions(_ options: [NSObject : AnyObject]?, statusHandler statusHandler: SCNSceneSourceStatusHandler?) -> SCNScene? ``` |

Modified SCNSceneSource.url

|  | Declaration |
| --- | --- |
| From | ``` var url: NSURL! { get } ``` |
| To | ``` var url: NSURL? { get } ``` |

Modified SCNShadable.handleBindingOfSymbol(String, usingBlock: SCNBindingBlock)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func handleBindingOfSymbol(_ symbol: String!, usingBlock block: SCNBindingBlock!) ``` | OS X 10.10 | -- |
| To | ``` optional func handleBindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock) ``` | OS X 10.9 | yes |

Modified SCNShadable.handleUnbindingOfSymbol(String, usingBlock: SCNBindingBlock)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func handleUnbindingOfSymbol(_ symbol: String!, usingBlock block: SCNBindingBlock!) ``` | OS X 10.10 | -- |
| To | ``` optional func handleUnbindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock) ``` | OS X 10.9 | yes |

Modified SCNShadable.program

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified SCNShadable.shaderModifiers

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional var shaderModifiers: [NSObject : AnyObject]! { get set } ``` | OS X 10.10 | -- |
| To | ``` optional var shaderModifiers: [NSObject : AnyObject]? { get set } ``` | OS X 10.9 | yes |

Modified SCNShape

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNShape.chamferProfile

|  | Declaration |
| --- | --- |
| From | ``` var chamferProfile: NSBezierPath! ``` |
| To | ``` @NSCopying var chamferProfile: NSBezierPath! ``` |

Modified SCNShape.path

|  | Declaration |
| --- | --- |
| From | ``` var path: NSBezierPath! ``` |
| To | ``` @NSCopying var path: NSBezierPath! ``` |

Modified SCNShape.init(path: NSBezierPath, extrusionDepth: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(path path: NSBezierPath!, extrusionDepth extrusionDepth: CGFloat) ``` |
| To | ``` convenience init(path path: NSBezierPath, extrusionDepth extrusionDepth: CGFloat) ``` |

Modified SCNSkinner

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNSkinner.baseGeometry

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNSkinner.init(baseGeometry: SCNGeometry!, bones:[AnyObject]!, boneInverseBindTransforms:[AnyObject]!, boneWeights: SCNGeometrySource!, boneIndices: SCNGeometrySource!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(baseGeometry baseGeometry: SCNGeometry!, bones bones: [AnyObject]!, boneInverseBindTransforms boneInverseBindTransforms: [AnyObject]!, boneWeights boneWeights: SCNGeometrySource!, boneIndices boneIndices: SCNGeometrySource!) ``` |
| To | ``` convenience init!(baseGeometry baseGeometry: SCNGeometry!, bones bones: [AnyObject]!, boneInverseBindTransforms boneInverseBindTransforms: [AnyObject]!, boneWeights boneWeights: SCNGeometrySource!, boneIndices boneIndices: SCNGeometrySource!) ``` |

Modified SCNSphere

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNTechnique.init(bySequencingTechniques: [AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(bySequencingTechniques techniques: [AnyObject]!) -> SCNTechnique ``` |
| To | ``` init?(bySequencingTechniques techniques: [AnyObject]) -> SCNTechnique ``` |

Modified SCNTechnique.init(dictionary: [NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(dictionary dictionary: [NSObject : AnyObject]!) -> SCNTechnique ``` |
| To | ``` init?(dictionary dictionary: [NSObject : AnyObject]) -> SCNTechnique ``` |

Modified SCNTechnique.dictionaryRepresentation

|  | Declaration |
| --- | --- |
| From | ``` var dictionaryRepresentation: [NSObject : AnyObject]! { get } ``` |
| To | ``` var dictionaryRepresentation: [NSObject : AnyObject] { get } ``` |

Modified SCNTechnique.handleBindingOfSymbol(String, usingBlock: SCNBindingBlock)

|  | Declaration |
| --- | --- |
| From | ``` func handleBindingOfSymbol(_ symbol: String!, usingBlock block: SCNBindingBlock!) ``` |
| To | ``` func handleBindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock) ``` |

Modified SCNTechniqueSupport.technique

|  | Declaration |
| --- | --- |
| From | ``` var technique: SCNTechnique! { get set } ``` |
| To | ``` @NSCopying var technique: SCNTechnique? { get set } ``` |

Modified SCNText

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNText.chamferProfile

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var chamferProfile: NSBezierPath! ``` | OS X 10.10 |
| To | ``` @NSCopying var chamferProfile: NSBezierPath! ``` | OS X 10.9 |

Modified SCNText.flatness

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNText.string

|  | Declaration |
| --- | --- |
| From | ``` var string: AnyObject! ``` |
| To | ``` @NSCopying var string: AnyObject! ``` |

Modified SCNText.init(string: AnyObject, extrusionDepth: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(string string: AnyObject!, extrusionDepth extrusionDepth: CGFloat) ``` |
| To | ``` convenience init(string string: AnyObject, extrusionDepth extrusionDepth: CGFloat) ``` |

Modified SCNTorus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNTransaction

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNTransaction.animationTimingFunction() -> CAMediaTimingFunction? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func animationTimingFunction() -> CAMediaTimingFunction! ``` |
| To | ``` class func animationTimingFunction() -> CAMediaTimingFunction? ``` |

Modified SCNTransaction.completionBlock() -> (() -> Void)? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func completionBlock() -> (() -> Void)! ``` |
| To | ``` class func completionBlock() -> (() -> Void)? ``` |

Modified SCNTransaction.setAnimationTimingFunction(CAMediaTimingFunction?) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setAnimationTimingFunction(_ function: CAMediaTimingFunction!) ``` |
| To | ``` class func setAnimationTimingFunction(_ function: CAMediaTimingFunction?) ``` |

Modified SCNTransaction.setCompletionBlock((() -> Void)?) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setCompletionBlock(_ block: (() -> Void)!) ``` |
| To | ``` class func setCompletionBlock(_ block: (() -> Void)?) ``` |

Modified SCNTransaction.setValue(AnyObject?, forKey: String) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setValue(_ anObject: AnyObject!, forKey key: String!) ``` |
| To | ``` class func setValue(_ anObject: AnyObject?, forKey key: String) ``` |

Modified SCNTransaction.valueForKey(String) -> AnyObject? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func valueForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` class func valueForKey(_ key: String) -> AnyObject? ``` |

Modified SCNTransformConstraint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNTransformConstraint.init(inWorldSpace: Bool, withBlock:(SCNNode!, SCNMatrix4) -> SCNMatrix4)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(inWorldSpace world: Bool, withBlock block: ((SCNNode!, SCNMatrix4) -> SCNMatrix4)!) ``` |
| To | ``` convenience init(inWorldSpace world: Bool, withBlock block: (SCNNode!, SCNMatrix4) -> SCNMatrix4) ``` |

Modified SCNTube

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNVector3 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCNVector3 {     var x: CGFloat     var y: CGFloat     var z: CGFloat } ``` |
| To | ``` struct SCNVector3 {     var x: CGFloat     var y: CGFloat     var z: CGFloat     init()     init(x x: CGFloat, y y: CGFloat, z z: CGFloat) } ``` |

Modified SCNVector4 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCNVector4 {     var x: CGFloat     var y: CGFloat     var z: CGFloat     var w: CGFloat } ``` |
| To | ``` struct SCNVector4 {     var x: CGFloat     var y: CGFloat     var z: CGFloat     var w: CGFloat     init()     init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) } ``` |

Modified SCNView

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SCNView.backgroundColor

|  | Declaration |
| --- | --- |
| From | ``` var backgroundColor: NSColor! ``` |
| To | ``` @NSCopying var backgroundColor: NSColor? ``` |

Modified SCNView.init(frame: NSRect, options:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(frame frame: NSRect, options options: [NSObject : AnyObject]!) ``` |
| To | ``` init(frame frame: NSRect, options options: [NSObject : AnyObject]?) ``` |

Modified SCNView.openGLContext

|  | Declaration |
| --- | --- |
| From | ``` var openGLContext: NSOpenGLContext! ``` |
| To | ``` var openGLContext: NSOpenGLContext ``` |

Modified SCNView.pause(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func pause(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func pause(_ sender: AnyObject?) ``` |

Modified SCNView.pixelFormat

|  | Declaration |
| --- | --- |
| From | ``` var pixelFormat: NSOpenGLPixelFormat! ``` |
| To | ``` var pixelFormat: NSOpenGLPixelFormat ``` |

Modified SCNView.play(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func play(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func play(_ sender: AnyObject?) ``` |

Modified SCNView.scene

|  | Declaration |
| --- | --- |
| From | ``` var scene: SCNScene! ``` |
| To | ``` var scene: SCNScene? ``` |

Modified SCNView.snapshot() -> NSImage?

|  | Declaration |
| --- | --- |
| From | ``` func snapshot() -> NSImage! ``` |
| To | ``` func snapshot() -> NSImage? ``` |

Modified SCNView.stop(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func stop(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func stop(_ sender: AnyObject?) ``` |

Modified SCNWrapMode.WrapModeClamp

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNWrapMode.WrapModeClampToBorder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNWrapMode.WrapModeMirror

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNWrapMode.WrapModeRepeat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SCNConsistencyElementIDErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNConsistencyElementIDErrorKey: NSString! ``` |
| To | ``` let SCNConsistencyElementIDErrorKey: String ``` |

Modified SCNConsistencyElementTypeErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNConsistencyElementTypeErrorKey: NSString! ``` |
| To | ``` let SCNConsistencyElementTypeErrorKey: String ``` |

Modified SCNConsistencyLineNumberErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNConsistencyLineNumberErrorKey: NSString! ``` |
| To | ``` let SCNConsistencyLineNumberErrorKey: String ``` |

Modified SCNDetailedErrorsKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNDetailedErrorsKey: NSString! ``` |
| To | ``` let SCNDetailedErrorsKey: String ``` |

Modified SCNErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let SCNErrorDomain: NSString! ``` |
| To | ``` let SCNErrorDomain: String ``` |

Modified SCNGeometrySourceSemanticBoneIndices

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticBoneIndices: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticBoneIndices: String ``` |

Modified SCNGeometrySourceSemanticBoneWeights

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticBoneWeights: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticBoneWeights: String ``` |

Modified SCNGeometrySourceSemanticColor

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticColor: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticColor: String ``` |

Modified SCNGeometrySourceSemanticEdgeCrease

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticEdgeCrease: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticEdgeCrease: String ``` |

Modified SCNGeometrySourceSemanticNormal

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticNormal: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticNormal: String ``` |

Modified SCNGeometrySourceSemanticTexcoord

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticTexcoord: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticTexcoord: String ``` |

Modified SCNGeometrySourceSemanticVertex

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticVertex: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticVertex: String ``` |

Modified SCNGeometrySourceSemanticVertexCrease

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticVertexCrease: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticVertexCrease: String ``` |

Modified SCNHitTestBackFaceCullingKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestBackFaceCullingKey: NSString! ``` |
| To | ``` let SCNHitTestBackFaceCullingKey: String ``` |

Modified SCNHitTestBoundingBoxOnlyKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestBoundingBoxOnlyKey: NSString! ``` |
| To | ``` let SCNHitTestBoundingBoxOnlyKey: String ``` |

Modified SCNHitTestClipToZRangeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestClipToZRangeKey: NSString! ``` |
| To | ``` let SCNHitTestClipToZRangeKey: String ``` |

Modified SCNHitTestFirstFoundOnlyKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestFirstFoundOnlyKey: NSString! ``` |
| To | ``` let SCNHitTestFirstFoundOnlyKey: String ``` |

Modified SCNHitTestIgnoreChildNodesKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestIgnoreChildNodesKey: NSString! ``` |
| To | ``` let SCNHitTestIgnoreChildNodesKey: String ``` |

Modified SCNHitTestIgnoreHiddenNodesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SCNHitTestIgnoreHiddenNodesKey: NSString! ``` | OS X 10.10 |
| To | ``` let SCNHitTestIgnoreHiddenNodesKey: String ``` | OS X 10.9 |

Modified SCNHitTestRootNodeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestRootNodeKey: NSString! ``` |
| To | ``` let SCNHitTestRootNodeKey: String ``` |

Modified SCNHitTestSortResultsKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestSortResultsKey: NSString! ``` |
| To | ``` let SCNHitTestSortResultsKey: String ``` |

Modified SCNLightAttenuationEndKey

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let SCNLightAttenuationEndKey: NSString! ``` | OS X 10.10 | -- |
| To | ``` let SCNLightAttenuationEndKey: String ``` | OS X 10.8 | OS X 10.10 |

Modified SCNLightAttenuationFalloffExponentKey

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let SCNLightAttenuationFalloffExponentKey: NSString! ``` | OS X 10.10 | -- |
| To | ``` let SCNLightAttenuationFalloffExponentKey: String ``` | OS X 10.8 | OS X 10.10 |

Modified SCNLightAttenuationStartKey

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let SCNLightAttenuationStartKey: NSString! ``` | OS X 10.10 | -- |
| To | ``` let SCNLightAttenuationStartKey: String ``` | OS X 10.8 | OS X 10.10 |

Modified SCNLightShadowFarClippingKey

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let SCNLightShadowFarClippingKey: NSString! ``` | OS X 10.10 | -- |
| To | ``` let SCNLightShadowFarClippingKey: String ``` | OS X 10.8 | OS X 10.10 |

Modified SCNLightShadowNearClippingKey

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let SCNLightShadowNearClippingKey: NSString! ``` | OS X 10.10 | -- |
| To | ``` let SCNLightShadowNearClippingKey: String ``` | OS X 10.8 | OS X 10.10 |

Modified SCNLightSpotInnerAngleKey

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let SCNLightSpotInnerAngleKey: NSString! ``` | OS X 10.10 | -- |
| To | ``` let SCNLightSpotInnerAngleKey: String ``` | OS X 10.8 | OS X 10.10 |

Modified SCNLightSpotOuterAngleKey

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let SCNLightSpotOuterAngleKey: NSString! ``` | OS X 10.10 | -- |
| To | ``` let SCNLightSpotOuterAngleKey: String ``` | OS X 10.8 | OS X 10.10 |

Modified SCNLightTypeAmbient

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightTypeAmbient: NSString! ``` |
| To | ``` let SCNLightTypeAmbient: String ``` |

Modified SCNLightTypeDirectional

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightTypeDirectional: NSString! ``` |
| To | ``` let SCNLightTypeDirectional: String ``` |

Modified SCNLightTypeOmni

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightTypeOmni: NSString! ``` |
| To | ``` let SCNLightTypeOmni: String ``` |

Modified SCNLightTypeSpot

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightTypeSpot: NSString! ``` |
| To | ``` let SCNLightTypeSpot: String ``` |

Modified SCNLightingModelBlinn

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightingModelBlinn: NSString! ``` |
| To | ``` let SCNLightingModelBlinn: String ``` |

Modified SCNLightingModelConstant

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightingModelConstant: NSString! ``` |
| To | ``` let SCNLightingModelConstant: String ``` |

Modified SCNLightingModelLambert

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightingModelLambert: NSString! ``` |
| To | ``` let SCNLightingModelLambert: String ``` |

Modified SCNLightingModelPhong

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightingModelPhong: NSString! ``` |
| To | ``` let SCNLightingModelPhong: String ``` |

Modified SCNModelTransform

|  | Declaration |
| --- | --- |
| From | ``` let SCNModelTransform: NSString! ``` |
| To | ``` let SCNModelTransform: String ``` |

Modified SCNModelViewProjectionTransform

|  | Declaration |
| --- | --- |
| From | ``` let SCNModelViewProjectionTransform: NSString! ``` |
| To | ``` let SCNModelViewProjectionTransform: String ``` |

Modified SCNModelViewTransform

|  | Declaration |
| --- | --- |
| From | ``` let SCNModelViewTransform: NSString! ``` |
| To | ``` let SCNModelViewTransform: String ``` |

Modified SCNNormalTransform

|  | Declaration |
| --- | --- |
| From | ``` let SCNNormalTransform: NSString! ``` |
| To | ``` let SCNNormalTransform: String ``` |

Modified SCNParticleEventBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNParticleEventBlock = (UnsafePointer<UnsafePointer<()>>, UnsafePointer<UInt>, UnsafePointer<UInt32>, Int) -> Void ``` |
| To | ``` typealias SCNParticleEventBlock = (UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<UInt32>, Int) -> Void ``` |

Modified SCNParticleModifierBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNParticleModifierBlock = (UnsafePointer<UnsafePointer<()>>, UnsafePointer<UInt>, Int, Int, Float) -> Void ``` |
| To | ``` typealias SCNParticleModifierBlock = (UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Int>, Int, Int, Float) -> Void ``` |

Modified SCNParticlePropertyAngle

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyAngle: NSString! ``` |
| To | ``` let SCNParticlePropertyAngle: String ``` |

Modified SCNParticlePropertyAngularVelocity

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyAngularVelocity: NSString! ``` |
| To | ``` let SCNParticlePropertyAngularVelocity: String ``` |

Modified SCNParticlePropertyBounce

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyBounce: NSString! ``` |
| To | ``` let SCNParticlePropertyBounce: String ``` |

Modified SCNParticlePropertyCharge

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyCharge: NSString! ``` |
| To | ``` let SCNParticlePropertyCharge: String ``` |

Modified SCNParticlePropertyColor

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyColor: NSString! ``` |
| To | ``` let SCNParticlePropertyColor: String ``` |

Modified SCNParticlePropertyContactNormal

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyContactNormal: NSString! ``` |
| To | ``` let SCNParticlePropertyContactNormal: String ``` |

Modified SCNParticlePropertyContactPoint

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyContactPoint: NSString! ``` |
| To | ``` let SCNParticlePropertyContactPoint: String ``` |

Modified SCNParticlePropertyFrame

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyFrame: NSString! ``` |
| To | ``` let SCNParticlePropertyFrame: String ``` |

Modified SCNParticlePropertyFrameRate

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyFrameRate: NSString! ``` |
| To | ``` let SCNParticlePropertyFrameRate: String ``` |

Modified SCNParticlePropertyFriction

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyFriction: NSString! ``` |
| To | ``` let SCNParticlePropertyFriction: String ``` |

Modified SCNParticlePropertyLife

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyLife: NSString! ``` |
| To | ``` let SCNParticlePropertyLife: String ``` |

Modified SCNParticlePropertyOpacity

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyOpacity: NSString! ``` |
| To | ``` let SCNParticlePropertyOpacity: String ``` |

Modified SCNParticlePropertyPosition

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyPosition: NSString! ``` |
| To | ``` let SCNParticlePropertyPosition: String ``` |

Modified SCNParticlePropertyRotationAxis

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyRotationAxis: NSString! ``` |
| To | ``` let SCNParticlePropertyRotationAxis: String ``` |

Modified SCNParticlePropertySize

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertySize: NSString! ``` |
| To | ``` let SCNParticlePropertySize: String ``` |

Modified SCNParticlePropertyVelocity

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyVelocity: NSString! ``` |
| To | ``` let SCNParticlePropertyVelocity: String ``` |

Modified SCNPhysicsShapeKeepAsCompoundKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsShapeKeepAsCompoundKey: NSString! ``` |
| To | ``` let SCNPhysicsShapeKeepAsCompoundKey: String ``` |

Modified SCNPhysicsShapeScaleKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsShapeScaleKey: NSString! ``` |
| To | ``` let SCNPhysicsShapeScaleKey: String ``` |

Modified SCNPhysicsShapeTypeBoundingBox

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsShapeTypeBoundingBox: NSString! ``` |
| To | ``` let SCNPhysicsShapeTypeBoundingBox: String ``` |

Modified SCNPhysicsShapeTypeConcavePolyhedron

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsShapeTypeConcavePolyhedron: NSString! ``` |
| To | ``` let SCNPhysicsShapeTypeConcavePolyhedron: String ``` |

Modified SCNPhysicsShapeTypeConvexHull

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsShapeTypeConvexHull: NSString! ``` |
| To | ``` let SCNPhysicsShapeTypeConvexHull: String ``` |

Modified SCNPhysicsShapeTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsShapeTypeKey: NSString! ``` |
| To | ``` let SCNPhysicsShapeTypeKey: String ``` |

Modified SCNPhysicsTestBackfaceCullingKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsTestBackfaceCullingKey: NSString! ``` |
| To | ``` let SCNPhysicsTestBackfaceCullingKey: String ``` |

Modified SCNPhysicsTestCollisionBitMaskKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsTestCollisionBitMaskKey: NSString! ``` |
| To | ``` let SCNPhysicsTestCollisionBitMaskKey: String ``` |

Modified SCNPhysicsTestSearchModeAll

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsTestSearchModeAll: NSString! ``` |
| To | ``` let SCNPhysicsTestSearchModeAll: String ``` |

Modified SCNPhysicsTestSearchModeAny

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsTestSearchModeAny: NSString! ``` |
| To | ``` let SCNPhysicsTestSearchModeAny: String ``` |

Modified SCNPhysicsTestSearchModeClosest

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsTestSearchModeClosest: NSString! ``` |
| To | ``` let SCNPhysicsTestSearchModeClosest: String ``` |

Modified SCNPhysicsTestSearchModeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsTestSearchModeKey: NSString! ``` |
| To | ``` let SCNPhysicsTestSearchModeKey: String ``` |

Modified SCNProgramMappingChannelKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNProgramMappingChannelKey: NSString! ``` |
| To | ``` let SCNProgramMappingChannelKey: String ``` |

Modified SCNProjectionTransform

|  | Declaration |
| --- | --- |
| From | ``` let SCNProjectionTransform: NSString! ``` |
| To | ``` let SCNProjectionTransform: String ``` |

Modified SCNSceneEndTimeAttributeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneEndTimeAttributeKey: NSString! ``` |
| To | ``` let SCNSceneEndTimeAttributeKey: String ``` |

Modified SCNSceneExportDestinationURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SCNSceneExportDestinationURL: NSString! ``` | OS X 10.10 |
| To | ``` let SCNSceneExportDestinationURL: String ``` | OS X 10.9 |

Modified SCNSceneExportProgressHandler

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNSceneExportProgressHandler = (Float, NSError!, UnsafePointer<ObjCBool>) -> Void ``` |
| To | ``` typealias SCNSceneExportProgressHandler = (Float, NSError!, UnsafeMutablePointer<ObjCBool>) -> Void ``` |

Modified SCNSceneFrameRateAttributeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneFrameRateAttributeKey: NSString! ``` |
| To | ``` let SCNSceneFrameRateAttributeKey: String ``` |

Modified SCNSceneSourceAnimationImportPolicyDoNotPlay

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAnimationImportPolicyDoNotPlay: NSString! ``` |
| To | ``` let SCNSceneSourceAnimationImportPolicyDoNotPlay: String ``` |

Modified SCNSceneSourceAnimationImportPolicyKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAnimationImportPolicyKey: NSString! ``` |
| To | ``` let SCNSceneSourceAnimationImportPolicyKey: String ``` |

Modified SCNSceneSourceAnimationImportPolicyPlay

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAnimationImportPolicyPlay: NSString! ``` |
| To | ``` let SCNSceneSourceAnimationImportPolicyPlay: String ``` |

Modified SCNSceneSourceAnimationImportPolicyPlayRepeatedly

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAnimationImportPolicyPlayRepeatedly: NSString! ``` |
| To | ``` let SCNSceneSourceAnimationImportPolicyPlayRepeatedly: String ``` |

Modified SCNSceneSourceAnimationImportPolicyPlayUsingSceneTimeBase

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAnimationImportPolicyPlayUsingSceneTimeBase: NSString! ``` |
| To | ``` let SCNSceneSourceAnimationImportPolicyPlayUsingSceneTimeBase: String ``` |

Modified SCNSceneSourceAssetAuthorKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetAuthorKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetAuthorKey: String ``` |

Modified SCNSceneSourceAssetAuthoringToolKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetAuthoringToolKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetAuthoringToolKey: String ``` |

Modified SCNSceneSourceAssetContributorsKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetContributorsKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetContributorsKey: String ``` |

Modified SCNSceneSourceAssetCreatedDateKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetCreatedDateKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetCreatedDateKey: String ``` |

Modified SCNSceneSourceAssetDirectoryURLsKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetDirectoryURLsKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetDirectoryURLsKey: String ``` |

Modified SCNSceneSourceAssetModifiedDateKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetModifiedDateKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetModifiedDateKey: String ``` |

Modified SCNSceneSourceAssetUnitKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetUnitKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetUnitKey: String ``` |

Modified SCNSceneSourceAssetUnitMeterKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetUnitMeterKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetUnitMeterKey: String ``` |

Modified SCNSceneSourceAssetUnitNameKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetUnitNameKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetUnitNameKey: String ``` |

Modified SCNSceneSourceAssetUpAxisKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetUpAxisKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetUpAxisKey: String ``` |

Modified SCNSceneSourceCheckConsistencyKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceCheckConsistencyKey: NSString! ``` |
| To | ``` let SCNSceneSourceCheckConsistencyKey: String ``` |

Modified SCNSceneSourceConvertToYUpKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceConvertToYUpKey: NSString! ``` |
| To | ``` let SCNSceneSourceConvertToYUpKey: String ``` |

Modified SCNSceneSourceConvertUnitsToMetersKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceConvertUnitsToMetersKey: NSString! ``` |
| To | ``` let SCNSceneSourceConvertUnitsToMetersKey: String ``` |

Modified SCNSceneSourceCreateNormalsIfAbsentKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceCreateNormalsIfAbsentKey: NSString! ``` |
| To | ``` let SCNSceneSourceCreateNormalsIfAbsentKey: String ``` |

Modified SCNSceneSourceFlattenSceneKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceFlattenSceneKey: NSString! ``` |
| To | ``` let SCNSceneSourceFlattenSceneKey: String ``` |

Modified SCNSceneSourceOverrideAssetURLsKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceOverrideAssetURLsKey: NSString! ``` |
| To | ``` let SCNSceneSourceOverrideAssetURLsKey: String ``` |

Modified SCNSceneSourceStatusHandler

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNSceneSourceStatusHandler = (Float, SCNSceneSourceStatus, NSError!, UnsafePointer<ObjCBool>) -> Void ``` |
| To | ``` typealias SCNSceneSourceStatusHandler = (Float, SCNSceneSourceStatus, NSError!, UnsafeMutablePointer<ObjCBool>) -> Void ``` |

Modified SCNSceneSourceStrictConformanceKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceStrictConformanceKey: NSString! ``` |
| To | ``` let SCNSceneSourceStrictConformanceKey: String ``` |

Modified SCNSceneSourceUseSafeModeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceUseSafeModeKey: NSString! ``` |
| To | ``` let SCNSceneSourceUseSafeModeKey: String ``` |

Modified SCNSceneStartTimeAttributeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneStartTimeAttributeKey: NSString! ``` |
| To | ``` let SCNSceneStartTimeAttributeKey: String ``` |

Modified SCNSceneUpAxisAttributeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneUpAxisAttributeKey: NSString! ``` |
| To | ``` let SCNSceneUpAxisAttributeKey: String ``` |

Modified SCNShaderModifierEntryPointFragment

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SCNShaderModifierEntryPointFragment: NSString! ``` | OS X 10.10 |
| To | ``` let SCNShaderModifierEntryPointFragment: String ``` | OS X 10.9 |

Modified SCNShaderModifierEntryPointGeometry

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SCNShaderModifierEntryPointGeometry: NSString! ``` | OS X 10.10 |
| To | ``` let SCNShaderModifierEntryPointGeometry: String ``` | OS X 10.9 |

Modified SCNShaderModifierEntryPointLightingModel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SCNShaderModifierEntryPointLightingModel: NSString! ``` | OS X 10.10 |
| To | ``` let SCNShaderModifierEntryPointLightingModel: String ``` | OS X 10.9 |

Modified SCNShaderModifierEntryPointSurface

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SCNShaderModifierEntryPointSurface: NSString! ``` | OS X 10.10 |
| To | ``` let SCNShaderModifierEntryPointSurface: String ``` | OS X 10.9 |

Modified SCNViewTransform

|  | Declaration |
| --- | --- |
| From | ``` let SCNViewTransform: NSString! ``` |
| To | ``` let SCNViewTransform: String ``` |

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
