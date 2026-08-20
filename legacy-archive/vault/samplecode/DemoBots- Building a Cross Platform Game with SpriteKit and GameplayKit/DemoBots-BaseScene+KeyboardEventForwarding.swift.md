---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_BaseScene_KeyboardEventForwarding_swift.html
archived_at: '2026-07-18T03:06:15.682151Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-ControlInputSource.swift.md)[Previous](DemoBots-ProgressScene.swift.md)

# DemoBots/BaseScene+KeyboardEventForwarding.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An extension of `BaseScene` to provide OS X platform specific functionality. This file is only included in the OS X target.
*/

import Cocoa

/*
    Extend `BaseScene` to forward events from the scene to a platform-specific
    control input source. On OS X, this is a `KeyboardControlInputSource`.
*/
extension BaseScene {
    // MARK: Properties

    var keyboardControlInputSource: KeyboardControlInputSource {
        return sceneManager.gameInput.nativeControlInputSource as! KeyboardControlInputSource
    }

    // MARK: NSResponder

    override func mouseDown(with event: NSEvent) {
        keyboardControlInputSource.handleMouseDownEvent()
    }

    override func mouseUp(with event: NSEvent) {
        keyboardControlInputSource.handleMouseUpEvent()
    }

    override func keyDown(with event: NSEvent) {
        guard let characters = event.charactersIgnoringModifiers?.characters else { return }

        for character in characters {
            keyboardControlInputSource.handleKeyDown(forCharacter: character)
        }
    }

    override func keyUp(with event: NSEvent) {
        guard let characters = event.charactersIgnoringModifiers?.characters else { return }

        for character in characters {
            keyboardControlInputSource.handleKeyUp(forCharacter: character)
        }
    }
}
```

[Next](DemoBots-ControlInputSource.swift.md)[Previous](DemoBots-ProgressScene.swift.md)

