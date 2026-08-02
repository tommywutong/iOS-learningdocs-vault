---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Swift_iOS_ControlOverlay_swift.html
archived_at: '2026-07-26T19:54:17.206192Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Swift-iOS-ButtonOverlay.swift.md)[Previous](Swift-macOS-AppDelegate.swift.md)

# Swift/iOS/ControlOverlay.swift

```swift
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Exposes game controller action button type functionality with screen-rendered buttons.
 */

import SpriteKit

class ControlOverlay: SKNode {

    let buttonMargin = CGFloat( 25 )

    var leftPad = PadOverlay()
    var rightPad = PadOverlay()
    var buttonA = ButtonOverlay("A")
    var buttonB = ButtonOverlay("B")

    init(frame: CGRect) {
        super.init()

        leftPad.position = CGPoint(x: CGFloat(20), y: CGFloat(40))
        addChild(leftPad)

        rightPad.position = CGPoint(x: CGFloat(frame.size.width - 20 - rightPad.size.width), y: CGFloat(40))
        addChild(rightPad)

        let buttonDistance = rightPad.size.height / CGFloat( 2 ) + buttonMargin + buttonA.size.height / CGFloat( 2 )
        let center = CGPoint( x: rightPad.position.x + rightPad.size.width / 2.0, y: rightPad.position.y + rightPad.size.height / 2.0 )

        let buttonAx = center.x - buttonDistance * CGFloat(cosf(Float.pi / 4.0)) - (buttonB.size.width / 2)
        let buttonAy = center.y + buttonDistance * CGFloat(sinf(Float.pi / 4.0)) - (buttonB.size.height / 2)
        buttonA.position = CGPoint(x: buttonAx, y: buttonAy)
        addChild(buttonA)

        let buttonBx = center.x - buttonDistance * CGFloat(cosf(Float.pi / 2.0)) - (buttonB.size.width / 2)
        let buttonBy = center.y + buttonDistance * CGFloat(sinf(Float.pi / 2.0)) - (buttonB.size.height / 2)
        buttonB.position = CGPoint(x: buttonBx, y: buttonBy)
        addChild(buttonB)
    }

    override init() {
        super.init()
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```

[Next](Swift-iOS-ButtonOverlay.swift.md)[Previous](Swift-macOS-AppDelegate.swift.md)

