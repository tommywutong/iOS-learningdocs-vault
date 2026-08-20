---
title: 'HelloGameKit: A skeleton app for turn based games on watchOS'
apple_id: TP40017337
resource_type: Sample Code
platform: watchOS
topic: null
technology: GameCenter
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGameKit/Listings/HelloGameKit_WatchKit_Extension_InterfaceController_swift.html
archived_at: '2026-07-18T03:11:48.724969Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGameKit: A skeleton app for turn based games on watchOS](HelloGameKit-%20A%20skeleton%20app%20for%20turn%20based%20games%20on%20watchOS.md)


[Next](HelloGameKit%20WatchKit%20Extension-ExtensionDelegate.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-GameScene.swift.md)

# HelloGameKit WatchKit Extension/InterfaceController.swift

```swift
/*
     Copyright (C) 2016 Apple Inc. All Rights Reserved.
     See LICENSE.txt for this sample’s licensing information

     Abstract:
     This is the main interface for the watchkit app extension
 */

import WatchKit
import Foundation
import GameKit
import CoreMotion

class InterfaceController: WKInterfaceController {
    // MARK: Properties

    var gameScene: GameScene!

    private var _match: GKTurnBasedMatch?
    var match: GKTurnBasedMatch? {
        get {
            return _match
        }

        set {
            _match = newValue
            if let opponentPlayer = newValue?.firstOpponentParticipant?.player {
                gameScene.bottomPlayer = opponentPlayer
            }
            else {
                gameScene.bottomLabel?.text = "Auto-Match Player"
            }
        }
    }

    let motionManager = CMMotionManager()

    // MARK: IB Outlets

    @IBOutlet weak var sceneInterface: WKInterfaceSKScene!

    // MARK: WKInterfaceController

    override func awake(withContext context: Any?) {
        super.awake(withContext: context)

        motionManager.accelerometerUpdateInterval = 1.0/30.0

        gameScene = GameScene(fileNamed: "GameScene")!

        // Set the scale mode to scale to fit the window.
        gameScene.scaleMode = .aspectFit

        sceneInterface.presentScene(gameScene)

        let localPlayer = GKLocalPlayer.localPlayer()
        print("***** authenticating LocalPlayer")

        localPlayer.authenticateHandler = { error in
            if let error = error {
                print("***** auth failed \(error)")
                self.gameScene.bottomLabel?.fontSize = 10
                self.gameScene.bottomLabel?.text = "\(error)"
            }
            else {
                print("***** auth successful \(localPlayer)")
                self.gameScene.topPlayer = localPlayer
                self.gameScene.currentPlayer = localPlayer
                self.gameScene.bottomLabelTapHandler = {
                    self.pushController(withName: "PlayersInterfaceController", context: self)
                }
            }
        }
    }

    override func willActivate() {
        // This method is called when watch view controller is about to be visible to user
        super.willActivate()
        if motionManager.isAccelerometerAvailable {
            print("***** installing acceleration handler")
            motionManager.startAccelerometerUpdates(to: OperationQueue.current!, withHandler: { data, error in
                guard let data = data else { return }

                self.gameScene.didReceiveAccelerometerUpdate(accelerometerData: data)
            })
        }
    }

    override func didDeactivate() {
        // This method is called when watch view controller is no longer visible
        super.didDeactivate()
        motionManager.stopAccelerometerUpdates()
    }

    // MARK: IBActions

    @IBAction func didTap(recognizer: WKTapGestureRecognizer) {
        // forward to the gameScene
        WKInterfaceDevice.current().play(.click)
        gameScene.didTap(recognizer)
    }

    @IBAction func didPan(recognizer: WKPanGestureRecognizer) {
        // forward to the gameScene
        gameScene.didPan(recognizer)
    }

    @IBAction func didLongPress(recognizer: WKLongPressGestureRecognizer) {
        if let match = self.match, let model = gameScene.model {
            self.gameScene.flashMessage("Saving")
            print("***** ending turn")
            model.endTurn(for: match) {
                self.gameScene.flashMessage("Ended Turn")
                print("***** ended turn successfully")
                self.gameScene.updateUI()

                WKInterfaceDevice.current().play(.success)
            }
        }
        else {
            WKInterfaceDevice.current().play(.stop)
        }
    }

    @IBAction func didSwipe(recognizer: WKSwipeGestureRecognizer) {
        // Push matches view with self
        let localPlayer = GKLocalPlayer.localPlayer()
        if localPlayer.isAuthenticated {
            self.pushController(withName: "MatchesInterfaceController", context: self)
        }
        else {
            WKInterfaceDevice.current().play(.failure)
        }
    }

    func didSelect(player: GKPlayer?) {
        gameScene.bottomPlayer = player
        // if we select a player go ahead and create a match
        didSelect(match: nil)
        popToRootController()
    }

    func didSelect(match: GKTurnBasedMatch?) {
        if let match = match {
            self.load(match: match, completionHandler: {
                self.popToRootController()
            })
        }
        else {
            // no match was selected so we auto-match
            print("***** creating match")
            let request = GKMatchRequest()
            request.minPlayers = 2
            request.maxPlayers = 2
            if let opponent = gameScene.bottomPlayer {
                request.recipients = [opponent]
            }
            GKTurnBasedMatch.find(for: request, withCompletionHandler: { (match, error) in
                print("***** match created")
                if let match = match {
                    self.load(match: match, completionHandler: {
                        self.popToRootController()
                    })
                }
            })
        }
    }

    // MARK: Convenience

    func load(match: GKTurnBasedMatch, completionHandler: @escaping (() -> Swift.Void)) {
        print("***** loading match")
        GameModel.loadGameModel(match: match) { (model, error) in
            if error == nil && model != nil {
                print("***** match load succeeded")
                self.gameScene.model = model!
                self.gameScene.currentPlayer = match.currentParticipant?.player ?? nil
                self.match = match
                completionHandler()
            }
            else {
                print("***** match load failed")
                completionHandler()
            }
        }
    }
}
```

[Next](HelloGameKit%20WatchKit%20Extension-ExtensionDelegate.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-GameScene.swift.md)

