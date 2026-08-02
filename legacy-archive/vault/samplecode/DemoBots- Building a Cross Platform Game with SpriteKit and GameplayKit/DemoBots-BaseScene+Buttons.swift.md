---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_BaseScene_Buttons_swift.html
archived_at: '2026-07-18T03:06:15.453775Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-TouchControlInputNode.swift.md)[Previous](DemoBots-GameInput.swift.md)

# DemoBots/BaseScene+Buttons.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An extension of `BaseScene` to enable it to respond to button presses.
*/

import Foundation

/// Extends `BaseScene` to respond to ButtonNode events.
extension BaseScene: ButtonNodeResponderType {

    /// Searches the scene for all `ButtonNode`s.
    func findAllButtonsInScene() -> [ButtonNode] {
        return ButtonIdentifier.allButtonIdentifiers.flatMap { buttonIdentifier in
            childNode(withName: "//\(buttonIdentifier.rawValue)") as? ButtonNode
        }
    }

    // MARK: ButtonNodeResponderType

    func buttonTriggered(button: ButtonNode) {
        switch button.buttonIdentifier! {
            case .home:
                sceneManager.transitionToScene(identifier: .home)

            case .proceedToNextScene:
                sceneManager.transitionToScene(identifier: .nextLevel)

            case .replay:
                sceneManager.transitionToScene(identifier: .currentLevel)

            case .screenRecorderToggle:
                #if os(iOS)
                toggleScreenRecording(button: button)
                #endif

            case .viewRecordedContent:
                #if os(iOS)
                displayRecordedContent()
                #endif

            default:
                fatalError("Unsupported ButtonNode type in Scene.")
        }
    }
}
```

[Next](DemoBots-TouchControlInputNode.swift.md)[Previous](DemoBots-GameInput.swift.md)

