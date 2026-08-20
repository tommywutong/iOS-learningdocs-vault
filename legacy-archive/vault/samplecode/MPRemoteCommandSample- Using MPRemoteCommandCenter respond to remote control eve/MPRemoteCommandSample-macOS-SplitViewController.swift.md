---
title: 'MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control
  events'
apple_id: TP40017322
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/MPRemoteCommandSample/Listings/MPRemoteCommandSample_macOS_SplitViewController_swift.html
archived_at: '2026-07-27T06:57:10.512997Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control events](MPRemoteCommandSample-%20Using%20MPRemoteCommandCenter%20respond%20to%20remote%20control%20eve.md)


[Next](Shared-Model-Asset.swift.md)[Previous](MPRemoteCommandSample-macOS-RemoteCommandView.swift.md)

# MPRemoteCommandSample-macOS/SplitViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    `SplitViewController` is an `NSSplitViewController` subclass.
 */

import Cocoa

class SplitViewController: NSSplitViewController {

    // MARK: View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()

        splitView.autosaveName = "SplitViewControllerAutoSaveName"

        minimumThicknessForInlineSidebars = 10.0
    }

}
```

[Next](Shared-Model-Asset.swift.md)[Previous](MPRemoteCommandSample-macOS-RemoteCommandView.swift.md)
