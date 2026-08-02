---
title: 'HelloGameKit: A skeleton app for turn based games on watchOS'
apple_id: TP40017337
resource_type: Sample Code
platform: watchOS
topic: null
technology: GameCenter
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGameKit/Listings/HelloGameKit_WatchKit_Extension_GameScene_swift.html
archived_at: '2026-07-18T03:11:48.603584Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGameKit: A skeleton app for turn based games on watchOS](HelloGameKit-%20A%20skeleton%20app%20for%20turn%20based%20games%20on%20watchOS.md)


[Next](HelloGameKit%20WatchKit%20Extension-InterfaceController.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-MatchesInterfaceController.swift.md)

# HelloGameKit WatchKit Extension/GameScene.swift

```swift
/*
     Copyright (C) 2016 Apple Inc. All Rights Reserved.
     See LICENSE.txt for this sample’s licensing information

     Abstract:
     This is the SpriteKit scene that renders the game scene.  It consists of label nodes for both players, an indicator of the number of gestures recorded and renders gestures as the user taps the screen
 */

import SpriteKit
import WatchKit
import GameKit
import CoreMotion

extension WKGestureRecognizer {
    func position() -> CGPoint {
        let location = locationInObject()
        let bounds = objectBounds()
        return CGPoint(x:location.x, y:bounds.maxY - location.y)
    }
}

extension SKLabelNode {
    func setTextWithPulse(_ text: String?) {
        if let text = text {
            self.text = text
            self.run(SKAction(named: "Pulse")!, withKey: "fadeInOut")
        }
    }
}

class GameScene: SKScene {
    // MARK: Properties

    private var lastUpdateTime: TimeInterval = 0
    internal var topLabel: SKLabelNode?
    internal var middleLabel: SKLabelNode?
    internal var middleLabelBasePosition : CGPoint? // we store this for use with the accelerometer
    internal var bottomLabel: SKLabelNode?
    internal var bottomLabelTapHandler: (() -> Void)?

    private var spinnyNode: SKShapeNode?
    private var tappyNode: SKShapeNode?

    private var _model: GameModel?
    var model: GameModel? {
        get {
            if _model == nil {
                _model = GameModel()
            }
            return _model
        }

        set {
            _model = newValue
            updateUI()
        }
    }

    private var _topPlayer: GKPlayer? = nil
    internal var topPlayer: GKPlayer? {
        get {
            return _topPlayer
        }

        set {
            _topPlayer = newValue
            if let player = _topPlayer {
                let nickname = player.alias != nil ? player.alias: player.displayName
                topLabel?.setTextWithPulse(nickname)
            }
            else {
                topLabel?.setTextWithPulse("Authenticating")
            }
        }
    }

    private var _bottomPlayer: GKPlayer? = nil
    internal var bottomPlayer: GKPlayer? {
        get {
            return _bottomPlayer
        }

        set {
            _bottomPlayer = newValue
            if let player = bottomPlayer {
                let nickname = player.alias != nil ? player.alias: player.displayName
                bottomLabel?.setTextWithPulse(nickname)
            }
            else {
                bottomLabel?.setTextWithPulse("Auto-Match Player")
            }
        }
    }
    private var _currentPlayer: GKPlayer? = nil
    internal var currentPlayer: GKPlayer? {
        get {
            return _currentPlayer
        }

        set {
            _currentPlayer = newValue
            if let playerID = _currentPlayer?.playerID {
                if let player = _topPlayer, let topPlayerID = player.playerID, let label = self.topLabel, topPlayerID == playerID {
                    label.text = "<\(player.displayName!)>"
                    self.flashMessage("\(player.displayName!)'s turn")
                }                
            }
        }
    }

    var isLocalPlayerTurn: Bool {
        if let player = currentPlayer {
            return player == GKLocalPlayer.localPlayer()
        }
        else {
            return false
        }
    }

    // MARK: SKScene

    override func sceneDidLoad() {
        lastUpdateTime = 0

        topLabel = childNode(withName: "//topLabel") as? SKLabelNode
        middleLabel = childNode(withName: "//middleLabel") as? SKLabelNode
        self.middleLabelBasePosition = middleLabel?.position
        bottomLabel = childNode(withName: "//bottomLabel") as? SKLabelNode

        if let label = middleLabel {
            label.alpha = 0.0
            label.run(SKAction.fadeIn(withDuration: 2.0))
        }

        let dimension = (size.width + size.height) * 0.05
        spinnyNode = SKShapeNode(rectOf: CGSize(width: dimension, height: dimension), cornerRadius: dimension * 0.3)

        if let spinnyNode = spinnyNode {
            spinnyNode.lineWidth = 2.5

            spinnyNode.run(SKAction.repeatForever(SKAction.rotate(byAngle: CGFloat(M_PI), duration: 1)))
            spinnyNode.run(SKAction.sequence([SKAction.wait(forDuration: 0.5),
                                              SKAction.fadeOut(withDuration: 0.5),
                                              SKAction.removeFromParent()]))
        }

        tappyNode = SKShapeNode(circleOfRadius: dimension)

        if let tappyNode = tappyNode {
            tappyNode.lineWidth = 2.5

            tappyNode.run(SKAction.sequence([SKAction.scale(to: 1.5, duration: 0.2),
                                             SKAction.scale(to: 1.0, duration: 0.2),
                                             SKAction.wait(forDuration: 0.2),
                                             SKAction.fadeOut(withDuration: 0.5),
                                             SKAction.removeFromParent()
            ]))
        }
    }

    // MARK: Gesture handling

    func didTap(_ recognizer: WKTapGestureRecognizer) {
        let position = recognizer.position()
        let hitNodes = self.nodes(at: position)
        if  hitNodes.contains(bottomLabel!) {
            if let tapHandler = bottomLabelTapHandler {
                tapHandler()
            }
        }
        else {
            if isLocalPlayerTurn {
                if let node = tappyNode?.copy() as! SKShapeNode? {
                    node.position = recognizer.position()
                    node.strokeColor = UIColor.orange
                    self.addChild(node)
                    if let model = self.model {
                        let move = model.addMove()
                        move.add(position: node.position)

                        updateUI()
                    }
                }
            }
        }
    }

    func didPan(_ recognizer: WKPanGestureRecognizer) {
        guard isLocalPlayerTurn else { return }

        if let node = spinnyNode?.copy() as! SKShapeNode? {
            node.position = recognizer.position()
            switch recognizer.state {
                case .began:
                    node.strokeColor = UIColor.green
                    let move = model?.addMove()
                    move?.add(position: node.position)

                case .changed:
                    node.strokeColor = UIColor.blue

                case .cancelled, .ended:
                    node.strokeColor = UIColor.red

                case .possible, .failed, .recognized:
                    node.strokeColor = UIColor.white // should never see this
            }

            if let model = self.model {
                model.currentMove?.add(position: node.position)
                self.updateUI()
            }
            addChild(node)
        }
    }

    // MARK: Accelerometer

    func didReceiveAccelerometerUpdate(accelerometerData: CMAccelerometerData) {
        if let label = middleLabel, let basePosition = middleLabelBasePosition {
            let acceleration = accelerometerData.acceleration
            let x = acceleration.x, y = acceleration.y

            // move the green counter around

            let currentPosition = label.position
            let position = CGPoint(x: basePosition.x - 50 * CGFloat(x), y: basePosition.y - 50 * CGFloat(y))
            let dx = position.x - currentPosition.x
            let dy = position.y - currentPosition.y
            if (sqrt(dx*dx + dy*dy) > 0.1) {
                let filterdPosition = CGPoint(x: (position.x + 4 * currentPosition.x) / 5.0, y: (position.y + 4 * currentPosition.y) / 5.0)
                label.position = filterdPosition
            }
        }
    }

    // MARK: UI Refresh

    func updateUI() {
        if let label = middleLabel {
            if let count = model?.moves.count {
                label.text = "\(count)"
            }
            else {
                label.text = "0"
            }
        }
    }

    // MARK Convenience

    func setupNewGame() {
        model = GameModel()
        bottomPlayer = nil
    }

    func pulseLabel(label: SKLabelNode?) {
        label?.run(SKAction(named: "Pulse")!, withKey: "fadeInOut")
    }

    func flashMessage(_ message: String) {
        if let label = middleLabel?.copy() as! SKLabelNode? {
            label.position.y += 20
            label.run(.sequence([.fadeIn(withDuration: 0.5),
                                 .fadeOut(withDuration: 0.5),
                                 .removeFromParent()]))
        }
    }
}
```

[Next](HelloGameKit%20WatchKit%20Extension-InterfaceController.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-MatchesInterfaceController.swift.md)

