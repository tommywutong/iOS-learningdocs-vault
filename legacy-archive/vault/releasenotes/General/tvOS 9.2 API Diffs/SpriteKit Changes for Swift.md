---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Swift/SpriteKit.html
archived_at: '2026-07-18T02:58:06.567432Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# SpriteKit Changes for Swift

### SpriteKit

Modified [SKNode](https://developer.apple.com/documentation/spritekit/sknode)

|  | Declaration |
| --- | --- |
| From | ``` class SKNode : UIResponder, NSCopying, NSCoding {     init()     init?(coder aDecoder: NSCoder)     class func node() -> Self     convenience init?(fileNamed filename: String)     class func nodeWithFileNamed(_ filename: String) -> Self?     var frame: CGRect { get }     func calculateAccumulatedFrame() -> CGRect     var position: CGPoint     var zPosition: CGFloat     var zRotation: CGFloat     var xScale: CGFloat     var yScale: CGFloat     var speed: CGFloat     var alpha: CGFloat     var paused: Bool     var hidden: Bool     var userInteractionEnabled: Bool     var parent: SKNode? { get }     var children: [SKNode] { get }     var name: String?     var scene: SKScene? { get }     var physicsBody: SKPhysicsBody?     var userData: NSMutableDictionary?     @NSCopying var reachConstraints: SKReachConstraints?     var constraints: [SKConstraint]?     func setScale(_ scale: CGFloat)     func addChild(_ node: SKNode)     func insertChild(_ node: SKNode, atIndex index: Int)     func removeChildrenInArray(_ nodes: [SKNode])     func removeAllChildren()     func removeFromParent()     func moveToParent(_ parent: SKNode)     func childNodeWithName(_ name: String) -> SKNode?     func enumerateChildNodesWithName(_ name: String, usingBlock block: (SKNode, UnsafeMutablePointer<ObjCBool>) -> Void)     func objectForKeyedSubscript(_ name: String) -> [SKNode]     func inParentHierarchy(_ parent: SKNode) -> Bool     func runAction(_ action: SKAction)     func runAction(_ action: SKAction, completion block: () -> Void)     func runAction(_ action: SKAction, withKey key: String)     func hasActions() -> Bool     func actionForKey(_ key: String) -> SKAction?     func removeActionForKey(_ key: String)     func removeAllActions()     func containsPoint(_ p: CGPoint) -> Bool     func nodeAtPoint(_ p: CGPoint) -> SKNode     func nodesAtPoint(_ p: CGPoint) -> [SKNode]     func convertPoint(_ point: CGPoint, fromNode node: SKNode) -> CGPoint     func convertPoint(_ point: CGPoint, toNode node: SKNode) -> CGPoint     func intersectsNode(_ node: SKNode) -> Bool     func isEqualToNode(_ node: SKNode) -> Bool     class func obstaclesFromSpriteTextures(_ sprites: [SKNode], accuracy accuracy: Float) -> [GKPolygonObstacle]     class func obstaclesFromNodeBounds(_ nodes: [SKNode]) -> [GKPolygonObstacle]     class func obstaclesFromNodePhysicsBodies(_ nodes: [SKNode]) -> [GKPolygonObstacle] } extension SKNode {     subscript (_ name: String) -> [SKNode] { get } } extension SKNode {     subscript (_ name: String) -> [SKNode] { get } } ``` |
| To | ``` class SKNode : UIResponder, NSCopying, NSCoding {     init()     init?(coder aDecoder: NSCoder)     class func node() -> Self     convenience init?(fileNamed filename: String)     class func nodeWithFileNamed(_ filename: String) -> Self?     var frame: CGRect { get }     func calculateAccumulatedFrame() -> CGRect     var position: CGPoint     var zPosition: CGFloat     var zRotation: CGFloat     var xScale: CGFloat     var yScale: CGFloat     var speed: CGFloat     var alpha: CGFloat     var paused: Bool     var hidden: Bool     var userInteractionEnabled: Bool     var parent: SKNode? { get }     var children: [SKNode] { get }     var name: String?     var scene: SKScene? { get }     var physicsBody: SKPhysicsBody?     var userData: NSMutableDictionary?     @NSCopying var reachConstraints: SKReachConstraints?     var constraints: [SKConstraint]?     func setScale(_ scale: CGFloat)     func addChild(_ node: SKNode)     func insertChild(_ node: SKNode, atIndex index: Int)     func removeChildrenInArray(_ nodes: [SKNode])     func removeAllChildren()     func removeFromParent()     func moveToParent(_ parent: SKNode)     func childNodeWithName(_ name: String) -> SKNode?     func enumerateChildNodesWithName(_ name: String, usingBlock block: (SKNode, UnsafeMutablePointer<ObjCBool>) -> Void)     subscript (_ name: String) -> [SKNode] { get }     func objectForKeyedSubscript(_ name: String) -> [SKNode]     func inParentHierarchy(_ parent: SKNode) -> Bool     func runAction(_ action: SKAction)     func runAction(_ action: SKAction, completion block: () -> Void)     func runAction(_ action: SKAction, withKey key: String)     func hasActions() -> Bool     func actionForKey(_ key: String) -> SKAction?     func removeActionForKey(_ key: String)     func removeAllActions()     func containsPoint(_ p: CGPoint) -> Bool     func nodeAtPoint(_ p: CGPoint) -> SKNode     func nodesAtPoint(_ p: CGPoint) -> [SKNode]     func convertPoint(_ point: CGPoint, fromNode node: SKNode) -> CGPoint     func convertPoint(_ point: CGPoint, toNode node: SKNode) -> CGPoint     func intersectsNode(_ node: SKNode) -> Bool     func isEqualToNode(_ node: SKNode) -> Bool     class func obstaclesFromSpriteTextures(_ sprites: [SKNode], accuracy accuracy: Float) -> [GKPolygonObstacle]     class func obstaclesFromNodeBounds(_ nodes: [SKNode]) -> [GKPolygonObstacle]     class func obstaclesFromNodePhysicsBodies(_ nodes: [SKNode]) -> [GKPolygonObstacle] } ``` |

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
