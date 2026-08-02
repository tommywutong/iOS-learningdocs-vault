---
title: 'HelloGameKit: A skeleton app for turn based games on watchOS'
apple_id: TP40017337
resource_type: Sample Code
platform: watchOS
topic: null
technology: GameCenter
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGameKit/Listings/HelloGameKit_WatchKit_Extension_Move_swift.html
archived_at: '2026-07-18T03:11:49.083737Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGameKit: A skeleton app for turn based games on watchOS](HelloGameKit-%20A%20skeleton%20app%20for%20turn%20based%20games%20on%20watchOS.md)


[Next](HelloGameKit%20WatchKit%20Extension-GameModel.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-TitleWithDetailRowController.swift.md)

# HelloGameKit WatchKit Extension/Move.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A move is one or more points recorded by a gesture
*/

import UIKit

class Move: NSObject, NSCoding {
    // MARK: Properties

    private(set) var points = [CGPoint]()

    let playerID: String

    // MARK: Initialization

    init(playerID: String) {
        self.playerID = playerID

        super.init()
    }

    required init?(coder aDecoder: NSCoder) {
        let pointStrings = aDecoder.decodeObject(forKey:"points") as! [String]

        points = pointStrings.map { CGPointFromString($0) }
        playerID = aDecoder.decodeObject(forKey:"playerID") as! String
    }

    // MARK: NSCoding

    func encode(with aCoder: NSCoder) {
        let pointStrings = points.map { NSStringFromCGPoint($0) }
        aCoder.encode(pointStrings as NSArray, forKey: "points")
        aCoder.encode(playerID as NSString, forKey: "playerID")
    }

    // MARK: Public Accessors

    func add(position: CGPoint) {
        points.append(position)
    }
}
```

[Next](HelloGameKit%20WatchKit%20Extension-GameModel.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-TitleWithDetailRowController.swift.md)

