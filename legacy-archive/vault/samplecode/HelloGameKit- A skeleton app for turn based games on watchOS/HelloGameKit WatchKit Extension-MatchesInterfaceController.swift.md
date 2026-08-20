---
title: 'HelloGameKit: A skeleton app for turn based games on watchOS'
apple_id: TP40017337
resource_type: Sample Code
platform: watchOS
topic: null
technology: GameCenter
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGameKit/Listings/HelloGameKit_WatchKit_Extension_MatchesInterfaceController_swift.html
archived_at: '2026-07-18T03:11:48.997858Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGameKit: A skeleton app for turn based games on watchOS](HelloGameKit-%20A%20skeleton%20app%20for%20turn%20based%20games%20on%20watchOS.md)


[Next](HelloGameKit%20WatchKit%20Extension-GameScene.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-ButtonRowController.swift.md)

# HelloGameKit WatchKit Extension/MatchesInterfaceController.swift

```swift
/*
     Copyright (C) 2016 Apple Inc. All Rights Reserved.
     See LICENSE.txt for this sample’s licensing information

     Abstract:
     MatchesInterfaceController is a ListWithButtinInterfaceController subclass that specialize to loading turn based matches.  It adopts the ListDataSource protocol and extends GKTurnBasedMatch with the ListItem protocol
 */

import WatchKit
import GameKit

extension GKTurnBasedMatch: ListItem {
    // MARK: ListItem Properties

    var firstOpponentParticipant: GKTurnBasedParticipant? {
        let localPlayerID = GKLocalPlayer.localPlayer().playerID!
        let opponentParticipant = participants?.first { participant in
            let playerID = participant.player?.playerID
            return playerID != localPlayerID
        }

        return opponentParticipant
    }

    var title: String {
        if let opponentPlayer = firstOpponentParticipant?.player {
            return opponentPlayer.alias ?? opponentPlayer.displayName!
        }
        else {
            return "Auto-Match"
        }
    }

    var detail: String {
        if let message = self.message, !message.isEmpty {
            return message
        }
        switch status {
        case .matching:
            if currentParticipant?.player == GKLocalPlayer.localPlayer() {
                return "Your Turn"
            }
            else {
                return "Finding Player"
            }

        case .open:
            if currentParticipant?.player == GKLocalPlayer.localPlayer() {
                return "Your Turn"
            }
            else {
                return "Their Turn"
            }
        case .ended:
            return "Game Over"

        default:
            return "<unknown>"
        }
    }
}

class MatchesInterfaceController: ListWithButtonInterfaceController, ListDataSource {
    // MARK: WKInterfaceController

    override func awake(withContext context: Any?) {
        self.dataSource = self
        super.awake(withContext: context)
    }

    // MARK: ListDataSource methods
    func buttonTitle() -> String {
        return "New Match"
    }

    func loadItems(completionHandler: @escaping (([ListItem]) -> Void)) {
        guard loadingState != .loading else { return }
        loadingState = .loading

        GKTurnBasedMatch.loadMatches { [unowned self] (matches, error) in
            if let items = matches {
                print("***** loaded \(items.count) matches")
                let result = items.sorted { (m1, m2) -> Bool in
                    guard let creationDate1 = m1.creationDate, let creationDate2 = m2.creationDate else { return false }
                    return creationDate1 < creationDate2
                }

                completionHandler(result)
            }
            else {
                // Failed to find any matches.
                completionHandler([])
            }

            self.loadingState = error == nil ? .complete: .failed
        }
    }

    override func didSelect(item: ListItem?) {
        let match = item as? GKTurnBasedMatch
        if let controller = presentingController {
            loadingState = .exiting
            controller.didSelect(match: match)
        }
    }
}
```

[Next](HelloGameKit%20WatchKit%20Extension-GameScene.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-ButtonRowController.swift.md)

