---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Swift_Shared_UI_Button_swift.html
archived_at: '2026-07-26T19:54:17.426384Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Swift-Shared-UI-Slider.swift.md)[Previous](Swift-Shared-Overlay.swift.md)

# Swift/Shared/UI/Button.swift

```swift
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A basic `SKNode` based button.
 */

import SpriteKit

class Button: SKNode {
    var width: CGFloat {
        return size.width
    }

    var label: SKLabelNode?
    var background: SKSpriteNode?
    private(set) var actionClicked: Selector?
    private(set) var targetClicked: Any?
    var size = CGSize.zero

    func setText(_ txt: String) {
        label!.text = txt
    }

    func setBackgroundColor(_ col: SKColor) {
        guard let background = background else { return }
        background.color = col
    }

    func setClickedTarget(_ target: Any, action: Selector) {
        targetClicked = target
        actionClicked = action
    }

    init(text txt: String) {
        super.init()

        // create a label
        let fontName: String = "Optima-ExtraBlack"
        label = SKLabelNode(fontNamed: fontName)
        label!.text = txt
        label!.fontSize = 18
        label!.fontColor = SKColor.white
        label!.position = CGPoint(x: CGFloat(0.0), y: CGFloat(-8.0))

        // create the background
        size = CGSize(width: CGFloat(label!.frame.size.width + 10.0), height: CGFloat(30.0))
        background = SKSpriteNode(color: SKColor(red: CGFloat(0), green: CGFloat(0), blue: CGFloat(0), alpha: CGFloat(0.75)), size: size)

        // add to the root node
        addChild(background!)
        addChild(label!)

        // Track mouse event
        isUserInteractionEnabled = true
    }

    init(skNode node: SKNode) {
        super.init()

        // Track mouse event
        isUserInteractionEnabled = true
        size = node.frame.size
        addChild(node)
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    func height() -> CGFloat {
        return size.height
    }

#if os( OSX )
    override func mouseDown(with event: NSEvent) {
        setBackgroundColor(SKColor(red: CGFloat(0), green: CGFloat(0), blue: CGFloat(0), alpha: CGFloat(1.0)))
    }

    override func mouseUp(with event: NSEvent) {
        setBackgroundColor(SKColor(red: CGFloat(0), green: CGFloat(0), blue: CGFloat(0), alpha: CGFloat(0.75)))

        let x = position.x + ((parent?.position.x) ?? CGFloat(0))
        let y = position.y + ((parent?.position.y) ?? CGFloat(0))
        let p = event.locationInWindow

        if fabs(p.x - x) < width / 2 * xScale && fabs(p.y - y) < height() / 2 * yScale {
            _ = (targetClicked! as AnyObject).perform(actionClicked, with: self)
        }
    }

#endif
#if os( iOS )
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        _ = (targetClicked! as AnyObject).perform(actionClicked, with: self)
    }
#endif
}
```

[Next](Swift-Shared-UI-Slider.swift.md)[Previous](Swift-Shared-Overlay.swift.md)

