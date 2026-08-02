---
title: 'HelloGameKit: A skeleton app for turn based games on watchOS'
apple_id: TP40017337
resource_type: Sample Code
platform: watchOS
topic: null
technology: GameCenter
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGameKit/Listings/HelloGameKit_WatchKit_Extension_PlayersInterfaceController_swift.html
archived_at: '2026-07-18T03:11:49.122969Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGameKit: A skeleton app for turn based games on watchOS](HelloGameKit-%20A%20skeleton%20app%20for%20turn%20based%20games%20on%20watchOS.md)


[Next](HelloGameKit%20WatchKit%20Extension-TitleWithDetailRowController.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-ListWithButtonInterfaceController.swift.md)

# HelloGameKit WatchKit Extension/PlayersInterfaceController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 PlayersInterfaceController is a ListWithButtinInterfaceController subclass that specialize to loading recent players.  It adopts the ListDataSource protocol and extends GKPlayer with the ListItem protocol
 */

import WatchKit
import Foundation
import GameKit

extension GKPlayer: ListItem {
    // MARK: ListItem Properties

    var title: String {
        return alias ?? "<no nickname>"
    }

    var detail: String {
        return displayName ?? "<no displayName>"
    }
}

class PlayersInterfaceController: ListWithButtonInterfaceController, ListDataSource {
    // MARK: WKInterfaceController

    override func awake(withContext context: Any?) {
        dataSource = self
        super.awake(withContext: context)
    }

    // MARK: ListDataSource methods

    func buttonTitle() -> String {
        return "Auto Match"
    }

    func loadItems(completionHandler: @escaping (([ListItem]) -> Void)) {
        guard loadingState != .loading else { return }
        loadingState = .loading

        GKLocalPlayer.localPlayer().loadRecentPlayers { [unowned self] (players, error) in
            if let items = players {
                let result = items.sorted { (p1, p2) -> Bool in
                    guard let displayName1 = p1.displayName, let displayName2 = p2.displayName else { return false }
                    return displayName1 < displayName2
                }

                completionHandler(result)
            }
            else {
                // No players were found.
                completionHandler([])
            }

            self.loadingState = error == nil ? .complete: .failed
        }
    }

    override func didSelect(item: ListItem?) {
        let player = item as? GKPlayer

        if let controller = presentingController {
            loadingState = .exiting
            controller.didSelect(player: player)
        }
    }
}
```

[Next](HelloGameKit%20WatchKit%20Extension-TitleWithDetailRowController.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-ListWithButtonInterfaceController.swift.md)

