---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/SpriteKit.html
archived_at: '2026-07-18T02:53:44.197517Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# SpriteKit Changes for Swift

### SpriteKit

Removed SKShapeNode.getMirror() -> MirrorTypeRemoved SKSpriteNode.getMirror() -> MirrorTypeRemoved SKTexture.getMirror() -> MirrorTypeRemoved SKTextureAtlas.getMirror() -> MirrorTypeRemoved SKVideoNode.init(videoFileNamed: String!) -> SKVideoNodeRemoved SKVideoNode.init(videoURL: NSURL!) -> SKVideoNodeAdded [SK3DNode.projectPoint(_: vector_float3) -> vector_float3](https://developer.apple.com/documentation/spritekit/sk3dnode/1520400-projectpoint)Added [SK3DNode.unprojectPoint(_: vector_float3) -> vector_float3](https://developer.apple.com/documentation/spritekit/sk3dnode/1520024-unprojectpoint)Added [SKAction.animateWithNormalTextures(_: [SKTexture], timePerFrame: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417746-animate)Added [SKAction.animateWithNormalTextures(_: [SKTexture], timePerFrame: NSTimeInterval, resize: Bool, restore: Bool) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417810-animatewithnormaltextures)Added [SKAction.applyAngularImpulse(_: CGFloat, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417775-applyangularimpulse)Added [SKAction.applyForce(_: CGVector, atPoint: CGPoint, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417823-applyforce)Added [SKAction.applyForce(_: CGVector, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417782-applyforce)Added [SKAction.applyImpulse(_: CGVector, atPoint: CGPoint, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417732-applyimpulse)Added [SKAction.applyImpulse(_: CGVector, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417770-applyimpulse)Added [SKAction.applyTorque(_: CGFloat, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417756-applytorque)Added [SKAction.changeChargeBy(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417714-changechargeby)Added [SKAction.changeChargeTo(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417752-changechargeto)Added [SKAction.changeMassBy(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417710-changemassby)Added [SKAction.changeMassTo(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417780-changemassto)Added [SKAction.changeObstructionBy(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1520346-changeobstructionby)Added [SKAction.changeObstructionTo(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1519718-changeobstructionto)Added [SKAction.changeOcclusionBy(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1520117-changeocclusionby)Added [SKAction.changeOcclusionTo(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1520433-changeocclusionto)Added [SKAction.changePlaybackRateBy(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417670-changeplaybackrate)Added [SKAction.changePlaybackRateTo(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417808-changeplaybackrate)Added [SKAction.changeReverbBy(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1519568-changereverb)Added [SKAction.changeReverbTo(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1520320-changereverbto)Added [SKAction.changeVolumeBy(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417726-changevolumeby)Added [SKAction.changeVolumeTo(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417682-changevolumeto)Added [SKAction.init(named: String)](https://developer.apple.com/documentation/spritekit/skaction/1417814-init)Added [SKAction.init(named: String, duration: NSTimeInterval)](https://developer.apple.com/documentation/spritekit/skaction/1417697-actionnamed)Added [SKAction.init(named: String, fromURL: NSURL)](https://developer.apple.com/documentation/spritekit/skaction/1417680-init)Added [SKAction.init(named: String, fromURL: NSURL, duration: NSTimeInterval)](https://developer.apple.com/documentation/spritekit/skaction/1417754-init)Added [SKAction.pause() -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417820-pause)Added [SKAction.performSelector(_: Selector, onTarget: AnyObject) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417764-perform)Added [SKAction.play() -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417730-play)Added [SKAction.setNormalTexture(_: SKTexture) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417706-setnormaltexture)Added [SKAction.setNormalTexture(_: SKTexture, resize: Bool) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417654-setnormaltexture)Added [SKAction.stereoPanBy(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1519713-stereopan)Added [SKAction.stereoPanTo(_: Float, duration: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1519976-stereopanto)Added [SKAction.stop() -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417794-stop)Added [SKAudioNode](https://developer.apple.com/documentation/spritekit/skaudionode)Added [SKAudioNode.autoplayLooped](https://developer.apple.com/documentation/spritekit/skaudionode/1520336-autoplaylooped)Added [SKAudioNode.avAudioNode](https://developer.apple.com/documentation/spritekit/skaudionode/1519633-avaudionode)Added [SKAudioNode.init(AVAudioNode: AVAudioNode?)](https://developer.apple.com/documentation/spritekit/skaudionode/1520232-initwithavaudionode)Added [SKAudioNode.init(coder: NSCoder)](https://developer.apple.com/documentation/spritekit/skaudionode/1520341-initwithcoder)Added [SKAudioNode.init(fileNamed: String)](https://developer.apple.com/documentation/spritekit/skaudionode/1519678-initwithfilenamed)Added [SKAudioNode.init(URL: NSURL)](https://developer.apple.com/documentation/spritekit/skaudionode/1519661-init)Added [SKAudioNode.positional](https://developer.apple.com/documentation/spritekit/skaudionode/1520418-ispositional)Added [SKCameraNode](https://developer.apple.com/documentation/spritekit/skcameranode)Added [SKCameraNode.containedNodeSet() -> Set<SKNode>](https://developer.apple.com/documentation/spritekit/skcameranode/1434222-containednodeset)Added [SKCameraNode.containsNode(_: SKNode) -> Bool](https://developer.apple.com/documentation/spritekit/skcameranode/1434224-containsnode)Added [SKEmitterNode.particleRenderOrder](https://developer.apple.com/documentation/spritekit/skemitternode/1397986-particlerenderorder)Added [SKFieldNode.customFieldWithEvaluationBlock(_: SKFieldForceEvaluator) -> SKFieldNode [class]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519710-customfieldwithevaluationblock)Added [SKFieldNode.direction](https://developer.apple.com/documentation/spritekit/skfieldnode/1520091-direction)Added [SKFieldNode.linearGravityFieldWithVector(_: vector_float3) -> SKFieldNode [class]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520145-lineargravityfieldwithvector)Added [SKFieldNode.velocityFieldWithVector(_: vector_float3) -> SKFieldNode [class]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520271-velocityfieldwithvector)Added [SKNode.isEqualToNode(_: SKNode) -> Bool](https://developer.apple.com/documentation/spritekit/sknode/1483078-isequaltonode)Added [SKNode.moveToParent(_: SKNode)](https://developer.apple.com/documentation/spritekit/sknode/1483021-move)Added [SKNode.obstaclesFromNodeBounds(_: [SKNode]) -> [GKPolygonObstacle] [class]](https://developer.apple.com/documentation/spritekit/sknode/1483132-obstacles)Added [SKNode.obstaclesFromNodePhysicsBodies(_: [SKNode]) -> [GKPolygonObstacle] [class]](https://developer.apple.com/documentation/spritekit/sknode/1483085-obstacles)Added [SKNode.obstaclesFromSpriteTextures(_: [SKNode], accuracy: Float) -> [GKPolygonObstacle] [class]](https://developer.apple.com/documentation/spritekit/sknode/1483134-obstacles)Added [SKParticleRenderOrder [enum]](https://developer.apple.com/documentation/spritekit/skparticlerenderorder)Added [SKParticleRenderOrder.DontCare](https://developer.apple.com/documentation/spritekit/skparticlerenderorder/skparticlerenderorderdontcare)Added [SKParticleRenderOrder.OldestFirst](https://developer.apple.com/documentation/spritekit/skparticlerenderorder/oldestfirst)Added [SKParticleRenderOrder.OldestLast](https://developer.apple.com/documentation/spritekit/skparticlerenderorder/oldestlast)Added [SKPhysicsWorld.sampleFieldsAt(_: vector_float3) -> vector_float3](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449627-samplefieldsat)Added [SKReferenceNode](https://developer.apple.com/documentation/spritekit/skreferencenode)Added [SKReferenceNode.didLoadReferenceNode(_: SKNode?)](https://developer.apple.com/documentation/spritekit/skreferencenode/1508364-didload)Added [SKReferenceNode.init(coder: NSCoder)](https://developer.apple.com/documentation/spritekit/skreferencenode/1508363-initwithcoder)Added [SKReferenceNode.init(fileNamed: String)](https://developer.apple.com/documentation/spritekit/skreferencenode/1508368-referencenodewithfilenamed)Added [SKReferenceNode.init(fileNamed: String?)](https://developer.apple.com/documentation/spritekit/skreferencenode/1508369-initwithfilenamed)Added [SKReferenceNode.init(URL: NSURL?)](https://developer.apple.com/documentation/spritekit/skreferencenode/1508366-init)Added [SKReferenceNode.init(URL: NSURL)](https://developer.apple.com/documentation/spritekit/skreferencenode/1508365-init)Added [SKReferenceNode.resolveReferenceNode()](https://developer.apple.com/documentation/spritekit/skreferencenode/1508371-resolvereferencenode)Added [SKScene.audioEngine](https://developer.apple.com/documentation/spritekit/skscene/1519644-audioengine)Added [SKScene.camera](https://developer.apple.com/documentation/spritekit/skscene/1519696-camera)Added [SKScene.listener](https://developer.apple.com/documentation/spritekit/skscene/1520363-listener)Added SKTexture.CGImageAdded [SKTextureAtlas.preloadTextureAtlasesNamed(_: [String], withCompletionHandler: (NSError?, [SKTextureAtlas]) -> Void) [class]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427377-preloadtextureatlasesnamed)Added [SKUniform.init(name: String, texture: SKTexture)](https://developer.apple.com/documentation/spritekit/skuniform/1455470-uniformwithname)Added [SKVideoNode.init(fileNamed: String)](https://developer.apple.com/documentation/spritekit/skvideonode/1407922-initwithfilenamed)Added [SKVideoNode.init(URL: NSURL)](https://developer.apple.com/documentation/spritekit/skvideonode/1407898-initwithurl)Added SK_VERSIONAdded [SKFieldForceEvaluator](https://developer.apple.com/documentation/spritekit/skfieldforceevaluator)Modified [NSEvent.locationInNode(_: SKNode) -> CGPoint](https://developer.apple.com/documentation/appkit/nsevent/1483105-location)

|  | Declaration |
| --- | --- |
| From | ``` func locationInNode(_ node: SKNode!) -> CGPoint ``` |
| To | ``` func locationInNode(_ node: SKNode) -> CGPoint ``` |

Modified [SK3DNode](https://developer.apple.com/documentation/spritekit/sk3dnode)

|  | Declaration |
| --- | --- |
| From | ``` class SK3DNode : SKNode {     init(viewportSize viewportSize: CGSize)     init?(coder aDecoder: NSCoder)     class func nodeWithViewportSize(_ viewportSize: CGSize) -> Self     var viewportSize: CGSize     var scnScene: SCNScene!     var sceneTime: NSTimeInterval     func hitTest(_ thePoint: CGPoint, options options: [NSObject : AnyObject]!) -> [AnyObject]!     var playing: Bool     var loops: Bool     var pointOfView: SCNNode!     var autoenablesDefaultLighting: Bool } ``` |
| To | ``` class SK3DNode : SKNode {     init(viewportSize viewportSize: CGSize)     init?(coder aDecoder: NSCoder)     class func nodeWithViewportSize(_ viewportSize: CGSize) -> Self     var viewportSize: CGSize     var scnScene: SCNScene?     var sceneTime: NSTimeInterval     func hitTest(_ point: CGPoint, options options: [String : AnyObject]?) -> [SCNHitTestResult]     func projectPoint(_ point: vector_float3) -> vector_float3     func unprojectPoint(_ point: vector_float3) -> vector_float3     var playing: Bool     var loops: Bool     var pointOfView: SCNNode?     var autoenablesDefaultLighting: Bool } ``` |

Modified [SK3DNode.hitTest(_: CGPoint, options: [String : AnyObject]?) -> [SCNHitTestResult]](https://developer.apple.com/documentation/spritekit/sk3dnode/1519782-hittest)

|  | Declaration |
| --- | --- |
| From | ``` func hitTest(_ thePoint: CGPoint, options options: [NSObject : AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func hitTest(_ point: CGPoint, options options: [String : AnyObject]?) -> [SCNHitTestResult] ``` |

Modified [SK3DNode.pointOfView](https://developer.apple.com/documentation/spritekit/sk3dnode/1519786-pointofview)

|  | Declaration |
| --- | --- |
| From | ``` var pointOfView: SCNNode! ``` |
| To | ``` var pointOfView: SCNNode? ``` |

Modified [SK3DNode.scnScene](https://developer.apple.com/documentation/spritekit/sk3dnode/1519834-scnscene)

|  | Declaration |
| --- | --- |
| From | ``` var scnScene: SCNScene! ``` |
| To | ``` var scnScene: SCNScene? ``` |

Modified [SKAction](https://developer.apple.com/documentation/spritekit/skaction)

|  | Declaration |
| --- | --- |
| From | ``` class SKAction : NSObject, NSCopying, NSCoding {     var duration: NSTimeInterval     var timingMode: SKActionTimingMode     var timingFunction: SKActionTimingFunction?     var speed: CGFloat     func reversedAction() -> SKAction } extension SKAction {     class func moveBy(_ delta: CGVector, duration sec: NSTimeInterval) -> SKAction     class func moveByX(_ deltaX: CGFloat, y deltaY: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func moveTo(_ location: CGPoint, duration sec: NSTimeInterval) -> SKAction     class func moveToX(_ x: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func moveToY(_ y: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func rotateByAngle(_ radians: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func rotateToAngle(_ radians: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func rotateToAngle(_ radians: CGFloat, duration sec: NSTimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SKAction     class func resizeByWidth(_ width: CGFloat, height height: CGFloat, duration duration: NSTimeInterval) -> SKAction     class func resizeToWidth(_ width: CGFloat, height height: CGFloat, duration duration: NSTimeInterval) -> SKAction     class func resizeToWidth(_ width: CGFloat, duration duration: NSTimeInterval) -> SKAction     class func resizeToHeight(_ height: CGFloat, duration duration: NSTimeInterval) -> SKAction     class func scaleBy(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleXBy(_ xScale: CGFloat, y yScale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleXTo(_ xScale: CGFloat, y yScale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleXTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleYTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func sequence(_ actions: [AnyObject]) -> SKAction!     class func group(_ actions: [AnyObject]) -> SKAction!     class func repeatAction(_ action: SKAction, count count: Int) -> SKAction     class func repeatActionForever(_ action: SKAction) -> SKAction     class func fadeInWithDuration(_ sec: NSTimeInterval) -> SKAction     class func fadeOutWithDuration(_ sec: NSTimeInterval) -> SKAction     class func fadeAlphaBy(_ factor: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func fadeAlphaTo(_ alpha: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func hide() -> SKAction     class func unhide() -> SKAction     class func setTexture(_ texture: SKTexture) -> SKAction     class func setTexture(_ texture: SKTexture, resize resize: Bool) -> SKAction     class func animateWithTextures(_ textures: [AnyObject], timePerFrame sec: NSTimeInterval) -> SKAction     class func animateWithTextures(_ textures: [AnyObject], timePerFrame sec: NSTimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction     class func playSoundFileNamed(_ soundFile: String, waitForCompletion wait: Bool) -> SKAction     class func colorizeWithColor(_ color: NSColor, colorBlendFactor colorBlendFactor: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func colorizeWithColorBlendFactor(_ colorBlendFactor: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func falloffTo(_ falloff: Float, duration sec: NSTimeInterval) -> SKAction     class func falloffBy(_ falloff: Float, duration sec: NSTimeInterval) -> SKAction     class func followPath(_ path: CGPath, duration sec: NSTimeInterval) -> SKAction     class func followPath(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, duration sec: NSTimeInterval) -> SKAction     class func followPath(_ path: CGPath, speed speed: CGFloat) -> SKAction     class func followPath(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, speed speed: CGFloat) -> SKAction     class func speedBy(_ speed: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func speedTo(_ speed: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func reachTo(_ position: CGPoint, rootNode root: SKNode, duration sec: NSTimeInterval) -> SKAction     class func reachTo(_ position: CGPoint, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction     class func reachToNode(_ node: SKNode, rootNode root: SKNode, duration sec: NSTimeInterval) -> SKAction     class func reachToNode(_ node: SKNode, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction     class func strengthTo(_ strength: Float, duration sec: NSTimeInterval) -> SKAction     class func strengthBy(_ strength: Float, duration sec: NSTimeInterval) -> SKAction     class func waitForDuration(_ sec: NSTimeInterval) -> SKAction     class func waitForDuration(_ sec: NSTimeInterval, withRange durationRange: NSTimeInterval) -> SKAction     class func removeFromParent() -> SKAction     class func performSelector(_ selector: Selector, onTarget target: AnyObject!) -> SKAction!     class func runBlock(_ block: dispatch_block_t) -> SKAction     class func runBlock(_ block: dispatch_block_t, queue queue: dispatch_queue_t?) -> SKAction     class func runAction(_ action: SKAction, onChildWithName name: String) -> SKAction     class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SKNode!, CGFloat) -> Void) -> SKAction } ``` |
| To | ``` class SKAction : NSObject, NSCopying, NSCoding {     var duration: NSTimeInterval     var timingMode: SKActionTimingMode     var timingFunction: SKActionTimingFunction     var speed: CGFloat     func reversedAction() -> SKAction } extension SKAction {     class func moveBy(_ delta: CGVector, duration sec: NSTimeInterval) -> SKAction     class func moveByX(_ deltaX: CGFloat, y deltaY: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func moveTo(_ location: CGPoint, duration sec: NSTimeInterval) -> SKAction     class func moveToX(_ x: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func moveToY(_ y: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func rotateByAngle(_ radians: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func rotateToAngle(_ radians: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func rotateToAngle(_ radians: CGFloat, duration sec: NSTimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SKAction     class func resizeByWidth(_ width: CGFloat, height height: CGFloat, duration duration: NSTimeInterval) -> SKAction     class func resizeToWidth(_ width: CGFloat, height height: CGFloat, duration duration: NSTimeInterval) -> SKAction     class func resizeToWidth(_ width: CGFloat, duration duration: NSTimeInterval) -> SKAction     class func resizeToHeight(_ height: CGFloat, duration duration: NSTimeInterval) -> SKAction     class func scaleBy(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleXBy(_ xScale: CGFloat, y yScale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleXTo(_ xScale: CGFloat, y yScale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleXTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleYTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func sequence(_ actions: [SKAction]) -> SKAction     class func group(_ actions: [SKAction]) -> SKAction     class func repeatAction(_ action: SKAction, count count: Int) -> SKAction     class func repeatActionForever(_ action: SKAction) -> SKAction     class func fadeInWithDuration(_ sec: NSTimeInterval) -> SKAction     class func fadeOutWithDuration(_ sec: NSTimeInterval) -> SKAction     class func fadeAlphaBy(_ factor: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func fadeAlphaTo(_ alpha: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func hide() -> SKAction     class func unhide() -> SKAction     class func setTexture(_ texture: SKTexture) -> SKAction     class func setNormalTexture(_ texture: SKTexture) -> SKAction     class func setTexture(_ texture: SKTexture, resize resize: Bool) -> SKAction     class func setNormalTexture(_ texture: SKTexture, resize resize: Bool) -> SKAction     class func animateWithTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval) -> SKAction     class func animateWithNormalTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval) -> SKAction     class func animateWithTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction     class func animateWithNormalTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction     class func playSoundFileNamed(_ soundFile: String, waitForCompletion wait: Bool) -> SKAction     class func colorizeWithColor(_ color: NSColor, colorBlendFactor colorBlendFactor: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func colorizeWithColorBlendFactor(_ colorBlendFactor: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func falloffTo(_ falloff: Float, duration sec: NSTimeInterval) -> SKAction     class func falloffBy(_ falloff: Float, duration sec: NSTimeInterval) -> SKAction     class func followPath(_ path: CGPath, duration sec: NSTimeInterval) -> SKAction     class func followPath(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, duration sec: NSTimeInterval) -> SKAction     class func followPath(_ path: CGPath, speed speed: CGFloat) -> SKAction     class func followPath(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, speed speed: CGFloat) -> SKAction     class func speedBy(_ speed: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func speedTo(_ speed: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func reachTo(_ position: CGPoint, rootNode root: SKNode, duration sec: NSTimeInterval) -> SKAction     class func reachTo(_ position: CGPoint, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction     class func reachToNode(_ node: SKNode, rootNode root: SKNode, duration sec: NSTimeInterval) -> SKAction     class func reachToNode(_ node: SKNode, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction     class func strengthTo(_ strength: Float, duration sec: NSTimeInterval) -> SKAction     class func strengthBy(_ strength: Float, duration sec: NSTimeInterval) -> SKAction     class func waitForDuration(_ sec: NSTimeInterval) -> SKAction     class func waitForDuration(_ sec: NSTimeInterval, withRange durationRange: NSTimeInterval) -> SKAction     class func removeFromParent() -> SKAction     class func performSelector(_ selector: Selector, onTarget target: AnyObject) -> SKAction     class func runBlock(_ block: dispatch_block_t) -> SKAction     class func runBlock(_ block: dispatch_block_t, queue queue: dispatch_queue_t) -> SKAction     class func runAction(_ action: SKAction, onChildWithName name: String) -> SKAction     class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SKNode, CGFloat) -> Void) -> SKAction      init?(named name: String)     class func actionNamed(_ name: String) -> SKAction?      init?(named name: String, duration sec: NSTimeInterval)     class func actionNamed(_ name: String, duration sec: NSTimeInterval) -> SKAction?      init?(named name: String, fromURL url: NSURL)     class func actionNamed(_ name: String, fromURL url: NSURL) -> SKAction?      init?(named name: String, fromURL url: NSURL, duration sec: NSTimeInterval)     class func actionNamed(_ name: String, fromURL url: NSURL, duration sec: NSTimeInterval) -> SKAction? } extension SKAction {     class func changeChargeTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeChargeBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeMassTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeMassBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func applyForce(_ force: CGVector, duration sec: NSTimeInterval) -> SKAction     class func applyForce(_ force: CGVector, atPoint point: CGPoint, duration sec: NSTimeInterval) -> SKAction     class func applyTorque(_ torque: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func applyImpulse(_ impulse: CGVector, duration sec: NSTimeInterval) -> SKAction     class func applyImpulse(_ impulse: CGVector, atPoint point: CGPoint, duration sec: NSTimeInterval) -> SKAction     class func applyAngularImpulse(_ impulse: CGFloat, duration sec: NSTimeInterval) -> SKAction } extension SKAction {     class func play() -> SKAction     class func pause() -> SKAction     class func stop() -> SKAction     class func changePlaybackRateTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changePlaybackRateBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction } extension SKAction {     class func changeVolumeTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeVolumeBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction } extension SKAction {     class func stereoPanTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func stereoPanBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeReverbTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeReverbBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeObstructionTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeObstructionBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeOcclusionTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeOcclusionBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction } ``` |

Modified [SKAction.animateWithTextures(_: [SKTexture], timePerFrame: NSTimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417828-animate)

|  | Declaration |
| --- | --- |
| From | ``` class func animateWithTextures(_ textures: [AnyObject], timePerFrame sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func animateWithTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval) -> SKAction ``` |

Modified [SKAction.animateWithTextures(_: [SKTexture], timePerFrame: NSTimeInterval, resize: Bool, restore: Bool) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417656-animatewithtextures)

|  | Declaration |
| --- | --- |
| From | ``` class func animateWithTextures(_ textures: [AnyObject], timePerFrame sec: NSTimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction ``` |
| To | ``` class func animateWithTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction ``` |

Modified [SKAction.customActionWithDuration(_: NSTimeInterval, actionBlock: (SKNode, CGFloat) -> Void) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417745-customactionwithduration)

|  | Declaration |
| --- | --- |
| From | ``` class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SKNode!, CGFloat) -> Void) -> SKAction ``` |
| To | ``` class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SKNode, CGFloat) -> Void) -> SKAction ``` |

Modified [SKAction.group(_: [SKAction]) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417688-group)

|  | Declaration |
| --- | --- |
| From | ``` class func group(_ actions: [AnyObject]) -> SKAction! ``` |
| To | ``` class func group(_ actions: [SKAction]) -> SKAction ``` |

Modified [SKAction.runBlock(_: dispatch_block_t, queue: dispatch_queue_t) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417799-runblock)

|  | Declaration |
| --- | --- |
| From | ``` class func runBlock(_ block: dispatch_block_t, queue queue: dispatch_queue_t?) -> SKAction ``` |
| To | ``` class func runBlock(_ block: dispatch_block_t, queue queue: dispatch_queue_t) -> SKAction ``` |

Modified [SKAction.sequence(_: [SKAction]) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417817-sequence)

|  | Declaration |
| --- | --- |
| From | ``` class func sequence(_ actions: [AnyObject]) -> SKAction! ``` |
| To | ``` class func sequence(_ actions: [SKAction]) -> SKAction ``` |

Modified [SKAction.timingFunction](https://developer.apple.com/documentation/spritekit/skaction/1417666-timingfunction)

|  | Declaration |
| --- | --- |
| From | ``` var timingFunction: SKActionTimingFunction? ``` |
| To | ``` var timingFunction: SKActionTimingFunction ``` |

Modified [SKActionTimingMode [enum]](https://developer.apple.com/documentation/spritekit/skactiontimingmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SKBlendMode [enum]](https://developer.apple.com/documentation/spritekit/skblendmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SKConstraint](https://developer.apple.com/documentation/spritekit/skconstraint)

|  | Declaration |
| --- | --- |
| From | ``` class SKConstraint : NSObject, NSCoding, NSCopying {     var enabled: Bool     var referenceNode: SKNode?     class func positionX(_ range: SKRange) -> Self     class func positionY(_ range: SKRange) -> Self     class func positionX(_ xRange: SKRange, y yRange: SKRange) -> Self     class func distance(_ range: SKRange!, toNode node: SKNode!) -> Self     class func distance(_ range: SKRange, toPoint point: CGPoint) -> Self     class func distance(_ range: SKRange, toPoint point: CGPoint, inNode node: SKNode) -> Self     class func zRotation(_ zRange: SKRange) -> Self     class func orientToNode(_ node: SKNode, offset radians: SKRange) -> Self     class func orientToPoint(_ point: CGPoint, offset radians: SKRange) -> Self     class func orientToPoint(_ point: CGPoint, inNode node: SKNode, offset radians: SKRange) -> Self } ``` |
| To | ``` class SKConstraint : NSObject, NSCoding, NSCopying {     var enabled: Bool     var referenceNode: SKNode?     class func positionX(_ range: SKRange) -> Self     class func positionY(_ range: SKRange) -> Self     class func positionX(_ xRange: SKRange, y yRange: SKRange) -> Self     class func distance(_ range: SKRange, toNode node: SKNode) -> Self     class func distance(_ range: SKRange, toPoint point: CGPoint) -> Self     class func distance(_ range: SKRange, toPoint point: CGPoint, inNode node: SKNode) -> Self     class func zRotation(_ zRange: SKRange) -> Self     class func orientToNode(_ node: SKNode, offset radians: SKRange) -> Self     class func orientToPoint(_ point: CGPoint, offset radians: SKRange) -> Self     class func orientToPoint(_ point: CGPoint, inNode node: SKNode, offset radians: SKRange) -> Self } ``` |

Modified [SKConstraint.distance(_: SKRange, toNode: SKNode) -> Self [class]](https://developer.apple.com/documentation/spritekit/skconstraint/1519750-distance)

|  | Declaration |
| --- | --- |
| From | ``` class func distance(_ range: SKRange!, toNode node: SKNode!) -> Self ``` |
| To | ``` class func distance(_ range: SKRange, toNode node: SKNode) -> Self ``` |

Modified [SKEmitterNode](https://developer.apple.com/documentation/spritekit/skemitternode)

|  | Declaration |
| --- | --- |
| From | ``` class SKEmitterNode : SKNode {     func advanceSimulationTime(_ sec: NSTimeInterval)     func resetSimulation()     var particleTexture: SKTexture?     var particleZPosition: CGFloat     var particleZPositionRange: CGFloat     var particleZPositionSpeed: CGFloat     var particleBlendMode: SKBlendMode     var particleColor: NSColor!     var particleColorRedRange: CGFloat     var particleColorGreenRange: CGFloat     var particleColorBlueRange: CGFloat     var particleColorAlphaRange: CGFloat     var particleColorRedSpeed: CGFloat     var particleColorGreenSpeed: CGFloat     var particleColorBlueSpeed: CGFloat     var particleColorAlphaSpeed: CGFloat     var particleColorSequence: SKKeyframeSequence?     var particleColorBlendFactor: CGFloat     var particleColorBlendFactorRange: CGFloat     var particleColorBlendFactorSpeed: CGFloat     var particleColorBlendFactorSequence: SKKeyframeSequence?     var particlePosition: CGPoint     var particlePositionRange: CGVector     var particleSpeed: CGFloat     var particleSpeedRange: CGFloat     var emissionAngle: CGFloat     var emissionAngleRange: CGFloat     var xAcceleration: CGFloat     var yAcceleration: CGFloat     var particleBirthRate: CGFloat     var numParticlesToEmit: Int     var particleLifetime: CGFloat     var particleLifetimeRange: CGFloat     var particleRotation: CGFloat     var particleRotationRange: CGFloat     var particleRotationSpeed: CGFloat     var particleSize: CGSize     var particleScale: CGFloat     var particleScaleRange: CGFloat     var particleScaleSpeed: CGFloat     var particleScaleSequence: SKKeyframeSequence?     var particleAlpha: CGFloat     var particleAlphaRange: CGFloat     var particleAlphaSpeed: CGFloat     var particleAlphaSequence: SKKeyframeSequence?     @NSCopying var particleAction: SKAction?     var fieldBitMask: UInt32     weak var targetNode: SKNode?     var shader: SKShader? } ``` |
| To | ``` class SKEmitterNode : SKNode {     func advanceSimulationTime(_ sec: NSTimeInterval)     func resetSimulation()     var particleTexture: SKTexture?     var particleBlendMode: SKBlendMode     var particleColor: NSColor     var particleColorRedRange: CGFloat     var particleColorGreenRange: CGFloat     var particleColorBlueRange: CGFloat     var particleColorAlphaRange: CGFloat     var particleColorRedSpeed: CGFloat     var particleColorGreenSpeed: CGFloat     var particleColorBlueSpeed: CGFloat     var particleColorAlphaSpeed: CGFloat     var particleColorSequence: SKKeyframeSequence?     var particleColorBlendFactor: CGFloat     var particleColorBlendFactorRange: CGFloat     var particleColorBlendFactorSpeed: CGFloat     var particleColorBlendFactorSequence: SKKeyframeSequence?     var particlePosition: CGPoint     var particlePositionRange: CGVector     var particleSpeed: CGFloat     var particleSpeedRange: CGFloat     var emissionAngle: CGFloat     var emissionAngleRange: CGFloat     var xAcceleration: CGFloat     var yAcceleration: CGFloat     var particleBirthRate: CGFloat     var numParticlesToEmit: Int     var particleLifetime: CGFloat     var particleLifetimeRange: CGFloat     var particleRotation: CGFloat     var particleRotationRange: CGFloat     var particleRotationSpeed: CGFloat     var particleSize: CGSize     var particleScale: CGFloat     var particleScaleRange: CGFloat     var particleScaleSpeed: CGFloat     var particleScaleSequence: SKKeyframeSequence?     var particleAlpha: CGFloat     var particleAlphaRange: CGFloat     var particleAlphaSpeed: CGFloat     var particleAlphaSequence: SKKeyframeSequence?     @NSCopying var particleAction: SKAction?     var fieldBitMask: UInt32     weak var targetNode: SKNode?     var shader: SKShader?     var particleZPosition: CGFloat     var particleRenderOrder: SKParticleRenderOrder     var particleZPositionRange: CGFloat     var particleZPositionSpeed: CGFloat } ``` |

Modified [SKEmitterNode.particleColor](https://developer.apple.com/documentation/spritekit/skemitternode/1398049-particlecolor)

|  | Declaration |
| --- | --- |
| From | ``` var particleColor: NSColor! ``` |
| To | ``` var particleColor: NSColor ``` |

Modified [SKEmitterNode.particleZPositionRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397974-particlezpositionrange)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [SKEmitterNode.particleZPositionSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398008-particlezpositionspeed)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [SKFieldNode](https://developer.apple.com/documentation/spritekit/skfieldnode)

|  | Declaration |
| --- | --- |
| From | ``` class SKFieldNode : SKNode {     var region: SKRegion!     var strength: Float     var falloff: Float     var minimumRadius: Float     var enabled: Bool     var exclusive: Bool     var categoryBitMask: UInt32     var smoothness: Float     var animationSpeed: Float     var texture: SKTexture!     class func dragField() -> SKFieldNode     class func vortexField() -> SKFieldNode     class func radialGravityField() -> SKFieldNode     class func velocityFieldWithTexture(_ velocityTexture: SKTexture) -> SKFieldNode     class func noiseFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode     class func turbulenceFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode     class func springField() -> SKFieldNode     class func electricField() -> SKFieldNode     class func magneticField() -> SKFieldNode } ``` |
| To | ``` class SKFieldNode : SKNode {     var region: SKRegion?     var strength: Float     var falloff: Float     var minimumRadius: Float     var enabled: Bool     var exclusive: Bool     var categoryBitMask: UInt32     var direction: vector_float3     var smoothness: Float     var animationSpeed: Float     var texture: SKTexture?     class func dragField() -> SKFieldNode     class func vortexField() -> SKFieldNode     class func radialGravityField() -> SKFieldNode     class func linearGravityFieldWithVector(_ direction: vector_float3) -> SKFieldNode     class func velocityFieldWithVector(_ direction: vector_float3) -> SKFieldNode     class func velocityFieldWithTexture(_ velocityTexture: SKTexture) -> SKFieldNode     class func noiseFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode     class func turbulenceFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode     class func springField() -> SKFieldNode     class func electricField() -> SKFieldNode     class func magneticField() -> SKFieldNode     class func customFieldWithEvaluationBlock(_ block: SKFieldForceEvaluator) -> SKFieldNode } ``` |

Modified [SKFieldNode.region](https://developer.apple.com/documentation/spritekit/skfieldnode/1519551-region)

|  | Declaration |
| --- | --- |
| From | ``` var region: SKRegion! ``` |
| To | ``` var region: SKRegion? ``` |

Modified [SKFieldNode.texture](https://developer.apple.com/documentation/spritekit/skfieldnode/1519928-texture)

|  | Declaration |
| --- | --- |
| From | ``` var texture: SKTexture! ``` |
| To | ``` var texture: SKTexture? ``` |

Modified [SKInterpolationMode [enum]](https://developer.apple.com/documentation/spritekit/skinterpolationmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SKKeyframeSequence](https://developer.apple.com/documentation/spritekit/skkeyframesequence)

|  | Declaration |
| --- | --- |
| From | ``` class SKKeyframeSequence : NSObject, NSCoding, NSCopying {     init!(keyframeValues values: [AnyObject], times times: [AnyObject])     convenience init(capacity numItems: Int)     init?(coder aDecoder: NSCoder)     func count() -> Int     func addKeyframeValue(_ value: AnyObject, time time: CGFloat)     func removeLastKeyframe()     func removeKeyframeAtIndex(_ index: Int)     func setKeyframeValue(_ value: AnyObject, forIndex index: Int)     func setKeyframeTime(_ time: CGFloat, forIndex index: Int)     func setKeyframeValue(_ value: AnyObject, time time: CGFloat, forIndex index: Int)     func getKeyframeValueForIndex(_ index: Int) -> AnyObject     func getKeyframeTimeForIndex(_ index: Int) -> CGFloat     func sampleAtTime(_ time: CGFloat) -> AnyObject!     var interpolationMode: SKInterpolationMode     var repeatMode: SKRepeatMode } ``` |
| To | ``` class SKKeyframeSequence : NSObject, NSCoding, NSCopying {     init(keyframeValues values: [AnyObject], times times: [NSNumber])     convenience init(capacity numItems: Int)     init?(coder aDecoder: NSCoder)     func count() -> Int     func addKeyframeValue(_ value: AnyObject, time time: CGFloat)     func removeLastKeyframe()     func removeKeyframeAtIndex(_ index: Int)     func setKeyframeValue(_ value: AnyObject, forIndex index: Int)     func setKeyframeTime(_ time: CGFloat, forIndex index: Int)     func setKeyframeValue(_ value: AnyObject, time time: CGFloat, forIndex index: Int)     func getKeyframeValueForIndex(_ index: Int) -> AnyObject     func getKeyframeTimeForIndex(_ index: Int) -> CGFloat     func sampleAtTime(_ time: CGFloat) -> AnyObject?     var interpolationMode: SKInterpolationMode     var repeatMode: SKRepeatMode } ``` |

Modified [SKKeyframeSequence.init(keyframeValues: [AnyObject], times: [NSNumber])](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390896-initwithkeyframevalues)

|  | Declaration |
| --- | --- |
| From | ``` init!(keyframeValues values: [AnyObject], times times: [AnyObject]) ``` |
| To | ``` init(keyframeValues values: [AnyObject], times times: [NSNumber]) ``` |

Modified [SKKeyframeSequence.sampleAtTime(_: CGFloat) -> AnyObject?](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390904-sample)

|  | Declaration |
| --- | --- |
| From | ``` func sampleAtTime(_ time: CGFloat) -> AnyObject! ``` |
| To | ``` func sampleAtTime(_ time: CGFloat) -> AnyObject? ``` |

Modified [SKLabelHorizontalAlignmentMode [enum]](https://developer.apple.com/documentation/spritekit/sklabelhorizontalalignmentmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SKLabelNode](https://developer.apple.com/documentation/spritekit/sklabelnode)

|  | Declaration |
| --- | --- |
| From | ``` class SKLabelNode : SKNode {     convenience init(text text: String)     class func labelNodeWithText(_ text: String) -> Self     convenience init!(fontNamed fontName: String!)     class func labelNodeWithFontNamed(_ fontName: String!) -> Self!     init(fontNamed fontName: String!)     var verticalAlignmentMode: SKLabelVerticalAlignmentMode     var horizontalAlignmentMode: SKLabelHorizontalAlignmentMode     var fontName: String!     var text: String     var fontSize: CGFloat     var fontColor: NSColor     var colorBlendFactor: CGFloat     var color: NSColor?     var blendMode: SKBlendMode } ``` |
| To | ``` class SKLabelNode : SKNode {     convenience init(text text: String?)     class func labelNodeWithText(_ text: String?) -> Self     convenience init(fontNamed fontName: String?)     class func labelNodeWithFontNamed(_ fontName: String?) -> Self     init(fontNamed fontName: String?)     var verticalAlignmentMode: SKLabelVerticalAlignmentMode     var horizontalAlignmentMode: SKLabelHorizontalAlignmentMode     var fontName: String?     var text: String?     var fontSize: CGFloat     var fontColor: NSColor?     var colorBlendFactor: CGFloat     var color: NSColor?     var blendMode: SKBlendMode } ``` |

Modified [SKLabelNode.fontColor](https://developer.apple.com/documentation/spritekit/sklabelnode/1520057-fontcolor)

|  | Declaration |
| --- | --- |
| From | ``` var fontColor: NSColor ``` |
| To | ``` var fontColor: NSColor? ``` |

Modified [SKLabelNode.fontName](https://developer.apple.com/documentation/spritekit/sklabelnode/1520129-fontname)

|  | Declaration |
| --- | --- |
| From | ``` var fontName: String! ``` |
| To | ``` var fontName: String? ``` |

Modified [SKLabelNode.init(fontNamed: String?)](https://developer.apple.com/documentation/spritekit/sklabelnode/1519917-initwithfontnamed)

|  | Declaration |
| --- | --- |
| From | ``` init(fontNamed fontName: String!) ``` |
| To | ``` init(fontNamed fontName: String?) ``` |

Modified [SKLabelNode.init(text: String?)](https://developer.apple.com/documentation/spritekit/sklabelnode/1519612-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(text text: String) ``` |
| To | ``` convenience init(text text: String?) ``` |

Modified [SKLabelNode.text](https://developer.apple.com/documentation/spritekit/sklabelnode/1519788-text)

|  | Declaration |
| --- | --- |
| From | ``` var text: String ``` |
| To | ``` var text: String? ``` |

Modified [SKLabelVerticalAlignmentMode [enum]](https://developer.apple.com/documentation/spritekit/sklabelverticalalignmentmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SKLightNode](https://developer.apple.com/documentation/spritekit/sklightnode)

|  | Declaration |
| --- | --- |
| From | ``` class SKLightNode : SKNode {     var enabled: Bool     var lightColor: NSColor     var ambientColor: NSColor!     var shadowColor: NSColor!     var falloff: CGFloat     var categoryBitMask: UInt32 } ``` |
| To | ``` class SKLightNode : SKNode {     var enabled: Bool     var lightColor: NSColor     var ambientColor: NSColor     var shadowColor: NSColor     var falloff: CGFloat     var categoryBitMask: UInt32 } ``` |

Modified [SKLightNode.ambientColor](https://developer.apple.com/documentation/spritekit/sklightnode/1520139-ambientcolor)

|  | Declaration |
| --- | --- |
| From | ``` var ambientColor: NSColor! ``` |
| To | ``` var ambientColor: NSColor ``` |

Modified [SKLightNode.shadowColor](https://developer.apple.com/documentation/spritekit/sklightnode/1519844-shadowcolor)

|  | Declaration |
| --- | --- |
| From | ``` var shadowColor: NSColor! ``` |
| To | ``` var shadowColor: NSColor ``` |

Modified [SKNode](https://developer.apple.com/documentation/spritekit/sknode)

|  | Declaration |
| --- | --- |
| From | ``` class SKNode : NSResponder, NSCopying, NSCoding {     init()     init?(coder aDecoder: NSCoder)     class func node() -> Self     convenience init!(fileNamed filename: String)     class func nodeWithFileNamed(_ filename: String) -> Self!     var frame: CGRect { get }     func calculateAccumulatedFrame() -> CGRect     var position: CGPoint     var zPosition: CGFloat     var zRotation: CGFloat     var xScale: CGFloat     var yScale: CGFloat     var speed: CGFloat     var alpha: CGFloat     var paused: Bool     var hidden: Bool     var userInteractionEnabled: Bool     var parent: SKNode? { get }     var children: [AnyObject] { get }     var name: String?     var scene: SKScene? { get }     var physicsBody: SKPhysicsBody?     var userData: NSMutableDictionary?     @NSCopying var reachConstraints: SKReachConstraints?     var constraints: [AnyObject]?     func setScale(_ scale: CGFloat)     func addChild(_ node: SKNode)     func insertChild(_ node: SKNode!, atIndex index: Int)     func removeChildrenInArray(_ nodes: [AnyObject]!)     func removeAllChildren()     func removeFromParent()     func childNodeWithName(_ name: String) -> SKNode?     func enumerateChildNodesWithName(_ name: String, usingBlock block: ((SKNode!, UnsafeMutablePointer<ObjCBool>) -> Void)!)     func objectForKeyedSubscript(_ name: String) -> [AnyObject]     func inParentHierarchy(_ parent: SKNode) -> Bool     func runAction(_ action: SKAction!)     func runAction(_ action: SKAction!, completion block: (() -> Void)!)     func runAction(_ action: SKAction, withKey key: String!)     func hasActions() -> Bool     func actionForKey(_ key: String) -> SKAction?     func removeActionForKey(_ key: String!)     func removeAllActions()     func containsPoint(_ p: CGPoint) -> Bool     func nodeAtPoint(_ p: CGPoint) -> SKNode     func nodesAtPoint(_ p: CGPoint) -> [AnyObject]     func convertPoint(_ point: CGPoint, fromNode node: SKNode) -> CGPoint     func convertPoint(_ point: CGPoint, toNode node: SKNode) -> CGPoint     func intersectsNode(_ node: SKNode) -> Bool } extension SKNode {     subscript (name: String) -> [SKNode] { get } } extension SKNode {     subscript (name: String) -> [SKNode] { get } } ``` |
| To | ``` class SKNode : NSResponder, NSCopying {     init()     init?(coder aDecoder: NSCoder)     class func node() -> Self     convenience init?(fileNamed filename: String)     class func nodeWithFileNamed(_ filename: String) -> Self?     var frame: CGRect { get }     func calculateAccumulatedFrame() -> CGRect     var position: CGPoint     var zPosition: CGFloat     var zRotation: CGFloat     var xScale: CGFloat     var yScale: CGFloat     var speed: CGFloat     var alpha: CGFloat     var paused: Bool     var hidden: Bool     var userInteractionEnabled: Bool     var parent: SKNode? { get }     var children: [SKNode] { get }     var name: String?     var scene: SKScene? { get }     var physicsBody: SKPhysicsBody?     var userData: NSMutableDictionary?     @NSCopying var reachConstraints: SKReachConstraints?     var constraints: [SKConstraint]?     func setScale(_ scale: CGFloat)     func addChild(_ node: SKNode)     func insertChild(_ node: SKNode, atIndex index: Int)     func removeChildrenInArray(_ nodes: [SKNode])     func removeAllChildren()     func removeFromParent()     func moveToParent(_ parent: SKNode)     func childNodeWithName(_ name: String) -> SKNode?     func enumerateChildNodesWithName(_ name: String, usingBlock block: (SKNode, UnsafeMutablePointer<ObjCBool>) -> Void)     func objectForKeyedSubscript(_ name: String) -> [SKNode]     func inParentHierarchy(_ parent: SKNode) -> Bool     func runAction(_ action: SKAction)     func runAction(_ action: SKAction, completion block: () -> Void)     func runAction(_ action: SKAction, withKey key: String)     func hasActions() -> Bool     func actionForKey(_ key: String) -> SKAction?     func removeActionForKey(_ key: String)     func removeAllActions()     func containsPoint(_ p: CGPoint) -> Bool     func nodeAtPoint(_ p: CGPoint) -> SKNode     func nodesAtPoint(_ p: CGPoint) -> [SKNode]     func convertPoint(_ point: CGPoint, fromNode node: SKNode) -> CGPoint     func convertPoint(_ point: CGPoint, toNode node: SKNode) -> CGPoint     func intersectsNode(_ node: SKNode) -> Bool     func isEqualToNode(_ node: SKNode) -> Bool     class func obstaclesFromSpriteTextures(_ sprites: [SKNode], accuracy accuracy: Float) -> [GKPolygonObstacle]     class func obstaclesFromNodeBounds(_ nodes: [SKNode]) -> [GKPolygonObstacle]     class func obstaclesFromNodePhysicsBodies(_ nodes: [SKNode]) -> [GKPolygonObstacle] } extension SKNode {     subscript (_ name: String) -> [SKNode] { get } } extension SKNode {     subscript (_ name: String) -> [SKNode] { get } } ``` |

Modified [SKNode.children](https://developer.apple.com/documentation/spritekit/sknode/1483028-children)

|  | Declaration |
| --- | --- |
| From | ``` var children: [AnyObject] { get } ``` |
| To | ``` var children: [SKNode] { get } ``` |

Modified [SKNode.constraints](https://developer.apple.com/documentation/spritekit/sknode/1483124-constraints)

|  | Declaration |
| --- | --- |
| From | ``` var constraints: [AnyObject]? ``` |
| To | ``` var constraints: [SKConstraint]? ``` |

Modified [SKNode.enumerateChildNodesWithName(_: String, usingBlock: (SKNode, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/spritekit/sknode/1483024-enumeratechildnodeswithname)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateChildNodesWithName(_ name: String, usingBlock block: ((SKNode!, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateChildNodesWithName(_ name: String, usingBlock block: (SKNode, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [SKNode.init(fileNamed: String)](https://developer.apple.com/documentation/spritekit/sknode/1483083-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(fileNamed filename: String) ``` |
| To | ``` convenience init?(fileNamed filename: String) ``` |

Modified [SKNode.insertChild(_: SKNode, atIndex: Int)](https://developer.apple.com/documentation/spritekit/sknode/1483062-insertchild)

|  | Declaration |
| --- | --- |
| From | ``` func insertChild(_ node: SKNode!, atIndex index: Int) ``` |
| To | ``` func insertChild(_ node: SKNode, atIndex index: Int) ``` |

Modified [SKNode.nodesAtPoint(_: CGPoint) -> [SKNode]](https://developer.apple.com/documentation/spritekit/sknode/1483072-nodes)

|  | Declaration |
| --- | --- |
| From | ``` func nodesAtPoint(_ p: CGPoint) -> [AnyObject] ``` |
| To | ``` func nodesAtPoint(_ p: CGPoint) -> [SKNode] ``` |

Modified [SKNode.removeActionForKey(_: String)](https://developer.apple.com/documentation/spritekit/sknode/1483076-removeaction)

|  | Declaration |
| --- | --- |
| From | ``` func removeActionForKey(_ key: String!) ``` |
| To | ``` func removeActionForKey(_ key: String) ``` |

Modified [SKNode.removeChildrenInArray(_: [SKNode])](https://developer.apple.com/documentation/spritekit/sknode/1483091-removechildren)

|  | Declaration |
| --- | --- |
| From | ``` func removeChildrenInArray(_ nodes: [AnyObject]!) ``` |
| To | ``` func removeChildrenInArray(_ nodes: [SKNode]) ``` |

Modified [SKNode.runAction(_: SKAction)](https://developer.apple.com/documentation/spritekit/sknode/1483093-runaction)

|  | Declaration |
| --- | --- |
| From | ``` func runAction(_ action: SKAction!) ``` |
| To | ``` func runAction(_ action: SKAction) ``` |

Modified [SKNode.runAction(_: SKAction, completion: () -> Void)](https://developer.apple.com/documentation/spritekit/sknode/1483103-run)

|  | Declaration |
| --- | --- |
| From | ``` func runAction(_ action: SKAction!, completion block: (() -> Void)!) ``` |
| To | ``` func runAction(_ action: SKAction, completion block: () -> Void) ``` |

Modified [SKNode.runAction(_: SKAction, withKey: String)](https://developer.apple.com/documentation/spritekit/sknode/1483042-run)

|  | Declaration |
| --- | --- |
| From | ``` func runAction(_ action: SKAction, withKey key: String!) ``` |
| To | ``` func runAction(_ action: SKAction, withKey key: String) ``` |

Modified SKNode.subscript(_: String) -> [SKNode]

|  | Declaration |
| --- | --- |
| From | ``` subscript (name: String) -> [SKNode] { get } ``` |
| To | ``` subscript (_ name: String) -> [SKNode] { get } ``` |

Modified [SKPhysicsBody](https://developer.apple.com/documentation/spritekit/skphysicsbody)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsBody : NSObject, NSCopying, NSCoding {     init(circleOfRadius r: CGFloat) -> SKPhysicsBody     class func bodyWithCircleOfRadius(_ r: CGFloat) -> SKPhysicsBody     init(circleOfRadius r: CGFloat, center center: CGPoint) -> SKPhysicsBody     class func bodyWithCircleOfRadius(_ r: CGFloat, center center: CGPoint) -> SKPhysicsBody     init!(rectangleOfSize s: CGSize) -> SKPhysicsBody     class func bodyWithRectangleOfSize(_ s: CGSize) -> SKPhysicsBody!     init!(rectangleOfSize s: CGSize, center center: CGPoint) -> SKPhysicsBody     class func bodyWithRectangleOfSize(_ s: CGSize, center center: CGPoint) -> SKPhysicsBody!     init!(polygonFromPath path: CGPath!) -> SKPhysicsBody     class func bodyWithPolygonFromPath(_ path: CGPath!) -> SKPhysicsBody!     init(edgeFromPoint p1: CGPoint, toPoint p2: CGPoint) -> SKPhysicsBody     class func bodyWithEdgeFromPoint(_ p1: CGPoint, toPoint p2: CGPoint) -> SKPhysicsBody     init(edgeChainFromPath path: CGPath!) -> SKPhysicsBody     class func bodyWithEdgeChainFromPath(_ path: CGPath!) -> SKPhysicsBody     init(edgeLoopFromPath path: CGPath!) -> SKPhysicsBody     class func bodyWithEdgeLoopFromPath(_ path: CGPath!) -> SKPhysicsBody     init(edgeLoopFromRect rect: CGRect) -> SKPhysicsBody     class func bodyWithEdgeLoopFromRect(_ rect: CGRect) -> SKPhysicsBody     init!(texture texture: SKTexture!, size size: CGSize) -> SKPhysicsBody     class func bodyWithTexture(_ texture: SKTexture!, size size: CGSize) -> SKPhysicsBody!     init!(texture texture: SKTexture!, alphaThreshold alphaThreshold: Float, size size: CGSize) -> SKPhysicsBody     class func bodyWithTexture(_ texture: SKTexture!, alphaThreshold alphaThreshold: Float, size size: CGSize) -> SKPhysicsBody!     init(bodies bodies: [AnyObject]) -> SKPhysicsBody     class func bodyWithBodies(_ bodies: [AnyObject]) -> SKPhysicsBody     var dynamic: Bool     var usesPreciseCollisionDetection: Bool     var allowsRotation: Bool     var pinned: Bool     var resting: Bool     var friction: CGFloat     var charge: CGFloat     var restitution: CGFloat     var linearDamping: CGFloat     var angularDamping: CGFloat     var density: CGFloat     var mass: CGFloat     var area: CGFloat { get }     var affectedByGravity: Bool     var fieldBitMask: UInt32     var categoryBitMask: UInt32     var collisionBitMask: UInt32     var contactTestBitMask: UInt32     var joints: [AnyObject] { get }     weak var node: SKNode? { get }     var velocity: CGVector     var angularVelocity: CGFloat     func applyForce(_ force: CGVector)     func applyForce(_ force: CGVector, atPoint point: CGPoint)     func applyTorque(_ torque: CGFloat)     func applyImpulse(_ impulse: CGVector)     func applyImpulse(_ impulse: CGVector, atPoint point: CGPoint)     func applyAngularImpulse(_ impulse: CGFloat)     func allContactedBodies() -> [AnyObject] } ``` |
| To | ``` class SKPhysicsBody : NSObject, NSCopying, NSCoding {      init(circleOfRadius r: CGFloat)     class func bodyWithCircleOfRadius(_ r: CGFloat) -> SKPhysicsBody      init(circleOfRadius r: CGFloat, center center: CGPoint)     class func bodyWithCircleOfRadius(_ r: CGFloat, center center: CGPoint) -> SKPhysicsBody      init(rectangleOfSize s: CGSize)     class func bodyWithRectangleOfSize(_ s: CGSize) -> SKPhysicsBody      init(rectangleOfSize s: CGSize, center center: CGPoint)     class func bodyWithRectangleOfSize(_ s: CGSize, center center: CGPoint) -> SKPhysicsBody      init(polygonFromPath path: CGPath)     class func bodyWithPolygonFromPath(_ path: CGPath) -> SKPhysicsBody      init(edgeFromPoint p1: CGPoint, toPoint p2: CGPoint)     class func bodyWithEdgeFromPoint(_ p1: CGPoint, toPoint p2: CGPoint) -> SKPhysicsBody      init(edgeChainFromPath path: CGPath)     class func bodyWithEdgeChainFromPath(_ path: CGPath) -> SKPhysicsBody      init(edgeLoopFromPath path: CGPath)     class func bodyWithEdgeLoopFromPath(_ path: CGPath) -> SKPhysicsBody      init(edgeLoopFromRect rect: CGRect)     class func bodyWithEdgeLoopFromRect(_ rect: CGRect) -> SKPhysicsBody      init(texture texture: SKTexture, size size: CGSize)     class func bodyWithTexture(_ texture: SKTexture, size size: CGSize) -> SKPhysicsBody      init(texture texture: SKTexture, alphaThreshold alphaThreshold: Float, size size: CGSize)     class func bodyWithTexture(_ texture: SKTexture, alphaThreshold alphaThreshold: Float, size size: CGSize) -> SKPhysicsBody      init(bodies bodies: [SKPhysicsBody])     class func bodyWithBodies(_ bodies: [SKPhysicsBody]) -> SKPhysicsBody     var dynamic: Bool     var usesPreciseCollisionDetection: Bool     var allowsRotation: Bool     var pinned: Bool     var resting: Bool     var friction: CGFloat     var charge: CGFloat     var restitution: CGFloat     var linearDamping: CGFloat     var angularDamping: CGFloat     var density: CGFloat     var mass: CGFloat     var area: CGFloat { get }     var affectedByGravity: Bool     var fieldBitMask: UInt32     var categoryBitMask: UInt32     var collisionBitMask: UInt32     var contactTestBitMask: UInt32     var joints: [SKPhysicsJoint] { get }     weak var node: SKNode? { get }     var velocity: CGVector     var angularVelocity: CGFloat     func applyForce(_ force: CGVector)     func applyForce(_ force: CGVector, atPoint point: CGPoint)     func applyTorque(_ torque: CGFloat)     func applyImpulse(_ impulse: CGVector)     func applyImpulse(_ impulse: CGVector, atPoint point: CGPoint)     func applyAngularImpulse(_ impulse: CGFloat)     func allContactedBodies() -> [SKPhysicsBody] } ``` |

Modified [SKPhysicsBody.allContactedBodies() -> [SKPhysicsBody]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520397-allcontactedbodies)

|  | Declaration |
| --- | --- |
| From | ``` func allContactedBodies() -> [AnyObject] ``` |
| To | ``` func allContactedBodies() -> [SKPhysicsBody] ``` |

Modified [SKPhysicsBody.init(bodies: [SKPhysicsBody])](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519736-init)

|  | Declaration |
| --- | --- |
| From | ``` init(bodies bodies: [AnyObject]) -> SKPhysicsBody ``` |
| To | ``` init(bodies bodies: [SKPhysicsBody]) ``` |

Modified [SKPhysicsBody.init(circleOfRadius: CGFloat)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520261-bodywithcircleofradius)

|  | Declaration |
| --- | --- |
| From | ``` init(circleOfRadius r: CGFloat) -> SKPhysicsBody ``` |
| To | ``` init(circleOfRadius r: CGFloat) ``` |

Modified [SKPhysicsBody.init(circleOfRadius: CGFloat, center: CGPoint)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519692-bodywithcircleofradius)

|  | Declaration |
| --- | --- |
| From | ``` init(circleOfRadius r: CGFloat, center center: CGPoint) -> SKPhysicsBody ``` |
| To | ``` init(circleOfRadius r: CGFloat, center center: CGPoint) ``` |

Modified [SKPhysicsBody.init(edgeChainFromPath: CGPath)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519871-bodywithedgechainfrompath)

|  | Declaration |
| --- | --- |
| From | ``` init(edgeChainFromPath path: CGPath!) -> SKPhysicsBody ``` |
| To | ``` init(edgeChainFromPath path: CGPath) ``` |

Modified [SKPhysicsBody.init(edgeFromPoint: CGPoint, toPoint: CGPoint)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520401-bodywithedgefrompoint)

|  | Declaration |
| --- | --- |
| From | ``` init(edgeFromPoint p1: CGPoint, toPoint p2: CGPoint) -> SKPhysicsBody ``` |
| To | ``` init(edgeFromPoint p1: CGPoint, toPoint p2: CGPoint) ``` |

Modified [SKPhysicsBody.init(edgeLoopFromPath: CGPath)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519732-bodywithedgeloopfrompath)

|  | Declaration |
| --- | --- |
| From | ``` init(edgeLoopFromPath path: CGPath!) -> SKPhysicsBody ``` |
| To | ``` init(edgeLoopFromPath path: CGPath) ``` |

Modified [SKPhysicsBody.init(edgeLoopFromRect: CGRect)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520055-bodywithedgeloopfromrect)

|  | Declaration |
| --- | --- |
| From | ``` init(edgeLoopFromRect rect: CGRect) -> SKPhysicsBody ``` |
| To | ``` init(edgeLoopFromRect rect: CGRect) ``` |

Modified [SKPhysicsBody.init(polygonFromPath: CGPath)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520379-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(polygonFromPath path: CGPath!) -> SKPhysicsBody ``` |
| To | ``` init(polygonFromPath path: CGPath) ``` |

Modified [SKPhysicsBody.init(rectangleOfSize: CGSize)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520295-bodywithrectangleofsize)

|  | Declaration |
| --- | --- |
| From | ``` init!(rectangleOfSize s: CGSize) -> SKPhysicsBody ``` |
| To | ``` init(rectangleOfSize s: CGSize) ``` |

Modified [SKPhysicsBody.init(rectangleOfSize: CGSize, center: CGPoint)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519936-bodywithrectangleofsize)

|  | Declaration |
| --- | --- |
| From | ``` init!(rectangleOfSize s: CGSize, center center: CGPoint) -> SKPhysicsBody ``` |
| To | ``` init(rectangleOfSize s: CGSize, center center: CGPoint) ``` |

Modified [SKPhysicsBody.init(texture: SKTexture, alphaThreshold: Float, size: CGSize)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519689-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(texture texture: SKTexture!, alphaThreshold alphaThreshold: Float, size size: CGSize) -> SKPhysicsBody ``` |
| To | ``` init(texture texture: SKTexture, alphaThreshold alphaThreshold: Float, size size: CGSize) ``` |

Modified [SKPhysicsBody.init(texture: SKTexture, size: CGSize)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519690-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(texture texture: SKTexture!, size size: CGSize) -> SKPhysicsBody ``` |
| To | ``` init(texture texture: SKTexture, size size: CGSize) ``` |

Modified [SKPhysicsBody.joints](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519849-joints)

|  | Declaration |
| --- | --- |
| From | ``` var joints: [AnyObject] { get } ``` |
| To | ``` var joints: [SKPhysicsJoint] { get } ``` |

Modified [SKPhysicsContact](https://developer.apple.com/documentation/spritekit/skphysicscontact)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsContact : NSObject {     var bodyA: SKPhysicsBody! { get }     var bodyB: SKPhysicsBody! { get }     var contactPoint: CGPoint { get }     var contactNormal: CGVector { get }     var collisionImpulse: CGFloat { get } } ``` |
| To | ``` class SKPhysicsContact : NSObject {     var bodyA: SKPhysicsBody { get }     var bodyB: SKPhysicsBody { get }     var contactPoint: CGPoint { get }     var contactNormal: CGVector { get }     var collisionImpulse: CGFloat { get } } ``` |

Modified [SKPhysicsContact.bodyA](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478533-bodya)

|  | Declaration |
| --- | --- |
| From | ``` var bodyA: SKPhysicsBody! { get } ``` |
| To | ``` var bodyA: SKPhysicsBody { get } ``` |

Modified [SKPhysicsContact.bodyB](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478526-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` var bodyB: SKPhysicsBody! { get } ``` |
| To | ``` var bodyB: SKPhysicsBody { get } ``` |

Modified [SKPhysicsJoint](https://developer.apple.com/documentation/spritekit/skphysicsjoint)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsJoint : NSObject, NSCoding {     var bodyA: SKPhysicsBody!     var bodyB: SKPhysicsBody!     var reactionForce: CGVector { get }     var reactionTorque: CGFloat { get } } ``` |
| To | ``` class SKPhysicsJoint : NSObject, NSCoding {     var bodyA: SKPhysicsBody     var bodyB: SKPhysicsBody     var reactionForce: CGVector { get }     var reactionTorque: CGFloat { get } } ``` |

Modified [SKPhysicsJoint.bodyA](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1520403-bodya)

|  | Declaration |
| --- | --- |
| From | ``` var bodyA: SKPhysicsBody! ``` |
| To | ``` var bodyA: SKPhysicsBody ``` |

Modified [SKPhysicsJoint.bodyB](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1519693-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` var bodyB: SKPhysicsBody! ``` |
| To | ``` var bodyB: SKPhysicsBody ``` |

Modified [SKPhysicsJointFixed](https://developer.apple.com/documentation/spritekit/skphysicsjointfixed)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsJointFixed : SKPhysicsJoint {     class func jointWithBodyA(_ bodyA: SKPhysicsBody!, bodyB bodyB: SKPhysicsBody!, anchor anchor: CGPoint) -> SKPhysicsJointFixed! } ``` |
| To | ``` class SKPhysicsJointFixed : SKPhysicsJoint {     class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint) -> SKPhysicsJointFixed } ``` |

Modified [SKPhysicsJointFixed.jointWithBodyA(_: SKPhysicsBody, bodyB: SKPhysicsBody, anchor: CGPoint) -> SKPhysicsJointFixed [class]](https://developer.apple.com/documentation/spritekit/skphysicsjointfixed/1520076-jointwithbodya)

|  | Declaration |
| --- | --- |
| From | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody!, bodyB bodyB: SKPhysicsBody!, anchor anchor: CGPoint) -> SKPhysicsJointFixed! ``` |
| To | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint) -> SKPhysicsJointFixed ``` |

Modified [SKPhysicsJointLimit](https://developer.apple.com/documentation/spritekit/skphysicsjointlimit)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsJointLimit : SKPhysicsJoint {     var maxLength: CGFloat     class func jointWithBodyA(_ bodyA: SKPhysicsBody!, bodyB bodyB: SKPhysicsBody!, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointLimit! } ``` |
| To | ``` class SKPhysicsJointLimit : SKPhysicsJoint {     var maxLength: CGFloat     class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointLimit } ``` |

Modified [SKPhysicsJointLimit.jointWithBodyA(_: SKPhysicsBody, bodyB: SKPhysicsBody, anchorA: CGPoint, anchorB: CGPoint) -> SKPhysicsJointLimit [class]](https://developer.apple.com/documentation/spritekit/skphysicsjointlimit/1520402-jointwithbodya)

|  | Declaration |
| --- | --- |
| From | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody!, bodyB bodyB: SKPhysicsBody!, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointLimit! ``` |
| To | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointLimit ``` |

Modified [SKPhysicsJointPin](https://developer.apple.com/documentation/spritekit/skphysicsjointpin)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsJointPin : SKPhysicsJoint {     class func jointWithBodyA(_ bodyA: SKPhysicsBody!, bodyB bodyB: SKPhysicsBody!, anchor anchor: CGPoint) -> SKPhysicsJointPin!     var shouldEnableLimits: Bool     var lowerAngleLimit: CGFloat     var upperAngleLimit: CGFloat     var frictionTorque: CGFloat     var rotationSpeed: CGFloat } ``` |
| To | ``` class SKPhysicsJointPin : SKPhysicsJoint {     class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint) -> SKPhysicsJointPin     var shouldEnableLimits: Bool     var lowerAngleLimit: CGFloat     var upperAngleLimit: CGFloat     var frictionTorque: CGFloat     var rotationSpeed: CGFloat } ``` |

Modified [SKPhysicsJointPin.jointWithBodyA(_: SKPhysicsBody, bodyB: SKPhysicsBody, anchor: CGPoint) -> SKPhysicsJointPin [class]](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1519698-jointwithbodya)

|  | Declaration |
| --- | --- |
| From | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody!, bodyB bodyB: SKPhysicsBody!, anchor anchor: CGPoint) -> SKPhysicsJointPin! ``` |
| To | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint) -> SKPhysicsJointPin ``` |

Modified [SKPhysicsJointSliding](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsJointSliding : SKPhysicsJoint {     class func jointWithBodyA(_ bodyA: SKPhysicsBody!, bodyB bodyB: SKPhysicsBody!, anchor anchor: CGPoint, axis axis: CGVector) -> SKPhysicsJointSliding!     var shouldEnableLimits: Bool     var lowerDistanceLimit: CGFloat     var upperDistanceLimit: CGFloat } ``` |
| To | ``` class SKPhysicsJointSliding : SKPhysicsJoint {     class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint, axis axis: CGVector) -> SKPhysicsJointSliding     var shouldEnableLimits: Bool     var lowerDistanceLimit: CGFloat     var upperDistanceLimit: CGFloat } ``` |

Modified [SKPhysicsJointSliding.jointWithBodyA(_: SKPhysicsBody, bodyB: SKPhysicsBody, anchor: CGPoint, axis: CGVector) -> SKPhysicsJointSliding [class]](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/1520333-joint)

|  | Declaration |
| --- | --- |
| From | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody!, bodyB bodyB: SKPhysicsBody!, anchor anchor: CGPoint, axis axis: CGVector) -> SKPhysicsJointSliding! ``` |
| To | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint, axis axis: CGVector) -> SKPhysicsJointSliding ``` |

Modified [SKPhysicsJointSpring](https://developer.apple.com/documentation/spritekit/skphysicsjointspring)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsJointSpring : SKPhysicsJoint {     class func jointWithBodyA(_ bodyA: SKPhysicsBody!, bodyB bodyB: SKPhysicsBody!, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointSpring!     var damping: CGFloat     var frequency: CGFloat } ``` |
| To | ``` class SKPhysicsJointSpring : SKPhysicsJoint {     class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointSpring     var damping: CGFloat     var frequency: CGFloat } ``` |

Modified [SKPhysicsJointSpring.jointWithBodyA(_: SKPhysicsBody, bodyB: SKPhysicsBody, anchorA: CGPoint, anchorB: CGPoint) -> SKPhysicsJointSpring [class]](https://developer.apple.com/documentation/spritekit/skphysicsjointspring/1519665-joint)

|  | Declaration |
| --- | --- |
| From | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody!, bodyB bodyB: SKPhysicsBody!, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointSpring! ``` |
| To | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointSpring ``` |

Modified [SKPhysicsWorld](https://developer.apple.com/documentation/spritekit/skphysicsworld)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsWorld : NSObject, NSCoding {     var gravity: CGVector     var speed: CGFloat     unowned(unsafe) var contactDelegate: SKPhysicsContactDelegate!     func addJoint(_ joint: SKPhysicsJoint)     func removeJoint(_ joint: SKPhysicsJoint)     func removeAllJoints()     func bodyAtPoint(_ point: CGPoint) -> SKPhysicsBody?     func bodyInRect(_ rect: CGRect) -> SKPhysicsBody?     func bodyAlongRayStart(_ start: CGPoint, end end: CGPoint) -> SKPhysicsBody?     func enumerateBodiesAtPoint(_ point: CGPoint, usingBlock block: ((SKPhysicsBody!, UnsafeMutablePointer<ObjCBool>) -> Void)!)     func enumerateBodiesInRect(_ rect: CGRect, usingBlock block: ((SKPhysicsBody!, UnsafeMutablePointer<ObjCBool>) -> Void)!)     func enumerateBodiesAlongRayStart(_ start: CGPoint, end end: CGPoint, usingBlock block: ((SKPhysicsBody!, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void)!) } ``` |
| To | ``` class SKPhysicsWorld : NSObject, NSCoding {     var gravity: CGVector     var speed: CGFloat     unowned(unsafe) var contactDelegate: SKPhysicsContactDelegate?     func addJoint(_ joint: SKPhysicsJoint)     func removeJoint(_ joint: SKPhysicsJoint)     func removeAllJoints()     func sampleFieldsAt(_ position: vector_float3) -> vector_float3     func bodyAtPoint(_ point: CGPoint) -> SKPhysicsBody?     func bodyInRect(_ rect: CGRect) -> SKPhysicsBody?     func bodyAlongRayStart(_ start: CGPoint, end end: CGPoint) -> SKPhysicsBody?     func enumerateBodiesAtPoint(_ point: CGPoint, usingBlock block: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateBodiesInRect(_ rect: CGRect, usingBlock block: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateBodiesAlongRayStart(_ start: CGPoint, end end: CGPoint, usingBlock block: (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void) } ``` |

Modified [SKPhysicsWorld.contactDelegate](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449602-contactdelegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var contactDelegate: SKPhysicsContactDelegate! ``` |
| To | ``` unowned(unsafe) var contactDelegate: SKPhysicsContactDelegate? ``` |

Modified [SKPhysicsWorld.enumerateBodiesAlongRayStart(_: CGPoint, end: CGPoint, usingBlock: (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449615-enumeratebodies)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateBodiesAlongRayStart(_ start: CGPoint, end end: CGPoint, usingBlock block: ((SKPhysicsBody!, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateBodiesAlongRayStart(_ start: CGPoint, end end: CGPoint, usingBlock block: (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [SKPhysicsWorld.enumerateBodiesAtPoint(_: CGPoint, usingBlock: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449597-enumeratebodies)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateBodiesAtPoint(_ point: CGPoint, usingBlock block: ((SKPhysicsBody!, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateBodiesAtPoint(_ point: CGPoint, usingBlock block: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [SKPhysicsWorld.enumerateBodiesInRect(_: CGRect, usingBlock: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449619-enumeratebodies)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateBodiesInRect(_ rect: CGRect, usingBlock block: ((SKPhysicsBody!, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateBodiesInRect(_ rect: CGRect, usingBlock block: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [SKRegion](https://developer.apple.com/documentation/spritekit/skregion)

|  | Declaration |
| --- | --- |
| From | ``` class SKRegion : NSObject, NSCopying, NSCoding {     var path: CGPath? { get }     class func infiniteRegion() -> Self     init(radius radius: Float)     init(size size: CGSize)     init(path path: CGPath!)     func inverseRegion() -> Self     func regionByUnionWithRegion(_ region: SKRegion!) -> Self!     func regionByDifferenceFromRegion(_ region: SKRegion) -> Self     func regionByIntersectionWithRegion(_ region: SKRegion!) -> Self!     func containsPoint(_ point: CGPoint) -> Bool } ``` |
| To | ``` class SKRegion : NSObject, NSCopying, NSCoding {     var path: CGPath? { get }     class func infiniteRegion() -> Self     init(radius radius: Float)     init(size size: CGSize)     init(path path: CGPath)     func inverseRegion() -> Self     func regionByUnionWithRegion(_ region: SKRegion) -> Self     func regionByDifferenceFromRegion(_ region: SKRegion) -> Self     func regionByIntersectionWithRegion(_ region: SKRegion) -> Self     func containsPoint(_ point: CGPoint) -> Bool } ``` |

Modified [SKRegion.init(path: CGPath)](https://developer.apple.com/documentation/spritekit/skregion/1519857-init)

|  | Declaration |
| --- | --- |
| From | ``` init(path path: CGPath!) ``` |
| To | ``` init(path path: CGPath) ``` |

Modified [SKRegion.regionByIntersectionWithRegion(_: SKRegion) -> Self](https://developer.apple.com/documentation/spritekit/skregion/1519646-byintersection)

|  | Declaration |
| --- | --- |
| From | ``` func regionByIntersectionWithRegion(_ region: SKRegion!) -> Self! ``` |
| To | ``` func regionByIntersectionWithRegion(_ region: SKRegion) -> Self ``` |

Modified [SKRegion.regionByUnionWithRegion(_: SKRegion) -> Self](https://developer.apple.com/documentation/spritekit/skregion/1519702-byunion)

|  | Declaration |
| --- | --- |
| From | ``` func regionByUnionWithRegion(_ region: SKRegion!) -> Self! ``` |
| To | ``` func regionByUnionWithRegion(_ region: SKRegion) -> Self ``` |

Modified [SKRepeatMode [enum]](https://developer.apple.com/documentation/spritekit/skrepeatmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SKScene](https://developer.apple.com/documentation/spritekit/skscene)

|  | Declaration |
| --- | --- |
| From | ``` class SKScene : SKEffectNode {     init(size size: CGSize)     class func sceneWithSize(_ size: CGSize) -> Self     var size: CGSize     var scaleMode: SKSceneScaleMode     var backgroundColor: NSColor     unowned(unsafe) var delegate: SKSceneDelegate?     var anchorPoint: CGPoint     var physicsWorld: SKPhysicsWorld { get }     func convertPointFromView(_ point: CGPoint) -> CGPoint     func convertPointToView(_ point: CGPoint) -> CGPoint     weak var view: SKView? { get }     func update(_ currentTime: NSTimeInterval)     func didEvaluateActions()     func didSimulatePhysics()     func didApplyConstraints()     func didFinishUpdate()     func didMoveToView(_ view: SKView)     func willMoveFromView(_ view: SKView)     func didChangeSize(_ oldSize: CGSize) } ``` |
| To | ``` class SKScene : SKEffectNode {     init(size size: CGSize)     class func sceneWithSize(_ size: CGSize) -> Self     var size: CGSize     var scaleMode: SKSceneScaleMode     weak var camera: SKCameraNode?     weak var listener: SKNode?     var audioEngine: AVAudioEngine { get }     var backgroundColor: NSColor     unowned(unsafe) var delegate: SKSceneDelegate?     var anchorPoint: CGPoint     var physicsWorld: SKPhysicsWorld { get }     func convertPointFromView(_ point: CGPoint) -> CGPoint     func convertPointToView(_ point: CGPoint) -> CGPoint     weak var view: SKView? { get }     func update(_ currentTime: NSTimeInterval)     func didEvaluateActions()     func didSimulatePhysics()     func didApplyConstraints()     func didFinishUpdate()     func didMoveToView(_ view: SKView)     func willMoveFromView(_ view: SKView)     func didChangeSize(_ oldSize: CGSize) } ``` |

Modified [SKSceneScaleMode [enum]](https://developer.apple.com/documentation/spritekit/skscenescalemode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SKShader](https://developer.apple.com/documentation/spritekit/skshader)

|  | Declaration |
| --- | --- |
| From | ``` class SKShader : NSObject, NSCopying, NSCoding {     init(source source: String!)     init(source source: String!, uniforms uniforms: [AnyObject]!)     convenience init!()     class func shader() -> Self!     class func shaderWithSource(_ source: String!) -> Self     class func shaderWithSource(_ source: String!, uniforms uniforms: [AnyObject]!) -> Self     convenience init!(fileNamed name: String)     class func shaderWithFileNamed(_ name: String) -> Self!     var source: String!     var uniforms: [AnyObject]     func addUniform(_ uniform: SKUniform)     func uniformNamed(_ name: String) -> SKUniform?     func removeUniformNamed(_ name: String) } ``` |
| To | ``` class SKShader : NSObject, NSCopying, NSCoding {     init(source source: String)     init(source source: String, uniforms uniforms: [SKUniform])     convenience init()     class func shader() -> Self     class func shaderWithSource(_ source: String) -> Self     class func shaderWithSource(_ source: String, uniforms uniforms: [SKUniform]) -> Self     convenience init(fileNamed name: String)     class func shaderWithFileNamed(_ name: String) -> Self     var source: String?     var uniforms: [SKUniform]     func addUniform(_ uniform: SKUniform)     func uniformNamed(_ name: String) -> SKUniform?     func removeUniformNamed(_ name: String) } ``` |

Modified [SKShader.init(fileNamed: String)](https://developer.apple.com/documentation/spritekit/skshader/1477557-shaderwithfilenamed)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(fileNamed name: String) ``` |
| To | ``` convenience init(fileNamed name: String) ``` |

Modified [SKShader.init(source: String)](https://developer.apple.com/documentation/spritekit/skshader/1477571-initwithsource)

|  | Declaration |
| --- | --- |
| From | ``` init(source source: String!) ``` |
| To | ``` init(source source: String) ``` |

Modified [SKShader.init(source: String, uniforms: [SKUniform])](https://developer.apple.com/documentation/spritekit/skshader/1477555-initwithsource)

|  | Declaration |
| --- | --- |
| From | ``` init(source source: String!, uniforms uniforms: [AnyObject]!) ``` |
| To | ``` init(source source: String, uniforms uniforms: [SKUniform]) ``` |

Modified [SKShader.source](https://developer.apple.com/documentation/spritekit/skshader/1477544-source)

|  | Declaration |
| --- | --- |
| From | ``` var source: String! ``` |
| To | ``` var source: String? ``` |

Modified [SKShader.uniforms](https://developer.apple.com/documentation/spritekit/skshader/1477565-uniforms)

|  | Declaration |
| --- | --- |
| From | ``` var uniforms: [AnyObject] ``` |
| To | ``` var uniforms: [SKUniform] ``` |

Modified [SKShapeNode](https://developer.apple.com/documentation/spritekit/skshapenode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKShapeNode : SKNode {     convenience init(path path: CGPath!)     class func shapeNodeWithPath(_ path: CGPath!) -> Self     convenience init(path path: CGPath!, centered centered: Bool)     class func shapeNodeWithPath(_ path: CGPath!, centered centered: Bool) -> Self     convenience init(rect rect: CGRect)     class func shapeNodeWithRect(_ rect: CGRect) -> Self     convenience init(rectOfSize size: CGSize)     class func shapeNodeWithRectOfSize(_ size: CGSize) -> Self     convenience init(rect rect: CGRect, cornerRadius cornerRadius: CGFloat)     class func shapeNodeWithRect(_ rect: CGRect, cornerRadius cornerRadius: CGFloat) -> Self     convenience init(rectOfSize size: CGSize, cornerRadius cornerRadius: CGFloat)     class func shapeNodeWithRectOfSize(_ size: CGSize, cornerRadius cornerRadius: CGFloat) -> Self     convenience init(circleOfRadius radius: CGFloat)     class func shapeNodeWithCircleOfRadius(_ radius: CGFloat) -> Self     convenience init(ellipseInRect rect: CGRect)     class func shapeNodeWithEllipseInRect(_ rect: CGRect) -> Self     convenience init(ellipseOfSize size: CGSize)     class func shapeNodeWithEllipseOfSize(_ size: CGSize) -> Self     convenience init(points points: UnsafeMutablePointer<CGPoint>, count numPoints: Int)     class func shapeNodeWithPoints(_ points: UnsafeMutablePointer<CGPoint>, count numPoints: Int) -> Self     convenience init(splinePoints points: UnsafeMutablePointer<CGPoint>, count numPoints: Int)     class func shapeNodeWithSplinePoints(_ points: UnsafeMutablePointer<CGPoint>, count numPoints: Int) -> Self     var path: CGPath!     var strokeColor: NSColor     var fillColor: NSColor     var blendMode: SKBlendMode     var antialiased: Bool     var lineWidth: CGFloat     var glowWidth: CGFloat     var lineCap: CGLineCap     var lineJoin: CGLineJoin     var miterLimit: CGFloat     var lineLength: CGFloat { get }     var fillTexture: SKTexture?     var fillShader: SKShader?     var strokeTexture: SKTexture?     var strokeShader: SKShader? } extension SKShapeNode : Reflectable {     func getMirror() -> MirrorType } extension SKShapeNode : Reflectable {     func getMirror() -> MirrorType } ``` | AnyObject, Reflectable |
| To | ``` class SKShapeNode : SKNode {     convenience init(path path: CGPath)     class func shapeNodeWithPath(_ path: CGPath) -> Self     convenience init(path path: CGPath, centered centered: Bool)     class func shapeNodeWithPath(_ path: CGPath, centered centered: Bool) -> Self     convenience init(rect rect: CGRect)     class func shapeNodeWithRect(_ rect: CGRect) -> Self     convenience init(rectOfSize size: CGSize)     class func shapeNodeWithRectOfSize(_ size: CGSize) -> Self     convenience init(rect rect: CGRect, cornerRadius cornerRadius: CGFloat)     class func shapeNodeWithRect(_ rect: CGRect, cornerRadius cornerRadius: CGFloat) -> Self     convenience init(rectOfSize size: CGSize, cornerRadius cornerRadius: CGFloat)     class func shapeNodeWithRectOfSize(_ size: CGSize, cornerRadius cornerRadius: CGFloat) -> Self     convenience init(circleOfRadius radius: CGFloat)     class func shapeNodeWithCircleOfRadius(_ radius: CGFloat) -> Self     convenience init(ellipseInRect rect: CGRect)     class func shapeNodeWithEllipseInRect(_ rect: CGRect) -> Self     convenience init(ellipseOfSize size: CGSize)     class func shapeNodeWithEllipseOfSize(_ size: CGSize) -> Self     convenience init(points points: UnsafeMutablePointer<CGPoint>, count numPoints: Int)     class func shapeNodeWithPoints(_ points: UnsafeMutablePointer<CGPoint>, count numPoints: Int) -> Self     convenience init(splinePoints points: UnsafeMutablePointer<CGPoint>, count numPoints: Int)     class func shapeNodeWithSplinePoints(_ points: UnsafeMutablePointer<CGPoint>, count numPoints: Int) -> Self     var path: CGPath?     var strokeColor: NSColor     var fillColor: NSColor     var blendMode: SKBlendMode     var antialiased: Bool     var lineWidth: CGFloat     var glowWidth: CGFloat     var lineCap: CGLineCap     var lineJoin: CGLineJoin     var miterLimit: CGFloat     var lineLength: CGFloat { get }     var fillTexture: SKTexture?     var fillShader: SKShader?     var strokeTexture: SKTexture?     var strokeShader: SKShader? } extension SKShapeNode : _Reflectable { } extension SKShapeNode : _Reflectable { } ``` | AnyObject |

Modified [SKShapeNode.init(path: CGPath)](https://developer.apple.com/documentation/spritekit/skshapenode/1520022-shapenodewithpath)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(path path: CGPath!) ``` |
| To | ``` convenience init(path path: CGPath) ``` |

Modified [SKShapeNode.init(path: CGPath, centered: Bool)](https://developer.apple.com/documentation/spritekit/skshapenode/1519649-shapenodewithpath)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(path path: CGPath!, centered centered: Bool) ``` |
| To | ``` convenience init(path path: CGPath, centered centered: Bool) ``` |

Modified [SKShapeNode.path](https://developer.apple.com/documentation/spritekit/skshapenode/1519741-path)

|  | Declaration |
| --- | --- |
| From | ``` var path: CGPath! ``` |
| To | ``` var path: CGPath? ``` |

Modified [SKSpriteNode](https://developer.apple.com/documentation/spritekit/skspritenode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKSpriteNode : SKNode {     convenience init(texture texture: SKTexture!, size size: CGSize)     class func spriteNodeWithTexture(_ texture: SKTexture!, size size: CGSize) -> Self     convenience init!(texture texture: SKTexture!)     class func spriteNodeWithTexture(_ texture: SKTexture!) -> Self!     convenience init(texture texture: SKTexture!, normalMap normalMap: SKTexture?)     class func spriteNodeWithTexture(_ texture: SKTexture!, normalMap normalMap: SKTexture?) -> Self     convenience init(imageNamed name: String)     class func spriteNodeWithImageNamed(_ name: String) -> Self     convenience init(imageNamed name: String, normalMapped generateNormalMap: Bool)     class func spriteNodeWithImageNamed(_ name: String, normalMapped generateNormalMap: Bool) -> Self     convenience init!(color color: NSColor!, size size: CGSize)     class func spriteNodeWithColor(_ color: NSColor!, size size: CGSize) -> Self!     init(texture texture: SKTexture!, color color: NSColor!, size size: CGSize)     convenience init(texture texture: SKTexture!)     convenience init(imageNamed name: String)     convenience init(color color: NSColor!, size size: CGSize)     init?(coder aDecoder: NSCoder)     var texture: SKTexture?     var normalTexture: SKTexture?     var lightingBitMask: UInt32     var shadowCastBitMask: UInt32     var shadowedBitMask: UInt32     var centerRect: CGRect     var colorBlendFactor: CGFloat     var color: NSColor     var blendMode: SKBlendMode     var anchorPoint: CGPoint     var size: CGSize     var shader: SKShader? } extension SKSpriteNode : Reflectable {     func getMirror() -> MirrorType } extension SKSpriteNode : Reflectable {     func getMirror() -> MirrorType } ``` | AnyObject, Reflectable |
| To | ``` class SKSpriteNode : SKNode {     convenience init(texture texture: SKTexture?, size size: CGSize)     class func spriteNodeWithTexture(_ texture: SKTexture?, size size: CGSize) -> Self     convenience init(texture texture: SKTexture?)     class func spriteNodeWithTexture(_ texture: SKTexture?) -> Self     convenience init(texture texture: SKTexture?, normalMap normalMap: SKTexture?)     class func spriteNodeWithTexture(_ texture: SKTexture?, normalMap normalMap: SKTexture?) -> Self     convenience init(imageNamed name: String)     class func spriteNodeWithImageNamed(_ name: String) -> Self     convenience init(imageNamed name: String, normalMapped generateNormalMap: Bool)     class func spriteNodeWithImageNamed(_ name: String, normalMapped generateNormalMap: Bool) -> Self     convenience init(color color: NSColor, size size: CGSize)     class func spriteNodeWithColor(_ color: NSColor, size size: CGSize) -> Self     init(texture texture: SKTexture?, color color: NSColor, size size: CGSize)     convenience init(texture texture: SKTexture?)     convenience init(imageNamed name: String)     convenience init(color color: NSColor, size size: CGSize)     init?(coder aDecoder: NSCoder)     var texture: SKTexture?     var normalTexture: SKTexture?     var lightingBitMask: UInt32     var shadowCastBitMask: UInt32     var shadowedBitMask: UInt32     var centerRect: CGRect     var colorBlendFactor: CGFloat     var color: NSColor     var blendMode: SKBlendMode     var anchorPoint: CGPoint     var size: CGSize     var shader: SKShader? } extension SKSpriteNode : _Reflectable { } extension SKSpriteNode : _Reflectable { } ``` | AnyObject |

Modified [SKSpriteNode.init(color: NSColor, size: CGSize)](https://developer.apple.com/documentation/spritekit/skspritenode/1519762-initwithcolor)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(color color: NSColor!, size size: CGSize) ``` |
| To | ``` convenience init(color color: NSColor, size size: CGSize) ``` |

Modified [SKSpriteNode.init(texture: SKTexture?)](https://developer.apple.com/documentation/spritekit/skspritenode/1519942-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(texture texture: SKTexture!) ``` |
| To | ``` convenience init(texture texture: SKTexture?) ``` |

Modified [SKSpriteNode.init(texture: SKTexture?, color: NSColor, size: CGSize)](https://developer.apple.com/documentation/spritekit/skspritenode/1520029-init)

|  | Declaration |
| --- | --- |
| From | ``` init(texture texture: SKTexture!, color color: NSColor!, size size: CGSize) ``` |
| To | ``` init(texture texture: SKTexture?, color color: NSColor, size size: CGSize) ``` |

Modified [SKSpriteNode.init(texture: SKTexture?, normalMap: SKTexture?)](https://developer.apple.com/documentation/spritekit/skspritenode/1520153-spritenodewithtexture)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(texture texture: SKTexture!, normalMap normalMap: SKTexture?) ``` |
| To | ``` convenience init(texture texture: SKTexture?, normalMap normalMap: SKTexture?) ``` |

Modified [SKSpriteNode.init(texture: SKTexture?, size: CGSize)](https://developer.apple.com/documentation/spritekit/skspritenode/1519812-spritenodewithtexture)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(texture texture: SKTexture!, size size: CGSize) ``` |
| To | ``` convenience init(texture texture: SKTexture?, size size: CGSize) ``` |

Modified [SKTexture](https://developer.apple.com/documentation/spritekit/sktexture)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKTexture : NSObject, NSCopying, NSCoding {     convenience init!(imageNamed name: String)     class func textureWithImageNamed(_ name: String) -> Self!     convenience init(rect rect: CGRect, inTexture texture: SKTexture)     class func textureWithRect(_ rect: CGRect, inTexture texture: SKTexture) -> Self     convenience init!(vectorNoiseWithSmoothness smoothness: CGFloat, size size: CGSize)     class func textureVectorNoiseWithSmoothness(_ smoothness: CGFloat, size size: CGSize) -> Self!     convenience init!(noiseWithSmoothness smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool)     class func textureNoiseWithSmoothness(_ smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool) -> Self!     convenience init(CGImage image: CGImage!)     class func textureWithCGImage(_ image: CGImage!) -> Self     convenience init(image image: NSImage)     class func textureWithImage(_ image: NSImage) -> Self     convenience init!(data pixelData: NSData!, size size: CGSize)     class func textureWithData(_ pixelData: NSData!, size size: CGSize) -> Self!     convenience init!(data pixelData: NSData!, size size: CGSize, flipped flipped: Bool)     class func textureWithData(_ pixelData: NSData!, size size: CGSize, flipped flipped: Bool) -> Self!     convenience init!(data pixelData: NSData!, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32)     class func textureWithData(_ pixelData: NSData!, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) -> Self!     func textureByApplyingCIFilter(_ filter: CIFilter) -> Self     func textureByGeneratingNormalMap() -> Self!     func textureByGeneratingNormalMapWithSmoothness(_ smoothness: CGFloat, contrast contrast: CGFloat) -> Self!     func textureRect() -> CGRect     func size() -> CGSize     var filteringMode: SKTextureFilteringMode     var usesMipmaps: Bool     class func preloadTextures(_ textures: [AnyObject]!, withCompletionHandler completionHandler: (() -> Void)!)     func preloadWithCompletionHandler(_ completionHandler: (() -> Void)!) } extension SKTexture : Reflectable {     func getMirror() -> MirrorType } extension SKTexture : Reflectable {     func getMirror() -> MirrorType } ``` | AnyObject, NSCoding, NSCopying, Reflectable |
| To | ``` class SKTexture : NSObject, NSCopying, NSCoding {     convenience init(imageNamed name: String)     class func textureWithImageNamed(_ name: String) -> Self     convenience init(rect rect: CGRect, inTexture texture: SKTexture)     class func textureWithRect(_ rect: CGRect, inTexture texture: SKTexture) -> Self     convenience init(vectorNoiseWithSmoothness smoothness: CGFloat, size size: CGSize)     class func textureVectorNoiseWithSmoothness(_ smoothness: CGFloat, size size: CGSize) -> Self     convenience init(noiseWithSmoothness smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool)     class func textureNoiseWithSmoothness(_ smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool) -> Self     convenience init(CGImage image: CGImage)     class func textureWithCGImage(_ image: CGImage) -> Self     convenience init(image image: NSImage)     class func textureWithImage(_ image: NSImage) -> Self     convenience init(data pixelData: NSData, size size: CGSize)     class func textureWithData(_ pixelData: NSData, size size: CGSize) -> Self     convenience init(data pixelData: NSData, size size: CGSize, flipped flipped: Bool)     class func textureWithData(_ pixelData: NSData, size size: CGSize, flipped flipped: Bool) -> Self     convenience init(data pixelData: NSData, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32)     class func textureWithData(_ pixelData: NSData, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) -> Self     func textureByApplyingCIFilter(_ filter: CIFilter) -> Self     func textureByGeneratingNormalMap() -> Self     func textureByGeneratingNormalMapWithSmoothness(_ smoothness: CGFloat, contrast contrast: CGFloat) -> Self     func textureRect() -> CGRect     func size() -> CGSize     var filteringMode: SKTextureFilteringMode     var usesMipmaps: Bool     var CGImage: CGImage { get }     class func preloadTextures(_ textures: [SKTexture], withCompletionHandler completionHandler: () -> Void)     func preloadWithCompletionHandler(_ completionHandler: () -> Void) } extension SKTexture : _Reflectable { } extension SKTexture : _Reflectable { } ``` | AnyObject, NSCoding, NSCopying |

Modified [SKTexture.init(CGImage: CGImage)](https://developer.apple.com/documentation/spritekit/sktexture/1519576-texturewithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(CGImage image: CGImage!) ``` |
| To | ``` convenience init(CGImage image: CGImage) ``` |

Modified [SKTexture.init(data: NSData, size: CGSize)](https://developer.apple.com/documentation/spritekit/sktexture/1519962-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(data pixelData: NSData!, size size: CGSize) ``` |
| To | ``` convenience init(data pixelData: NSData, size size: CGSize) ``` |

Modified [SKTexture.init(data: NSData, size: CGSize, flipped: Bool)](https://developer.apple.com/documentation/spritekit/sktexture/1519674-texturewithdata)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(data pixelData: NSData!, size size: CGSize, flipped flipped: Bool) ``` |
| To | ``` convenience init(data pixelData: NSData, size size: CGSize, flipped flipped: Bool) ``` |

Modified [SKTexture.init(data: NSData, size: CGSize, rowLength: UInt32, alignment: UInt32)](https://developer.apple.com/documentation/spritekit/sktexture/1520181-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(data pixelData: NSData!, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) ``` |
| To | ``` convenience init(data pixelData: NSData, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) ``` |

Modified [SKTexture.init(imageNamed: String)](https://developer.apple.com/documentation/spritekit/sktexture/1520086-texturewithimagenamed)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(imageNamed name: String) ``` |
| To | ``` convenience init(imageNamed name: String) ``` |

Modified [SKTexture.init(noiseWithSmoothness: CGFloat, size: CGSize, grayscale: Bool)](https://developer.apple.com/documentation/spritekit/sktexture/1519971-texturenoisewithsmoothness)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(noiseWithSmoothness smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool) ``` |
| To | ``` convenience init(noiseWithSmoothness smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool) ``` |

Modified [SKTexture.init(vectorNoiseWithSmoothness: CGFloat, size: CGSize)](https://developer.apple.com/documentation/spritekit/sktexture/1520393-texturevectornoisewithsmoothness)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(vectorNoiseWithSmoothness smoothness: CGFloat, size size: CGSize) ``` |
| To | ``` convenience init(vectorNoiseWithSmoothness smoothness: CGFloat, size size: CGSize) ``` |

Modified [SKTexture.preloadTextures(_: [SKTexture], withCompletionHandler: () -> Void) [class]](https://developer.apple.com/documentation/spritekit/sktexture/1519817-preloadtextures)

|  | Declaration |
| --- | --- |
| From | ``` class func preloadTextures(_ textures: [AnyObject]!, withCompletionHandler completionHandler: (() -> Void)!) ``` |
| To | ``` class func preloadTextures(_ textures: [SKTexture], withCompletionHandler completionHandler: () -> Void) ``` |

Modified [SKTexture.preloadWithCompletionHandler(_: () -> Void)](https://developer.apple.com/documentation/spritekit/sktexture/1520172-preloadwithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func preloadWithCompletionHandler(_ completionHandler: (() -> Void)!) ``` |
| To | ``` func preloadWithCompletionHandler(_ completionHandler: () -> Void) ``` |

Modified [SKTexture.textureByGeneratingNormalMap() -> Self](https://developer.apple.com/documentation/spritekit/sktexture/1519687-texturebygeneratingnormalmap)

|  | Declaration |
| --- | --- |
| From | ``` func textureByGeneratingNormalMap() -> Self! ``` |
| To | ``` func textureByGeneratingNormalMap() -> Self ``` |

Modified [SKTexture.textureByGeneratingNormalMapWithSmoothness(_: CGFloat, contrast: CGFloat) -> Self](https://developer.apple.com/documentation/spritekit/sktexture/1520441-texturebygeneratingnormalmapwith)

|  | Declaration |
| --- | --- |
| From | ``` func textureByGeneratingNormalMapWithSmoothness(_ smoothness: CGFloat, contrast contrast: CGFloat) -> Self! ``` |
| To | ``` func textureByGeneratingNormalMapWithSmoothness(_ smoothness: CGFloat, contrast contrast: CGFloat) -> Self ``` |

Modified [SKTextureAtlas](https://developer.apple.com/documentation/spritekit/sktextureatlas)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKTextureAtlas : NSObject, NSCoding {     convenience init!(named name: String)     class func atlasNamed(_ name: String) -> Self!     convenience init!(dictionary properties: [NSObject : AnyObject])     class func atlasWithDictionary(_ properties: [NSObject : AnyObject]) -> Self!     func textureNamed(_ name: String) -> SKTexture!     class func preloadTextureAtlases(_ textureAtlases: [AnyObject]!, withCompletionHandler completionHandler: (() -> Void)!)     func preloadWithCompletionHandler(_ completionHandler: () -> Void)     var textureNames: [AnyObject] { get } } extension SKTextureAtlas : Reflectable {     func getMirror() -> MirrorType } extension SKTextureAtlas : Reflectable {     func getMirror() -> MirrorType } ``` | AnyObject, NSCoding, Reflectable |
| To | ``` class SKTextureAtlas : NSObject, NSCoding {     convenience init(named name: String)     class func atlasNamed(_ name: String) -> Self     convenience init(dictionary properties: [String : AnyObject])     class func atlasWithDictionary(_ properties: [String : AnyObject]) -> Self     func textureNamed(_ name: String) -> SKTexture     class func preloadTextureAtlases(_ textureAtlases: [SKTextureAtlas], withCompletionHandler completionHandler: () -> Void)     class func preloadTextureAtlasesNamed(_ atlasNames: [String], withCompletionHandler completionHandler: (NSError?, [SKTextureAtlas]) -> Void)     func preloadWithCompletionHandler(_ completionHandler: () -> Void)     var textureNames: [String] { get } } extension SKTextureAtlas : _Reflectable { } extension SKTextureAtlas : _Reflectable { } ``` | AnyObject, NSCoding |

Modified [SKTextureAtlas.init(dictionary: [String : AnyObject])](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427383-atlaswithdictionary)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(dictionary properties: [NSObject : AnyObject]) ``` |
| To | ``` convenience init(dictionary properties: [String : AnyObject]) ``` |

Modified [SKTextureAtlas.init(named: String)](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427381-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(named name: String) ``` |
| To | ``` convenience init(named name: String) ``` |

Modified [SKTextureAtlas.preloadTextureAtlases(_: [SKTextureAtlas], withCompletionHandler: () -> Void) [class]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427379-preloadtextureatlases)

|  | Declaration |
| --- | --- |
| From | ``` class func preloadTextureAtlases(_ textureAtlases: [AnyObject]!, withCompletionHandler completionHandler: (() -> Void)!) ``` |
| To | ``` class func preloadTextureAtlases(_ textureAtlases: [SKTextureAtlas], withCompletionHandler completionHandler: () -> Void) ``` |

Modified [SKTextureAtlas.textureNamed(_: String) -> SKTexture](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427375-texturenamed)

|  | Declaration |
| --- | --- |
| From | ``` func textureNamed(_ name: String) -> SKTexture! ``` |
| To | ``` func textureNamed(_ name: String) -> SKTexture ``` |

Modified [SKTextureAtlas.textureNames](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427373-texturenames)

|  | Declaration |
| --- | --- |
| From | ``` var textureNames: [AnyObject] { get } ``` |
| To | ``` var textureNames: [String] { get } ``` |

Modified [SKTextureFilteringMode [enum]](https://developer.apple.com/documentation/spritekit/sktexturefilteringmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SKTransition](https://developer.apple.com/documentation/spritekit/sktransition)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKTransition : NSObject {     class func crossFadeWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func fadeWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func fadeWithColor(_ color: NSColor, duration sec: NSTimeInterval) -> SKTransition     class func flipHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func flipVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func revealWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition     class func moveInWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition     class func pushWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition     class func doorsOpenHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func doorsOpenVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func doorsCloseHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func doorsCloseVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func doorwayWithDuration(_ sec: NSTimeInterval) -> SKTransition     init(CIFilter filter: CIFilter, duration sec: NSTimeInterval) -> SKTransition     class func transitionWithCIFilter(_ filter: CIFilter, duration sec: NSTimeInterval) -> SKTransition     var pausesIncomingScene: Bool     var pausesOutgoingScene: Bool } ``` | AnyObject |
| To | ``` class SKTransition : NSObject, NSCopying {     class func crossFadeWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func fadeWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func fadeWithColor(_ color: NSColor, duration sec: NSTimeInterval) -> SKTransition     class func flipHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func flipVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func revealWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition     class func moveInWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition     class func pushWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition     class func doorsOpenHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func doorsOpenVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func doorsCloseHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func doorsCloseVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func doorwayWithDuration(_ sec: NSTimeInterval) -> SKTransition      init(CIFilter filter: CIFilter, duration sec: NSTimeInterval)     class func transitionWithCIFilter(_ filter: CIFilter, duration sec: NSTimeInterval) -> SKTransition     var pausesIncomingScene: Bool     var pausesOutgoingScene: Bool } ``` | AnyObject, NSCopying |

Modified [SKTransition.init(CIFilter: CIFilter, duration: NSTimeInterval)](https://developer.apple.com/documentation/spritekit/sktransition/1395895-init)

|  | Declaration |
| --- | --- |
| From | ``` init(CIFilter filter: CIFilter, duration sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` init(CIFilter filter: CIFilter, duration sec: NSTimeInterval) ``` |

Modified [SKTransitionDirection [enum]](https://developer.apple.com/documentation/spritekit/sktransitiondirection)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SKUniform](https://developer.apple.com/documentation/spritekit/skuniform)

|  | Declaration |
| --- | --- |
| From | ``` class SKUniform : NSObject, NSCopying, NSCoding {     convenience init!(name name: String!)     class func uniformWithName(_ name: String!) -> Self!     convenience init!(name name: String!, texture texture: SKTexture!)     class func uniformWithName(_ name: String!, texture texture: SKTexture!) -> Self!     convenience init!(name name: String!, float value: Float)     class func uniformWithName(_ name: String!, float value: Float) -> Self!     convenience init!(name name: String!, floatVector2 value: GLKVector2)     class func uniformWithName(_ name: String!, floatVector2 value: GLKVector2) -> Self!     convenience init!(name name: String!, floatVector3 value: GLKVector3)     class func uniformWithName(_ name: String!, floatVector3 value: GLKVector3) -> Self!     convenience init!(name name: String!, floatVector4 value: GLKVector4)     class func uniformWithName(_ name: String!, floatVector4 value: GLKVector4) -> Self!     convenience init!(name name: String!, floatMatrix2 value: GLKMatrix2)     class func uniformWithName(_ name: String!, floatMatrix2 value: GLKMatrix2) -> Self!     convenience init!(name name: String!, floatMatrix3 value: GLKMatrix3)     class func uniformWithName(_ name: String!, floatMatrix3 value: GLKMatrix3) -> Self!     convenience init!(name name: String!, floatMatrix4 value: GLKMatrix4)     class func uniformWithName(_ name: String!, floatMatrix4 value: GLKMatrix4) -> Self!     var name: String { get }     var uniformType: SKUniformType { get }     var textureValue: SKTexture!     var floatValue: Float     var floatVector2Value: GLKVector2     var floatVector3Value: GLKVector3     var floatVector4Value: GLKVector4     var floatMatrix2Value: GLKMatrix2     var floatMatrix3Value: GLKMatrix3     var floatMatrix4Value: GLKMatrix4     init!(name name: String!)     init!(name name: String!, texture texture: SKTexture!)     init!(name name: String!, float value: Float)     init!(name name: String!, floatVector2 value: GLKVector2)     init!(name name: String!, floatVector3 value: GLKVector3)     init!(name name: String!, floatVector4 value: GLKVector4)     init!(name name: String!, floatMatrix2 value: GLKMatrix2)     init!(name name: String!, floatMatrix3 value: GLKMatrix3)     init!(name name: String!, floatMatrix4 value: GLKMatrix4) } ``` |
| To | ``` class SKUniform : NSObject, NSCopying, NSCoding {     convenience init(name name: String)     class func uniformWithName(_ name: String) -> Self     convenience init(name name: String, texture texture: SKTexture)     class func uniformWithName(_ name: String, texture texture: SKTexture) -> Self     convenience init(name name: String, float value: Float)     class func uniformWithName(_ name: String, float value: Float) -> Self     convenience init(name name: String, floatVector2 value: GLKVector2)     class func uniformWithName(_ name: String, floatVector2 value: GLKVector2) -> Self     convenience init(name name: String, floatVector3 value: GLKVector3)     class func uniformWithName(_ name: String, floatVector3 value: GLKVector3) -> Self     convenience init(name name: String, floatVector4 value: GLKVector4)     class func uniformWithName(_ name: String, floatVector4 value: GLKVector4) -> Self     convenience init(name name: String, floatMatrix2 value: GLKMatrix2)     class func uniformWithName(_ name: String, floatMatrix2 value: GLKMatrix2) -> Self     convenience init(name name: String, floatMatrix3 value: GLKMatrix3)     class func uniformWithName(_ name: String, floatMatrix3 value: GLKMatrix3) -> Self     convenience init(name name: String, floatMatrix4 value: GLKMatrix4)     class func uniformWithName(_ name: String, floatMatrix4 value: GLKMatrix4) -> Self     var name: String { get }     var uniformType: SKUniformType { get }     var textureValue: SKTexture?     var floatValue: Float     var floatVector2Value: GLKVector2     var floatVector3Value: GLKVector3     var floatVector4Value: GLKVector4     var floatMatrix2Value: GLKMatrix2     var floatMatrix3Value: GLKMatrix3     var floatMatrix4Value: GLKMatrix4     init(name name: String)     init(name name: String, texture texture: SKTexture?)     init(name name: String, float value: Float)     init(name name: String, floatVector2 value: GLKVector2)     init(name name: String, floatVector3 value: GLKVector3)     init(name name: String, floatVector4 value: GLKVector4)     init(name name: String, floatMatrix2 value: GLKMatrix2)     init(name name: String, floatMatrix3 value: GLKMatrix3)     init(name name: String, floatMatrix4 value: GLKMatrix4) } ``` |

Modified [SKUniform.init(name: String)](https://developer.apple.com/documentation/spritekit/skuniform/1455420-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!) ``` |
| To | ``` init(name name: String) ``` |

Modified [SKUniform.init(name: String, float: Float)](https://developer.apple.com/documentation/spritekit/skuniform/1455447-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, float value: Float) ``` |
| To | ``` init(name name: String, float value: Float) ``` |

Modified [SKUniform.init(name: String, floatMatrix2: GLKMatrix2)](https://developer.apple.com/documentation/spritekit/skuniform/1455431-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, floatMatrix2 value: GLKMatrix2) ``` |
| To | ``` init(name name: String, floatMatrix2 value: GLKMatrix2) ``` |

Modified [SKUniform.init(name: String, floatMatrix3: GLKMatrix3)](https://developer.apple.com/documentation/spritekit/skuniform/1455462-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, floatMatrix3 value: GLKMatrix3) ``` |
| To | ``` init(name name: String, floatMatrix3 value: GLKMatrix3) ``` |

Modified [SKUniform.init(name: String, floatMatrix4: GLKMatrix4)](https://developer.apple.com/documentation/spritekit/skuniform/1455429-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, floatMatrix4 value: GLKMatrix4) ``` |
| To | ``` init(name name: String, floatMatrix4 value: GLKMatrix4) ``` |

Modified [SKUniform.init(name: String, floatVector2: GLKVector2)](https://developer.apple.com/documentation/spritekit/skuniform/1455444-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, floatVector2 value: GLKVector2) ``` |
| To | ``` init(name name: String, floatVector2 value: GLKVector2) ``` |

Modified [SKUniform.init(name: String, floatVector3: GLKVector3)](https://developer.apple.com/documentation/spritekit/skuniform/1455416-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, floatVector3 value: GLKVector3) ``` |
| To | ``` init(name name: String, floatVector3 value: GLKVector3) ``` |

Modified [SKUniform.init(name: String, floatVector4: GLKVector4)](https://developer.apple.com/documentation/spritekit/skuniform/1455418-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, floatVector4 value: GLKVector4) ``` |
| To | ``` init(name name: String, floatVector4 value: GLKVector4) ``` |

Modified [SKUniform.init(name: String, texture: SKTexture?)](https://developer.apple.com/documentation/spritekit/skuniform/1455452-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, texture texture: SKTexture!) ``` |
| To | ``` init(name name: String, texture texture: SKTexture?) ``` |

Modified [SKUniform.textureValue](https://developer.apple.com/documentation/spritekit/skuniform/1455449-texturevalue)

|  | Declaration |
| --- | --- |
| From | ``` var textureValue: SKTexture! ``` |
| To | ``` var textureValue: SKTexture? ``` |

Modified [SKUniformType [enum]](https://developer.apple.com/documentation/spritekit/skuniformtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SKVideoNode](https://developer.apple.com/documentation/spritekit/skvideonode)

|  | Declaration |
| --- | --- |
| From | ``` class SKVideoNode : SKNode {     init!(AVPlayer player: AVPlayer!) -> SKVideoNode     class func videoNodeWithAVPlayer(_ player: AVPlayer!) -> SKVideoNode!     init!(videoFileNamed videoFile: String!) -> SKVideoNode     class func videoNodeWithVideoFileNamed(_ videoFile: String!) -> SKVideoNode!     init!(videoURL videoURL: NSURL!) -> SKVideoNode     class func videoNodeWithVideoURL(_ videoURL: NSURL!) -> SKVideoNode!     init!(AVPlayer player: AVPlayer!)     init!(videoFileNamed videoFile: String)     init!(videoURL url: NSURL)     init?(coder aDecoder: NSCoder)     func play()     func pause()     var size: CGSize     var anchorPoint: CGPoint } ``` |
| To | ``` class SKVideoNode : SKNode {      init(AVPlayer player: AVPlayer)     class func videoNodeWithAVPlayer(_ player: AVPlayer) -> SKVideoNode      init(videoFileNamed videoFile: String)     class func videoNodeWithVideoFileNamed(_ videoFile: String) -> SKVideoNode      init(fileNamed videoFile: String)     class func videoNodeWithFileNamed(_ videoFile: String) -> SKVideoNode      init(videoURL videoURL: NSURL)     class func videoNodeWithVideoURL(_ videoURL: NSURL) -> SKVideoNode      init(URL videoURL: NSURL)     class func videoNodeWithURL(_ videoURL: NSURL) -> SKVideoNode     init(AVPlayer player: AVPlayer)     init(videoFileNamed videoFile: String)     init(fileNamed videoFile: String)     init(videoURL url: NSURL)     init(URL url: NSURL)     init?(coder aDecoder: NSCoder)     func play()     func pause()     var size: CGSize     var anchorPoint: CGPoint } ``` |

Modified [SKVideoNode.init(AVPlayer: AVPlayer)](https://developer.apple.com/documentation/spritekit/skvideonode/1407900-initwithavplayer)

|  | Declaration |
| --- | --- |
| From | ``` init!(AVPlayer player: AVPlayer!) ``` |
| To | ``` init(AVPlayer player: AVPlayer) ``` |

Modified [SKVideoNode.init(videoFileNamed: String)](https://developer.apple.com/documentation/spritekit/skvideonode/1407918-initwithvideofilenamed)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init!(videoFileNamed videoFile: String) ``` | OS X 10.10 | -- |
| To | ``` init(videoFileNamed videoFile: String) ``` | OS X 10.8 | OS X 10.10 |

Modified [SKVideoNode.init(videoURL: NSURL)](https://developer.apple.com/documentation/spritekit/skvideonode/1407908-init)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init!(videoURL url: NSURL) ``` | OS X 10.10 | -- |
| To | ``` init(videoURL url: NSURL) ``` | OS X 10.8 | OS X 10.10 |

Modified [SKView](https://developer.apple.com/documentation/spritekit/skview)

|  | Declaration |
| --- | --- |
| From | ``` class SKView : NSView {     var paused: Bool     var showsFPS: Bool     var showsDrawCount: Bool     var showsNodeCount: Bool     var showsQuadCount: Bool     var showsPhysics: Bool     var showsFields: Bool     var asynchronous: Bool     var allowsTransparency: Bool     var ignoresSiblingOrder: Bool     var shouldCullNonVisibleNodes: Bool     var frameInterval: Int     func presentScene(_ scene: SKScene?)     func presentScene(_ scene: SKScene?, transition transition: SKTransition?)     var scene: SKScene? { get }     func textureFromNode(_ node: SKNode) -> SKTexture!     func textureFromNode(_ node: SKNode, crop crop: CGRect) -> SKTexture!     func convertPoint(_ point: CGPoint, toScene scene: SKScene) -> CGPoint     func convertPoint(_ point: CGPoint, fromScene scene: SKScene) -> CGPoint } ``` |
| To | ``` class SKView : NSView {     var paused: Bool     var showsFPS: Bool     var showsDrawCount: Bool     var showsNodeCount: Bool     var showsQuadCount: Bool     var showsPhysics: Bool     var showsFields: Bool     var asynchronous: Bool     var allowsTransparency: Bool     var ignoresSiblingOrder: Bool     var shouldCullNonVisibleNodes: Bool     var frameInterval: Int     func presentScene(_ scene: SKScene?)     func presentScene(_ scene: SKScene, transition transition: SKTransition)     var scene: SKScene? { get }     func textureFromNode(_ node: SKNode) -> SKTexture?     func textureFromNode(_ node: SKNode, crop crop: CGRect) -> SKTexture?     func convertPoint(_ point: CGPoint, toScene scene: SKScene) -> CGPoint     func convertPoint(_ point: CGPoint, fromScene scene: SKScene) -> CGPoint } ``` |

Modified [SKView.presentScene(_: SKScene, transition: SKTransition)](https://developer.apple.com/documentation/spritekit/skview/1520090-presentscene)

|  | Declaration |
| --- | --- |
| From | ``` func presentScene(_ scene: SKScene?, transition transition: SKTransition?) ``` |
| To | ``` func presentScene(_ scene: SKScene, transition transition: SKTransition) ``` |

Modified [SKView.textureFromNode(_: SKNode) -> SKTexture?](https://developer.apple.com/documentation/spritekit/skview/1520114-texture)

|  | Declaration |
| --- | --- |
| From | ``` func textureFromNode(_ node: SKNode) -> SKTexture! ``` |
| To | ``` func textureFromNode(_ node: SKNode) -> SKTexture? ``` |

Modified [SKView.textureFromNode(_: SKNode, crop: CGRect) -> SKTexture?](https://developer.apple.com/documentation/spritekit/skview/1519994-texturefromnode)

|  | Declaration |
| --- | --- |
| From | ``` func textureFromNode(_ node: SKNode, crop crop: CGRect) -> SKTexture! ``` |
| To | ``` func textureFromNode(_ node: SKNode, crop crop: CGRect) -> SKTexture? ``` |

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
