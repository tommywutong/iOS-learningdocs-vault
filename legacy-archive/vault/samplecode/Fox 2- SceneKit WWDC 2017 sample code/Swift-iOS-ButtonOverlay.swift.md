---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Swift_iOS_ButtonOverlay_swift.html
archived_at: '2026-07-26T19:54:17.215594Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Swift-iOS-GameViewController.swift.md)[Previous](Swift-iOS-ControlOverlay.swift.md)

# Swift/iOS/ButtonOverlay.swift

```swift
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Support class for action buttons.
 */

import SpriteKit

protocol ButtonOverlayDelegate: NSObjectProtocol {
    func willPress(_ button: ButtonOverlay)

    func didPress(_ button: ButtonOverlay)
}

class ButtonOverlay: SKNode {
    // Default 25, 25

    var size = CGSize.zero {
        didSet {
            if size != oldValue {
                updateForSizeChange()
            }
        }
    }
    weak var delegate: ButtonOverlayDelegate?

    private var trackingTouch: UITouch?
    private var inner: SKShapeNode!
    private var background: SKShapeNode!
    private var label: SKLabelNode?

    init(_ text: NSString) {
        super.init()

        size = CGSize(width: CGFloat(40), height: CGFloat(40))
        alpha = 0.7
        isUserInteractionEnabled = true
        buildPad(text)

    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    func buildPad(_ text: NSString) {
        let backgroundRect = CGRect(x: CGFloat(0), y: CGFloat(0), width: CGFloat(size.width), height: CGFloat(size.height))
        background = SKShapeNode()
        background.path = CGPath( ellipseIn: backgroundRect, transform: nil)
        background.strokeColor = SKColor.black
        background.lineWidth = 3.0
        addChild(background)

        inner = SKShapeNode()
        inner.path = CGPath( ellipseIn: CGRect( x: 0, y: 0, width: innerSize.width, height: innerSize.height ), transform: nil)
        inner.lineWidth = 1.0
        inner.fillColor = SKColor.white
        inner.strokeColor = SKColor.gray
        addChild(inner)

        label = SKLabelNode()
        label!.fontName = UIFont.boldSystemFont(ofSize: 24).fontName
        label!.fontSize = 24
        label!.fontColor = SKColor.black
        label?.verticalAlignmentMode = .center
        label?.horizontalAlignmentMode = .center
        label?.position = CGPoint(x: size.width / 2.0, y: size.height / 2.0 + 1.0)
        label?.text = text as String
        addChild(label!)
    }

    func updateForSizeChange() {
        guard let background = background  else { return }

        let backgroundRect = CGRect(x: CGFloat(0), y: CGFloat(0), width: CGFloat(size.width), height: CGFloat(size.height))
        background.path = CGPath(ellipseIn: backgroundRect, transform: nil)
        let innerRect = CGRect(x: CGFloat(0), y: CGFloat(0), width: CGFloat(size.width / 3.0), height: CGFloat(size.height / 3.0))
        inner.path = CGPath(ellipseIn: innerRect, transform: nil)

        label!.position = CGPoint(x: size.width / 2.0 - label!.frame.size.width / 2.0, y: size.height / 2.0 - label!.frame.size.height / 2.0)
    }

    var innerSize: CGSize {
        return CGSize(width: CGFloat(size.width), height: CGFloat(size.height))
    }

    func resetInteraction() {
        trackingTouch = nil
        inner.fillColor = SKColor.white
        delegate!.didPress(self)
    }

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        trackingTouch = touches.first
        inner.fillColor = SKColor.black
        delegate!.willPress(self)
    }

    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        if touches.contains(trackingTouch!) {
            resetInteraction()
        }
    }

    override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
        if touches.contains(trackingTouch!) {
            resetInteraction()
        }
    }
}
```

[Next](Swift-iOS-GameViewController.swift.md)[Previous](Swift-iOS-ControlOverlay.swift.md)

