---
title: 'Scoreboard: A demonstration of RTL support on macOS using NSStackView and
  localizedStringWithFormat'
apple_id: TP40017507
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/Scoreboard/Listings/Scoreboard_ViewController_swift.html
archived_at: '2026-07-18T03:23:26.028855Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Scoreboard: A demonstration of RTL support on macOS using NSStackView and localizedStringWithFormat](Scoreboard-%20A%20demonstration%20of%20RTL%20support%20on%20macOS%20using%20NSStackView%20and%20locali.md)


[Next](Scoreboard-AppDelegate.swift.md)[Previous](Scoreboard-%20A%20demonstration%20of%20RTL%20support%20on%20macOS%20using%20NSStackView%20and%20locali.md)

# Scoreboard/ViewController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The `ViewController` manages an array of players, compares the players scores and display the information of the player with the highest score.
 */

import Cocoa

private var myContext = 0

class ViewController: NSViewController {

    // MARK: Properties

    @IBOutlet weak var tableview: NSTableView!

    @IBOutlet weak var highScore: NSTextField!

    @IBOutlet var playersController: NSArrayController!

    dynamic var players = [PlayerInfo]()

    // MARK: NSViewController

    override func viewDidLoad() {
        super.viewDidLoad()

        if let savedPlayersData = UserDefaults.standard.object(forKey: "players") as? Data {
            players = NSKeyedUnarchiver.unarchiveObject(with: savedPlayersData) as! [PlayerInfo]
        }
        else {
            // Create a default set of players.
            players.append(PlayerInfo(name: "Aya", score: 8))
            players.append(PlayerInfo(name: "Joaquim", score: 3))
            players.append(PlayerInfo(name: "Rana", score: 5))
        }

        // Observe changes to the `playersController`'s content.
        playersController.addObserver(self, forKeyPath: "arrangedObjects.score", options: [.new, .initial], context: &myContext)
        playersController.addObserver(self, forKeyPath: "arrangedObjects.name", options: [.new, .initial], context: &myContext)
    }

    override func observeValue(forKeyPath keyPath: String?, of object: AnyObject?, change: [NSKeyValueChangeKey : AnyObject]?, context: UnsafeMutablePointer<Swift.Void>?) {
        guard context == &myContext else { return }

        // Compare players score and display the best player information.
        let bestPlayer = players.sorted(by: { player1, player2 -> Bool in
            return player1.score > player2.score
        }).first

        if let bestPlayer = bestPlayer {
            /*
                `localizedStringWithFormat` will surround %@ with unicode isolates
                characters to display bidirectional text correctecly.
            */
            highScore.stringValue = NSString.localizedStringWithFormat("%@ has the highest score %d!", bestPlayer.name, bestPlayer.score) as String
        }

        // Save the updated player data.
        let data = NSKeyedArchiver.archivedData(withRootObject: players)
        let defaults = UserDefaults.standard
        defaults.set(data, forKey: "players")
    }

    deinit {
        playersController.removeObserver(self, forKeyPath: "arrangedObjects.score")
        playersController.removeObserver(self, forKeyPath: "arrangedObjects.name")
    }

    // MARK: Interface Builder actions

    @IBAction func addRemovePlayer(sender: AnyObject) {
        if sender.selectedSegment == 0 {
            // The user clicked to add a new player.
            players.append(PlayerInfo(name: "Enter Name", score: 0))
            tableview.editColumn(0, row: tableview.numberOfRows - 1, with: nil, select: true)
        } else if tableview.selectedRow >= 0 {
            // The user clicked to remove the selected player.
            playersController.remove(atArrangedObjectIndex: tableview.selectedRow)
        }
    }
}
```

[Next](Scoreboard-AppDelegate.swift.md)[Previous](Scoreboard-%20A%20demonstration%20of%20RTL%20support%20on%20macOS%20using%20NSStackView%20and%20locali.md)

