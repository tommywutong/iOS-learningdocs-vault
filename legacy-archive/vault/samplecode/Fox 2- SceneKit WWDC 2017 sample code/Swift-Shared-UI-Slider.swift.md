---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Swift_Shared_UI_Slider_swift.html
archived_at: '2026-07-26T19:54:17.436175Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Swift-Shared-UI-Menu.swift.md)[Previous](Swift-Shared-UI-Button.swift.md)

# Swift/Shared/UI/Slider.swift

```swift
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A basic `SKNode` based slider.
 */

import SpriteKit

class Slider: SKNode {
    var value: CGFloat = 0.0 {
        didSet {
            slider!.position = CGPoint(x: CGFloat(background!.position.x + value * width ), y: CGFloat(0.0))
        }
    }

    var label: SKLabelNode?
    var slider: SKShapeNode?
    var background: SKSpriteNode?
    private(set) var actionClicked: Selector?
    private(set) var targetClicked: AnyObject?

    init(width: Int, height: Int, text txt: String) {
        super.init()

        // create a label
        let fontName: String = "Optima-ExtraBlack"
        label = SKLabelNode(fontNamed: fontName)
        label!.text = txt
        label!.fontSize = 18
        label!.fontColor = SKColor.white
        label!.position = CGPoint(x: 0.0, y: -8.0)

        // create background & slider
        background = SKSpriteNode(color: SKColor.white, size: CGSize(width: CGFloat(width), height: CGFloat(2)))
        slider = SKShapeNode(circleOfRadius: CGFloat( height ) )
        slider!.fillColor = SKColor.white
        background!.anchorPoint = CGPoint(x: CGFloat(0.0), y: CGFloat(0.5))

        slider!.position = CGPoint(x: CGFloat(label!.frame.size.width / 2.0 + 15), y: CGFloat(0.0))
        background!.position = CGPoint(x: CGFloat(label!.frame.size.width / 2.0 + 15), y: CGFloat(0.0))

        // add to the root node
        addChild(label!)
        addChild(background!)
        addChild(slider!)

        // track mouse event
        isUserInteractionEnabled = true
        value = 0.0
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    var width: CGFloat {
        return background!.frame.size.width
    }

    var height: CGFloat {
        return slider!.frame.size.height
    }

    func setBackgroundColor(_ col: SKColor) {
        background!.color = col
    }

    func setClickedTarget(_ target: AnyObject, action: Selector) {
        targetClicked = target
        actionClicked = action
    }

#if os( OSX )
    override func mouseDown(with event: NSEvent) {
        mouseDragged(with: event)
    }

    override func mouseUp(with event: NSEvent) {
        setBackgroundColor(SKColor.white)
    }

    override func mouseDragged(with event: NSEvent) {
        setBackgroundColor(SKColor.gray)

        let posInView = scene!.convert(position, from:parent!)

        let x = event.locationInWindow.x - posInView.x - background!.position.x
        let pos = fmax(fmin(x, width), 0.0)
        slider!.position = CGPoint(x: CGFloat(background!.position.x + pos), y: 0.0)
        value = pos / width
        _ = targetClicked?.perform(actionClicked, with: self)
    }

#endif
#if os( iOS )
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        setBackgroundColor(SKColor.gray)
        let x = touches.first!.location(in: self).x - background!.position.x
        let pos = max(fmin(x, width), 0.0)

        slider!.position = CGPoint(x: CGFloat(background!.position.x + pos), y: CGFloat(0.0))
        value = pos / width
        _ = targetClicked!.perform(actionClicked, with: self)
    }
#endif
}
```

[Next](Swift-Shared-UI-Menu.swift.md)[Previous](Swift-Shared-UI-Button.swift.md)

