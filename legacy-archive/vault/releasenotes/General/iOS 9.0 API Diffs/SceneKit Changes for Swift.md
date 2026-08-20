---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/SceneKit.html
archived_at: '2026-07-18T02:56:57.911398Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# SceneKit Changes for Swift

### SceneKit

Removed SCNActionable.hasActions() -> BoolRemoved SCNAnimatable.animationKeys() -> [AnyObject]?Removed SCNNode.presentationNode() -> SCNNodeRemoved SCNPhysicsCollisionCategory.init(_: UInt)Removed SCNPhysicsWorld.allBehaviors() -> [AnyObject]!Removed SCNSceneSource.entryWithIdentifier(_: String, withClass: AnyClass) -> AnyObject?Added double3.init(_: SCNVector3)Added double4.init(_: SCNVector4)Added double4x4.init(_: SCNMatrix4)Added float3.init(_: SCNVector3)Added float4.init(_: SCNVector4)Added float4x4.init(_: SCNMatrix4)Added [SCNAction.hide() -> SCNAction [class]](https://developer.apple.com/documentation/scenekit/scnaction/1523487-hide)Added [SCNAction.playAudioSource(_: SCNAudioSource, waitForCompletion: Bool) -> SCNAction [class]](https://developer.apple.com/documentation/scenekit/scnaction/1523651-playaudio)Added [SCNAction.unhide() -> SCNAction [class]](https://developer.apple.com/documentation/scenekit/scnaction/1524205-unhide)Added [SCNActionable.actionKeys](https://developer.apple.com/documentation/scenekit/scnactionable/1523036-actionkeys)Added [SCNActionable.hasActions](https://developer.apple.com/documentation/scenekit/scnactionable/1523794-hasactions)Added [SCNAnimatable.animationKeys](https://developer.apple.com/documentation/scenekit/scnanimatable/1523610-animationkeys)Added [SCNAudioPlayer](https://developer.apple.com/documentation/scenekit/scnaudioplayer)Added [SCNAudioPlayer.audioNode](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1522747-audionode)Added [SCNAudioPlayer.audioSource](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1523059-audiosource)Added [SCNAudioPlayer.didFinishPlayback](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1522818-didfinishplayback)Added [SCNAudioPlayer.init(AVAudioNode: AVAudioNode)](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1523010-init)Added [SCNAudioPlayer.init(source: SCNAudioSource)](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1522736-initwithsource)Added [SCNAudioPlayer.willStartPlayback](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1524115-willstartplayback)Added [SCNAudioSource](https://developer.apple.com/documentation/scenekit/scnaudiosource)Added [SCNAudioSource.init(fileNamed: String)](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524225-initwithfilenamed)Added [SCNAudioSource.init(named: String)](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524138-audiosourcenamed)Added [SCNAudioSource.init(URL: NSURL)](https://developer.apple.com/documentation/scenekit/scnaudiosource/1523264-initwithurl)Added [SCNAudioSource.load()](https://developer.apple.com/documentation/scenekit/scnaudiosource/1523399-load)Added [SCNAudioSource.loops](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524183-loops)Added [SCNAudioSource.positional](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524185-ispositional)Added [SCNAudioSource.rate](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524189-rate)Added [SCNAudioSource.reverbBlend](https://developer.apple.com/documentation/scenekit/scnaudiosource/1523450-reverbblend)Added [SCNAudioSource.shouldStream](https://developer.apple.com/documentation/scenekit/scnaudiosource/1523475-shouldstream)Added [SCNAudioSource.volume](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524106-volume)Added [SCNBillboardAxis [struct]](https://developer.apple.com/documentation/scenekit/scnbillboardaxis)Added [SCNBillboardAxis.All](https://developer.apple.com/documentation/scenekit/scnbillboardaxis/1468666-all)Added SCNBillboardAxis.init(rawValue: UInt)Added [SCNBillboardAxis.X](https://developer.apple.com/documentation/scenekit/scnbillboardaxis/1468664-x)Added [SCNBillboardAxis.Y](https://developer.apple.com/documentation/scenekit/scnbillboardaxis/1468668-y)Added [SCNBillboardAxis.Z](https://developer.apple.com/documentation/scenekit/scnbillboardaxis/1468647-z)Added [SCNBillboardConstraint](https://developer.apple.com/documentation/scenekit/scnbillboardconstraint)Added [SCNBillboardConstraint.freeAxes](https://developer.apple.com/documentation/scenekit/scnbillboardconstraint/1468685-freeaxes)Added [SCNBlendMode [enum]](https://developer.apple.com/documentation/scenekit/scnblendmode)Added [SCNBlendMode.Add](https://developer.apple.com/documentation/scenekit/scnblendmode/scnblendmodeadd)Added [SCNBlendMode.Alpha](https://developer.apple.com/documentation/scenekit/scnblendmode/scnblendmodealpha)Added [SCNBlendMode.Multiply](https://developer.apple.com/documentation/scenekit/scnblendmode/multiply)Added [SCNBlendMode.Replace](https://developer.apple.com/documentation/scenekit/scnblendmode/scnblendmodereplace)Added [SCNBlendMode.Screen](https://developer.apple.com/documentation/scenekit/scnblendmode/screen)Added [SCNBlendMode.Subtract](https://developer.apple.com/documentation/scenekit/scnblendmode/scnblendmodesubtract)Added [SCNBufferFrequency [enum]](https://developer.apple.com/documentation/scenekit/scnbufferfrequency)Added [SCNBufferFrequency.PerFrame](https://developer.apple.com/documentation/scenekit/scnbufferfrequency/perframe)Added [SCNBufferFrequency.PerNode](https://developer.apple.com/documentation/scenekit/scnbufferfrequency/scnbufferfrequencypernode)Added [SCNBufferFrequency.PerShadable](https://developer.apple.com/documentation/scenekit/scnbufferfrequency/pershadable)Added [SCNBufferStream](https://developer.apple.com/documentation/scenekit/scnbufferstream)Added [SCNBufferStream.writeBytes(_: UnsafeMutablePointer<Void>, length: Int)](https://developer.apple.com/documentation/scenekit/scnbufferstream/1523175-writebytes)Added [SCNDebugOptions [struct]](https://developer.apple.com/documentation/scenekit/scndebugoptions)Added SCNDebugOptions.init(rawValue: UInt)Added [SCNDebugOptions.None](https://developer.apple.com/documentation/scenekit/scndebugoptions/scndebugoptionnone)Added [SCNDebugOptions.ShowBoundingBoxes](https://developer.apple.com/documentation/scenekit/scndebugoptions/scndebugoptionshowboundingboxes)Added [SCNDebugOptions.ShowLightExtents](https://developer.apple.com/documentation/scenekit/scndebugoptions/scndebugoptionshowlightextents)Added [SCNDebugOptions.ShowLightInfluences](https://developer.apple.com/documentation/scenekit/scndebugoptions/scndebugoptionshowlightinfluences)Added [SCNDebugOptions.ShowPhysicsFields](https://developer.apple.com/documentation/scenekit/scndebugoptions/scndebugoptionshowphysicsfields)Added [SCNDebugOptions.ShowPhysicsShapes](https://developer.apple.com/documentation/scenekit/scndebugoptions/1522896-showphysicsshapes)Added [SCNDebugOptions.ShowWireframe](https://developer.apple.com/documentation/scenekit/scndebugoptions/scndebugoptionshowwireframe)Added [SCNGeometry.geometryElements](https://developer.apple.com/documentation/scenekit/scngeometry/1523046-geometryelements)Added [SCNGeometry.geometrySources](https://developer.apple.com/documentation/scenekit/scngeometry/1523662-sources)Added SCNGeometryElement.init<IndexType : IntegerType>(indices: [IndexType], primitiveType: SCNGeometryPrimitiveType)Added [SCNGeometrySource.init(buffer: MTLBuffer, vertexFormat: MTLVertexFormat, semantic: String, vertexCount: Int, dataOffset: Int, dataStride: Int)](https://developer.apple.com/documentation/scenekit/scngeometrysource/1522873-init)Added [SCNIKConstraint.init(chainRootNode: SCNNode)](https://developer.apple.com/documentation/scenekit/scnikconstraint/1468694-init)Added [SCNMaterial.ambientOcclusion](https://developer.apple.com/documentation/scenekit/scnmaterial/1462579-ambientocclusion)Added [SCNMaterial.blendMode](https://developer.apple.com/documentation/scenekit/scnmaterial/1462585-blendmode)Added [SCNMaterial.selfIllumination](https://developer.apple.com/documentation/scenekit/scnmaterial/1462524-selfillumination)Added SCNMatrix4.init(_: double4x4)Added SCNMatrix4.init(_: float4x4)Added [SCNNode.addAudioPlayer(_: SCNAudioPlayer)](https://developer.apple.com/documentation/scenekit/scnnode/1523464-addaudioplayer)Added [SCNNode.audioPlayers](https://developer.apple.com/documentation/scenekit/scnnode/1523244-audioplayers)Added [SCNNode.presentationNode](https://developer.apple.com/documentation/scenekit/scnnode/1408030-presentation)Added [SCNNode.removeAllAudioPlayers()](https://developer.apple.com/documentation/scenekit/scnnode/1523570-removeallaudioplayers)Added [SCNNode.removeAudioPlayer(_: SCNAudioPlayer)](https://developer.apple.com/documentation/scenekit/scnnode/1522767-removeaudioplayer)Added [SCNPhysicsBody.affectedByGravity](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514738-affectedbygravity)Added [SCNPhysicsBody.contactTestBitMask](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514746-contacttestbitmask)Added [SCNPhysicsBody.momentOfInertia](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514777-momentofinertia)Added [SCNPhysicsBody.usesDefaultMomentOfInertia](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514761-usesdefaultmomentofinertia)Added [SCNPhysicsShape.options](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508904-options)Added [SCNPhysicsShape.sourceObject](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508888-sourceobject)Added [SCNPhysicsShape.transforms](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508898-transforms)Added [SCNPhysicsWorld.allBehaviors](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512853-allbehaviors)Added [SCNProgram.fragmentFunctionName](https://developer.apple.com/documentation/scenekit/scnprogram/1524012-fragmentfunctionname)Added [SCNProgram.handleBindingOfBufferNamed(_: String, frequency: SCNBufferFrequency, usingBlock: SCNBufferBindingBlock)](https://developer.apple.com/documentation/scenekit/scnprogram/1524047-handlebindingofbuffernamed)Added [SCNProgram.library](https://developer.apple.com/documentation/scenekit/scnprogram/1522934-library)Added [SCNProgram.vertexFunctionName](https://developer.apple.com/documentation/scenekit/scnprogram/1522799-vertexfunctionname)Added [SCNReferenceLoadingPolicy [enum]](https://developer.apple.com/documentation/scenekit/scnreferenceloadingpolicy)Added [SCNReferenceLoadingPolicy.Immediate](https://developer.apple.com/documentation/scenekit/scnreferenceloadingpolicy/scnreferenceloadingpolicyimmediate)Added [SCNReferenceLoadingPolicy.OnDemand](https://developer.apple.com/documentation/scenekit/scnreferenceloadingpolicy/scnreferenceloadingpolicyondemand)Added [SCNReferenceNode](https://developer.apple.com/documentation/scenekit/scnreferencenode)Added [SCNReferenceNode.init(coder: NSCoder)](https://developer.apple.com/documentation/scenekit/scnreferencenode/1524061-initwithcoder)Added [SCNReferenceNode.init(URL: NSURL)](https://developer.apple.com/documentation/scenekit/scnreferencenode/1523967-initwithurl)Added [SCNReferenceNode.load()](https://developer.apple.com/documentation/scenekit/scnreferencenode/1523204-load)Added [SCNReferenceNode.loaded](https://developer.apple.com/documentation/scenekit/scnreferencenode/1523906-loaded)Added [SCNReferenceNode.loadingPolicy](https://developer.apple.com/documentation/scenekit/scnreferencenode/1522996-loadingpolicy)Added [SCNReferenceNode.referenceURL](https://developer.apple.com/documentation/scenekit/scnreferencenode/1522733-referenceurl)Added [SCNReferenceNode.unload()](https://developer.apple.com/documentation/scenekit/scnreferencenode/1523566-unload)Added [SCNRenderer.init(device: MTLDevice?, options: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/scenekit/scnrenderer/1518404-init)Added [SCNRenderer.renderAtTime(_: CFTimeInterval, viewport: CGRect, commandBuffer: MTLCommandBuffer, passDescriptor: MTLRenderPassDescriptor)](https://developer.apple.com/documentation/scenekit/scnrenderer/1518401-render)Added [SCNRenderingAPI [enum]](https://developer.apple.com/documentation/scenekit/scnrenderingapi)Added [SCNRenderingAPI.Metal](https://developer.apple.com/documentation/scenekit/scnrenderingapi/metal)Added [SCNRenderingAPI.OpenGLES2](https://developer.apple.com/documentation/scenekit/scnrenderingapi/scnrenderingapiopengles2)Added [SCNSceneRenderer.audioEngine](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522686-audioengine)Added [SCNSceneRenderer.audioEnvironmentNode](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523582-audioenvironmentnode)Added [SCNSceneRenderer.audioListener](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523747-audiolistener)Added [SCNSceneRenderer.colorPixelFormat](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523701-colorpixelformat)Added [SCNSceneRenderer.commandQueue](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523974-commandqueue)Added [SCNSceneRenderer.currentRenderCommandEncoder](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522609-currentrendercommandencoder)Added [SCNSceneRenderer.debugOptions](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523281-debugoptions)Added [SCNSceneRenderer.depthPixelFormat](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523780-depthpixelformat)Added [SCNSceneRenderer.device](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523935-device)Added [SCNSceneRenderer.nodesInsideFrustumWithPointOfView(_: SCNNode) -> [SCNNode]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522942-nodesinsidefrustum)Added [SCNSceneRenderer.presentScene(_: SCNScene, withTransition: SKTransition, incomingPointOfView: SCNNode?, completionHandler: (() -> Void)?)](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523028-presentscene)Added [SCNSceneRenderer.renderingAPI](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522616-renderingapi)Added [SCNSceneRenderer.stencilPixelFormat](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523315-stencilpixelformat)Added SCNSceneSource.entryWithIdentifier<T>(_: String, withClass: T.Type) -> T?Added [SCNTechnique.setObject(_: AnyObject?, forKeyedSubscript: NSCopying)](https://developer.apple.com/documentation/scenekit/scntechnique/1520495-setobject)Added [SCNTechnique.subscript(_: AnyObject) -> AnyObject?](https://developer.apple.com/documentation/scenekit/scntechnique/1520493-objectforkeyedsubscript)Added SCNVector3.init(_: float3)Added SCNVector3.init(_: double3)Added SCNVector3.init(_: CGFloat, _: CGFloat, _: CGFloat)Added SCNVector3.init(_: Int, _: Int, _: Int)Added SCNVector3.init(_: Float, _: Float, _: Float)Added SCNVector3.init(_: Double, _: Double, _: Double)Added SCNVector4.init(_: double4)Added SCNVector4.init(_: float4)Added SCNVector4.init(_: Int, _: Int, _: Int, _: Int)Added SCNVector4.init(_: Double, _: Double, _: Double, _: Double)Added SCNVector4.init(_: Float, _: Float, _: Float, _: Float)Added SCNVector4.init(_: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)Added [SCNWrapMode.ClampToBorder](https://developer.apple.com/documentation/scenekit/scnwrapmode/scnwrapmodeclamptoborder)Added [SCNBufferBindingBlock](https://developer.apple.com/documentation/scenekit/scnbufferbindingblock)Added [SCNFloat](https://developer.apple.com/documentation/scenekit/scnfloat)Added [SCNPreferLowPowerDeviceKey](https://developer.apple.com/documentation/scenekit/scnview/option/1522859-preferlowpowerdevice)Added [SCNPreferredDeviceKey](https://developer.apple.com/documentation/scenekit/scnpreferreddevicekey)Added [SCNPreferredRenderingAPIKey](https://developer.apple.com/documentation/scenekit/scnpreferredrenderingapikey)Added [SCNVector3FromFloat3(_: vector_float3) -> SCNVector3](https://developer.apple.com/documentation/scenekit/1524143-scnvector3fromfloat3)Added [SCNVector3ToFloat3(_: SCNVector3) -> vector_float3](https://developer.apple.com/documentation/scenekit/1523448-scnvector3tofloat3)Added [SCNVector4FromFloat4(_: vector_float4) -> SCNVector4](https://developer.apple.com/documentation/scenekit/1523606-scnvector4fromfloat4)Added [SCNVector4ToFloat4(_: SCNVector4) -> vector_float4](https://developer.apple.com/documentation/scenekit/1523001-scnvector4tofloat4)Modified [CAAnimation.animationEvents](https://developer.apple.com/documentation/quartzcore/caanimation/1523940-animationevents)

|  | Declaration |
| --- | --- |
| From | ``` var animationEvents: [AnyObject]! ``` |
| To | ``` var animationEvents: [SCNAnimationEvent]? ``` |

Modified [NSValue.init(SCNMatrix4: SCNMatrix4)](https://developer.apple.com/documentation/foundation/nsvalue/1409680-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(SCNMatrix4 v: SCNMatrix4) -> NSValue ``` |
| To | ``` init(SCNMatrix4 v: SCNMatrix4) ``` |

Modified [NSValue.init(SCNVector3: SCNVector3)](https://developer.apple.com/documentation/foundation/nsvalue/1409671-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(SCNVector3 v: SCNVector3) -> NSValue ``` |
| To | ``` init(SCNVector3 v: SCNVector3) ``` |

Modified [NSValue.init(SCNVector4: SCNVector4)](https://developer.apple.com/documentation/foundation/nsvalue/1409688-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(SCNVector4 v: SCNVector4) -> NSValue ``` |
| To | ``` init(SCNVector4 v: SCNVector4) ``` |

Modified [SCNAction](https://developer.apple.com/documentation/scenekit/scnaction)

|  | Declaration |
| --- | --- |
| From | ``` class SCNAction : NSObject, NSCopying, NSSecureCoding, NSCoding {     var duration: NSTimeInterval     var timingMode: SCNActionTimingMode     var timingFunction: SCNActionTimingFunction?     var speed: CGFloat     func reversedAction() -> SCNAction } extension SCNAction {     class func moveByX(_ deltaX: CGFloat, y deltaY: CGFloat, z deltaZ: CGFloat, duration duration: NSTimeInterval) -> SCNAction     class func moveBy(_ delta: SCNVector3, duration duration: NSTimeInterval) -> SCNAction     class func moveTo(_ location: SCNVector3, duration duration: NSTimeInterval) -> SCNAction     class func rotateByX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval) -> SCNAction     class func rotateToX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval) -> SCNAction     class func rotateToX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SCNAction     class func rotateByAngle(_ angle: CGFloat, aroundAxis axis: SCNVector3, duration duration: NSTimeInterval) -> SCNAction     class func rotateToAxisAngle(_ axisAngle: SCNVector4, duration duration: NSTimeInterval) -> SCNAction     class func scaleBy(_ scale: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func scaleTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func sequence(_ actions: [AnyObject]) -> SCNAction     class func group(_ actions: [AnyObject]) -> SCNAction     class func repeatAction(_ action: SCNAction, count count: Int) -> SCNAction     class func repeatActionForever(_ action: SCNAction) -> SCNAction     class func fadeInWithDuration(_ sec: NSTimeInterval) -> SCNAction     class func fadeOutWithDuration(_ sec: NSTimeInterval) -> SCNAction     class func fadeOpacityBy(_ factor: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func fadeOpacityTo(_ opacity: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func waitForDuration(_ sec: NSTimeInterval) -> SCNAction     class func waitForDuration(_ sec: NSTimeInterval, withRange durationRange: NSTimeInterval) -> SCNAction     class func removeFromParentNode() -> SCNAction     class func runBlock(_ block: (SCNNode!) -> Void) -> SCNAction     class func runBlock(_ block: (SCNNode!) -> Void, queue queue: dispatch_queue_t?) -> SCNAction     class func javaScriptActionWithScript(_ script: String, duration seconds: NSTimeInterval) -> SCNAction     class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SCNNode!, CGFloat) -> Void) -> SCNAction } ``` |
| To | ``` class SCNAction : NSObject, NSCopying, NSSecureCoding, NSCoding {     var duration: NSTimeInterval     var timingMode: SCNActionTimingMode     var timingFunction: SCNActionTimingFunction?     var speed: CGFloat     func reversedAction() -> SCNAction     class func moveByX(_ deltaX: CGFloat, y deltaY: CGFloat, z deltaZ: CGFloat, duration duration: NSTimeInterval) -> SCNAction     class func moveBy(_ delta: SCNVector3, duration duration: NSTimeInterval) -> SCNAction     class func moveTo(_ location: SCNVector3, duration duration: NSTimeInterval) -> SCNAction     class func rotateByX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval) -> SCNAction     class func rotateToX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval) -> SCNAction     class func rotateToX(_ xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration duration: NSTimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SCNAction     class func rotateByAngle(_ angle: CGFloat, aroundAxis axis: SCNVector3, duration duration: NSTimeInterval) -> SCNAction     class func rotateToAxisAngle(_ axisAngle: SCNVector4, duration duration: NSTimeInterval) -> SCNAction     class func scaleBy(_ scale: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func scaleTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func sequence(_ actions: [SCNAction]) -> SCNAction     class func group(_ actions: [SCNAction]) -> SCNAction     class func repeatAction(_ action: SCNAction, count count: Int) -> SCNAction     class func repeatActionForever(_ action: SCNAction) -> SCNAction     class func fadeInWithDuration(_ sec: NSTimeInterval) -> SCNAction     class func fadeOutWithDuration(_ sec: NSTimeInterval) -> SCNAction     class func fadeOpacityBy(_ factor: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func fadeOpacityTo(_ opacity: CGFloat, duration sec: NSTimeInterval) -> SCNAction     class func hide() -> SCNAction     class func unhide() -> SCNAction     class func waitForDuration(_ sec: NSTimeInterval) -> SCNAction     class func waitForDuration(_ sec: NSTimeInterval, withRange durationRange: NSTimeInterval) -> SCNAction     class func removeFromParentNode() -> SCNAction     class func runBlock(_ block: (SCNNode) -> Void) -> SCNAction     class func runBlock(_ block: (SCNNode) -> Void, queue queue: dispatch_queue_t) -> SCNAction     class func javaScriptActionWithScript(_ script: String, duration seconds: NSTimeInterval) -> SCNAction     class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SCNNode, CGFloat) -> Void) -> SCNAction     class func playAudioSource(_ source: SCNAudioSource, waitForCompletion wait: Bool) -> SCNAction } ``` |

Modified [SCNAction.customActionWithDuration(_: NSTimeInterval, actionBlock: (SCNNode, CGFloat) -> Void) -> SCNAction [class]](https://developer.apple.com/documentation/scenekit/scnaction/1523692-customactionwithduration)

|  | Declaration |
| --- | --- |
| From | ``` class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SCNNode!, CGFloat) -> Void) -> SCNAction ``` |
| To | ``` class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SCNNode, CGFloat) -> Void) -> SCNAction ``` |

Modified [SCNAction.group(_: [SCNAction]) -> SCNAction [class]](https://developer.apple.com/documentation/scenekit/scnaction/1522779-group)

|  | Declaration |
| --- | --- |
| From | ``` class func group(_ actions: [AnyObject]) -> SCNAction ``` |
| To | ``` class func group(_ actions: [SCNAction]) -> SCNAction ``` |

Modified [SCNAction.runBlock(_: (SCNNode) -> Void) -> SCNAction [class]](https://developer.apple.com/documentation/scenekit/scnaction/1523637-run)

|  | Declaration |
| --- | --- |
| From | ``` class func runBlock(_ block: (SCNNode!) -> Void) -> SCNAction ``` |
| To | ``` class func runBlock(_ block: (SCNNode) -> Void) -> SCNAction ``` |

Modified [SCNAction.runBlock(_: (SCNNode) -> Void, queue: dispatch_queue_t) -> SCNAction [class]](https://developer.apple.com/documentation/scenekit/scnaction/1522875-runblock)

|  | Declaration |
| --- | --- |
| From | ``` class func runBlock(_ block: (SCNNode!) -> Void, queue queue: dispatch_queue_t?) -> SCNAction ``` |
| To | ``` class func runBlock(_ block: (SCNNode) -> Void, queue queue: dispatch_queue_t) -> SCNAction ``` |

Modified [SCNAction.sequence(_: [SCNAction]) -> SCNAction [class]](https://developer.apple.com/documentation/scenekit/scnaction/1522793-sequence)

|  | Declaration |
| --- | --- |
| From | ``` class func sequence(_ actions: [AnyObject]) -> SCNAction ``` |
| To | ``` class func sequence(_ actions: [SCNAction]) -> SCNAction ``` |

Modified [SCNActionable](https://developer.apple.com/documentation/scenekit/scnactionable)

|  | Declaration |
| --- | --- |
| From | ``` protocol SCNActionable : NSObjectProtocol {     func runAction(_ action: SCNAction)     func runAction(_ action: SCNAction, completionHandler block: (() -> Void)?)     func runAction(_ action: SCNAction, forKey key: String?)     func runAction(_ action: SCNAction, forKey key: String?, completionHandler block: (() -> Void)?)     func hasActions() -> Bool     func actionForKey(_ key: String) -> SCNAction?     func removeActionForKey(_ key: String)     func removeAllActions() } ``` |
| To | ``` protocol SCNActionable : NSObjectProtocol {     func runAction(_ action: SCNAction)     func runAction(_ action: SCNAction, completionHandler block: (() -> Void)?)     func runAction(_ action: SCNAction, forKey key: String?)     func runAction(_ action: SCNAction, forKey key: String?, completionHandler block: (() -> Void)?)     var hasActions: Bool { get }     func actionForKey(_ key: String) -> SCNAction?     func removeActionForKey(_ key: String)     func removeAllActions()     var actionKeys: [String] { get } } ``` |

Modified [SCNActionTimingMode [enum]](https://developer.apple.com/documentation/scenekit/scnactiontimingmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SCNAnimatable](https://developer.apple.com/documentation/scenekit/scnanimatable)

|  | Declaration |
| --- | --- |
| From | ``` protocol SCNAnimatable : NSObjectProtocol {     func addAnimation(_ animation: CAAnimation, forKey key: String?)     func removeAllAnimations()     func removeAnimationForKey(_ key: String)     func animationKeys() -> [AnyObject]?     func animationForKey(_ key: String) -> CAAnimation?     func pauseAnimationForKey(_ key: String)     func resumeAnimationForKey(_ key: String)     func isAnimationForKeyPaused(_ key: String) -> Bool     func removeAnimationForKey(_ key: String, fadeOutDuration duration: CGFloat) } ``` |
| To | ``` protocol SCNAnimatable : NSObjectProtocol {     func addAnimation(_ animation: CAAnimation, forKey key: String?)     func removeAllAnimations()     func removeAnimationForKey(_ key: String)     var animationKeys: [String] { get }     func animationForKey(_ key: String) -> CAAnimation?     func pauseAnimationForKey(_ key: String)     func resumeAnimationForKey(_ key: String)     func isAnimationForKeyPaused(_ key: String) -> Bool     func removeAnimationForKey(_ key: String, fadeOutDuration duration: CGFloat) } ``` |

Modified [SCNAnimationEvent](https://developer.apple.com/documentation/scenekit/scnanimationevent)

|  | Declaration |
| --- | --- |
| From | ``` class SCNAnimationEvent : NSObject {     convenience init(keyTime time: CGFloat, block eventBlock: SCNAnimationEventBlock!)     class func animationEventWithKeyTime(_ time: CGFloat, block eventBlock: SCNAnimationEventBlock!) -> Self } ``` |
| To | ``` class SCNAnimationEvent : NSObject {     convenience init(keyTime time: CGFloat, block eventBlock: SCNAnimationEventBlock)     class func animationEventWithKeyTime(_ time: CGFloat, block eventBlock: SCNAnimationEventBlock) -> Self } ``` |

Modified [SCNAnimationEvent.init(keyTime: CGFloat, block: SCNAnimationEventBlock)](https://developer.apple.com/documentation/scenekit/scnanimationevent/1524004-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(keyTime time: CGFloat, block eventBlock: SCNAnimationEventBlock!) ``` |
| To | ``` convenience init(keyTime time: CGFloat, block eventBlock: SCNAnimationEventBlock) ``` |

Modified [SCNAntialiasingMode [enum]](https://developer.apple.com/documentation/scenekit/scnantialiasingmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [SCNCamera](https://developer.apple.com/documentation/scenekit/scncamera)

|  | Declaration |
| --- | --- |
| From | ``` class SCNCamera : NSObject, SCNAnimatable, NSObjectProtocol, SCNTechniqueSupport, NSCopying, NSSecureCoding, NSCoding {     convenience init!()     class func camera() -> Self!     var name: String?     var xFov: Double     var yFov: Double     var zNear: Double     var zFar: Double     var automaticallyAdjustsZRange: Bool     var usesOrthographicProjection: Bool     var orthographicScale: Double     func projectionTransform() -> SCNMatrix4     func setProjectionTransform(_ projectionTransform: SCNMatrix4)     var focalDistance: CGFloat     var focalSize: CGFloat     var focalBlurRadius: CGFloat     var aperture: CGFloat     var categoryBitMask: Int } ``` |
| To | ``` class SCNCamera : NSObject, SCNAnimatable, SCNTechniqueSupport, NSCopying, NSSecureCoding, NSCoding {     convenience init()     class func camera() -> Self     var name: String?     var xFov: Double     var yFov: Double     var zNear: Double     var zFar: Double     var automaticallyAdjustsZRange: Bool     var usesOrthographicProjection: Bool     var orthographicScale: Double     func projectionTransform() -> SCNMatrix4     func setProjectionTransform(_ projectionTransform: SCNMatrix4)     var focalDistance: CGFloat     var focalSize: CGFloat     var focalBlurRadius: CGFloat     var aperture: CGFloat     var categoryBitMask: Int } ``` |

Modified [SCNChamferMode [enum]](https://developer.apple.com/documentation/scenekit/scnchamfermode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SCNConstraint](https://developer.apple.com/documentation/scenekit/scnconstraint)

|  | Declaration |
| --- | --- |
| From | ``` class SCNConstraint : NSObject, NSCopying, NSSecureCoding, NSCoding, SCNAnimatable, NSObjectProtocol {     var influenceFactor: CGFloat } ``` |
| To | ``` class SCNConstraint : NSObject, NSCopying, NSSecureCoding, NSCoding, SCNAnimatable {     var influenceFactor: CGFloat } ``` |

Modified [SCNCullMode [enum]](https://developer.apple.com/documentation/scenekit/scncullmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SCNFilterMode [enum]](https://developer.apple.com/documentation/scenekit/scnfiltermode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SCNFloor](https://developer.apple.com/documentation/scenekit/scnfloor)

|  | Declaration |
| --- | --- |
| From | ``` class SCNFloor : SCNGeometry {     convenience init!()     class func floor() -> Self!     var reflectivity: CGFloat     var reflectionFalloffStart: CGFloat     var reflectionFalloffEnd: CGFloat     var reflectionResolutionScaleFactor: CGFloat } ``` |
| To | ``` class SCNFloor : SCNGeometry {     convenience init()     class func floor() -> Self     var reflectivity: CGFloat     var reflectionFalloffStart: CGFloat     var reflectionFalloffEnd: CGFloat     var reflectionResolutionScaleFactor: CGFloat } ``` |

Modified [SCNGeometry](https://developer.apple.com/documentation/scenekit/scngeometry)

|  | Declaration |
| --- | --- |
| From | ``` class SCNGeometry : NSObject, SCNAnimatable, NSObjectProtocol, SCNBoundingVolume, SCNShadable, NSCopying, NSSecureCoding, NSCoding {     convenience init!()     class func geometry() -> Self!     var name: String?     var materials: [AnyObject]?     var firstMaterial: SCNMaterial?     func insertMaterial(_ material: SCNMaterial, atIndex index: Int)     func removeMaterialAtIndex(_ index: Int)     func replaceMaterialAtIndex(_ index: Int, withMaterial material: SCNMaterial)     func materialWithName(_ name: String) -> SCNMaterial?     convenience init(sources sources: [AnyObject], elements elements: [AnyObject]?)     class func geometryWithSources(_ sources: [AnyObject], elements elements: [AnyObject]?) -> Self     func geometrySourcesForSemantic(_ semantic: String) -> [AnyObject]?     var geometryElementCount: Int { get }     func geometryElementAtIndex(_ elementIndex: Int) -> SCNGeometryElement?     var levelsOfDetail: [AnyObject]?     var subdivisionLevel: Int     var edgeCreasesElement: SCNGeometryElement?     var edgeCreasesSource: SCNGeometrySource? } ``` |
| To | ``` class SCNGeometry : NSObject, SCNAnimatable, SCNBoundingVolume, SCNShadable, NSCopying, NSSecureCoding, NSCoding {     convenience init()     class func geometry() -> Self     var name: String?     var materials: [SCNMaterial]     var firstMaterial: SCNMaterial?     func insertMaterial(_ material: SCNMaterial, atIndex index: Int)     func removeMaterialAtIndex(_ index: Int)     func replaceMaterialAtIndex(_ index: Int, withMaterial material: SCNMaterial)     func materialWithName(_ name: String) -> SCNMaterial?     convenience init(sources sources: [SCNGeometrySource], elements elements: [SCNGeometryElement])     class func geometryWithSources(_ sources: [SCNGeometrySource], elements elements: [SCNGeometryElement]) -> Self     var geometrySources: [SCNGeometrySource] { get }     func geometrySourcesForSemantic(_ semantic: String) -> [SCNGeometrySource]     var geometryElements: [SCNGeometryElement] { get }     var geometryElementCount: Int { get }     func geometryElementAtIndex(_ elementIndex: Int) -> SCNGeometryElement     var levelsOfDetail: [SCNLevelOfDetail]?     var subdivisionLevel: Int     var edgeCreasesElement: SCNGeometryElement?     var edgeCreasesSource: SCNGeometrySource? } ``` |

Modified [SCNGeometry.geometryElementAtIndex(_: Int) -> SCNGeometryElement](https://developer.apple.com/documentation/scenekit/scngeometry/1523266-geometryelementatindex)

|  | Declaration |
| --- | --- |
| From | ``` func geometryElementAtIndex(_ elementIndex: Int) -> SCNGeometryElement? ``` |
| To | ``` func geometryElementAtIndex(_ elementIndex: Int) -> SCNGeometryElement ``` |

Modified [SCNGeometry.geometrySourcesForSemantic(_: String) -> [SCNGeometrySource]](https://developer.apple.com/documentation/scenekit/scngeometry/1522926-sources)

|  | Declaration |
| --- | --- |
| From | ``` func geometrySourcesForSemantic(_ semantic: String) -> [AnyObject]? ``` |
| To | ``` func geometrySourcesForSemantic(_ semantic: String) -> [SCNGeometrySource] ``` |

Modified [SCNGeometry.init(sources: [SCNGeometrySource], elements: [SCNGeometryElement])](https://developer.apple.com/documentation/scenekit/scngeometry/1522803-geometrywithsources)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(sources sources: [AnyObject], elements elements: [AnyObject]?) ``` |
| To | ``` convenience init(sources sources: [SCNGeometrySource], elements elements: [SCNGeometryElement]) ``` |

Modified [SCNGeometry.levelsOfDetail](https://developer.apple.com/documentation/scenekit/scngeometry/1523745-levelsofdetail)

|  | Declaration |
| --- | --- |
| From | ``` var levelsOfDetail: [AnyObject]? ``` |
| To | ``` var levelsOfDetail: [SCNLevelOfDetail]? ``` |

Modified [SCNGeometry.materials](https://developer.apple.com/documentation/scenekit/scngeometry/1523472-materials)

|  | Declaration |
| --- | --- |
| From | ``` var materials: [AnyObject]? ``` |
| To | ``` var materials: [SCNMaterial] ``` |

Modified [SCNGeometryElement](https://developer.apple.com/documentation/scenekit/scngeometryelement)

|  | Declaration |
| --- | --- |
| From | ``` class SCNGeometryElement : NSObject, NSSecureCoding, NSCoding {     convenience init(data data: NSData, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int)     class func geometryElementWithData(_ data: NSData, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int) -> Self     var data: NSData? { get }     var primitiveType: SCNGeometryPrimitiveType { get }     var primitiveCount: Int { get }     var bytesPerIndex: Int { get } } ``` |
| To | ``` class SCNGeometryElement : NSObject, NSSecureCoding, NSCoding {     convenience init(data data: NSData?, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int)     class func geometryElementWithData(_ data: NSData?, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int) -> Self     var data: NSData { get }     var primitiveType: SCNGeometryPrimitiveType { get }     var primitiveCount: Int { get }     var bytesPerIndex: Int { get } } extension SCNGeometryElement {     convenience init<IndexType : IntegerType>(indices indices: [IndexType], primitiveType primitiveType: SCNGeometryPrimitiveType) } extension SCNGeometryElement {     convenience init<IndexType : IntegerType>(indices indices: [IndexType], primitiveType primitiveType: SCNGeometryPrimitiveType) } ``` |

Modified [SCNGeometryElement.data](https://developer.apple.com/documentation/scenekit/scngeometryelement/1523367-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData? { get } ``` |
| To | ``` var data: NSData { get } ``` |

Modified [SCNGeometryElement.init(data: NSData?, primitiveType: SCNGeometryPrimitiveType, primitiveCount: Int, bytesPerIndex: Int)](https://developer.apple.com/documentation/scenekit/scngeometryelement/1522615-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data data: NSData, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int) ``` |
| To | ``` convenience init(data data: NSData?, primitiveType primitiveType: SCNGeometryPrimitiveType, primitiveCount primitiveCount: Int, bytesPerIndex bytesPerIndex: Int) ``` |

Modified [SCNGeometryPrimitiveType [enum]](https://developer.apple.com/documentation/scenekit/scngeometryprimitivetype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SCNGeometrySource](https://developer.apple.com/documentation/scenekit/scngeometrysource)

|  | Declaration |
| --- | --- |
| From | ``` class SCNGeometrySource : NSObject, NSSecureCoding, NSCoding {     convenience init(data data: NSData, semantic semantic: String, vectorCount vectorCount: Int, floatComponents floatComponents: Bool, componentsPerVector componentsPerVector: Int, bytesPerComponent bytesPerComponent: Int, dataOffset offset: Int, dataStride stride: Int)     class func geometrySourceWithData(_ data: NSData, semantic semantic: String, vectorCount vectorCount: Int, floatComponents floatComponents: Bool, componentsPerVector componentsPerVector: Int, bytesPerComponent bytesPerComponent: Int, dataOffset offset: Int, dataStride stride: Int) -> Self     convenience init(vertices vertices: UnsafePointer<SCNVector3>, count count: Int)     class func geometrySourceWithVertices(_ vertices: UnsafePointer<SCNVector3>, count count: Int) -> Self     convenience init(normals normals: UnsafePointer<SCNVector3>, count count: Int)     class func geometrySourceWithNormals(_ normals: UnsafePointer<SCNVector3>, count count: Int) -> Self     convenience init(textureCoordinates texcoord: UnsafePointer<CGPoint>, count count: Int)     class func geometrySourceWithTextureCoordinates(_ texcoord: UnsafePointer<CGPoint>, count count: Int) -> Self     var data: NSData? { get }     var semantic: String { get }     var vectorCount: Int { get }     var floatComponents: Bool { get }     var componentsPerVector: Int { get }     var bytesPerComponent: Int { get }     var dataOffset: Int { get }     var dataStride: Int { get } } ``` |
| To | ``` class SCNGeometrySource : NSObject, NSSecureCoding, NSCoding {     convenience init(data data: NSData, semantic semantic: String, vectorCount vectorCount: Int, floatComponents floatComponents: Bool, componentsPerVector componentsPerVector: Int, bytesPerComponent bytesPerComponent: Int, dataOffset offset: Int, dataStride stride: Int)     class func geometrySourceWithData(_ data: NSData, semantic semantic: String, vectorCount vectorCount: Int, floatComponents floatComponents: Bool, componentsPerVector componentsPerVector: Int, bytesPerComponent bytesPerComponent: Int, dataOffset offset: Int, dataStride stride: Int) -> Self     convenience init(vertices vertices: UnsafePointer<SCNVector3>, count count: Int)     class func geometrySourceWithVertices(_ vertices: UnsafePointer<SCNVector3>, count count: Int) -> Self     convenience init(normals normals: UnsafePointer<SCNVector3>, count count: Int)     class func geometrySourceWithNormals(_ normals: UnsafePointer<SCNVector3>, count count: Int) -> Self     convenience init(textureCoordinates texcoord: UnsafePointer<CGPoint>, count count: Int)     class func geometrySourceWithTextureCoordinates(_ texcoord: UnsafePointer<CGPoint>, count count: Int) -> Self     convenience init(buffer mtlBuffer: MTLBuffer, vertexFormat vertexFormat: MTLVertexFormat, semantic semantic: String, vertexCount vertexCount: Int, dataOffset offset: Int, dataStride stride: Int)     class func geometrySourceWithBuffer(_ mtlBuffer: MTLBuffer, vertexFormat vertexFormat: MTLVertexFormat, semantic semantic: String, vertexCount vertexCount: Int, dataOffset offset: Int, dataStride stride: Int) -> Self     var data: NSData { get }     var semantic: String { get }     var vectorCount: Int { get }     var floatComponents: Bool { get }     var componentsPerVector: Int { get }     var bytesPerComponent: Int { get }     var dataOffset: Int { get }     var dataStride: Int { get } } ``` |

Modified [SCNGeometrySource.data](https://developer.apple.com/documentation/scenekit/scngeometrysource/1522881-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData? { get } ``` |
| To | ``` var data: NSData { get } ``` |

Modified [SCNIKConstraint](https://developer.apple.com/documentation/scenekit/scnikconstraint)

|  | Declaration |
| --- | --- |
| From | ``` class SCNIKConstraint : SCNConstraint {     class func inverseKinematicsConstraintWithChainRootNode(_ chainRootNode: SCNNode) -> Self     var chainRootNode: SCNNode { get }     var targetPosition: SCNVector3     func setMaxAllowedRotationAngle(_ angle: CGFloat, forJoint node: SCNNode)     func maxAllowedRotationAngleForJoint(_ node: SCNNode) -> CGFloat } ``` |
| To | ``` class SCNIKConstraint : SCNConstraint {     init(chainRootNode chainRootNode: SCNNode)     class func inverseKinematicsConstraintWithChainRootNode(_ chainRootNode: SCNNode) -> Self     var chainRootNode: SCNNode { get }     var targetPosition: SCNVector3     func setMaxAllowedRotationAngle(_ angle: CGFloat, forJoint node: SCNNode)     func maxAllowedRotationAngleForJoint(_ node: SCNNode) -> CGFloat } ``` |

Modified [SCNLight](https://developer.apple.com/documentation/scenekit/scnlight)

|  | Declaration |
| --- | --- |
| From | ``` class SCNLight : NSObject, SCNAnimatable, NSObjectProtocol, SCNTechniqueSupport, NSCopying, NSSecureCoding, NSCoding {     convenience init!()     class func light() -> Self!     var type: String     var color: AnyObject     var name: String?     var castsShadow: Bool     var shadowColor: AnyObject     var shadowRadius: CGFloat     var shadowMapSize: CGSize     var shadowSampleCount: Int     var shadowMode: SCNShadowMode     var shadowBias: CGFloat     var orthographicScale: CGFloat     var zNear: CGFloat     var zFar: CGFloat     var attenuationStartDistance: CGFloat     var attenuationEndDistance: CGFloat     var attenuationFalloffExponent: CGFloat     var spotInnerAngle: CGFloat     var spotOuterAngle: CGFloat     var gobo: SCNMaterialProperty { get }     var categoryBitMask: Int } ``` |
| To | ``` class SCNLight : NSObject, SCNAnimatable, SCNTechniqueSupport, NSCopying, NSSecureCoding, NSCoding {     convenience init()     class func light() -> Self     var type: String     var color: AnyObject     var name: String?     var castsShadow: Bool     var shadowColor: AnyObject     var shadowRadius: CGFloat     var shadowMapSize: CGSize     var shadowSampleCount: Int     var shadowMode: SCNShadowMode     var shadowBias: CGFloat     var orthographicScale: CGFloat     var zNear: CGFloat     var zFar: CGFloat     var attenuationStartDistance: CGFloat     var attenuationEndDistance: CGFloat     var attenuationFalloffExponent: CGFloat     var spotInnerAngle: CGFloat     var spotOuterAngle: CGFloat     var gobo: SCNMaterialProperty? { get }     var categoryBitMask: Int } ``` |

Modified [SCNLight.gobo](https://developer.apple.com/documentation/scenekit/scnlight/1523524-gobo)

|  | Declaration |
| --- | --- |
| From | ``` var gobo: SCNMaterialProperty { get } ``` |
| To | ``` var gobo: SCNMaterialProperty? { get } ``` |

Modified [SCNLookAtConstraint](https://developer.apple.com/documentation/scenekit/scnlookatconstraint)

|  | Declaration |
| --- | --- |
| From | ``` class SCNLookAtConstraint : SCNConstraint {     convenience init(target target: SCNNode)     class func lookAtConstraintWithTarget(_ target: SCNNode) -> Self     var target: SCNNode? { get }     var gimbalLockEnabled: Bool } ``` |
| To | ``` class SCNLookAtConstraint : SCNConstraint {     convenience init(target target: SCNNode)     class func lookAtConstraintWithTarget(_ target: SCNNode) -> Self     var target: SCNNode { get }     var gimbalLockEnabled: Bool } ``` |

Modified [SCNLookAtConstraint.target](https://developer.apple.com/documentation/scenekit/scnlookatconstraint/1468677-target)

|  | Declaration |
| --- | --- |
| From | ``` var target: SCNNode? { get } ``` |
| To | ``` var target: SCNNode { get } ``` |

Modified [SCNMaterial](https://developer.apple.com/documentation/scenekit/scnmaterial)

|  | Declaration |
| --- | --- |
| From | ``` class SCNMaterial : NSObject, SCNAnimatable, NSObjectProtocol, SCNShadable, NSCopying, NSSecureCoding, NSCoding {     convenience init!()     class func material() -> Self!     var name: String?     var diffuse: SCNMaterialProperty { get }     var ambient: SCNMaterialProperty { get }     var specular: SCNMaterialProperty { get }     var emission: SCNMaterialProperty { get }     var transparent: SCNMaterialProperty { get }     var reflective: SCNMaterialProperty { get }     var multiply: SCNMaterialProperty { get }     var normal: SCNMaterialProperty { get }     var shininess: CGFloat     var transparency: CGFloat     var lightingModelName: String     var litPerPixel: Bool     var doubleSided: Bool     var cullMode: SCNCullMode     var transparencyMode: SCNTransparencyMode     var locksAmbientWithDiffuse: Bool     var writesToDepthBuffer: Bool     var readsFromDepthBuffer: Bool     var fresnelExponent: CGFloat } ``` |
| To | ``` class SCNMaterial : NSObject, SCNAnimatable, SCNShadable, NSCopying, NSSecureCoding, NSCoding {     convenience init()     class func material() -> Self     var name: String?     var diffuse: SCNMaterialProperty { get }     var ambient: SCNMaterialProperty { get }     var specular: SCNMaterialProperty { get }     var emission: SCNMaterialProperty { get }     var transparent: SCNMaterialProperty { get }     var reflective: SCNMaterialProperty { get }     var multiply: SCNMaterialProperty { get }     var normal: SCNMaterialProperty { get }     var ambientOcclusion: SCNMaterialProperty { get }     var selfIllumination: SCNMaterialProperty { get }     var shininess: CGFloat     var transparency: CGFloat     var lightingModelName: String     var litPerPixel: Bool     var doubleSided: Bool     var cullMode: SCNCullMode     var transparencyMode: SCNTransparencyMode     var locksAmbientWithDiffuse: Bool     var writesToDepthBuffer: Bool     var readsFromDepthBuffer: Bool     var fresnelExponent: CGFloat     var blendMode: SCNBlendMode } ``` |

Modified [SCNMaterialProperty](https://developer.apple.com/documentation/scenekit/scnmaterialproperty)

|  | Declaration |
| --- | --- |
| From | ``` class SCNMaterialProperty : NSObject, SCNAnimatable, NSObjectProtocol, NSSecureCoding, NSCoding {     convenience init(contents contents: AnyObject)     class func materialPropertyWithContents(_ contents: AnyObject) -> Self     var contents: AnyObject!     var intensity: CGFloat     var minificationFilter: SCNFilterMode     var magnificationFilter: SCNFilterMode     var mipFilter: SCNFilterMode     var contentsTransform: SCNMatrix4     var wrapS: SCNWrapMode     var wrapT: SCNWrapMode     var borderColor: AnyObject     var mappingChannel: Int     var maxAnisotropy: CGFloat } ``` |
| To | ``` class SCNMaterialProperty : NSObject, SCNAnimatable, NSSecureCoding, NSCoding {     convenience init(contents contents: AnyObject)     class func materialPropertyWithContents(_ contents: AnyObject) -> Self     var contents: AnyObject?     var intensity: CGFloat     var minificationFilter: SCNFilterMode     var magnificationFilter: SCNFilterMode     var mipFilter: SCNFilterMode     var contentsTransform: SCNMatrix4     var wrapS: SCNWrapMode     var wrapT: SCNWrapMode     var borderColor: AnyObject?     var mappingChannel: Int     var maxAnisotropy: CGFloat } ``` |

Modified [SCNMaterialProperty.borderColor](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/1395376-bordercolor)

|  | Declaration |
| --- | --- |
| From | ``` var borderColor: AnyObject ``` |
| To | ``` var borderColor: AnyObject? ``` |

Modified [SCNMaterialProperty.contents](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/1395372-contents)

|  | Declaration |
| --- | --- |
| From | ``` var contents: AnyObject! ``` |
| To | ``` var contents: AnyObject? ``` |

Modified [SCNMatrix4 [struct]](https://developer.apple.com/documentation/scenekit/scnmatrix4)

|  | Declaration |
| --- | --- |
| From | ``` struct SCNMatrix4 {     var m11: Float     var m12: Float     var m13: Float     var m14: Float     var m21: Float     var m22: Float     var m23: Float     var m24: Float     var m31: Float     var m32: Float     var m33: Float     var m34: Float     var m41: Float     var m42: Float     var m43: Float     var m44: Float     init()     init(m11 m11: Float, m12 m12: Float, m13 m13: Float, m14 m14: Float, m21 m21: Float, m22 m22: Float, m23 m23: Float, m24 m24: Float, m31 m31: Float, m32 m32: Float, m33 m33: Float, m34 m34: Float, m41 m41: Float, m42 m42: Float, m43 m43: Float, m44 m44: Float) } ``` |
| To | ``` struct SCNMatrix4 {     var m11: Float     var m12: Float     var m13: Float     var m14: Float     var m21: Float     var m22: Float     var m23: Float     var m24: Float     var m31: Float     var m32: Float     var m33: Float     var m34: Float     var m41: Float     var m42: Float     var m43: Float     var m44: Float     init()     init(m11 m11: Float, m12 m12: Float, m13 m13: Float, m14 m14: Float, m21 m21: Float, m22 m22: Float, m23 m23: Float, m24 m24: Float, m31 m31: Float, m32 m32: Float, m33 m33: Float, m34 m34: Float, m41 m41: Float, m42 m42: Float, m43 m43: Float, m44 m44: Float) } extension SCNMatrix4 {     init(_ m: float4x4)     init(_ m: double4x4) } extension SCNMatrix4 {     init(_ m: float4x4)     init(_ m: double4x4) } ``` |

Modified [SCNMorpher](https://developer.apple.com/documentation/scenekit/scnmorpher)

|  | Declaration |
| --- | --- |
| From | ``` class SCNMorpher : NSObject, SCNAnimatable, NSObjectProtocol, NSSecureCoding, NSCoding {     var targets: [AnyObject]?     func setWeight(_ weight: CGFloat, forTargetAtIndex targetIndex: Int)     func weightForTargetAtIndex(_ targetIndex: Int) -> CGFloat     var calculationMode: SCNMorpherCalculationMode } ``` |
| To | ``` class SCNMorpher : NSObject, SCNAnimatable, NSSecureCoding, NSCoding {     var targets: [SCNGeometry]     func setWeight(_ weight: CGFloat, forTargetAtIndex targetIndex: Int)     func weightForTargetAtIndex(_ targetIndex: Int) -> CGFloat     var calculationMode: SCNMorpherCalculationMode } ``` |

Modified [SCNMorpher.targets](https://developer.apple.com/documentation/scenekit/scnmorpher/1523572-targets)

|  | Declaration |
| --- | --- |
| From | ``` var targets: [AnyObject]? ``` |
| To | ``` var targets: [SCNGeometry] ``` |

Modified [SCNMorpherCalculationMode [enum]](https://developer.apple.com/documentation/scenekit/scnmorphercalculationmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SCNNode](https://developer.apple.com/documentation/scenekit/scnnode)

|  | Declaration |
| --- | --- |
| From | ``` class SCNNode : NSObject, NSCopying, NSSecureCoding, NSCoding, SCNAnimatable, NSObjectProtocol, SCNActionable, SCNBoundingVolume {     convenience init!()     class func node() -> Self!     init(geometry geometry: SCNGeometry) -> SCNNode     class func nodeWithGeometry(_ geometry: SCNGeometry) -> SCNNode     func clone() -> AnyObject     func flattenedClone() -> SCNNode     var name: String?     var light: SCNLight?     var camera: SCNCamera?     var geometry: SCNGeometry?     var skinner: SCNSkinner?     var morpher: SCNMorpher?     var transform: SCNMatrix4     var position: SCNVector3     var rotation: SCNVector4     var orientation: SCNQuaternion     var eulerAngles: SCNVector3     var scale: SCNVector3     var pivot: SCNMatrix4     var worldTransform: SCNMatrix4 { get }     var hidden: Bool     var opacity: CGFloat     var renderingOrder: Int     var castsShadow: Bool     var parentNode: SCNNode? { get }     var childNodes: [AnyObject] { get }     func addChildNode(_ child: SCNNode)     func insertChildNode(_ child: SCNNode, atIndex index: Int)     func removeFromParentNode()     func replaceChildNode(_ oldChild: SCNNode, with newChild: SCNNode)     func childNodeWithName(_ name: String, recursively recursively: Bool) -> SCNNode?     func childNodesPassingTest(_ predicate: (SCNNode!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AnyObject]     func enumerateChildNodesUsingBlock(_ block: (SCNNode!, UnsafeMutablePointer<ObjCBool>) -> Void)     func convertPosition(_ position: SCNVector3, toNode node: SCNNode?) -> SCNVector3     func convertPosition(_ position: SCNVector3, fromNode node: SCNNode?) -> SCNVector3     func convertTransform(_ transform: SCNMatrix4, toNode node: SCNNode?) -> SCNMatrix4     func convertTransform(_ transform: SCNMatrix4, fromNode node: SCNNode?) -> SCNMatrix4     var physicsBody: SCNPhysicsBody?     var physicsField: SCNPhysicsField?     var constraints: [AnyObject]?     var filters: [AnyObject]?     func presentationNode() -> SCNNode     var paused: Bool     unowned(unsafe) var rendererDelegate: SCNNodeRendererDelegate?     func hitTestWithSegmentFromPoint(_ pointA: SCNVector3, toPoint pointB: SCNVector3, options options: [NSObject : AnyObject]?) -> [AnyObject]?     var categoryBitMask: Int } extension SCNNode {     func addParticleSystem(_ system: SCNParticleSystem)     func removeAllParticleSystems()     func removeParticleSystem(_ system: SCNParticleSystem)     var particleSystems: [AnyObject]? { get } } ``` |
| To | ``` class SCNNode : NSObject, NSCopying, NSSecureCoding, NSCoding, SCNAnimatable, SCNActionable, SCNBoundingVolume {     convenience init()     class func node() -> Self      init(geometry geometry: SCNGeometry?)     class func nodeWithGeometry(_ geometry: SCNGeometry?) -> SCNNode     func clone() -> Self     func flattenedClone() -> Self     var name: String?     var light: SCNLight?     var camera: SCNCamera?     var geometry: SCNGeometry?     var skinner: SCNSkinner?     var morpher: SCNMorpher?     var transform: SCNMatrix4     var position: SCNVector3     var rotation: SCNVector4     var orientation: SCNQuaternion     var eulerAngles: SCNVector3     var scale: SCNVector3     var pivot: SCNMatrix4     var worldTransform: SCNMatrix4 { get }     var hidden: Bool     var opacity: CGFloat     var renderingOrder: Int     var castsShadow: Bool     var parentNode: SCNNode? { get }     var childNodes: [SCNNode] { get }     func addChildNode(_ child: SCNNode)     func insertChildNode(_ child: SCNNode, atIndex index: Int)     func removeFromParentNode()     func replaceChildNode(_ oldChild: SCNNode, with newChild: SCNNode)     func childNodeWithName(_ name: String, recursively recursively: Bool) -> SCNNode?     func childNodesPassingTest(_ predicate: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]     func enumerateChildNodesUsingBlock(_ block: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)     func convertPosition(_ position: SCNVector3, toNode node: SCNNode?) -> SCNVector3     func convertPosition(_ position: SCNVector3, fromNode node: SCNNode?) -> SCNVector3     func convertTransform(_ transform: SCNMatrix4, toNode node: SCNNode?) -> SCNMatrix4     func convertTransform(_ transform: SCNMatrix4, fromNode node: SCNNode?) -> SCNMatrix4     var physicsBody: SCNPhysicsBody?     var physicsField: SCNPhysicsField?     var constraints: [SCNConstraint]?     var filters: [CIFilter]?     var presentationNode: SCNNode { get }     var paused: Bool     unowned(unsafe) var rendererDelegate: SCNNodeRendererDelegate?     func hitTestWithSegmentFromPoint(_ pointA: SCNVector3, toPoint pointB: SCNVector3, options options: [String : AnyObject]?) -> [SCNHitTestResult]     var categoryBitMask: Int } extension SCNNode {     func addAudioPlayer(_ player: SCNAudioPlayer)     func removeAllAudioPlayers()     func removeAudioPlayer(_ player: SCNAudioPlayer)     var audioPlayers: [SCNAudioPlayer] { get } } extension SCNNode {     func addParticleSystem(_ system: SCNParticleSystem)     func removeAllParticleSystems()     func removeParticleSystem(_ system: SCNParticleSystem)     var particleSystems: [SCNParticleSystem]? { get } } ``` |

Modified [SCNNode.childNodes](https://developer.apple.com/documentation/scenekit/scnnode/1407984-childnodes)

|  | Declaration |
| --- | --- |
| From | ``` var childNodes: [AnyObject] { get } ``` |
| To | ``` var childNodes: [SCNNode] { get } ``` |

Modified [SCNNode.childNodesPassingTest(_: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]](https://developer.apple.com/documentation/scenekit/scnnode/1407982-childnodespassingtest)

|  | Declaration |
| --- | --- |
| From | ``` func childNodesPassingTest(_ predicate: (SCNNode!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AnyObject] ``` |
| To | ``` func childNodesPassingTest(_ predicate: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode] ``` |

Modified [SCNNode.clone() -> Self](https://developer.apple.com/documentation/scenekit/scnnode/1408046-clone)

|  | Declaration |
| --- | --- |
| From | ``` func clone() -> AnyObject ``` |
| To | ``` func clone() -> Self ``` |

Modified [SCNNode.constraints](https://developer.apple.com/documentation/scenekit/scnnode/1408016-constraints)

|  | Declaration |
| --- | --- |
| From | ``` var constraints: [AnyObject]? ``` |
| To | ``` var constraints: [SCNConstraint]? ``` |

Modified [SCNNode.enumerateChildNodesUsingBlock(_: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/scenekit/scnnode/1408032-enumeratechildnodesusingblock)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateChildNodesUsingBlock(_ block: (SCNNode!, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateChildNodesUsingBlock(_ block: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [SCNNode.filters](https://developer.apple.com/documentation/scenekit/scnnode/1407949-filters)

|  | Declaration |
| --- | --- |
| From | ``` var filters: [AnyObject]? ``` |
| To | ``` var filters: [CIFilter]? ``` |

Modified [SCNNode.flattenedClone() -> Self](https://developer.apple.com/documentation/scenekit/scnnode/1407960-flattenedclone)

|  | Declaration |
| --- | --- |
| From | ``` func flattenedClone() -> SCNNode ``` |
| To | ``` func flattenedClone() -> Self ``` |

Modified [SCNNode.hitTestWithSegmentFromPoint(_: SCNVector3, toPoint: SCNVector3, options: [String : AnyObject]?) -> [SCNHitTestResult]](https://developer.apple.com/documentation/scenekit/scnnode/1407998-hittestwithsegmentfrompoint)

|  | Declaration |
| --- | --- |
| From | ``` func hitTestWithSegmentFromPoint(_ pointA: SCNVector3, toPoint pointB: SCNVector3, options options: [NSObject : AnyObject]?) -> [AnyObject]? ``` |
| To | ``` func hitTestWithSegmentFromPoint(_ pointA: SCNVector3, toPoint pointB: SCNVector3, options options: [String : AnyObject]?) -> [SCNHitTestResult] ``` |

Modified [SCNNode.init(geometry: SCNGeometry?)](https://developer.apple.com/documentation/scenekit/scnnode/1408020-init)

|  | Declaration |
| --- | --- |
| From | ``` init(geometry geometry: SCNGeometry) -> SCNNode ``` |
| To | ``` init(geometry geometry: SCNGeometry?) ``` |

Modified [SCNNode.particleSystems](https://developer.apple.com/documentation/scenekit/scnnode/1522705-particlesystems)

|  | Declaration |
| --- | --- |
| From | ``` var particleSystems: [AnyObject]? { get } ``` |
| To | ``` var particleSystems: [SCNParticleSystem]? { get } ``` |

Modified [SCNNodeRendererDelegate](https://developer.apple.com/documentation/scenekit/scnnoderendererdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol SCNNodeRendererDelegate : NSObjectProtocol {     optional func renderNode(_ node: SCNNode, renderer renderer: SCNRenderer, arguments arguments: [NSObject : AnyObject]) } ``` |
| To | ``` protocol SCNNodeRendererDelegate : NSObjectProtocol {     optional func renderNode(_ node: SCNNode, renderer renderer: SCNRenderer, arguments arguments: [String : NSValue]) } ``` |

Modified [SCNNodeRendererDelegate.renderNode(_: SCNNode, renderer: SCNRenderer, arguments: [String : NSValue])](https://developer.apple.com/documentation/scenekit/scnnoderendererdelegate/1407993-rendernode)

|  | Declaration |
| --- | --- |
| From | ``` optional func renderNode(_ node: SCNNode, renderer renderer: SCNRenderer, arguments arguments: [NSObject : AnyObject]) ``` |
| To | ``` optional func renderNode(_ node: SCNNode, renderer renderer: SCNRenderer, arguments arguments: [String : NSValue]) ``` |

Modified [SCNParticleBirthDirection [enum]](https://developer.apple.com/documentation/scenekit/scnparticlebirthdirection)

|  | Introduction | Raw Value Type |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 8.0 | Int |

Modified [SCNParticleBirthLocation [enum]](https://developer.apple.com/documentation/scenekit/scnparticlebirthlocation)

|  | Introduction | Raw Value Type |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 8.0 | Int |

Modified [SCNParticleBlendMode [enum]](https://developer.apple.com/documentation/scenekit/scnparticleblendmode)

|  | Introduction | Raw Value Type |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 8.0 | Int |

Modified [SCNParticleEvent [enum]](https://developer.apple.com/documentation/scenekit/scnparticleevent)

|  | Introduction | Raw Value Type |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 8.0 | Int |

Modified [SCNParticleImageSequenceAnimationMode [enum]](https://developer.apple.com/documentation/scenekit/scnparticleimagesequenceanimationmode)

|  | Introduction | Raw Value Type |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 8.0 | Int |

Modified [SCNParticleInputMode [enum]](https://developer.apple.com/documentation/scenekit/scnparticleinputmode)

|  | Introduction | Raw Value Type |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 8.0 | Int |

Modified [SCNParticleModifierStage [enum]](https://developer.apple.com/documentation/scenekit/scnparticlemodifierstage)

|  | Introduction | Raw Value Type |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 8.0 | Int |

Modified [SCNParticleOrientationMode [enum]](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode)

|  | Introduction | Raw Value Type |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 8.0 | Int |

Modified [SCNParticlePropertyController](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller)

|  | Declaration |
| --- | --- |
| From | ``` class SCNParticlePropertyController : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init(animation animation: CAAnimation)     class func controllerWithAnimation(_ animation: CAAnimation) -> Self     var animation: CAAnimation!     var inputMode: SCNParticleInputMode     var inputScale: CGFloat     var inputBias: CGFloat     weak var inputOrigin: SCNNode!     var inputProperty: String! } ``` |
| To | ``` class SCNParticlePropertyController : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init(animation animation: CAAnimation)     class func controllerWithAnimation(_ animation: CAAnimation) -> Self     var animation: CAAnimation     var inputMode: SCNParticleInputMode     var inputScale: CGFloat     var inputBias: CGFloat     weak var inputOrigin: SCNNode?     var inputProperty: String? } ``` |

Modified [SCNParticlePropertyController.animation](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1523707-animation)

|  | Declaration |
| --- | --- |
| From | ``` var animation: CAAnimation! ``` |
| To | ``` var animation: CAAnimation ``` |

Modified [SCNParticlePropertyController.inputOrigin](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1522895-inputorigin)

|  | Declaration |
| --- | --- |
| From | ``` weak var inputOrigin: SCNNode! ``` |
| To | ``` weak var inputOrigin: SCNNode? ``` |

Modified [SCNParticlePropertyController.inputProperty](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1522973-inputproperty)

|  | Declaration |
| --- | --- |
| From | ``` var inputProperty: String! ``` |
| To | ``` var inputProperty: String? ``` |

Modified [SCNParticleSortingMode [enum]](https://developer.apple.com/documentation/scenekit/scnparticlesortingmode)

|  | Introduction | Raw Value Type |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 8.0 | Int |

Modified [SCNParticleSystem](https://developer.apple.com/documentation/scenekit/scnparticlesystem)

|  | Declaration |
| --- | --- |
| From | ``` class SCNParticleSystem : NSObject, NSCopying, NSSecureCoding, NSCoding, SCNAnimatable, NSObjectProtocol {     convenience init!()     class func particleSystem() -> Self!     convenience init!(named name: String, inDirectory directory: String!)     class func particleSystemNamed(_ name: String, inDirectory directory: String!) -> Self!     var emissionDuration: CGFloat     var emissionDurationVariation: CGFloat     var idleDuration: CGFloat     var idleDurationVariation: CGFloat     var loops: Bool     var birthRate: CGFloat     var birthRateVariation: CGFloat     var warmupDuration: CGFloat     var emitterShape: SCNGeometry!     var birthLocation: SCNParticleBirthLocation     var birthDirection: SCNParticleBirthDirection     var spreadingAngle: CGFloat     var emittingDirection: SCNVector3     var acceleration: SCNVector3     var local: Bool     var particleAngle: CGFloat     var particleAngleVariation: CGFloat     var particleVelocity: CGFloat     var particleVelocityVariation: CGFloat     var particleAngularVelocity: CGFloat     var particleAngularVelocityVariation: CGFloat     var particleLifeSpan: CGFloat     var particleLifeSpanVariation: CGFloat     var systemSpawnedOnDying: SCNParticleSystem!     var systemSpawnedOnCollision: SCNParticleSystem!     var systemSpawnedOnLiving: SCNParticleSystem!     var particleImage: AnyObject!     var imageSequenceColumnCount: Int     var imageSequenceRowCount: Int     var imageSequenceInitialFrame: CGFloat     var imageSequenceInitialFrameVariation: CGFloat     var imageSequenceFrameRate: CGFloat     var imageSequenceFrameRateVariation: CGFloat     var imageSequenceAnimationMode: SCNParticleImageSequenceAnimationMode     var particleColor: UIColor!     var particleColorVariation: SCNVector4     var particleSize: CGFloat     var particleSizeVariation: CGFloat     var blendMode: SCNParticleBlendMode     var blackPassEnabled: Bool     var orientationMode: SCNParticleOrientationMode     var sortingMode: SCNParticleSortingMode     var lightingEnabled: Bool     var affectedByGravity: Bool     var affectedByPhysicsFields: Bool     var particleDiesOnCollision: Bool     var colliderNodes: [AnyObject]!     var particleMass: CGFloat     var particleMassVariation: CGFloat     var particleBounce: CGFloat     var particleBounceVariation: CGFloat     var particleFriction: CGFloat     var particleFrictionVariation: CGFloat     var particleCharge: CGFloat     var particleChargeVariation: CGFloat     var dampingFactor: CGFloat     var speedFactor: CGFloat     var stretchFactor: CGFloat     var fresnelExponent: CGFloat     var propertyControllers: [NSObject : AnyObject]!     func reset()     func handleEvent(_ event: SCNParticleEvent, forProperties properties: [AnyObject], withBlock block: SCNParticleEventBlock)     func addModifierForProperties(_ properties: [AnyObject], atStage stage: SCNParticleModifierStage, withBlock block: SCNParticleModifierBlock)     func removeModifiersOfStage(_ stage: SCNParticleModifierStage)     func removeAllModifiers() } ``` |
| To | ``` class SCNParticleSystem : NSObject, NSCopying, NSSecureCoding, NSCoding, SCNAnimatable {     convenience init()     class func particleSystem() -> Self     convenience init?(named name: String, inDirectory directory: String?)     class func particleSystemNamed(_ name: String, inDirectory directory: String?) -> Self?     var emissionDuration: CGFloat     var emissionDurationVariation: CGFloat     var idleDuration: CGFloat     var idleDurationVariation: CGFloat     var loops: Bool     var birthRate: CGFloat     var birthRateVariation: CGFloat     var warmupDuration: CGFloat     var emitterShape: SCNGeometry?     var birthLocation: SCNParticleBirthLocation     var birthDirection: SCNParticleBirthDirection     var spreadingAngle: CGFloat     var emittingDirection: SCNVector3     var acceleration: SCNVector3     var local: Bool     var particleAngle: CGFloat     var particleAngleVariation: CGFloat     var particleVelocity: CGFloat     var particleVelocityVariation: CGFloat     var particleAngularVelocity: CGFloat     var particleAngularVelocityVariation: CGFloat     var particleLifeSpan: CGFloat     var particleLifeSpanVariation: CGFloat     var systemSpawnedOnDying: SCNParticleSystem?     var systemSpawnedOnCollision: SCNParticleSystem?     var systemSpawnedOnLiving: SCNParticleSystem?     var particleImage: AnyObject?     var imageSequenceColumnCount: Int     var imageSequenceRowCount: Int     var imageSequenceInitialFrame: CGFloat     var imageSequenceInitialFrameVariation: CGFloat     var imageSequenceFrameRate: CGFloat     var imageSequenceFrameRateVariation: CGFloat     var imageSequenceAnimationMode: SCNParticleImageSequenceAnimationMode     var particleColor: UIColor     var particleColorVariation: SCNVector4     var particleSize: CGFloat     var particleSizeVariation: CGFloat     var blendMode: SCNParticleBlendMode     var blackPassEnabled: Bool     var orientationMode: SCNParticleOrientationMode     var sortingMode: SCNParticleSortingMode     var lightingEnabled: Bool     var affectedByGravity: Bool     var affectedByPhysicsFields: Bool     var particleDiesOnCollision: Bool     var colliderNodes: [SCNNode]?     var particleMass: CGFloat     var particleMassVariation: CGFloat     var particleBounce: CGFloat     var particleBounceVariation: CGFloat     var particleFriction: CGFloat     var particleFrictionVariation: CGFloat     var particleCharge: CGFloat     var particleChargeVariation: CGFloat     var dampingFactor: CGFloat     var speedFactor: CGFloat     var stretchFactor: CGFloat     var fresnelExponent: CGFloat     var propertyControllers: [String : SCNParticlePropertyController]?     func reset()     func handleEvent(_ event: SCNParticleEvent, forProperties properties: [String], withBlock block: SCNParticleEventBlock)     func addModifierForProperties(_ properties: [String], atStage stage: SCNParticleModifierStage, withBlock block: SCNParticleModifierBlock)     func removeModifiersOfStage(_ stage: SCNParticleModifierStage)     func removeAllModifiers() } ``` |

Modified [SCNParticleSystem.addModifierForProperties(_: [String], atStage: SCNParticleModifierStage, withBlock: SCNParticleModifierBlock)](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522635-addmodifier)

|  | Declaration |
| --- | --- |
| From | ``` func addModifierForProperties(_ properties: [AnyObject], atStage stage: SCNParticleModifierStage, withBlock block: SCNParticleModifierBlock) ``` |
| To | ``` func addModifierForProperties(_ properties: [String], atStage stage: SCNParticleModifierStage, withBlock block: SCNParticleModifierBlock) ``` |

Modified [SCNParticleSystem.colliderNodes](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523516-collidernodes)

|  | Declaration |
| --- | --- |
| From | ``` var colliderNodes: [AnyObject]! ``` |
| To | ``` var colliderNodes: [SCNNode]? ``` |

Modified [SCNParticleSystem.emitterShape](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522737-emittershape)

|  | Declaration |
| --- | --- |
| From | ``` var emitterShape: SCNGeometry! ``` |
| To | ``` var emitterShape: SCNGeometry? ``` |

Modified [SCNParticleSystem.handleEvent(_: SCNParticleEvent, forProperties: [String], withBlock: SCNParticleEventBlock)](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523251-handleevent)

|  | Declaration |
| --- | --- |
| From | ``` func handleEvent(_ event: SCNParticleEvent, forProperties properties: [AnyObject], withBlock block: SCNParticleEventBlock) ``` |
| To | ``` func handleEvent(_ event: SCNParticleEvent, forProperties properties: [String], withBlock block: SCNParticleEventBlock) ``` |

Modified [SCNParticleSystem.init(named: String, inDirectory: String?)](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522772-particlesystemnamed)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(named name: String, inDirectory directory: String!) ``` |
| To | ``` convenience init?(named name: String, inDirectory directory: String?) ``` |

Modified [SCNParticleSystem.particleColor](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523248-particlecolor)

|  | Declaration |
| --- | --- |
| From | ``` var particleColor: UIColor! ``` |
| To | ``` var particleColor: UIColor ``` |

Modified [SCNParticleSystem.particleImage](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524153-particleimage)

|  | Declaration |
| --- | --- |
| From | ``` var particleImage: AnyObject! ``` |
| To | ``` var particleImage: AnyObject? ``` |

Modified [SCNParticleSystem.propertyControllers](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522775-propertycontrollers)

|  | Declaration |
| --- | --- |
| From | ``` var propertyControllers: [NSObject : AnyObject]! ``` |
| To | ``` var propertyControllers: [String : SCNParticlePropertyController]? ``` |

Modified [SCNParticleSystem.systemSpawnedOnCollision](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524068-systemspawnedoncollision)

|  | Declaration |
| --- | --- |
| From | ``` var systemSpawnedOnCollision: SCNParticleSystem! ``` |
| To | ``` var systemSpawnedOnCollision: SCNParticleSystem? ``` |

Modified [SCNParticleSystem.systemSpawnedOnDying](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524091-systemspawnedondying)

|  | Declaration |
| --- | --- |
| From | ``` var systemSpawnedOnDying: SCNParticleSystem! ``` |
| To | ``` var systemSpawnedOnDying: SCNParticleSystem? ``` |

Modified [SCNParticleSystem.systemSpawnedOnLiving](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522751-systemspawnedonliving)

|  | Declaration |
| --- | --- |
| From | ``` var systemSpawnedOnLiving: SCNParticleSystem! ``` |
| To | ``` var systemSpawnedOnLiving: SCNParticleSystem? ``` |

Modified [SCNPhysicsBallSocketJoint](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint)

|  | Declaration |
| --- | --- |
| From | ``` class SCNPhysicsBallSocketJoint : SCNPhysicsBehavior {     convenience init!(bodyA bodyA: SCNPhysicsBody!, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, anchorB anchorB: SCNVector3)     class func jointWithBodyA(_ bodyA: SCNPhysicsBody!, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, anchorB anchorB: SCNVector3) -> Self!     convenience init!(body body: SCNPhysicsBody!, anchor anchor: SCNVector3)     class func jointWithBody(_ body: SCNPhysicsBody!, anchor anchor: SCNVector3) -> Self!     var bodyA: SCNPhysicsBody! { get }     var anchorA: SCNVector3     var bodyB: SCNPhysicsBody! { get }     var anchorB: SCNVector3 } ``` |
| To | ``` class SCNPhysicsBallSocketJoint : SCNPhysicsBehavior {     convenience init(bodyA bodyA: SCNPhysicsBody, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody, anchorB anchorB: SCNVector3)     class func jointWithBodyA(_ bodyA: SCNPhysicsBody, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody, anchorB anchorB: SCNVector3) -> Self     convenience init(body body: SCNPhysicsBody, anchor anchor: SCNVector3)     class func jointWithBody(_ body: SCNPhysicsBody, anchor anchor: SCNVector3) -> Self     var bodyA: SCNPhysicsBody { get }     var anchorA: SCNVector3     var bodyB: SCNPhysicsBody? { get }     var anchorB: SCNVector3 } ``` |

Modified [SCNPhysicsBallSocketJoint.bodyA](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387981-bodya)

|  | Declaration |
| --- | --- |
| From | ``` var bodyA: SCNPhysicsBody! { get } ``` |
| To | ``` var bodyA: SCNPhysicsBody { get } ``` |

Modified [SCNPhysicsBallSocketJoint.bodyB](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387902-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` var bodyB: SCNPhysicsBody! { get } ``` |
| To | ``` var bodyB: SCNPhysicsBody? { get } ``` |

Modified [SCNPhysicsBallSocketJoint.init(body: SCNPhysicsBody, anchor: SCNVector3)](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387975-jointwithbody)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(body body: SCNPhysicsBody!, anchor anchor: SCNVector3) ``` |
| To | ``` convenience init(body body: SCNPhysicsBody, anchor anchor: SCNVector3) ``` |

Modified [SCNPhysicsBallSocketJoint.init(bodyA: SCNPhysicsBody, anchorA: SCNVector3, bodyB: SCNPhysicsBody, anchorB: SCNVector3)](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387926-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(bodyA bodyA: SCNPhysicsBody!, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, anchorB anchorB: SCNVector3) ``` |
| To | ``` convenience init(bodyA bodyA: SCNPhysicsBody, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody, anchorB anchorB: SCNVector3) ``` |

Modified [SCNPhysicsBody](https://developer.apple.com/documentation/scenekit/scnphysicsbody)

|  | Declaration |
| --- | --- |
| From | ``` class SCNPhysicsBody : NSObject, NSCopying, NSSecureCoding, NSCoding {     class func staticBody() -> Self     class func dynamicBody() -> Self     class func kinematicBody() -> Self     convenience init(type type: SCNPhysicsBodyType, shape shape: SCNPhysicsShape?)     class func bodyWithType(_ type: SCNPhysicsBodyType, shape shape: SCNPhysicsShape?) -> Self     var type: SCNPhysicsBodyType     var mass: CGFloat     var charge: CGFloat     var friction: CGFloat     var restitution: CGFloat     var rollingFriction: CGFloat     var physicsShape: SCNPhysicsShape?     var isResting: Bool { get }     var allowsResting: Bool     var velocity: SCNVector3     var angularVelocity: SCNVector4     var damping: CGFloat     var angularDamping: CGFloat     var velocityFactor: SCNVector3     var angularVelocityFactor: SCNVector3     var categoryBitMask: Int     var collisionBitMask: Int     func applyForce(_ direction: SCNVector3, impulse impulse: Bool)     func applyForce(_ direction: SCNVector3, atPosition position: SCNVector3, impulse impulse: Bool)     func applyTorque(_ torque: SCNVector4, impulse impulse: Bool)     func clearAllForces()     func resetTransform() } ``` |
| To | ``` class SCNPhysicsBody : NSObject, NSCopying, NSSecureCoding, NSCoding {     class func staticBody() -> Self     class func dynamicBody() -> Self     class func kinematicBody() -> Self     convenience init(type type: SCNPhysicsBodyType, shape shape: SCNPhysicsShape?)     class func bodyWithType(_ type: SCNPhysicsBodyType, shape shape: SCNPhysicsShape?) -> Self     var type: SCNPhysicsBodyType     var mass: CGFloat     var momentOfInertia: SCNVector3     var usesDefaultMomentOfInertia: Bool     var charge: CGFloat     var friction: CGFloat     var restitution: CGFloat     var rollingFriction: CGFloat     var physicsShape: SCNPhysicsShape?     var isResting: Bool { get }     var allowsResting: Bool     var velocity: SCNVector3     var angularVelocity: SCNVector4     var damping: CGFloat     var angularDamping: CGFloat     var velocityFactor: SCNVector3     var angularVelocityFactor: SCNVector3     var categoryBitMask: Int     var collisionBitMask: Int     var contactTestBitMask: Int     var affectedByGravity: Bool     func applyForce(_ direction: SCNVector3, impulse impulse: Bool)     func applyForce(_ direction: SCNVector3, atPosition position: SCNVector3, impulse impulse: Bool)     func applyTorque(_ torque: SCNVector4, impulse impulse: Bool)     func clearAllForces()     func resetTransform() } ``` |

Modified [SCNPhysicsBodyType [enum]](https://developer.apple.com/documentation/scenekit/scnphysicsbodytype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SCNPhysicsCollisionCategory [struct]](https://developer.apple.com/documentation/scenekit/scnphysicscollisioncategory)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SCNPhysicsCollisionCategory : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Default: SCNPhysicsCollisionCategory { get }     static var Static: SCNPhysicsCollisionCategory { get }     static var All: SCNPhysicsCollisionCategory { get } } ``` | RawOptionSetType |
| To | ``` struct SCNPhysicsCollisionCategory : OptionSetType {     init(rawValue rawValue: UInt)     static var Default: SCNPhysicsCollisionCategory { get }     static var Static: SCNPhysicsCollisionCategory { get }     static var All: SCNPhysicsCollisionCategory { get } } ``` | OptionSetType |

Modified [SCNPhysicsFieldScope [enum]](https://developer.apple.com/documentation/scenekit/scnphysicsfieldscope)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SCNPhysicsHingeJoint](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint)

|  | Declaration |
| --- | --- |
| From | ``` class SCNPhysicsHingeJoint : SCNPhysicsBehavior {     convenience init(bodyA bodyA: SCNPhysicsBody, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3)     class func jointWithBodyA(_ bodyA: SCNPhysicsBody, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3) -> Self     convenience init(body body: SCNPhysicsBody, axis axis: SCNVector3, anchor anchor: SCNVector3)     class func jointWithBody(_ body: SCNPhysicsBody, axis axis: SCNVector3, anchor anchor: SCNVector3) -> Self     var bodyA: SCNPhysicsBody! { get }     var axisA: SCNVector3     var anchorA: SCNVector3     var bodyB: SCNPhysicsBody! { get }     var axisB: SCNVector3     var anchorB: SCNVector3 } ``` |
| To | ``` class SCNPhysicsHingeJoint : SCNPhysicsBehavior {     convenience init(bodyA bodyA: SCNPhysicsBody, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3)     class func jointWithBodyA(_ bodyA: SCNPhysicsBody, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3) -> Self     convenience init(body body: SCNPhysicsBody, axis axis: SCNVector3, anchor anchor: SCNVector3)     class func jointWithBody(_ body: SCNPhysicsBody, axis axis: SCNVector3, anchor anchor: SCNVector3) -> Self     var bodyA: SCNPhysicsBody { get }     var axisA: SCNVector3     var anchorA: SCNVector3     var bodyB: SCNPhysicsBody? { get }     var axisB: SCNVector3     var anchorB: SCNVector3 } ``` |

Modified [SCNPhysicsHingeJoint.bodyA](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387973-bodya)

|  | Declaration |
| --- | --- |
| From | ``` var bodyA: SCNPhysicsBody! { get } ``` |
| To | ``` var bodyA: SCNPhysicsBody { get } ``` |

Modified [SCNPhysicsHingeJoint.bodyB](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387918-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` var bodyB: SCNPhysicsBody! { get } ``` |
| To | ``` var bodyB: SCNPhysicsBody? { get } ``` |

Modified [SCNPhysicsShape](https://developer.apple.com/documentation/scenekit/scnphysicsshape)

|  | Declaration |
| --- | --- |
| From | ``` class SCNPhysicsShape : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(geometry geometry: SCNGeometry, options options: [NSObject : AnyObject]?)     class func shapeWithGeometry(_ geometry: SCNGeometry, options options: [NSObject : AnyObject]?) -> Self     convenience init(node node: SCNNode, options options: [NSObject : AnyObject]?)     class func shapeWithNode(_ node: SCNNode, options options: [NSObject : AnyObject]?) -> Self     convenience init(shapes shapes: [AnyObject], transforms transforms: [AnyObject])     class func shapeWithShapes(_ shapes: [AnyObject], transforms transforms: [AnyObject]) -> Self } ``` |
| To | ``` class SCNPhysicsShape : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(geometry geometry: SCNGeometry, options options: [String : AnyObject]?)     class func shapeWithGeometry(_ geometry: SCNGeometry, options options: [String : AnyObject]?) -> Self     convenience init(node node: SCNNode, options options: [String : AnyObject]?)     class func shapeWithNode(_ node: SCNNode, options options: [String : AnyObject]?) -> Self     convenience init(shapes shapes: [SCNPhysicsShape], transforms transforms: [NSValue]?)     class func shapeWithShapes(_ shapes: [SCNPhysicsShape], transforms transforms: [NSValue]?) -> Self     var options: [String : AnyObject]? { get }     var sourceObject: AnyObject { get }     var transforms: [NSValue]? { get } } ``` |

Modified [SCNPhysicsShape.init(geometry: SCNGeometry, options: [String : AnyObject]?)](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508897-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(geometry geometry: SCNGeometry, options options: [NSObject : AnyObject]?) ``` |
| To | ``` convenience init(geometry geometry: SCNGeometry, options options: [String : AnyObject]?) ``` |

Modified [SCNPhysicsShape.init(node: SCNNode, options: [String : AnyObject]?)](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508889-shapewithnode)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(node node: SCNNode, options options: [NSObject : AnyObject]?) ``` |
| To | ``` convenience init(node node: SCNNode, options options: [String : AnyObject]?) ``` |

Modified [SCNPhysicsShape.init(shapes: [SCNPhysicsShape], transforms: [NSValue]?)](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508886-shapewithshapes)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(shapes shapes: [AnyObject], transforms transforms: [AnyObject]) ``` |
| To | ``` convenience init(shapes shapes: [SCNPhysicsShape], transforms transforms: [NSValue]?) ``` |

Modified [SCNPhysicsSliderJoint](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint)

|  | Declaration |
| --- | --- |
| From | ``` class SCNPhysicsSliderJoint : SCNPhysicsBehavior {     convenience init!(bodyA bodyA: SCNPhysicsBody!, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3)     class func jointWithBodyA(_ bodyA: SCNPhysicsBody!, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3) -> Self!     convenience init!(body body: SCNPhysicsBody!, axis axis: SCNVector3, anchor anchor: SCNVector3)     class func jointWithBody(_ body: SCNPhysicsBody!, axis axis: SCNVector3, anchor anchor: SCNVector3) -> Self!     var bodyA: SCNPhysicsBody! { get }     var axisA: SCNVector3     var anchorA: SCNVector3     var bodyB: SCNPhysicsBody! { get }     var axisB: SCNVector3     var anchorB: SCNVector3     var minimumLinearLimit: CGFloat     var maximumLinearLimit: CGFloat     var minimumAngularLimit: CGFloat     var maximumAngularLimit: CGFloat     var motorTargetLinearVelocity: CGFloat     var motorMaximumForce: CGFloat     var motorTargetAngularVelocity: CGFloat     var motorMaximumTorque: CGFloat } ``` |
| To | ``` class SCNPhysicsSliderJoint : SCNPhysicsBehavior {     convenience init(bodyA bodyA: SCNPhysicsBody, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3)     class func jointWithBodyA(_ bodyA: SCNPhysicsBody, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3) -> Self     convenience init(body body: SCNPhysicsBody, axis axis: SCNVector3, anchor anchor: SCNVector3)     class func jointWithBody(_ body: SCNPhysicsBody, axis axis: SCNVector3, anchor anchor: SCNVector3) -> Self     var bodyA: SCNPhysicsBody { get }     var axisA: SCNVector3     var anchorA: SCNVector3     var bodyB: SCNPhysicsBody? { get }     var axisB: SCNVector3     var anchorB: SCNVector3     var minimumLinearLimit: CGFloat     var maximumLinearLimit: CGFloat     var minimumAngularLimit: CGFloat     var maximumAngularLimit: CGFloat     var motorTargetLinearVelocity: CGFloat     var motorMaximumForce: CGFloat     var motorTargetAngularVelocity: CGFloat     var motorMaximumTorque: CGFloat } ``` |

Modified [SCNPhysicsSliderJoint.bodyA](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387987-bodya)

|  | Declaration |
| --- | --- |
| From | ``` var bodyA: SCNPhysicsBody! { get } ``` |
| To | ``` var bodyA: SCNPhysicsBody { get } ``` |

Modified [SCNPhysicsSliderJoint.bodyB](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387896-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` var bodyB: SCNPhysicsBody! { get } ``` |
| To | ``` var bodyB: SCNPhysicsBody? { get } ``` |

Modified [SCNPhysicsSliderJoint.init(body: SCNPhysicsBody, axis: SCNVector3, anchor: SCNVector3)](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387932-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(body body: SCNPhysicsBody!, axis axis: SCNVector3, anchor anchor: SCNVector3) ``` |
| To | ``` convenience init(body body: SCNPhysicsBody, axis axis: SCNVector3, anchor anchor: SCNVector3) ``` |

Modified [SCNPhysicsSliderJoint.init(bodyA: SCNPhysicsBody, axisA: SCNVector3, anchorA: SCNVector3, bodyB: SCNPhysicsBody, axisB: SCNVector3, anchorB: SCNVector3)](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387922-jointwithbodya)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(bodyA bodyA: SCNPhysicsBody!, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody!, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3) ``` |
| To | ``` convenience init(bodyA bodyA: SCNPhysicsBody, axisA axisA: SCNVector3, anchorA anchorA: SCNVector3, bodyB bodyB: SCNPhysicsBody, axisB axisB: SCNVector3, anchorB anchorB: SCNVector3) ``` |

Modified [SCNPhysicsVehicle](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle)

|  | Declaration |
| --- | --- |
| From | ``` class SCNPhysicsVehicle : SCNPhysicsBehavior {     convenience init(chassisBody chassisBody: SCNPhysicsBody!, wheels wheels: [AnyObject])     class func vehicleWithChassisBody(_ chassisBody: SCNPhysicsBody!, wheels wheels: [AnyObject]) -> Self     var speedInKilometersPerHour: CGFloat { get }     var wheels: [AnyObject]! { get }     var chassisBody: SCNPhysicsBody! { get }     func applyEngineForce(_ value: CGFloat, forWheelAtIndex index: Int)     func setSteeringAngle(_ value: CGFloat, forWheelAtIndex index: Int)     func applyBrakingForce(_ value: CGFloat, forWheelAtIndex index: Int) } ``` |
| To | ``` class SCNPhysicsVehicle : SCNPhysicsBehavior {     convenience init(chassisBody chassisBody: SCNPhysicsBody, wheels wheels: [SCNPhysicsVehicleWheel])     class func vehicleWithChassisBody(_ chassisBody: SCNPhysicsBody, wheels wheels: [SCNPhysicsVehicleWheel]) -> Self     var speedInKilometersPerHour: CGFloat { get }     var wheels: [SCNPhysicsVehicleWheel] { get }     var chassisBody: SCNPhysicsBody { get }     func applyEngineForce(_ value: CGFloat, forWheelAtIndex index: Int)     func setSteeringAngle(_ value: CGFloat, forWheelAtIndex index: Int)     func applyBrakingForce(_ value: CGFloat, forWheelAtIndex index: Int) } ``` |

Modified [SCNPhysicsVehicle.chassisBody](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387985-chassisbody)

|  | Declaration |
| --- | --- |
| From | ``` var chassisBody: SCNPhysicsBody! { get } ``` |
| To | ``` var chassisBody: SCNPhysicsBody { get } ``` |

Modified [SCNPhysicsVehicle.init(chassisBody: SCNPhysicsBody, wheels: [SCNPhysicsVehicleWheel])](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387943-vehiclewithchassisbody)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(chassisBody chassisBody: SCNPhysicsBody!, wheels wheels: [AnyObject]) ``` |
| To | ``` convenience init(chassisBody chassisBody: SCNPhysicsBody, wheels wheels: [SCNPhysicsVehicleWheel]) ``` |

Modified [SCNPhysicsVehicle.wheels](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387906-wheels)

|  | Declaration |
| --- | --- |
| From | ``` var wheels: [AnyObject]! { get } ``` |
| To | ``` var wheels: [SCNPhysicsVehicleWheel] { get } ``` |

Modified [SCNPhysicsVehicleWheel](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel)

|  | Declaration |
| --- | --- |
| From | ``` class SCNPhysicsVehicleWheel : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(node node: SCNNode!)     class func wheelWithNode(_ node: SCNNode!) -> Self     var node: SCNNode! { get }     var suspensionStiffness: CGFloat     var suspensionCompression: CGFloat     var suspensionDamping: CGFloat     var maximumSuspensionTravel: CGFloat     var frictionSlip: CGFloat     var maximumSuspensionForce: CGFloat     var connectionPosition: SCNVector3     var steeringAxis: SCNVector3     var axle: SCNVector3     var radius: CGFloat     var suspensionRestLength: CGFloat } ``` |
| To | ``` class SCNPhysicsVehicleWheel : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(node node: SCNNode)     class func wheelWithNode(_ node: SCNNode) -> Self     var node: SCNNode { get }     var suspensionStiffness: CGFloat     var suspensionCompression: CGFloat     var suspensionDamping: CGFloat     var maximumSuspensionTravel: CGFloat     var frictionSlip: CGFloat     var maximumSuspensionForce: CGFloat     var connectionPosition: SCNVector3     var steeringAxis: SCNVector3     var axle: SCNVector3     var radius: CGFloat     var suspensionRestLength: CGFloat } ``` |

Modified [SCNPhysicsVehicleWheel.init(node: SCNNode)](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387989-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(node node: SCNNode!) ``` |
| To | ``` convenience init(node node: SCNNode) ``` |

Modified [SCNPhysicsVehicleWheel.node](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387892-node)

|  | Declaration |
| --- | --- |
| From | ``` var node: SCNNode! { get } ``` |
| To | ``` var node: SCNNode { get } ``` |

Modified [SCNPhysicsWorld](https://developer.apple.com/documentation/scenekit/scnphysicsworld)

|  | Declaration |
| --- | --- |
| From | ``` class SCNPhysicsWorld : NSObject, NSSecureCoding, NSCoding {     var gravity: SCNVector3     var speed: CGFloat     var timeStep: NSTimeInterval     unowned(unsafe) var contactDelegate: SCNPhysicsContactDelegate!     func addBehavior(_ behavior: SCNPhysicsBehavior!)     func removeBehavior(_ behavior: SCNPhysicsBehavior!)     func removeAllBehaviors()     func allBehaviors() -> [AnyObject]!     func rayTestWithSegmentFromPoint(_ origin: SCNVector3, toPoint dest: SCNVector3, options options: [NSObject : AnyObject]!) -> [AnyObject]!     func contactTestBetweenBody(_ bodyA: SCNPhysicsBody!, andBody bodyB: SCNPhysicsBody!, options options: [NSObject : AnyObject]!) -> [AnyObject]!     func contactTestWithBody(_ body: SCNPhysicsBody!, options options: [NSObject : AnyObject]!) -> [AnyObject]!     func convexSweepTestWithShape(_ shape: SCNPhysicsShape!, fromTransform from: SCNMatrix4, toTransform to: SCNMatrix4, options options: [NSObject : AnyObject]!) -> [AnyObject]!     func updateCollisionPairs() } ``` |
| To | ``` class SCNPhysicsWorld : NSObject, NSSecureCoding, NSCoding {     var gravity: SCNVector3     var speed: CGFloat     var timeStep: NSTimeInterval     unowned(unsafe) var contactDelegate: SCNPhysicsContactDelegate?     func addBehavior(_ behavior: SCNPhysicsBehavior)     func removeBehavior(_ behavior: SCNPhysicsBehavior)     func removeAllBehaviors()     var allBehaviors: [SCNPhysicsBehavior] { get }     func rayTestWithSegmentFromPoint(_ origin: SCNVector3, toPoint dest: SCNVector3, options options: [String : AnyObject]?) -> [SCNHitTestResult]     func contactTestBetweenBody(_ bodyA: SCNPhysicsBody, andBody bodyB: SCNPhysicsBody, options options: [String : AnyObject]?) -> [SCNPhysicsContact]     func contactTestWithBody(_ body: SCNPhysicsBody, options options: [String : AnyObject]?) -> [SCNPhysicsContact]     func convexSweepTestWithShape(_ shape: SCNPhysicsShape, fromTransform from: SCNMatrix4, toTransform to: SCNMatrix4, options options: [String : AnyObject]?) -> [SCNPhysicsContact]     func updateCollisionPairs() } ``` |

Modified [SCNPhysicsWorld.addBehavior(_: SCNPhysicsBehavior)](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512839-addbehavior)

|  | Declaration |
| --- | --- |
| From | ``` func addBehavior(_ behavior: SCNPhysicsBehavior!) ``` |
| To | ``` func addBehavior(_ behavior: SCNPhysicsBehavior) ``` |

Modified [SCNPhysicsWorld.contactDelegate](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512843-contactdelegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var contactDelegate: SCNPhysicsContactDelegate! ``` |
| To | ``` unowned(unsafe) var contactDelegate: SCNPhysicsContactDelegate? ``` |

Modified [SCNPhysicsWorld.contactTestBetweenBody(_: SCNPhysicsBody, andBody: SCNPhysicsBody, options: [String : AnyObject]?) -> [SCNPhysicsContact]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512875-contacttestbetweenbody)

|  | Declaration |
| --- | --- |
| From | ``` func contactTestBetweenBody(_ bodyA: SCNPhysicsBody!, andBody bodyB: SCNPhysicsBody!, options options: [NSObject : AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func contactTestBetweenBody(_ bodyA: SCNPhysicsBody, andBody bodyB: SCNPhysicsBody, options options: [String : AnyObject]?) -> [SCNPhysicsContact] ``` |

Modified [SCNPhysicsWorld.contactTestWithBody(_: SCNPhysicsBody, options: [String : AnyObject]?) -> [SCNPhysicsContact]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512841-contacttestwithbody)

|  | Declaration |
| --- | --- |
| From | ``` func contactTestWithBody(_ body: SCNPhysicsBody!, options options: [NSObject : AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func contactTestWithBody(_ body: SCNPhysicsBody, options options: [String : AnyObject]?) -> [SCNPhysicsContact] ``` |

Modified [SCNPhysicsWorld.convexSweepTestWithShape(_: SCNPhysicsShape, fromTransform: SCNMatrix4, toTransform: SCNMatrix4, options: [String : AnyObject]?) -> [SCNPhysicsContact]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512859-convexsweeptest)

|  | Declaration |
| --- | --- |
| From | ``` func convexSweepTestWithShape(_ shape: SCNPhysicsShape!, fromTransform from: SCNMatrix4, toTransform to: SCNMatrix4, options options: [NSObject : AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func convexSweepTestWithShape(_ shape: SCNPhysicsShape, fromTransform from: SCNMatrix4, toTransform to: SCNMatrix4, options options: [String : AnyObject]?) -> [SCNPhysicsContact] ``` |

Modified [SCNPhysicsWorld.rayTestWithSegmentFromPoint(_: SCNVector3, toPoint: SCNVector3, options: [String : AnyObject]?) -> [SCNHitTestResult]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512857-raytestwithsegmentfrompoint)

|  | Declaration |
| --- | --- |
| From | ``` func rayTestWithSegmentFromPoint(_ origin: SCNVector3, toPoint dest: SCNVector3, options options: [NSObject : AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func rayTestWithSegmentFromPoint(_ origin: SCNVector3, toPoint dest: SCNVector3, options options: [String : AnyObject]?) -> [SCNHitTestResult] ``` |

Modified [SCNPhysicsWorld.removeBehavior(_: SCNPhysicsBehavior)](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512870-removebehavior)

|  | Declaration |
| --- | --- |
| From | ``` func removeBehavior(_ behavior: SCNPhysicsBehavior!) ``` |
| To | ``` func removeBehavior(_ behavior: SCNPhysicsBehavior) ``` |

Modified [SCNProgram](https://developer.apple.com/documentation/scenekit/scnprogram)

|  | Declaration |
| --- | --- |
| From | ``` class SCNProgram : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init!()     class func program() -> Self!     var vertexShader: String!     var fragmentShader: String!     var opaque: Bool     func setSemantic(_ semantic: String!, forSymbol symbol: String, options options: [NSObject : AnyObject]!)     func semanticForSymbol(_ symbol: String) -> String!     unowned(unsafe) var delegate: SCNProgramDelegate? } ``` |
| To | ``` class SCNProgram : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init()     class func program() -> Self     var vertexShader: String?     var fragmentShader: String?     var vertexFunctionName: String?     var fragmentFunctionName: String?     func handleBindingOfBufferNamed(_ name: String, frequency frequency: SCNBufferFrequency, usingBlock block: SCNBufferBindingBlock)     var opaque: Bool     func setSemantic(_ semantic: String?, forSymbol symbol: String, options options: [String : AnyObject]?)     func semanticForSymbol(_ symbol: String) -> String?     unowned(unsafe) var delegate: SCNProgramDelegate?     var library: MTLLibrary? } ``` |

Modified [SCNProgram.fragmentShader](https://developer.apple.com/documentation/scenekit/scnprogram/1523135-fragmentshader)

|  | Declaration |
| --- | --- |
| From | ``` var fragmentShader: String! ``` |
| To | ``` var fragmentShader: String? ``` |

Modified [SCNProgram.semanticForSymbol(_: String) -> String?](https://developer.apple.com/documentation/scenekit/scnprogram/1523350-semantic)

|  | Declaration |
| --- | --- |
| From | ``` func semanticForSymbol(_ symbol: String) -> String! ``` |
| To | ``` func semanticForSymbol(_ symbol: String) -> String? ``` |

Modified [SCNProgram.setSemantic(_: String?, forSymbol: String, options: [String : AnyObject]?)](https://developer.apple.com/documentation/scenekit/scnprogram/1522730-setsemantic)

|  | Declaration |
| --- | --- |
| From | ``` func setSemantic(_ semantic: String!, forSymbol symbol: String, options options: [NSObject : AnyObject]!) ``` |
| To | ``` func setSemantic(_ semantic: String?, forSymbol symbol: String, options options: [String : AnyObject]?) ``` |

Modified [SCNProgram.vertexShader](https://developer.apple.com/documentation/scenekit/scnprogram/1522891-vertexshader)

|  | Declaration |
| --- | --- |
| From | ``` var vertexShader: String! ``` |
| To | ``` var vertexShader: String? ``` |

Modified [SCNRenderer](https://developer.apple.com/documentation/scenekit/scnrenderer)

|  | Declaration |
| --- | --- |
| From | ``` class SCNRenderer : NSObject, SCNSceneRenderer, NSObjectProtocol, SCNTechniqueSupport {     convenience init(context context: UnsafeMutablePointer<Void>, options options: [NSObject : AnyObject]?)     class func rendererWithContext(_ context: UnsafeMutablePointer<Void>, options options: [NSObject : AnyObject]?) -> Self     var scene: SCNScene?     func render()     func renderAtTime(_ time: CFTimeInterval)     var nextFrameTime: CFTimeInterval { get } } ``` |
| To | ``` class SCNRenderer : NSObject, SCNSceneRenderer, SCNTechniqueSupport {     convenience init(context context: EAGLContext, options options: [NSObject : AnyObject]?)     class func rendererWithContext(_ context: EAGLContext, options options: [NSObject : AnyObject]?) -> Self     convenience init(device device: MTLDevice?, options options: [NSObject : AnyObject]?)     class func rendererWithDevice(_ device: MTLDevice?, options options: [NSObject : AnyObject]?) -> Self     var scene: SCNScene?     func renderAtTime(_ time: CFTimeInterval)     func renderAtTime(_ time: CFTimeInterval, viewport viewport: CGRect, commandBuffer commandBuffer: MTLCommandBuffer, passDescriptor renderPassDescriptor: MTLRenderPassDescriptor)     var nextFrameTime: CFTimeInterval { get }     func render() } ``` |

Modified [SCNRenderer.init(context: EAGLContext, options: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/scenekit/scnrenderer/1518408-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(context context: UnsafeMutablePointer<Void>, options options: [NSObject : AnyObject]?) ``` |
| To | ``` convenience init(context context: EAGLContext, options options: [NSObject : AnyObject]?) ``` |

Modified [SCNRenderer.render()](https://developer.apple.com/documentation/scenekit/scnrenderer/1518403-render)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [SCNScene](https://developer.apple.com/documentation/scenekit/scnscene)

|  | Declaration |
| --- | --- |
| From | ``` class SCNScene : NSObject, NSSecureCoding, NSCoding {     convenience init!()     class func scene() -> Self!     var rootNode: SCNNode { get }     var physicsWorld: SCNPhysicsWorld { get }     func attributeForKey(_ key: String) -> AnyObject?     func setAttribute(_ attribute: AnyObject, forKey key: String)     var background: SCNMaterialProperty { get }     convenience init?(named name: String)     class func sceneNamed(_ name: String) -> Self?     convenience init?(named name: String, inDirectory directory: String?, options options: [NSObject : AnyObject]?)     class func sceneNamed(_ name: String, inDirectory directory: String?, options options: [NSObject : AnyObject]?) -> Self?     convenience init?(URL url: NSURL, options options: [NSObject : AnyObject]?, error error: NSErrorPointer)     class func sceneWithURL(_ url: NSURL, options options: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Self?     var fogStartDistance: CGFloat     var fogEndDistance: CGFloat     var fogDensityExponent: CGFloat     var fogColor: AnyObject     var paused: Bool } extension SCNScene {     func addParticleSystem(_ system: SCNParticleSystem, withTransform transform: SCNMatrix4)     func removeAllParticleSystems()     func removeParticleSystem(_ system: SCNParticleSystem)     var particleSystems: [AnyObject]? { get } } ``` |
| To | ``` class SCNScene : NSObject, NSSecureCoding, NSCoding {     convenience init()     class func scene() -> Self     var rootNode: SCNNode { get }     var physicsWorld: SCNPhysicsWorld { get }     func attributeForKey(_ key: String) -> AnyObject?     func setAttribute(_ attribute: AnyObject?, forKey key: String)     var background: SCNMaterialProperty { get }     convenience init?(named name: String)     class func sceneNamed(_ name: String) -> Self?     convenience init?(named name: String, inDirectory directory: String?, options options: [String : AnyObject]?)     class func sceneNamed(_ name: String, inDirectory directory: String?, options options: [String : AnyObject]?) -> Self?     convenience init(URL url: NSURL, options options: [String : AnyObject]?) throws     class func sceneWithURL(_ url: NSURL, options options: [String : AnyObject]?) throws -> Self     var fogStartDistance: CGFloat     var fogEndDistance: CGFloat     var fogDensityExponent: CGFloat     var fogColor: AnyObject     var paused: Bool } extension SCNScene {     func addParticleSystem(_ system: SCNParticleSystem, withTransform transform: SCNMatrix4)     func removeAllParticleSystems()     func removeParticleSystem(_ system: SCNParticleSystem)     var particleSystems: [SCNParticleSystem]? { get } } ``` |

Modified [SCNScene.init(named: String, inDirectory: String?, options: [String : AnyObject]?)](https://developer.apple.com/documentation/scenekit/scnscene/1522851-scenenamed)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(named name: String, inDirectory directory: String?, options options: [NSObject : AnyObject]?) ``` |
| To | ``` convenience init?(named name: String, inDirectory directory: String?, options options: [String : AnyObject]?) ``` |

Modified [SCNScene.init(URL: NSURL, options: [String : AnyObject]?) throws](https://developer.apple.com/documentation/scenekit/scnscene/1522660-scenewithurl)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(URL url: NSURL, options options: [NSObject : AnyObject]?, error error: NSErrorPointer) ``` |
| To | ``` convenience init(URL url: NSURL, options options: [String : AnyObject]?) throws ``` |

Modified [SCNScene.particleSystems](https://developer.apple.com/documentation/scenekit/scnscene/1522787-particlesystems)

|  | Declaration |
| --- | --- |
| From | ``` var particleSystems: [AnyObject]? { get } ``` |
| To | ``` var particleSystems: [SCNParticleSystem]? { get } ``` |

Modified [SCNScene.setAttribute(_: AnyObject?, forKey: String)](https://developer.apple.com/documentation/scenekit/scnscene/1524229-setattribute)

|  | Declaration |
| --- | --- |
| From | ``` func setAttribute(_ attribute: AnyObject, forKey key: String) ``` |
| To | ``` func setAttribute(_ attribute: AnyObject?, forKey key: String) ``` |

Modified [SCNSceneRenderer](https://developer.apple.com/documentation/scenekit/scnscenerenderer)

|  | Declaration |
| --- | --- |
| From | ``` protocol SCNSceneRenderer : NSObjectProtocol {     var scene: SCNScene? { get set }     var sceneTime: NSTimeInterval { get set }     unowned(unsafe) var delegate: SCNSceneRendererDelegate? { get set }     func hitTest(_ thePoint: CGPoint, options options: [NSObject : AnyObject]?) -> [AnyObject]?     func isNodeInsideFrustum(_ node: SCNNode, withPointOfView pointOfView: SCNNode?) -> Bool     func projectPoint(_ point: SCNVector3) -> SCNVector3     func unprojectPoint(_ point: SCNVector3) -> SCNVector3     var playing: Bool { get set }     var loops: Bool { get set }     var pointOfView: SCNNode? { get set }     var autoenablesDefaultLighting: Bool { get set }     var jitteringEnabled: Bool { get set }     func prepareObject(_ object: AnyObject, shouldAbortBlock block: (() -> Bool)?) -> Bool     func prepareObjects(_ objects: [AnyObject], withCompletionHandler completionHandler: ((Bool) -> Void)?)     var showsStatistics: Bool { get set }     var overlaySKScene: SKScene! { get set }     var context: UnsafeMutablePointer<Void> { get } } ``` |
| To | ``` protocol SCNSceneRenderer : NSObjectProtocol {     var scene: SCNScene? { get set }     func presentScene(_ scene: SCNScene, withTransition transition: SKTransition, incomingPointOfView pointOfView: SCNNode?, completionHandler completionHandler: (() -> Void)?)     var sceneTime: NSTimeInterval { get set }     unowned(unsafe) var delegate: SCNSceneRendererDelegate? { get set }     func hitTest(_ point: CGPoint, options options: [String : AnyObject]?) -> [SCNHitTestResult]     func isNodeInsideFrustum(_ node: SCNNode, withPointOfView pointOfView: SCNNode) -> Bool     func nodesInsideFrustumWithPointOfView(_ pointOfView: SCNNode) -> [SCNNode]     func projectPoint(_ point: SCNVector3) -> SCNVector3     func unprojectPoint(_ point: SCNVector3) -> SCNVector3     var playing: Bool { get set }     var loops: Bool { get set }     var pointOfView: SCNNode? { get set }     var autoenablesDefaultLighting: Bool { get set }     var jitteringEnabled: Bool { get set }     func prepareObject(_ object: AnyObject, shouldAbortBlock block: (() -> Bool)?) -> Bool     func prepareObjects(_ objects: [AnyObject], withCompletionHandler completionHandler: ((Bool) -> Void)?)     var showsStatistics: Bool { get set }     var debugOptions: SCNDebugOptions { get set }     var overlaySKScene: SKScene? { get set }     var renderingAPI: SCNRenderingAPI { get }     var context: UnsafeMutablePointer<Void> { get }     var currentRenderCommandEncoder: MTLRenderCommandEncoder? { get }     var device: MTLDevice? { get }     var colorPixelFormat: MTLPixelFormat { get }     var depthPixelFormat: MTLPixelFormat { get }     var stencilPixelFormat: MTLPixelFormat { get }     var commandQueue: MTLCommandQueue? { get }     var audioEngine: AVAudioEngine { get }     var audioEnvironmentNode: AVAudioEnvironmentNode { get }     var audioListener: SCNNode? { get set } } ``` |

Modified [SCNSceneRenderer.hitTest(_: CGPoint, options: [String : AnyObject]?) -> [SCNHitTestResult]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522929-hittest)

|  | Declaration |
| --- | --- |
| From | ``` func hitTest(_ thePoint: CGPoint, options options: [NSObject : AnyObject]?) -> [AnyObject]? ``` |
| To | ``` func hitTest(_ point: CGPoint, options options: [String : AnyObject]?) -> [SCNHitTestResult] ``` |

Modified [SCNSceneRenderer.isNodeInsideFrustum(_: SCNNode, withPointOfView: SCNNode) -> Bool](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522647-isnodeinsidefrustum)

|  | Declaration |
| --- | --- |
| From | ``` func isNodeInsideFrustum(_ node: SCNNode, withPointOfView pointOfView: SCNNode?) -> Bool ``` |
| To | ``` func isNodeInsideFrustum(_ node: SCNNode, withPointOfView pointOfView: SCNNode) -> Bool ``` |

Modified [SCNSceneRenderer.overlaySKScene](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1524051-overlayskscene)

|  | Declaration |
| --- | --- |
| From | ``` var overlaySKScene: SKScene! { get set } ``` |
| To | ``` var overlaySKScene: SKScene? { get set } ``` |

Modified [SCNSceneSource](https://developer.apple.com/documentation/scenekit/scnscenesource)

|  | Declaration |
| --- | --- |
| From | ``` class SCNSceneSource : NSObject {     convenience init?(URL url: NSURL, options options: [NSObject : AnyObject]?)     class func sceneSourceWithURL(_ url: NSURL, options options: [NSObject : AnyObject]?) -> Self?     convenience init?(data data: NSData, options options: [NSObject : AnyObject]?)     class func sceneSourceWithData(_ data: NSData, options options: [NSObject : AnyObject]?) -> Self?     init?(URL url: NSURL, options options: [NSObject : AnyObject]?)     init?(data data: NSData, options options: [NSObject : AnyObject]?)     var url: NSURL? { get }     var data: NSData? { get }     func sceneWithOptions(_ options: [NSObject : AnyObject]?, statusHandler statusHandler: SCNSceneSourceStatusHandler?) -> SCNScene?     func sceneWithOptions(_ options: [NSObject : AnyObject]?, error error: NSErrorPointer) -> SCNScene?     func propertyForKey(_ key: String) -> AnyObject?     func entryWithIdentifier(_ uid: String, withClass entryClass: AnyClass) -> AnyObject?     func identifiersOfEntriesWithClass(_ entryClass: AnyClass) -> [AnyObject]?     func entriesPassingTest(_ predicate: (AnyObject!, String!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AnyObject] } ``` |
| To | ``` class SCNSceneSource : NSObject {     convenience init?(URL url: NSURL, options options: [String : AnyObject]?)     class func sceneSourceWithURL(_ url: NSURL, options options: [String : AnyObject]?) -> Self?     convenience init?(data data: NSData, options options: [String : AnyObject]?)     class func sceneSourceWithData(_ data: NSData, options options: [String : AnyObject]?) -> Self?     init?(URL url: NSURL, options options: [String : AnyObject]?)     init?(data data: NSData, options options: [String : AnyObject]?)     var url: NSURL? { get }     var data: NSData? { get }     func sceneWithOptions(_ options: [String : AnyObject]?, statusHandler statusHandler: SCNSceneSourceStatusHandler?) -> SCNScene?     func sceneWithOptions(_ options: [String : AnyObject]?) throws -> SCNScene     func propertyForKey(_ key: String) -> AnyObject?     func __entryWithIdentifier(_ uid: String, withClass entryClass: AnyClass) -> AnyObject?     func identifiersOfEntriesWithClass(_ entryClass: AnyClass) -> [String]     func entriesPassingTest(_ predicate: (AnyObject, String, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AnyObject] } extension SCNSceneSource {     @warn_unused_result     func entryWithIdentifier<T>(_ uid: String, withClass entryClass: T.Type) -> T? } extension SCNSceneSource {     @warn_unused_result     func entryWithIdentifier<T>(_ uid: String, withClass entryClass: T.Type) -> T? } ``` |

Modified [SCNSceneSource.entriesPassingTest(_: (AnyObject, String, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AnyObject]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523055-entries)

|  | Declaration |
| --- | --- |
| From | ``` func entriesPassingTest(_ predicate: (AnyObject!, String!, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AnyObject] ``` |
| To | ``` func entriesPassingTest(_ predicate: (AnyObject, String, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AnyObject] ``` |

Modified [SCNSceneSource.identifiersOfEntriesWithClass(_: AnyClass) -> [String]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523656-identifiersofentrieswithclass)

|  | Declaration |
| --- | --- |
| From | ``` func identifiersOfEntriesWithClass(_ entryClass: AnyClass) -> [AnyObject]? ``` |
| To | ``` func identifiersOfEntriesWithClass(_ entryClass: AnyClass) -> [String] ``` |

Modified [SCNSceneSource.init(data: NSData, options: [String : AnyObject]?)](https://developer.apple.com/documentation/scenekit/scnscenesource/1523500-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` init?(data data: NSData, options options: [NSObject : AnyObject]?) ``` |
| To | ``` init?(data data: NSData, options options: [String : AnyObject]?) ``` |

Modified [SCNSceneSource.init(URL: NSURL, options: [String : AnyObject]?)](https://developer.apple.com/documentation/scenekit/scnscenesource/1522629-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(URL url: NSURL, options options: [NSObject : AnyObject]?) ``` |
| To | ``` init?(URL url: NSURL, options options: [String : AnyObject]?) ``` |

Modified [SCNSceneSource.sceneWithOptions(_: [String : AnyObject]?) throws -> SCNScene](https://developer.apple.com/documentation/scenekit/scnscenesource/1523962-scenewithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func sceneWithOptions(_ options: [NSObject : AnyObject]?, error error: NSErrorPointer) -> SCNScene? ``` |
| To | ``` func sceneWithOptions(_ options: [String : AnyObject]?) throws -> SCNScene ``` |

Modified [SCNSceneSource.sceneWithOptions(_: [String : AnyObject]?, statusHandler: SCNSceneSourceStatusHandler?) -> SCNScene?](https://developer.apple.com/documentation/scenekit/scnscenesource/1522887-scenewithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func sceneWithOptions(_ options: [NSObject : AnyObject]?, statusHandler statusHandler: SCNSceneSourceStatusHandler?) -> SCNScene? ``` |
| To | ``` func sceneWithOptions(_ options: [String : AnyObject]?, statusHandler statusHandler: SCNSceneSourceStatusHandler?) -> SCNScene? ``` |

Modified [SCNSceneSourceStatus [enum]](https://developer.apple.com/documentation/scenekit/scnscenesourcestatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SCNShadable](https://developer.apple.com/documentation/scenekit/scnshadable)

|  | Declaration |
| --- | --- |
| From | ``` protocol SCNShadable : NSObjectProtocol {     optional var shaderModifiers: [NSObject : AnyObject]? { get set }     optional var program: SCNProgram! { get set }     optional func handleBindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock)     optional func handleUnbindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock) } ``` |
| To | ``` protocol SCNShadable : NSObjectProtocol {     optional var program: SCNProgram? { get set }     optional func handleBindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock?)     optional func handleUnbindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock?)     optional var shaderModifiers: [String : String]? { get set } } ``` |

Modified [SCNShadable.handleBindingOfSymbol(_: String, usingBlock: SCNBindingBlock?)](https://developer.apple.com/documentation/scenekit/scnshadable/1523063-handlebindingofsymbol)

|  | Declaration |
| --- | --- |
| From | ``` optional func handleBindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock) ``` |
| To | ``` optional func handleBindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock?) ``` |

Modified [SCNShadable.handleUnbindingOfSymbol(_: String, usingBlock: SCNBindingBlock?)](https://developer.apple.com/documentation/scenekit/scnshadable/1522783-handleunbinding)

|  | Declaration |
| --- | --- |
| From | ``` optional func handleUnbindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock) ``` |
| To | ``` optional func handleUnbindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock?) ``` |

Modified [SCNShadable.program](https://developer.apple.com/documentation/scenekit/scnshadable/1523689-program)

|  | Declaration |
| --- | --- |
| From | ``` optional var program: SCNProgram! { get set } ``` |
| To | ``` optional var program: SCNProgram? { get set } ``` |

Modified [SCNShadable.shaderModifiers](https://developer.apple.com/documentation/scenekit/scnshadable/1523348-shadermodifiers)

|  | Declaration |
| --- | --- |
| From | ``` optional var shaderModifiers: [NSObject : AnyObject]? { get set } ``` |
| To | ``` optional var shaderModifiers: [String : String]? { get set } ``` |

Modified [SCNShadowMode [enum]](https://developer.apple.com/documentation/scenekit/scnshadowmode)

|  | Introduction | Raw Value Type |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 8.0 | Int |

Modified [SCNShape](https://developer.apple.com/documentation/scenekit/scnshape)

|  | Declaration |
| --- | --- |
| From | ``` class SCNShape : SCNGeometry {     convenience init(path path: UIBezierPath, extrusionDepth extrusionDepth: CGFloat)     class func shapeWithPath(_ path: UIBezierPath, extrusionDepth extrusionDepth: CGFloat) -> Self     @NSCopying var path: UIBezierPath!     var extrusionDepth: CGFloat     var chamferMode: SCNChamferMode     var chamferRadius: CGFloat     @NSCopying var chamferProfile: UIBezierPath! } ``` |
| To | ``` class SCNShape : SCNGeometry {     convenience init(path path: UIBezierPath?, extrusionDepth extrusionDepth: CGFloat)     class func shapeWithPath(_ path: UIBezierPath?, extrusionDepth extrusionDepth: CGFloat) -> Self     @NSCopying var path: UIBezierPath?     var extrusionDepth: CGFloat     var chamferMode: SCNChamferMode     var chamferRadius: CGFloat     @NSCopying var chamferProfile: UIBezierPath? } ``` |

Modified [SCNShape.chamferProfile](https://developer.apple.com/documentation/scenekit/scnshape/1522865-chamferprofile)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var chamferProfile: UIBezierPath! ``` |
| To | ``` @NSCopying var chamferProfile: UIBezierPath? ``` |

Modified [SCNShape.init(path: UIBezierPath?, extrusionDepth: CGFloat)](https://developer.apple.com/documentation/scenekit/scnshape/1523432-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(path path: UIBezierPath, extrusionDepth extrusionDepth: CGFloat) ``` |
| To | ``` convenience init(path path: UIBezierPath?, extrusionDepth extrusionDepth: CGFloat) ``` |

Modified [SCNShape.path](https://developer.apple.com/documentation/scenekit/scnshape/1523434-path)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var path: UIBezierPath! ``` |
| To | ``` @NSCopying var path: UIBezierPath? ``` |

Modified [SCNSkinner](https://developer.apple.com/documentation/scenekit/scnskinner)

|  | Declaration |
| --- | --- |
| From | ``` class SCNSkinner : NSObject, NSSecureCoding, NSCoding {     var skeleton: SCNNode!     convenience init!(baseGeometry baseGeometry: SCNGeometry!, bones bones: [AnyObject]!, boneInverseBindTransforms boneInverseBindTransforms: [AnyObject]!, boneWeights boneWeights: SCNGeometrySource!, boneIndices boneIndices: SCNGeometrySource!)     class func skinnerWithBaseGeometry(_ baseGeometry: SCNGeometry!, bones bones: [AnyObject]!, boneInverseBindTransforms boneInverseBindTransforms: [AnyObject]!, boneWeights boneWeights: SCNGeometrySource!, boneIndices boneIndices: SCNGeometrySource!) -> Self!     var baseGeometry: SCNGeometry!     var baseGeometryBindTransform: SCNMatrix4     var boneInverseBindTransforms: [AnyObject]! { get }     var bones: [AnyObject]! { get }     var boneWeights: SCNGeometrySource! { get }     var boneIndices: SCNGeometrySource! { get } } ``` |
| To | ``` class SCNSkinner : NSObject, NSSecureCoding, NSCoding {     var skeleton: SCNNode?     convenience init(baseGeometry baseGeometry: SCNGeometry?, bones bones: [SCNNode], boneInverseBindTransforms boneInverseBindTransforms: [NSValue]?, boneWeights boneWeights: SCNGeometrySource, boneIndices boneIndices: SCNGeometrySource)     class func skinnerWithBaseGeometry(_ baseGeometry: SCNGeometry?, bones bones: [SCNNode], boneInverseBindTransforms boneInverseBindTransforms: [NSValue]?, boneWeights boneWeights: SCNGeometrySource, boneIndices boneIndices: SCNGeometrySource) -> Self     var baseGeometry: SCNGeometry?     var baseGeometryBindTransform: SCNMatrix4     var boneInverseBindTransforms: [NSValue]? { get }     var bones: [SCNNode] { get }     var boneWeights: SCNGeometrySource { get }     var boneIndices: SCNGeometrySource { get } } ``` |

Modified [SCNSkinner.baseGeometry](https://developer.apple.com/documentation/scenekit/scnskinner/1522823-basegeometry)

|  | Declaration |
| --- | --- |
| From | ``` var baseGeometry: SCNGeometry! ``` |
| To | ``` var baseGeometry: SCNGeometry? ``` |

Modified [SCNSkinner.boneIndices](https://developer.apple.com/documentation/scenekit/scnskinner/1524117-boneindices)

|  | Declaration |
| --- | --- |
| From | ``` var boneIndices: SCNGeometrySource! { get } ``` |
| To | ``` var boneIndices: SCNGeometrySource { get } ``` |

Modified [SCNSkinner.boneInverseBindTransforms](https://developer.apple.com/documentation/scenekit/scnskinner/1523802-boneinversebindtransforms)

|  | Declaration |
| --- | --- |
| From | ``` var boneInverseBindTransforms: [AnyObject]! { get } ``` |
| To | ``` var boneInverseBindTransforms: [NSValue]? { get } ``` |

Modified [SCNSkinner.bones](https://developer.apple.com/documentation/scenekit/scnskinner/1522732-bones)

|  | Declaration |
| --- | --- |
| From | ``` var bones: [AnyObject]! { get } ``` |
| To | ``` var bones: [SCNNode] { get } ``` |

Modified [SCNSkinner.boneWeights](https://developer.apple.com/documentation/scenekit/scnskinner/1522986-boneweights)

|  | Declaration |
| --- | --- |
| From | ``` var boneWeights: SCNGeometrySource! { get } ``` |
| To | ``` var boneWeights: SCNGeometrySource { get } ``` |

Modified [SCNSkinner.init(baseGeometry: SCNGeometry?, bones: [SCNNode], boneInverseBindTransforms: [NSValue]?, boneWeights: SCNGeometrySource, boneIndices: SCNGeometrySource)](https://developer.apple.com/documentation/scenekit/scnskinner/1523964-skinnerwithbasegeometry)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(baseGeometry baseGeometry: SCNGeometry!, bones bones: [AnyObject]!, boneInverseBindTransforms boneInverseBindTransforms: [AnyObject]!, boneWeights boneWeights: SCNGeometrySource!, boneIndices boneIndices: SCNGeometrySource!) ``` |
| To | ``` convenience init(baseGeometry baseGeometry: SCNGeometry?, bones bones: [SCNNode], boneInverseBindTransforms boneInverseBindTransforms: [NSValue]?, boneWeights boneWeights: SCNGeometrySource, boneIndices boneIndices: SCNGeometrySource) ``` |

Modified [SCNSkinner.skeleton](https://developer.apple.com/documentation/scenekit/scnskinner/1523048-skeleton)

|  | Declaration |
| --- | --- |
| From | ``` var skeleton: SCNNode! ``` |
| To | ``` var skeleton: SCNNode? ``` |

Modified [SCNTechnique](https://developer.apple.com/documentation/scenekit/scntechnique)

|  | Declaration |
| --- | --- |
| From | ``` class SCNTechnique : NSObject, SCNAnimatable, NSObjectProtocol, NSCopying, NSSecureCoding, NSCoding {     init?(dictionary dictionary: [NSObject : AnyObject]) -> SCNTechnique     class func techniqueWithDictionary(_ dictionary: [NSObject : AnyObject]) -> SCNTechnique?     init?(bySequencingTechniques techniques: [AnyObject]) -> SCNTechnique     class func techniqueBySequencingTechniques(_ techniques: [AnyObject]) -> SCNTechnique?     func handleBindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock)     var dictionaryRepresentation: [NSObject : AnyObject] { get } } ``` |
| To | ``` class SCNTechnique : NSObject, SCNAnimatable, NSCopying, NSSecureCoding, NSCoding {      init?(dictionary dictionary: [String : AnyObject])     class func techniqueWithDictionary(_ dictionary: [String : AnyObject]) -> SCNTechnique?      init?(bySequencingTechniques techniques: [SCNTechnique])     class func techniqueBySequencingTechniques(_ techniques: [SCNTechnique]) -> SCNTechnique?     func handleBindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock?)     var dictionaryRepresentation: [String : AnyObject] { get }     subscript (_ key: AnyObject) -> AnyObject? { get }     func objectForKeyedSubscript(_ key: AnyObject) -> AnyObject?     func setObject(_ obj: AnyObject?, forKeyedSubscript key: NSCopying) } ``` |

Modified [SCNTechnique.dictionaryRepresentation](https://developer.apple.com/documentation/scenekit/scntechnique/1520492-dictionaryrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` var dictionaryRepresentation: [NSObject : AnyObject] { get } ``` |
| To | ``` var dictionaryRepresentation: [String : AnyObject] { get } ``` |

Modified [SCNTechnique.handleBindingOfSymbol(_: String, usingBlock: SCNBindingBlock?)](https://developer.apple.com/documentation/scenekit/scntechnique/1520490-handlebinding)

|  | Declaration |
| --- | --- |
| From | ``` func handleBindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock) ``` |
| To | ``` func handleBindingOfSymbol(_ symbol: String, usingBlock block: SCNBindingBlock?) ``` |

Modified [SCNTechnique.init(bySequencingTechniques: [SCNTechnique])](https://developer.apple.com/documentation/scenekit/scntechnique/1520497-techniquebysequencingtechniques)

|  | Declaration |
| --- | --- |
| From | ``` init?(bySequencingTechniques techniques: [AnyObject]) -> SCNTechnique ``` |
| To | ``` init?(bySequencingTechniques techniques: [SCNTechnique]) ``` |

Modified [SCNTechnique.init(dictionary: [String : AnyObject])](https://developer.apple.com/documentation/scenekit/scntechnique/1520494-techniquewithdictionary)

|  | Declaration |
| --- | --- |
| From | ``` init?(dictionary dictionary: [NSObject : AnyObject]) -> SCNTechnique ``` |
| To | ``` init?(dictionary dictionary: [String : AnyObject]) ``` |

Modified [SCNText](https://developer.apple.com/documentation/scenekit/scntext)

|  | Declaration |
| --- | --- |
| From | ``` class SCNText : SCNGeometry {     convenience init(string string: AnyObject, extrusionDepth extrusionDepth: CGFloat)     class func textWithString(_ string: AnyObject, extrusionDepth extrusionDepth: CGFloat) -> Self     var extrusionDepth: CGFloat     @NSCopying var string: AnyObject!     var font: UIFont!     var wrapped: Bool     var containerFrame: CGRect     var truncationMode: String!     var alignmentMode: String!     var chamferRadius: CGFloat     @NSCopying var chamferProfile: UIBezierPath!     var flatness: CGFloat } ``` |
| To | ``` class SCNText : SCNGeometry {     convenience init(string string: AnyObject?, extrusionDepth extrusionDepth: CGFloat)     class func textWithString(_ string: AnyObject?, extrusionDepth extrusionDepth: CGFloat) -> Self     var extrusionDepth: CGFloat     @NSCopying var string: AnyObject?     var font: UIFont!     var wrapped: Bool     var containerFrame: CGRect     var truncationMode: String     var alignmentMode: String     var chamferRadius: CGFloat     @NSCopying var chamferProfile: UIBezierPath?     var flatness: CGFloat } ``` |

Modified [SCNText.alignmentMode](https://developer.apple.com/documentation/scenekit/scntext/1523158-alignmentmode)

|  | Declaration |
| --- | --- |
| From | ``` var alignmentMode: String! ``` |
| To | ``` var alignmentMode: String ``` |

Modified [SCNText.chamferProfile](https://developer.apple.com/documentation/scenekit/scntext/1523334-chamferprofile)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var chamferProfile: UIBezierPath! ``` |
| To | ``` @NSCopying var chamferProfile: UIBezierPath? ``` |

Modified [SCNText.init(string: AnyObject?, extrusionDepth: CGFloat)](https://developer.apple.com/documentation/scenekit/scntext/1522734-textwithstring)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(string string: AnyObject, extrusionDepth extrusionDepth: CGFloat) ``` |
| To | ``` convenience init(string string: AnyObject?, extrusionDepth extrusionDepth: CGFloat) ``` |

Modified [SCNText.string](https://developer.apple.com/documentation/scenekit/scntext/1523439-string)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var string: AnyObject! ``` |
| To | ``` @NSCopying var string: AnyObject? ``` |

Modified [SCNText.truncationMode](https://developer.apple.com/documentation/scenekit/scntext/1523414-truncationmode)

|  | Declaration |
| --- | --- |
| From | ``` var truncationMode: String! ``` |
| To | ``` var truncationMode: String ``` |

Modified [SCNTransformConstraint](https://developer.apple.com/documentation/scenekit/scntransformconstraint)

|  | Declaration |
| --- | --- |
| From | ``` class SCNTransformConstraint : SCNConstraint {     convenience init(inWorldSpace world: Bool, withBlock block: (SCNNode!, SCNMatrix4) -> SCNMatrix4)     class func transformConstraintInWorldSpace(_ world: Bool, withBlock block: (SCNNode!, SCNMatrix4) -> SCNMatrix4) -> Self } ``` |
| To | ``` class SCNTransformConstraint : SCNConstraint {     convenience init(inWorldSpace world: Bool, withBlock block: (SCNNode, SCNMatrix4) -> SCNMatrix4)     class func transformConstraintInWorldSpace(_ world: Bool, withBlock block: (SCNNode, SCNMatrix4) -> SCNMatrix4) -> Self } ``` |

Modified [SCNTransformConstraint.init(inWorldSpace: Bool, withBlock: (SCNNode, SCNMatrix4) -> SCNMatrix4)](https://developer.apple.com/documentation/scenekit/scntransformconstraint/1468679-transformconstraintinworldspace)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(inWorldSpace world: Bool, withBlock block: (SCNNode!, SCNMatrix4) -> SCNMatrix4) ``` |
| To | ``` convenience init(inWorldSpace world: Bool, withBlock block: (SCNNode, SCNMatrix4) -> SCNMatrix4) ``` |

Modified [SCNTransparencyMode [enum]](https://developer.apple.com/documentation/scenekit/scntransparencymode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SCNVector3 [struct]](https://developer.apple.com/documentation/scenekit/scnvector3)

|  | Declaration |
| --- | --- |
| From | ``` struct SCNVector3 {     var x: Float     var y: Float     var z: Float     init()     init(x x: Float, y y: Float, z z: Float) } ``` |
| To | ``` struct SCNVector3 {     var x: Float     var y: Float     var z: Float     init()     init(x x: Float, y y: Float, z z: Float) } extension SCNVector3 {     init(_ x: Float, _ y: Float, _ z: Float)     init(_ x: CGFloat, _ y: CGFloat, _ z: CGFloat)     init(_ x: Double, _ y: Double, _ z: Double)     init(_ x: Int, _ y: Int, _ z: Int)     init(_ v: float3)     init(_ v: double3) } extension SCNVector3 {     init(_ x: Float, _ y: Float, _ z: Float)     init(_ x: CGFloat, _ y: CGFloat, _ z: CGFloat)     init(_ x: Double, _ y: Double, _ z: Double)     init(_ x: Int, _ y: Int, _ z: Int)     init(_ v: float3)     init(_ v: double3) } ``` |

Modified [SCNVector4 [struct]](https://developer.apple.com/documentation/scenekit/scnvector4)

|  | Declaration |
| --- | --- |
| From | ``` struct SCNVector4 {     var x: Float     var y: Float     var z: Float     var w: Float     init()     init(x x: Float, y y: Float, z z: Float, w w: Float) } ``` |
| To | ``` struct SCNVector4 {     var x: Float     var y: Float     var z: Float     var w: Float     init()     init(x x: Float, y y: Float, z z: Float, w w: Float) } extension SCNVector4 {     init(_ x: Float, _ y: Float, _ z: Float, _ w: Float)     init(_ x: CGFloat, _ y: CGFloat, _ z: CGFloat, _ w: CGFloat)     init(_ x: Double, _ y: Double, _ z: Double, _ w: Double)     init(_ x: Int, _ y: Int, _ z: Int, _ w: Int)     init(_ v: float4)     init(_ v: double4) } extension SCNVector4 {     init(_ x: Float, _ y: Float, _ z: Float, _ w: Float)     init(_ x: CGFloat, _ y: CGFloat, _ z: CGFloat, _ w: CGFloat)     init(_ x: Double, _ y: Double, _ z: Double, _ w: Double)     init(_ x: Int, _ y: Int, _ z: Int, _ w: Int)     init(_ v: float4)     init(_ v: double4) } ``` |

Modified [SCNView](https://developer.apple.com/documentation/scenekit/scnview)

|  | Declaration |
| --- | --- |
| From | ``` class SCNView : UIView, SCNSceneRenderer, NSObjectProtocol, SCNTechniqueSupport {     init(frame frame: CGRect, options options: [NSObject : AnyObject]?)     var scene: SCNScene?     var allowsCameraControl: Bool     func snapshot() -> UIImage?     @IBAction func play(_ sender: AnyObject?)     @IBAction func pause(_ sender: AnyObject?)     @IBAction func stop(_ sender: AnyObject?)     var eaglContext: EAGLContext     var preferredFramesPerSecond: Int     var antialiasingMode: SCNAntialiasingMode } ``` |
| To | ``` class SCNView : UIView, SCNSceneRenderer, SCNTechniqueSupport {     init(frame frame: CGRect, options options: [String : AnyObject]?)     var scene: SCNScene?     var allowsCameraControl: Bool     func snapshot() -> UIImage     @IBAction func play(_ sender: AnyObject?)     @IBAction func pause(_ sender: AnyObject?)     @IBAction func stop(_ sender: AnyObject?)     var preferredFramesPerSecond: Int     var eaglContext: EAGLContext?     var antialiasingMode: SCNAntialiasingMode } ``` |

Modified [SCNView.eaglContext](https://developer.apple.com/documentation/scenekit/scnview/1621072-eaglcontext)

|  | Declaration |
| --- | --- |
| From | ``` var eaglContext: EAGLContext ``` |
| To | ``` var eaglContext: EAGLContext? ``` |

Modified [SCNView.init(frame: CGRect, options: [String : AnyObject]?)](https://developer.apple.com/documentation/scenekit/scnview/1524215-initwithframe)

|  | Declaration |
| --- | --- |
| From | ``` init(frame frame: CGRect, options options: [NSObject : AnyObject]?) ``` |
| To | ``` init(frame frame: CGRect, options options: [String : AnyObject]?) ``` |

Modified [SCNView.snapshot() -> UIImage](https://developer.apple.com/documentation/scenekit/scnview/1524031-snapshot)

|  | Declaration |
| --- | --- |
| From | ``` func snapshot() -> UIImage? ``` |
| To | ``` func snapshot() -> UIImage ``` |

Modified [SCNWrapMode [enum]](https://developer.apple.com/documentation/scenekit/scnwrapmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SCNAnimationEventBlock](https://developer.apple.com/documentation/scenekit/scnanimationeventblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNAnimationEventBlock = (CAAnimation!, AnyObject!, Bool) -> Void ``` |
| To | ``` typealias SCNAnimationEventBlock = (CAAnimation, AnyObject, Bool) -> Void ``` |

Modified [SCNBindingBlock](https://developer.apple.com/documentation/scenekit/scnbindingblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNBindingBlock = (UInt32, UInt32, SCNNode!, SCNRenderer!) -> Void ``` |
| To | ``` typealias SCNBindingBlock = (UInt32, UInt32, SCNNode, SCNRenderer) -> Void ``` |

Modified [SCNExportJavaScriptModule(_: JSContext)](https://developer.apple.com/documentation/scenekit/1524164-scnexportjavascriptmodule)

|  | Declaration |
| --- | --- |
| From | ``` func SCNExportJavaScriptModule(_ context: JSContext!) ``` |
| To | ``` func SCNExportJavaScriptModule(_ context: JSContext) ``` |

Modified [SCNSceneExportProgressHandler](https://developer.apple.com/documentation/scenekit/scnsceneexportprogresshandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNSceneExportProgressHandler = (Float, NSError!, UnsafeMutablePointer<ObjCBool>) -> Void ``` |
| To | ``` typealias SCNSceneExportProgressHandler = (Float, NSError?, UnsafeMutablePointer<ObjCBool>) -> Void ``` |

Modified [SCNSceneSourceStatusHandler](https://developer.apple.com/documentation/scenekit/scnscenesourcestatushandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNSceneSourceStatusHandler = (Float, SCNSceneSourceStatus, NSError!, UnsafeMutablePointer<ObjCBool>) -> Void ``` |
| To | ``` typealias SCNSceneSourceStatusHandler = (Float, SCNSceneSourceStatus, NSError?, UnsafeMutablePointer<ObjCBool>) -> Void ``` |

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
