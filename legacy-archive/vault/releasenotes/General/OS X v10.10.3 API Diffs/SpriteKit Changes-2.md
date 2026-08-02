---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/SpriteKit.html
archived_at: '2026-07-18T02:52:40.756895Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# SpriteKit Changes

## SpriteKit

Removed SK3DNode.nodeWithViewportSize(CGSize) -> Self! [class]Removed SKMutableTexture.mutableTextureWithSize(CGSize) -> Self! [class]Removed SKNode.node() -> Self! [class]Removed SKNode.objectForKeyedSubscript(String!) -> [AnyObject]!Removed SKRange.rangeWithLowerLimit(CGFloat, upperLimit: CGFloat) -> Self! [class]Removed SKScene.sceneWithSize(CGSize) -> Self! [class]Removed SKShader.shaderWithSource(String!) -> Self! [class]Removed SKShader.shaderWithSource(String!, uniforms:[AnyObject]!) -> Self! [class]Removed SKShapeNode.getMirror() -> MirrorRemoved SKSpriteNode.getMirror() -> MirrorRemoved SKTexture.getMirror() -> MirrorRemoved SKTextureAtlas.getMirror() -> MirrorAdded NSEvent.locationInNode(SKNode!) -> CGPointAdded SK3DNode.init(coder: NSCoder)Added SK3DNode.pointOfViewAdded SK3DNode.scnSceneAdded SKKeyframeSequence.init(coder: NSCoder)Added SKNode.init(coder: NSCoder)Added SKShapeNode.getMirror() -> MirrorTypeAdded SKSpriteNode.init(coder: NSCoder)Added SKSpriteNode.getMirror() -> MirrorTypeAdded SKTexture.getMirror() -> MirrorTypeAdded SKTextureAtlas.getMirror() -> MirrorTypeAdded SKUniform.floatMatrix2ValueAdded SKUniform.floatMatrix3ValueAdded SKUniform.floatMatrix4ValueAdded SKUniform.floatVector2ValueAdded SKUniform.floatVector3ValueAdded SKUniform.floatVector4ValueAdded SKUniform.init(name: String!, floatMatrix2: GLKMatrix2)Added SKUniform.init(name: String!, floatMatrix3: GLKMatrix3)Added SKUniform.init(name: String!, floatMatrix4: GLKMatrix4)Added SKUniform.init(name: String!, floatVector2: GLKVector2)Added SKUniform.init(name: String!, floatVector3: GLKVector3)Added SKUniform.init(name: String!, floatVector4: GLKVector4)Added SKVideoNode.init(AVPlayer: AVPlayer!)Added SKVideoNode.init(coder: NSCoder)Added SKVideoNode.init(videoFileNamed: String)Added SKVideoNode.init(videoURL: NSURL)Modified SKAction.animateWithTextures([AnyObject], timePerFrame: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func animateWithTextures(_ textures: [AnyObject]!, timePerFrame sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func animateWithTextures(_ textures: [AnyObject], timePerFrame sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.animateWithTextures([AnyObject], timePerFrame: NSTimeInterval, resize: Bool, restore: Bool) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func animateWithTextures(_ textures: [AnyObject]!, timePerFrame sec: NSTimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction! ``` |
| To | ``` class func animateWithTextures(_ textures: [AnyObject], timePerFrame sec: NSTimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction ``` |

Modified SKAction.colorizeWithColor(NSColor, colorBlendFactor: CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func colorizeWithColor(_ color: NSColor!, colorBlendFactor colorBlendFactor: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func colorizeWithColor(_ color: NSColor, colorBlendFactor colorBlendFactor: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.colorizeWithColorBlendFactor(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func colorizeWithColorBlendFactor(_ colorBlendFactor: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func colorizeWithColorBlendFactor(_ colorBlendFactor: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.customActionWithDuration(NSTimeInterval, actionBlock:(SKNode!, CGFloat) -> Void) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: ((SKNode!, CGFloat) -> Void)!) -> SKAction! ``` |
| To | ``` class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SKNode!, CGFloat) -> Void) -> SKAction ``` |

Modified SKAction.fadeAlphaBy(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fadeAlphaBy(_ factor: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func fadeAlphaBy(_ factor: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.fadeAlphaTo(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fadeAlphaTo(_ alpha: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func fadeAlphaTo(_ alpha: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.fadeInWithDuration(NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fadeInWithDuration(_ sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func fadeInWithDuration(_ sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.fadeOutWithDuration(NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fadeOutWithDuration(_ sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func fadeOutWithDuration(_ sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.falloffBy(Float, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func falloffBy(_ falloff: Float, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func falloffBy(_ falloff: Float, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.falloffTo(Float, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func falloffTo(_ falloff: Float, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func falloffTo(_ falloff: Float, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.followPath(CGPath, asOffset: Bool, orientToPath: Bool, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func followPath(_ path: CGPath!, asOffset offset: Bool, orientToPath orient: Bool, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func followPath(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.followPath(CGPath, asOffset: Bool, orientToPath: Bool, speed: CGFloat) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func followPath(_ path: CGPath!, asOffset offset: Bool, orientToPath orient: Bool, speed speed: CGFloat) -> SKAction! ``` |
| To | ``` class func followPath(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, speed speed: CGFloat) -> SKAction ``` |

Modified SKAction.followPath(CGPath, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func followPath(_ path: CGPath!, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func followPath(_ path: CGPath, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.followPath(CGPath, speed: CGFloat) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func followPath(_ path: CGPath!, speed speed: CGFloat) -> SKAction! ``` |
| To | ``` class func followPath(_ path: CGPath, speed speed: CGFloat) -> SKAction ``` |

Modified SKAction.group([AnyObject]) -> SKAction! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func group(_ actions: [AnyObject]!) -> SKAction! ``` |
| To | ``` class func group(_ actions: [AnyObject]) -> SKAction! ``` |

Modified SKAction.hide() -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func hide() -> SKAction! ``` |
| To | ``` class func hide() -> SKAction ``` |

Modified SKAction.moveBy(CGVector, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func moveBy(_ delta: CGVector, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func moveBy(_ delta: CGVector, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.moveByX(CGFloat, y: CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func moveByX(_ deltaX: CGFloat, y deltaY: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func moveByX(_ deltaX: CGFloat, y deltaY: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.moveTo(CGPoint, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func moveTo(_ location: CGPoint, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func moveTo(_ location: CGPoint, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.moveToX(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func moveToX(_ x: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func moveToX(_ x: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.moveToY(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func moveToY(_ y: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func moveToY(_ y: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.playSoundFileNamed(String, waitForCompletion: Bool) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func playSoundFileNamed(_ soundFile: String!, waitForCompletion wait: Bool) -> SKAction! ``` |
| To | ``` class func playSoundFileNamed(_ soundFile: String, waitForCompletion wait: Bool) -> SKAction ``` |

Modified SKAction.reachTo(CGPoint, rootNode: SKNode, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func reachTo(_ position: CGPoint, rootNode root: SKNode!, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func reachTo(_ position: CGPoint, rootNode root: SKNode, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.reachTo(CGPoint, rootNode: SKNode, velocity: CGFloat) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func reachTo(_ position: CGPoint, rootNode root: SKNode!, velocity velocity: CGFloat) -> SKAction! ``` |
| To | ``` class func reachTo(_ position: CGPoint, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction ``` |

Modified SKAction.reachToNode(SKNode, rootNode: SKNode, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func reachToNode(_ node: SKNode!, rootNode root: SKNode!, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func reachToNode(_ node: SKNode, rootNode root: SKNode, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.reachToNode(SKNode, rootNode: SKNode, velocity: CGFloat) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func reachToNode(_ node: SKNode!, rootNode root: SKNode!, velocity velocity: CGFloat) -> SKAction! ``` |
| To | ``` class func reachToNode(_ node: SKNode, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction ``` |

Modified SKAction.removeFromParent() -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func removeFromParent() -> SKAction! ``` |
| To | ``` class func removeFromParent() -> SKAction ``` |

Modified SKAction.repeatAction(SKAction, count: Int) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func repeatAction(_ action: SKAction!, count count: Int) -> SKAction! ``` |
| To | ``` class func repeatAction(_ action: SKAction, count count: Int) -> SKAction ``` |

Modified SKAction.repeatActionForever(SKAction) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func repeatActionForever(_ action: SKAction!) -> SKAction! ``` |
| To | ``` class func repeatActionForever(_ action: SKAction) -> SKAction ``` |

Modified SKAction.resizeByWidth(CGFloat, height: CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func resizeByWidth(_ width: CGFloat, height height: CGFloat, duration duration: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func resizeByWidth(_ width: CGFloat, height height: CGFloat, duration duration: NSTimeInterval) -> SKAction ``` |

Modified SKAction.resizeToHeight(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func resizeToHeight(_ height: CGFloat, duration duration: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func resizeToHeight(_ height: CGFloat, duration duration: NSTimeInterval) -> SKAction ``` |

Modified SKAction.resizeToWidth(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func resizeToWidth(_ width: CGFloat, duration duration: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func resizeToWidth(_ width: CGFloat, duration duration: NSTimeInterval) -> SKAction ``` |

Modified SKAction.resizeToWidth(CGFloat, height: CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func resizeToWidth(_ width: CGFloat, height height: CGFloat, duration duration: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func resizeToWidth(_ width: CGFloat, height height: CGFloat, duration duration: NSTimeInterval) -> SKAction ``` |

Modified SKAction.reversedAction() -> SKAction

|  | Declaration |
| --- | --- |
| From | ``` func reversedAction() -> SKAction! ``` |
| To | ``` func reversedAction() -> SKAction ``` |

Modified SKAction.rotateByAngle(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func rotateByAngle(_ radians: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func rotateByAngle(_ radians: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.rotateToAngle(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func rotateToAngle(_ radians: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func rotateToAngle(_ radians: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.rotateToAngle(CGFloat, duration: NSTimeInterval, shortestUnitArc: Bool) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func rotateToAngle(_ radians: CGFloat, duration sec: NSTimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SKAction! ``` |
| To | ``` class func rotateToAngle(_ radians: CGFloat, duration sec: NSTimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SKAction ``` |

Modified SKAction.runAction(SKAction, onChildWithName: String) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func runAction(_ action: SKAction!, onChildWithName name: String!) -> SKAction! ``` |
| To | ``` class func runAction(_ action: SKAction, onChildWithName name: String) -> SKAction ``` |

Modified SKAction.runBlock(dispatch_block_t) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func runBlock(_ block: dispatch_block_t!) -> SKAction! ``` |
| To | ``` class func runBlock(_ block: dispatch_block_t) -> SKAction ``` |

Modified SKAction.runBlock(dispatch_block_t, queue: dispatch_queue_t?) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func runBlock(_ block: dispatch_block_t!, queue queue: dispatch_queue_t!) -> SKAction! ``` |
| To | ``` class func runBlock(_ block: dispatch_block_t, queue queue: dispatch_queue_t?) -> SKAction ``` |

Modified SKAction.scaleBy(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func scaleBy(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func scaleBy(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.scaleTo(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func scaleTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func scaleTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.scaleXBy(CGFloat, y: CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func scaleXBy(_ xScale: CGFloat, y yScale: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func scaleXBy(_ xScale: CGFloat, y yScale: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.scaleXTo(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func scaleXTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func scaleXTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.scaleXTo(CGFloat, y: CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func scaleXTo(_ xScale: CGFloat, y yScale: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func scaleXTo(_ xScale: CGFloat, y yScale: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.scaleYTo(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func scaleYTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func scaleYTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.sequence([AnyObject]) -> SKAction! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func sequence(_ actions: [AnyObject]!) -> SKAction! ``` |
| To | ``` class func sequence(_ actions: [AnyObject]) -> SKAction! ``` |

Modified SKAction.setTexture(SKTexture) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setTexture(_ texture: SKTexture!) -> SKAction! ``` |
| To | ``` class func setTexture(_ texture: SKTexture) -> SKAction ``` |

Modified SKAction.setTexture(SKTexture, resize: Bool) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setTexture(_ texture: SKTexture!, resize resize: Bool) -> SKAction! ``` |
| To | ``` class func setTexture(_ texture: SKTexture, resize resize: Bool) -> SKAction ``` |

Modified SKAction.speedBy(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func speedBy(_ speed: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func speedBy(_ speed: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.speedTo(CGFloat, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func speedTo(_ speed: CGFloat, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func speedTo(_ speed: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.strengthBy(Float, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func strengthBy(_ strength: Float, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func strengthBy(_ strength: Float, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.strengthTo(Float, duration: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func strengthTo(_ strength: Float, duration sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func strengthTo(_ strength: Float, duration sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.timingFunction

|  | Declaration |
| --- | --- |
| From | ``` var timingFunction: SKActionTimingFunction! ``` |
| To | ``` var timingFunction: SKActionTimingFunction? ``` |

Modified SKAction.unhide() -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func unhide() -> SKAction! ``` |
| To | ``` class func unhide() -> SKAction ``` |

Modified SKAction.waitForDuration(NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func waitForDuration(_ sec: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func waitForDuration(_ sec: NSTimeInterval) -> SKAction ``` |

Modified SKAction.waitForDuration(NSTimeInterval, withRange: NSTimeInterval) -> SKAction [class]

|  | Declaration |
| --- | --- |
| From | ``` class func waitForDuration(_ sec: NSTimeInterval, withRange durationRange: NSTimeInterval) -> SKAction! ``` |
| To | ``` class func waitForDuration(_ sec: NSTimeInterval, withRange durationRange: NSTimeInterval) -> SKAction ``` |

Modified SKActionTimingMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SKBlendMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SKConstraint.distance(SKRange!, toNode: SKNode!) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func distance(_ range: SKRange!, toNode node: SKNode!) -> Self! ``` | OS X 10.10 |
| To | ``` class func distance(_ range: SKRange!, toNode node: SKNode!) -> Self ``` | OS X 10.10.3 |

Modified SKConstraint.distance(SKRange, toPoint: CGPoint) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func distance(_ range: SKRange!, toPoint point: CGPoint) -> Self! ``` | OS X 10.10 |
| To | ``` class func distance(_ range: SKRange, toPoint point: CGPoint) -> Self ``` | OS X 10.10.3 |

Modified SKConstraint.distance(SKRange, toPoint: CGPoint, inNode: SKNode) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func distance(_ range: SKRange!, toPoint point: CGPoint, inNode node: SKNode!) -> Self! ``` | OS X 10.10 |
| To | ``` class func distance(_ range: SKRange, toPoint point: CGPoint, inNode node: SKNode) -> Self ``` | OS X 10.10.3 |

Modified SKConstraint.orientToNode(SKNode, offset: SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func orientToNode(_ node: SKNode!, offset radians: SKRange!) -> Self! ``` | OS X 10.10 |
| To | ``` class func orientToNode(_ node: SKNode, offset radians: SKRange) -> Self ``` | OS X 10.10.3 |

Modified SKConstraint.orientToPoint(CGPoint, inNode: SKNode, offset: SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func orientToPoint(_ point: CGPoint, inNode node: SKNode!, offset radians: SKRange!) -> Self! ``` | OS X 10.10 |
| To | ``` class func orientToPoint(_ point: CGPoint, inNode node: SKNode, offset radians: SKRange) -> Self ``` | OS X 10.10.3 |

Modified SKConstraint.orientToPoint(CGPoint, offset: SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func orientToPoint(_ point: CGPoint, offset radians: SKRange!) -> Self! ``` | OS X 10.10 |
| To | ``` class func orientToPoint(_ point: CGPoint, offset radians: SKRange) -> Self ``` | OS X 10.10.3 |

Modified SKConstraint.positionX(SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func positionX(_ range: SKRange!) -> Self! ``` | OS X 10.10 |
| To | ``` class func positionX(_ range: SKRange) -> Self ``` | OS X 10.10.3 |

Modified SKConstraint.positionX(SKRange, y: SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func positionX(_ xRange: SKRange!, y yRange: SKRange!) -> Self! ``` | OS X 10.10 |
| To | ``` class func positionX(_ xRange: SKRange, y yRange: SKRange) -> Self ``` | OS X 10.10.3 |

Modified SKConstraint.positionY(SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func positionY(_ range: SKRange!) -> Self! ``` | OS X 10.10 |
| To | ``` class func positionY(_ range: SKRange) -> Self ``` | OS X 10.10.3 |

Modified SKConstraint.referenceNode

|  | Declaration |
| --- | --- |
| From | ``` var referenceNode: SKNode! ``` |
| To | ``` var referenceNode: SKNode? ``` |

Modified SKConstraint.zRotation(SKRange) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func zRotation(_ zRange: SKRange!) -> Self! ``` | OS X 10.10 |
| To | ``` class func zRotation(_ zRange: SKRange) -> Self ``` | OS X 10.10.3 |

Modified SKCropNode.maskNode

|  | Declaration |
| --- | --- |
| From | ``` var maskNode: SKNode! ``` |
| To | ``` var maskNode: SKNode? ``` |

Modified SKEffectNode.filter

|  | Declaration |
| --- | --- |
| From | ``` var filter: CIFilter! ``` |
| To | ``` var filter: CIFilter? ``` |

Modified SKEffectNode.shader

|  | Declaration |
| --- | --- |
| From | ``` var shader: SKShader! ``` |
| To | ``` var shader: SKShader? ``` |

Modified SKEmitterNode.particleAction

|  | Declaration |
| --- | --- |
| From | ``` var particleAction: SKAction! ``` |
| To | ``` @NSCopying var particleAction: SKAction? ``` |

Modified SKEmitterNode.particleAlphaSequence

|  | Declaration |
| --- | --- |
| From | ``` var particleAlphaSequence: SKKeyframeSequence! ``` |
| To | ``` var particleAlphaSequence: SKKeyframeSequence? ``` |

Modified SKEmitterNode.particleColorBlendFactorSequence

|  | Declaration |
| --- | --- |
| From | ``` var particleColorBlendFactorSequence: SKKeyframeSequence! ``` |
| To | ``` var particleColorBlendFactorSequence: SKKeyframeSequence? ``` |

Modified SKEmitterNode.particleColorSequence

|  | Declaration |
| --- | --- |
| From | ``` var particleColorSequence: SKKeyframeSequence! ``` |
| To | ``` var particleColorSequence: SKKeyframeSequence? ``` |

Modified SKEmitterNode.particleScaleSequence

|  | Declaration |
| --- | --- |
| From | ``` var particleScaleSequence: SKKeyframeSequence! ``` |
| To | ``` var particleScaleSequence: SKKeyframeSequence? ``` |

Modified SKEmitterNode.particleTexture

|  | Declaration |
| --- | --- |
| From | ``` var particleTexture: SKTexture! ``` |
| To | ``` var particleTexture: SKTexture? ``` |

Modified SKEmitterNode.shader

|  | Declaration |
| --- | --- |
| From | ``` var shader: SKShader! ``` |
| To | ``` var shader: SKShader? ``` |

Modified SKEmitterNode.targetNode

|  | Declaration |
| --- | --- |
| From | ``` var targetNode: SKNode! ``` |
| To | ``` weak var targetNode: SKNode? ``` |

Modified SKFieldNode.dragField() -> SKFieldNode [class]

|  | Declaration |
| --- | --- |
| From | ``` class func dragField() -> SKFieldNode! ``` |
| To | ``` class func dragField() -> SKFieldNode ``` |

Modified SKFieldNode.electricField() -> SKFieldNode [class]

|  | Declaration |
| --- | --- |
| From | ``` class func electricField() -> SKFieldNode! ``` |
| To | ``` class func electricField() -> SKFieldNode ``` |

Modified SKFieldNode.magneticField() -> SKFieldNode [class]

|  | Declaration |
| --- | --- |
| From | ``` class func magneticField() -> SKFieldNode! ``` |
| To | ``` class func magneticField() -> SKFieldNode ``` |

Modified SKFieldNode.noiseFieldWithSmoothness(CGFloat, animationSpeed: CGFloat) -> SKFieldNode [class]

|  | Declaration |
| --- | --- |
| From | ``` class func noiseFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode! ``` |
| To | ``` class func noiseFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode ``` |

Modified SKFieldNode.radialGravityField() -> SKFieldNode [class]

|  | Declaration |
| --- | --- |
| From | ``` class func radialGravityField() -> SKFieldNode! ``` |
| To | ``` class func radialGravityField() -> SKFieldNode ``` |

Modified SKFieldNode.springField() -> SKFieldNode [class]

|  | Declaration |
| --- | --- |
| From | ``` class func springField() -> SKFieldNode! ``` |
| To | ``` class func springField() -> SKFieldNode ``` |

Modified SKFieldNode.turbulenceFieldWithSmoothness(CGFloat, animationSpeed: CGFloat) -> SKFieldNode [class]

|  | Declaration |
| --- | --- |
| From | ``` class func turbulenceFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode! ``` |
| To | ``` class func turbulenceFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode ``` |

Modified SKFieldNode.velocityFieldWithTexture(SKTexture) -> SKFieldNode [class]

|  | Declaration |
| --- | --- |
| From | ``` class func velocityFieldWithTexture(_ velocityTexture: SKTexture!) -> SKFieldNode! ``` |
| To | ``` class func velocityFieldWithTexture(_ velocityTexture: SKTexture) -> SKFieldNode ``` |

Modified SKFieldNode.vortexField() -> SKFieldNode [class]

|  | Declaration |
| --- | --- |
| From | ``` class func vortexField() -> SKFieldNode! ``` |
| To | ``` class func vortexField() -> SKFieldNode ``` |

Modified SKKeyframeSequence.addKeyframeValue(AnyObject, time: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` func addKeyframeValue(_ value: AnyObject!, time time: CGFloat) ``` |
| To | ``` func addKeyframeValue(_ value: AnyObject, time time: CGFloat) ``` |

Modified SKKeyframeSequence.getKeyframeValueForIndex(Int) -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func getKeyframeValueForIndex(_ index: Int) -> AnyObject! ``` |
| To | ``` func getKeyframeValueForIndex(_ index: Int) -> AnyObject ``` |

Modified SKKeyframeSequence.init(keyframeValues: [AnyObject], times:[AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(keyframeValues values: [AnyObject]!, times times: [AnyObject]!) ``` |
| To | ``` init!(keyframeValues values: [AnyObject], times times: [AnyObject]) ``` |

Modified SKKeyframeSequence.setKeyframeValue(AnyObject, forIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func setKeyframeValue(_ value: AnyObject!, forIndex index: Int) ``` |
| To | ``` func setKeyframeValue(_ value: AnyObject, forIndex index: Int) ``` |

Modified SKKeyframeSequence.setKeyframeValue(AnyObject, time: CGFloat, forIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func setKeyframeValue(_ value: AnyObject!, time time: CGFloat, forIndex index: Int) ``` |
| To | ``` func setKeyframeValue(_ value: AnyObject, time time: CGFloat, forIndex index: Int) ``` |

Modified SKLabelHorizontalAlignmentMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SKLabelNode.color

|  | Declaration |
| --- | --- |
| From | ``` var color: NSColor! ``` |
| To | ``` var color: NSColor? ``` |

Modified SKLabelNode.fontColor

|  | Declaration |
| --- | --- |
| From | ``` var fontColor: NSColor! ``` |
| To | ``` var fontColor: NSColor ``` |

Modified SKLabelNode.text

|  | Declaration |
| --- | --- |
| From | ``` var text: String! ``` |
| To | ``` var text: String ``` |

Modified SKLabelNode.init(text: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(text text: String!) ``` |
| To | ``` convenience init(text text: String) ``` |

Modified SKLabelVerticalAlignmentMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SKLightNode.lightColor

|  | Declaration |
| --- | --- |
| From | ``` var lightColor: NSColor! ``` |
| To | ``` var lightColor: NSColor ``` |

Modified SKMutableTexture.modifyPixelDataWithBlock((UnsafeMutablePointer<Void>, Int) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func modifyPixelDataWithBlock(_ block: ((UnsafePointer<()>, UInt) -> Void)!) ``` | OS X 10.10 |
| To | ``` func modifyPixelDataWithBlock(_ block: (UnsafeMutablePointer<Void>, Int) -> Void) ``` | OS X 10.10.3 |

Modified SKNode.actionForKey(String) -> SKAction?

|  | Declaration |
| --- | --- |
| From | ``` func actionForKey(_ key: String!) -> SKAction! ``` |
| To | ``` func actionForKey(_ key: String) -> SKAction? ``` |

Modified SKNode.addChild(SKNode)

|  | Declaration |
| --- | --- |
| From | ``` func addChild(_ node: SKNode!) ``` |
| To | ``` func addChild(_ node: SKNode) ``` |

Modified SKNode.childNodeWithName(String) -> SKNode?

|  | Declaration |
| --- | --- |
| From | ``` func childNodeWithName(_ name: String!) -> SKNode! ``` |
| To | ``` func childNodeWithName(_ name: String) -> SKNode? ``` |

Modified SKNode.children

|  | Declaration |
| --- | --- |
| From | ``` var children: [AnyObject]! { get } ``` |
| To | ``` var children: [AnyObject] { get } ``` |

Modified SKNode.constraints

|  | Declaration |
| --- | --- |
| From | ``` var constraints: [AnyObject]! ``` |
| To | ``` var constraints: [AnyObject]? ``` |

Modified SKNode.convertPoint(CGPoint, fromNode: SKNode) -> CGPoint

|  | Declaration |
| --- | --- |
| From | ``` func convertPoint(_ point: CGPoint, fromNode node: SKNode!) -> CGPoint ``` |
| To | ``` func convertPoint(_ point: CGPoint, fromNode node: SKNode) -> CGPoint ``` |

Modified SKNode.convertPoint(CGPoint, toNode: SKNode) -> CGPoint

|  | Declaration |
| --- | --- |
| From | ``` func convertPoint(_ point: CGPoint, toNode node: SKNode!) -> CGPoint ``` |
| To | ``` func convertPoint(_ point: CGPoint, toNode node: SKNode) -> CGPoint ``` |

Modified SKNode.enumerateChildNodesWithName(String, usingBlock:((SKNode!, UnsafeMutablePointer<ObjCBool>) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateChildNodesWithName(_ name: String!, usingBlock block: ((SKNode!, UnsafePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateChildNodesWithName(_ name: String, usingBlock block: ((SKNode!, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |

Modified SKNode.init(fileNamed: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fileNamed filename: String!) ``` |
| To | ``` convenience init!(fileNamed filename: String) ``` |

Modified SKNode.inParentHierarchy(SKNode) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func inParentHierarchy(_ parent: SKNode!) -> Bool ``` |
| To | ``` func inParentHierarchy(_ parent: SKNode) -> Bool ``` |

Modified SKNode.intersectsNode(SKNode) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func intersectsNode(_ node: SKNode!) -> Bool ``` |
| To | ``` func intersectsNode(_ node: SKNode) -> Bool ``` |

Modified SKNode.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified SKNode.nodeAtPoint(CGPoint) -> SKNode

|  | Declaration |
| --- | --- |
| From | ``` func nodeAtPoint(_ p: CGPoint) -> SKNode! ``` |
| To | ``` func nodeAtPoint(_ p: CGPoint) -> SKNode ``` |

Modified SKNode.nodesAtPoint(CGPoint) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func nodesAtPoint(_ p: CGPoint) -> [AnyObject]! ``` |
| To | ``` func nodesAtPoint(_ p: CGPoint) -> [AnyObject] ``` |

Modified SKNode.parent

|  | Declaration |
| --- | --- |
| From | ``` var parent: SKNode! { get } ``` |
| To | ``` var parent: SKNode? { get } ``` |

Modified SKNode.physicsBody

|  | Declaration |
| --- | --- |
| From | ``` var physicsBody: SKPhysicsBody! ``` |
| To | ``` var physicsBody: SKPhysicsBody? ``` |

Modified SKNode.reachConstraints

|  | Declaration |
| --- | --- |
| From | ``` var reachConstraints: SKReachConstraints! ``` |
| To | ``` @NSCopying var reachConstraints: SKReachConstraints? ``` |

Modified SKNode.runAction(SKAction, withKey: String!)

|  | Declaration |
| --- | --- |
| From | ``` func runAction(_ action: SKAction!, withKey key: String!) ``` |
| To | ``` func runAction(_ action: SKAction, withKey key: String!) ``` |

Modified SKNode.scene

|  | Declaration |
| --- | --- |
| From | ``` var scene: SKScene! { get } ``` |
| To | ``` var scene: SKScene? { get } ``` |

Modified SKNode.userData

|  | Declaration |
| --- | --- |
| From | ``` var userData: NSMutableDictionary! ``` |
| To | ``` var userData: NSMutableDictionary? ``` |

Modified SKPhysicsBody.allContactedBodies() -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func allContactedBodies() -> [AnyObject]! ``` |
| To | ``` func allContactedBodies() -> [AnyObject] ``` |

Modified SKPhysicsBody.init(bodies: [AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(bodies bodies: [AnyObject]!) -> SKPhysicsBody ``` |
| To | ``` init(bodies bodies: [AnyObject]) -> SKPhysicsBody ``` |

Modified SKPhysicsBody.joints

|  | Declaration |
| --- | --- |
| From | ``` var joints: [AnyObject]! { get } ``` |
| To | ``` var joints: [AnyObject] { get } ``` |

Modified SKPhysicsBody.node

|  | Declaration |
| --- | --- |
| From | ``` var node: SKNode! { get } ``` |
| To | ``` weak var node: SKNode? { get } ``` |

Modified SKPhysicsBody.init(polygonFromPath: CGPath!)

|  | Declaration |
| --- | --- |
| From | ``` init(polygonFromPath path: CGPath!) -> SKPhysicsBody ``` |
| To | ``` init!(polygonFromPath path: CGPath!) -> SKPhysicsBody ``` |

Modified SKPhysicsBody.init(rectangleOfSize: CGSize)

|  | Declaration |
| --- | --- |
| From | ``` init(rectangleOfSize s: CGSize) -> SKPhysicsBody ``` |
| To | ``` init!(rectangleOfSize s: CGSize) -> SKPhysicsBody ``` |

Modified SKPhysicsBody.init(rectangleOfSize: CGSize, center: CGPoint)

|  | Declaration |
| --- | --- |
| From | ``` init(rectangleOfSize s: CGSize, center center: CGPoint) -> SKPhysicsBody ``` |
| To | ``` init!(rectangleOfSize s: CGSize, center center: CGPoint) -> SKPhysicsBody ``` |

Modified SKPhysicsBody.init(texture: SKTexture!, alphaThreshold: Float, size: CGSize)

|  | Declaration |
| --- | --- |
| From | ``` init(texture texture: SKTexture!, alphaThreshold alphaThreshold: Float, size size: CGSize) -> SKPhysicsBody ``` |
| To | ``` init!(texture texture: SKTexture!, alphaThreshold alphaThreshold: Float, size size: CGSize) -> SKPhysicsBody ``` |

Modified SKPhysicsBody.init(texture: SKTexture!, size: CGSize)

|  | Declaration |
| --- | --- |
| From | ``` init(texture texture: SKTexture!, size size: CGSize) -> SKPhysicsBody ``` |
| To | ``` init!(texture texture: SKTexture!, size size: CGSize) -> SKPhysicsBody ``` |

Modified SKPhysicsContactDelegate.didBeginContact(SKPhysicsContact)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func didBeginContact(_ contact: SKPhysicsContact!) ``` | -- |
| To | ``` optional func didBeginContact(_ contact: SKPhysicsContact) ``` | yes |

Modified SKPhysicsContactDelegate.didEndContact(SKPhysicsContact)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func didEndContact(_ contact: SKPhysicsContact!) ``` | -- |
| To | ``` optional func didEndContact(_ contact: SKPhysicsContact) ``` | yes |

Modified SKPhysicsWorld.addJoint(SKPhysicsJoint)

|  | Declaration |
| --- | --- |
| From | ``` func addJoint(_ joint: SKPhysicsJoint!) ``` |
| To | ``` func addJoint(_ joint: SKPhysicsJoint) ``` |

Modified SKPhysicsWorld.bodyAlongRayStart(CGPoint, end: CGPoint) -> SKPhysicsBody?

|  | Declaration |
| --- | --- |
| From | ``` func bodyAlongRayStart(_ start: CGPoint, end end: CGPoint) -> SKPhysicsBody! ``` |
| To | ``` func bodyAlongRayStart(_ start: CGPoint, end end: CGPoint) -> SKPhysicsBody? ``` |

Modified SKPhysicsWorld.bodyAtPoint(CGPoint) -> SKPhysicsBody?

|  | Declaration |
| --- | --- |
| From | ``` func bodyAtPoint(_ point: CGPoint) -> SKPhysicsBody! ``` |
| To | ``` func bodyAtPoint(_ point: CGPoint) -> SKPhysicsBody? ``` |

Modified SKPhysicsWorld.bodyInRect(CGRect) -> SKPhysicsBody?

|  | Declaration |
| --- | --- |
| From | ``` func bodyInRect(_ rect: CGRect) -> SKPhysicsBody! ``` |
| To | ``` func bodyInRect(_ rect: CGRect) -> SKPhysicsBody? ``` |

Modified SKPhysicsWorld.contactDelegate

|  | Declaration |
| --- | --- |
| From | ``` var contactDelegate: SKPhysicsContactDelegate! ``` |
| To | ``` unowned(unsafe) var contactDelegate: SKPhysicsContactDelegate! ``` |

Modified SKPhysicsWorld.enumerateBodiesAlongRayStart(CGPoint, end: CGPoint, usingBlock:((SKPhysicsBody!, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateBodiesAlongRayStart(_ start: CGPoint, end end: CGPoint, usingBlock block: ((SKPhysicsBody!, CGPoint, CGVector, UnsafePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateBodiesAlongRayStart(_ start: CGPoint, end end: CGPoint, usingBlock block: ((SKPhysicsBody!, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |

Modified SKPhysicsWorld.enumerateBodiesAtPoint(CGPoint, usingBlock:((SKPhysicsBody!, UnsafeMutablePointer<ObjCBool>) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateBodiesAtPoint(_ point: CGPoint, usingBlock block: ((SKPhysicsBody!, UnsafePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateBodiesAtPoint(_ point: CGPoint, usingBlock block: ((SKPhysicsBody!, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |

Modified SKPhysicsWorld.enumerateBodiesInRect(CGRect, usingBlock:((SKPhysicsBody!, UnsafeMutablePointer<ObjCBool>) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateBodiesInRect(_ rect: CGRect, usingBlock block: ((SKPhysicsBody!, UnsafePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateBodiesInRect(_ rect: CGRect, usingBlock block: ((SKPhysicsBody!, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |

Modified SKPhysicsWorld.removeJoint(SKPhysicsJoint)

|  | Declaration |
| --- | --- |
| From | ``` func removeJoint(_ joint: SKPhysicsJoint!) ``` |
| To | ``` func removeJoint(_ joint: SKPhysicsJoint) ``` |

Modified SKRange.rangeWithNoLimits() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func rangeWithNoLimits() -> Self! ``` | OS X 10.10 |
| To | ``` class func rangeWithNoLimits() -> Self ``` | OS X 10.10.3 |

Modified SKRegion.infiniteRegion() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func infiniteRegion() -> Self! ``` | OS X 10.10 |
| To | ``` class func infiniteRegion() -> Self ``` | OS X 10.10.3 |

Modified SKRegion.inverseRegion() -> Self

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func inverseRegion() -> Self! ``` | OS X 10.10 |
| To | ``` func inverseRegion() -> Self ``` | OS X 10.10.3 |

Modified SKRegion.path

|  | Declaration |
| --- | --- |
| From | ``` var path: CGPath! { get } ``` |
| To | ``` var path: CGPath? { get } ``` |

Modified SKRegion.regionByDifferenceFromRegion(SKRegion) -> Self

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func regionByDifferenceFromRegion(_ region: SKRegion!) -> Self! ``` | OS X 10.10 |
| To | ``` func regionByDifferenceFromRegion(_ region: SKRegion) -> Self ``` | OS X 10.10.3 |

Modified SKScene.backgroundColor

|  | Declaration |
| --- | --- |
| From | ``` var backgroundColor: NSColor! ``` |
| To | ``` var backgroundColor: NSColor ``` |

Modified SKScene.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: SKSceneDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: SKSceneDelegate? ``` |

Modified SKScene.didMoveToView(SKView)

|  | Declaration |
| --- | --- |
| From | ``` func didMoveToView(_ view: SKView!) ``` |
| To | ``` func didMoveToView(_ view: SKView) ``` |

Modified SKScene.physicsWorld

|  | Declaration |
| --- | --- |
| From | ``` var physicsWorld: SKPhysicsWorld! { get } ``` |
| To | ``` var physicsWorld: SKPhysicsWorld { get } ``` |

Modified SKScene.view

|  | Declaration |
| --- | --- |
| From | ``` var view: SKView! { get } ``` |
| To | ``` weak var view: SKView? { get } ``` |

Modified SKScene.willMoveFromView(SKView)

|  | Declaration |
| --- | --- |
| From | ``` func willMoveFromView(_ view: SKView!) ``` |
| To | ``` func willMoveFromView(_ view: SKView) ``` |

Modified SKSceneDelegate.didApplyConstraintsForScene(SKScene)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func didApplyConstraintsForScene(_ scene: SKScene!) ``` | -- |
| To | ``` optional func didApplyConstraintsForScene(_ scene: SKScene) ``` | yes |

Modified SKSceneDelegate.didEvaluateActionsForScene(SKScene)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func didEvaluateActionsForScene(_ scene: SKScene!) ``` | -- |
| To | ``` optional func didEvaluateActionsForScene(_ scene: SKScene) ``` | yes |

Modified SKSceneDelegate.didFinishUpdateForScene(SKScene)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func didFinishUpdateForScene(_ scene: SKScene!) ``` | -- |
| To | ``` optional func didFinishUpdateForScene(_ scene: SKScene) ``` | yes |

Modified SKSceneDelegate.didSimulatePhysicsForScene(SKScene)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func didSimulatePhysicsForScene(_ scene: SKScene!) ``` | -- |
| To | ``` optional func didSimulatePhysicsForScene(_ scene: SKScene) ``` | yes |

Modified SKSceneDelegate.update(NSTimeInterval, forScene: SKScene)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func update(_ currentTime: NSTimeInterval, forScene scene: SKScene!) ``` | -- |
| To | ``` optional func update(_ currentTime: NSTimeInterval, forScene scene: SKScene) ``` | yes |

Modified SKSceneScaleMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SKShader.addUniform(SKUniform)

|  | Declaration |
| --- | --- |
| From | ``` func addUniform(_ uniform: SKUniform!) ``` |
| To | ``` func addUniform(_ uniform: SKUniform) ``` |

Modified SKShader.init(fileNamed: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fileNamed name: String!) ``` |
| To | ``` convenience init!(fileNamed name: String) ``` |

Modified SKShader.removeUniformNamed(String)

|  | Declaration |
| --- | --- |
| From | ``` func removeUniformNamed(_ name: String!) ``` |
| To | ``` func removeUniformNamed(_ name: String) ``` |

Modified SKShader.uniformNamed(String) -> SKUniform?

|  | Declaration |
| --- | --- |
| From | ``` func uniformNamed(_ name: String!) -> SKUniform! ``` |
| To | ``` func uniformNamed(_ name: String) -> SKUniform? ``` |

Modified SKShader.uniforms

|  | Declaration |
| --- | --- |
| From | ``` var uniforms: [AnyObject]! ``` |
| To | ``` var uniforms: [AnyObject] ``` |

Modified SKShapeNode.fillColor

|  | Declaration |
| --- | --- |
| From | ``` var fillColor: NSColor! ``` |
| To | ``` var fillColor: NSColor ``` |

Modified SKShapeNode.fillShader

|  | Declaration |
| --- | --- |
| From | ``` var fillShader: SKShader! ``` |
| To | ``` var fillShader: SKShader? ``` |

Modified SKShapeNode.fillTexture

|  | Declaration |
| --- | --- |
| From | ``` var fillTexture: SKTexture! ``` |
| To | ``` var fillTexture: SKTexture? ``` |

Modified SKShapeNode.init(points: UnsafeMutablePointer<CGPoint>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(points points: UnsafePointer<CGPoint>, count numPoints: UInt) ``` |
| To | ``` convenience init(points points: UnsafeMutablePointer<CGPoint>, count numPoints: Int) ``` |

Modified SKShapeNode.init(splinePoints: UnsafeMutablePointer<CGPoint>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(splinePoints points: UnsafePointer<CGPoint>, count numPoints: UInt) ``` |
| To | ``` convenience init(splinePoints points: UnsafeMutablePointer<CGPoint>, count numPoints: Int) ``` |

Modified SKShapeNode.strokeColor

|  | Declaration |
| --- | --- |
| From | ``` var strokeColor: NSColor! ``` |
| To | ``` var strokeColor: NSColor ``` |

Modified SKShapeNode.strokeShader

|  | Declaration |
| --- | --- |
| From | ``` var strokeShader: SKShader! ``` |
| To | ``` var strokeShader: SKShader? ``` |

Modified SKShapeNode.strokeTexture

|  | Declaration |
| --- | --- |
| From | ``` var strokeTexture: SKTexture! ``` |
| To | ``` var strokeTexture: SKTexture? ``` |

Modified SKSpriteNode.color

|  | Declaration |
| --- | --- |
| From | ``` var color: NSColor! ``` |
| To | ``` var color: NSColor ``` |

Modified SKSpriteNode.init(imageNamed: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(imageNamed name: String!) ``` |
| To | ``` convenience init(imageNamed name: String) ``` |

Modified SKSpriteNode.init(imageNamed: String, normalMapped: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(imageNamed name: String!, normalMapped generateNormalMap: Bool) ``` |
| To | ``` convenience init(imageNamed name: String, normalMapped generateNormalMap: Bool) ``` |

Modified SKSpriteNode.normalTexture

|  | Declaration |
| --- | --- |
| From | ``` var normalTexture: SKTexture! ``` |
| To | ``` var normalTexture: SKTexture? ``` |

Modified SKSpriteNode.shader

|  | Declaration |
| --- | --- |
| From | ``` var shader: SKShader! ``` |
| To | ``` var shader: SKShader? ``` |

Modified SKSpriteNode.texture

|  | Declaration |
| --- | --- |
| From | ``` var texture: SKTexture! ``` |
| To | ``` var texture: SKTexture? ``` |

Modified SKSpriteNode.init(texture: SKTexture!, normalMap: SKTexture?)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(texture texture: SKTexture!, normalMap normalMap: SKTexture!) ``` |
| To | ``` convenience init(texture texture: SKTexture!, normalMap normalMap: SKTexture?) ``` |

Modified SKTexture.init(data: NSData!, size: CGSize)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data pixelData: NSData!, size size: CGSize) ``` |
| To | ``` convenience init!(data pixelData: NSData!, size size: CGSize) ``` |

Modified SKTexture.init(data: NSData!, size: CGSize, flipped: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data pixelData: NSData!, size size: CGSize, flipped flipped: Bool) ``` |
| To | ``` convenience init!(data pixelData: NSData!, size size: CGSize, flipped flipped: Bool) ``` |

Modified SKTexture.init(data: NSData!, size: CGSize, rowLength: UInt32, alignment: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data pixelData: NSData!, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) ``` |
| To | ``` convenience init!(data pixelData: NSData!, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) ``` |

Modified SKTexture.init(image: NSImage)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(image image: NSImage!) ``` |
| To | ``` convenience init(image image: NSImage) ``` |

Modified SKTexture.init(imageNamed: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(imageNamed name: String!) ``` |
| To | ``` convenience init!(imageNamed name: String) ``` |

Modified SKTexture.init(noiseWithSmoothness: CGFloat, size: CGSize, grayscale: Bool)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(noiseWithSmoothness smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool) ``` |
| To | ``` convenience init!(noiseWithSmoothness smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool) ``` |

Modified SKTexture.init(rect: CGRect, inTexture: SKTexture)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(rect rect: CGRect, inTexture texture: SKTexture!) ``` |
| To | ``` convenience init(rect rect: CGRect, inTexture texture: SKTexture) ``` |

Modified SKTexture.textureByApplyingCIFilter(CIFilter) -> Self

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func textureByApplyingCIFilter(_ filter: CIFilter!) -> Self! ``` | OS X 10.10 |
| To | ``` func textureByApplyingCIFilter(_ filter: CIFilter) -> Self ``` | OS X 10.10.3 |

Modified SKTexture.init(vectorNoiseWithSmoothness: CGFloat, size: CGSize)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(vectorNoiseWithSmoothness smoothness: CGFloat, size size: CGSize) ``` |
| To | ``` convenience init!(vectorNoiseWithSmoothness smoothness: CGFloat, size size: CGSize) ``` |

Modified SKTextureAtlas.init(dictionary: [NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` convenience init(dictionary properties: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init!(dictionary properties: [NSObject : AnyObject]) ``` |

Modified SKTextureAtlas.init(named: String)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(named name: String!) ``` |
| To | ``` convenience init!(named name: String) ``` |

Modified SKTextureAtlas.preloadWithCompletionHandler(() -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func preloadWithCompletionHandler(_ completionHandler: (() -> Void)!) ``` |
| To | ``` func preloadWithCompletionHandler(_ completionHandler: () -> Void) ``` |

Modified SKTextureAtlas.textureNamed(String) -> SKTexture!

|  | Declaration |
| --- | --- |
| From | ``` func textureNamed(_ name: String!) -> SKTexture! ``` |
| To | ``` func textureNamed(_ name: String) -> SKTexture! ``` |

Modified SKTextureAtlas.textureNames

|  | Declaration |
| --- | --- |
| From | ``` var textureNames: [AnyObject]! { get } ``` |
| To | ``` var textureNames: [AnyObject] { get } ``` |

Modified SKTextureFilteringMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SKTransition.init(CIFilter: CIFilter, duration: NSTimeInterval)

|  | Declaration |
| --- | --- |
| From | ``` init(CIFilter filter: CIFilter!, duration sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` init(CIFilter filter: CIFilter, duration sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransition.crossFadeWithDuration(NSTimeInterval) -> SKTransition [class]

|  | Declaration |
| --- | --- |
| From | ``` class func crossFadeWithDuration(_ sec: NSTimeInterval) -> SKTransition! ``` |
| To | ``` class func crossFadeWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransition.doorsCloseHorizontalWithDuration(NSTimeInterval) -> SKTransition [class]

|  | Declaration |
| --- | --- |
| From | ``` class func doorsCloseHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition! ``` |
| To | ``` class func doorsCloseHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransition.doorsCloseVerticalWithDuration(NSTimeInterval) -> SKTransition [class]

|  | Declaration |
| --- | --- |
| From | ``` class func doorsCloseVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition! ``` |
| To | ``` class func doorsCloseVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransition.doorsOpenHorizontalWithDuration(NSTimeInterval) -> SKTransition [class]

|  | Declaration |
| --- | --- |
| From | ``` class func doorsOpenHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition! ``` |
| To | ``` class func doorsOpenHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransition.doorsOpenVerticalWithDuration(NSTimeInterval) -> SKTransition [class]

|  | Declaration |
| --- | --- |
| From | ``` class func doorsOpenVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition! ``` |
| To | ``` class func doorsOpenVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransition.doorwayWithDuration(NSTimeInterval) -> SKTransition [class]

|  | Declaration |
| --- | --- |
| From | ``` class func doorwayWithDuration(_ sec: NSTimeInterval) -> SKTransition! ``` |
| To | ``` class func doorwayWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransition.fadeWithColor(NSColor, duration: NSTimeInterval) -> SKTransition [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fadeWithColor(_ color: NSColor!, duration sec: NSTimeInterval) -> SKTransition! ``` |
| To | ``` class func fadeWithColor(_ color: NSColor, duration sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransition.fadeWithDuration(NSTimeInterval) -> SKTransition [class]

|  | Declaration |
| --- | --- |
| From | ``` class func fadeWithDuration(_ sec: NSTimeInterval) -> SKTransition! ``` |
| To | ``` class func fadeWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransition.flipHorizontalWithDuration(NSTimeInterval) -> SKTransition [class]

|  | Declaration |
| --- | --- |
| From | ``` class func flipHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition! ``` |
| To | ``` class func flipHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransition.flipVerticalWithDuration(NSTimeInterval) -> SKTransition [class]

|  | Declaration |
| --- | --- |
| From | ``` class func flipVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition! ``` |
| To | ``` class func flipVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransition.moveInWithDirection(SKTransitionDirection, duration: NSTimeInterval) -> SKTransition [class]

|  | Declaration |
| --- | --- |
| From | ``` class func moveInWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition! ``` |
| To | ``` class func moveInWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransition.pushWithDirection(SKTransitionDirection, duration: NSTimeInterval) -> SKTransition [class]

|  | Declaration |
| --- | --- |
| From | ``` class func pushWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition! ``` |
| To | ``` class func pushWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransition.revealWithDirection(SKTransitionDirection, duration: NSTimeInterval) -> SKTransition [class]

|  | Declaration |
| --- | --- |
| From | ``` class func revealWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition! ``` |
| To | ``` class func revealWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition ``` |

Modified SKTransitionDirection [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SKUniform.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified SKUniform.init(name: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!) ``` |
| To | ``` init!(name name: String!) ``` |

Modified SKUniform.init(name: String!, float: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, float value: Float) ``` |
| To | ``` init!(name name: String!, float value: Float) ``` |

Modified SKUniform.init(name: String!, texture: SKTexture!)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, texture texture: SKTexture!) ``` |
| To | ``` init!(name name: String!, texture texture: SKTexture!) ``` |

Modified SKVideoNode.init(videoFileNamed: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(videoFileNamed videoFile: String!) ``` |
| To | ``` init!(videoFileNamed videoFile: String!) -> SKVideoNode ``` |

Modified SKVideoNode.init(videoURL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(videoURL url: NSURL!) ``` |
| To | ``` init!(videoURL videoURL: NSURL!) -> SKVideoNode ``` |

Modified SKView.convertPoint(CGPoint, fromScene: SKScene) -> CGPoint

|  | Declaration |
| --- | --- |
| From | ``` func convertPoint(_ point: CGPoint, fromScene scene: SKScene!) -> CGPoint ``` |
| To | ``` func convertPoint(_ point: CGPoint, fromScene scene: SKScene) -> CGPoint ``` |

Modified SKView.convertPoint(CGPoint, toScene: SKScene) -> CGPoint

|  | Declaration |
| --- | --- |
| From | ``` func convertPoint(_ point: CGPoint, toScene scene: SKScene!) -> CGPoint ``` |
| To | ``` func convertPoint(_ point: CGPoint, toScene scene: SKScene) -> CGPoint ``` |

Modified SKView.presentScene(SKScene?)

|  | Declaration |
| --- | --- |
| From | ``` func presentScene(_ scene: SKScene!) ``` |
| To | ``` func presentScene(_ scene: SKScene?) ``` |

Modified SKView.presentScene(SKScene?, transition: SKTransition?)

|  | Declaration |
| --- | --- |
| From | ``` func presentScene(_ scene: SKScene!, transition transition: SKTransition!) ``` |
| To | ``` func presentScene(_ scene: SKScene?, transition transition: SKTransition?) ``` |

Modified SKView.scene

|  | Declaration |
| --- | --- |
| From | ``` var scene: SKScene! { get } ``` |
| To | ``` var scene: SKScene? { get } ``` |

Modified SKView.textureFromNode(SKNode) -> SKTexture!

|  | Declaration |
| --- | --- |
| From | ``` func textureFromNode(_ node: SKNode!) -> SKTexture! ``` |
| To | ``` func textureFromNode(_ node: SKNode) -> SKTexture! ``` |

Modified SKView.textureFromNode(SKNode, crop: CGRect) -> SKTexture!

|  | Declaration |
| --- | --- |
| From | ``` func textureFromNode(_ node: SKNode!, crop crop: CGRect) -> SKTexture! ``` |
| To | ``` func textureFromNode(_ node: SKNode, crop crop: CGRect) -> SKTexture! ``` |

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
