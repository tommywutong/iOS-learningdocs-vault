---
title: 'Scoreboard: A demonstration of RTL support on macOS using NSStackView and
  localizedStringWithFormat'
apple_id: TP40017507
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/Scoreboard/Listings/Scoreboard_ClickableStepper_swift.html
archived_at: '2026-07-18T03:23:25.927516Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Scoreboard: A demonstration of RTL support on macOS using NSStackView and localizedStringWithFormat](Scoreboard-%20A%20demonstration%20of%20RTL%20support%20on%20macOS%20using%20NSStackView%20and%20locali.md)


[Next](Scoreboard-PlayerInfo.swift.md)[Previous](Scoreboard-AppDelegate.swift.md)

# Scoreboard/ClickableStepper.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The `ClickableStepper` returns the trackable area of the stepper in which the event occured, when the user interacts with the stepper to update the score.
 */

import Cocoa

class ClickableStepperCell : NSStepperCell {

    // MARK: NSCell

    override func hitTest(for event: NSEvent, in cellFrame: NSRect, of controlView: NSView) -> NSCellHitResult {
        return .trackableArea
    }
}
```

[Next](Scoreboard-PlayerInfo.swift.md)[Previous](Scoreboard-AppDelegate.swift.md)

