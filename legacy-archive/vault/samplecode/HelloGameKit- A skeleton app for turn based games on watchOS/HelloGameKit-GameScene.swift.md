---
title: 'HelloGameKit: A skeleton app for turn based games on watchOS'
apple_id: TP40017337
resource_type: Sample Code
platform: watchOS
topic: null
technology: GameCenter
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGameKit/Listings/HelloGameKit_GameScene_swift.html
archived_at: '2026-07-18T03:11:48.282674Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGameKit: A skeleton app for turn based games on watchOS](HelloGameKit-%20A%20skeleton%20app%20for%20turn%20based%20games%20on%20watchOS.md)


[Next](HelloGameKit-AppDelegate.swift.md)[Previous](HelloGameKit-GameViewController.swift.md)

# HelloGameKit/GameScene.swift

```swift
/*
     Copyright (C) 2016 Apple Inc. All Rights Reserved.
     See LICENSE.txt for this sample’s licensing information

     Abstract:
     This is the SpriteKit scene that renders the game scene. It allows users to perform multitouch actions and renders colorful feedback.
*/

import SpriteKit
import GameplayKit

class GameScene: SKScene {

    // MARK: Properties

    var entities = [GKEntity]()

    var graphs = [GKGraph]()

    private var lastUpdateTime: TimeInterval = 0

    private var label: SKLabelNode!

    private var spinnyNode: SKShapeNode!

    // MARK: SKScene

    override func sceneDidLoad() {
        lastUpdateTime = 0

        label = childNode(withName: "//helloLabel") as! SKLabelNode
        label.alpha = 0.0
        label.run(.fadeIn(withDuration: 2.0))

        let w = (size.width + size.height) * 0.05
        spinnyNode = SKShapeNode(rectOf: CGSize(width: w, height: w), cornerRadius: w * 0.3)

        if let spinnyNode = spinnyNode {
            spinnyNode.lineWidth = 2.5

            spinnyNode.run(.repeatForever(.rotate(byAngle: CGFloat(M_PI), duration: 1)))
            spinnyNode.run(.sequence([.wait(forDuration: 0.5),
                                      .fadeOut(withDuration: 0.5),
                                      .removeFromParent()]))
        }
    }

    override func update(_ currentTime: TimeInterval) {
        if lastUpdateTime == 0 {
            lastUpdateTime = currentTime
        }

        let dt = currentTime - lastUpdateTime

        for entity in entities {
            entity.update(deltaTime: dt)
        }

        lastUpdateTime = currentTime
    }

    // MARK: UIResponder

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        label.run(SKAction(named: "Pulse")!, withKey: "fadeInOut")

        for touch in touches {
            touchDown(atPoint: touch.location(in: self))
        }
    }

    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        for touch in touches {
            touchUp(atPoint: touch.location(in: self))
        }
    }

    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        for touch in touches {
            touchMoved(toPoint: touch.location(in: self))
        }
    }

    override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
        for touch in touches {
            touchUp(atPoint: touch.location(in: self))
        }
    }

    // MARK: Touch handling helpers

    private func touchDown(atPoint pos: CGPoint) {
        let node = spinnyNode.copy() as! SKShapeNode

        node.position = pos
        node.strokeColor = .green
        addChild(node)
    }

    private func touchMoved(toPoint pos: CGPoint) {
        let node = spinnyNode.copy() as! SKShapeNode

        node.position = pos
        node.strokeColor = .blue
        addChild(node)
    }

    private func touchUp(atPoint pos: CGPoint) {
        let node = spinnyNode.copy() as! SKShapeNode

        node.position = pos
        node.strokeColor = .red
        addChild(node)
    }
}
```

[Next](HelloGameKit-AppDelegate.swift.md)[Previous](HelloGameKit-GameViewController.swift.md)

