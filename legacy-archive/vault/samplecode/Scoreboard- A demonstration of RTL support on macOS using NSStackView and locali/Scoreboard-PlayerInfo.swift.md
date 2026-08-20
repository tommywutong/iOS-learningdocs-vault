---
title: 'Scoreboard: A demonstration of RTL support on macOS using NSStackView and
  localizedStringWithFormat'
apple_id: TP40017507
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/Scoreboard/Listings/Scoreboard_PlayerInfo_swift.html
archived_at: '2026-07-18T03:23:25.965881Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Scoreboard: A demonstration of RTL support on macOS using NSStackView and localizedStringWithFormat](Scoreboard-%20A%20demonstration%20of%20RTL%20support%20on%20macOS%20using%20NSStackView%20and%20locali.md)


[Next](README.md.md)[Previous](Scoreboard-ClickableStepper.swift.md)

# Scoreboard/PlayerInfo.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The `PlayerInfo` class manages the players information: name, score, image and stores the data to be displayed.
 */

import Foundation
import Cocoa

class PlayerInfo: NSObject, NSCoding {
    // MARK: Properties

    dynamic var name: String

    dynamic var score: Int

    dynamic var image: NSImage

    // MARK: Initialization

    init(name: String, score: Int, image: NSImage? = nil) {
        self.name = name
        self.score = score

        if let image = image {
            self.image = image
        }
        else {
            self.image = NSImage(named: "NSUserGuest")!
        }
    }

    // MARK: NSCoding

    required convenience init?(coder aDecoder: NSCoder) {
        guard let name = aDecoder.decodeObject(forKey: "playerName") as? String, let image = aDecoder.decodeObject(forKey: "image") as? NSImage else { return nil }
        let score = aDecoder.decodeInteger(forKey: "playerScore")

        self.init(name: name, score: score, image: image)
    }

    @objc(encodeWithCoder:) internal func encode(with encoder: NSCoder) {
        encoder.encode(name, forKey: "playerName")
        encoder.encode(score, forKey: "playerScore")
        encoder.encode(image, forKey: "image")
    }

}
```

[Next](README.md.md)[Previous](Scoreboard-ClickableStepper.swift.md)

