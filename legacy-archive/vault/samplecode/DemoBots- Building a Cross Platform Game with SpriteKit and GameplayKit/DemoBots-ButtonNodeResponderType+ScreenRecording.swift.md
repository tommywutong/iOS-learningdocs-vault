---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_ButtonNodeResponderType_ScreenRecording_swift.html
archived_at: '2026-07-18T03:06:15.949670Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-KeyboardControlInputSource.swift.md)[Previous](DemoBots-Entities-FlyingBot.swift.md)

# DemoBots/ButtonNodeResponderType+ScreenRecording.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A protocol extension that adds methods to `ButtonNodeResponderType` to enable screen recording with ReplayKit.
*/

import ReplayKit


/// The `NSUserDefaults` key used to store whether screen recording has been enabled.
let screenRecorderEnabledKey = "AppConfiguration.Defaults.screenRecorderEnabledKey"

/*
    Extend `ButtonNodeResponderType` to add methods for screen recording with ReplayKit.
    The type constraint ensures that only types that are `BaseScene` instances will
    get this additional functionality.
*/
extension ButtonNodeResponderType where Self: BaseScene {
    func toggleScreenRecording(button: ButtonNode) {

        button.isSelected = !button.isSelected

        UserDefaults.standard.set(button.isSelected, forKey: screenRecorderEnabledKey)
    }

    func displayRecordedContent() {
        guard let previewViewController = previewViewController else { fatalError("The user requested playback, but a valid preview controller does not exist.") }
        guard let rootViewController = view?.window?.rootViewController else { fatalError("The scene must be contained in a window with a root view controller.") }

        // `RPPreviewViewController` only supports full screen modal presentation.
        previewViewController.modalPresentationStyle = UIModalPresentationStyle.fullScreen

        rootViewController.present(previewViewController, animated: true, completion:nil)
    }
}
```

[Next](DemoBots-KeyboardControlInputSource.swift.md)[Previous](DemoBots-Entities-FlyingBot.swift.md)

