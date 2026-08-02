---
title: 'MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control
  events'
apple_id: TP40017322
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/MPRemoteCommandSample/Listings/MPRemoteCommandSample_macOS_WindowController_swift.html
archived_at: '2026-07-27T06:57:10.474078Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control events](MPRemoteCommandSample-%20Using%20MPRemoteCommandCenter%20respond%20to%20remote%20control%20eve.md)


[Next](MPRemoteCommandSample-macOS-AppDelegate.swift.md)[Previous](MPRemoteCommandSample-macOS-RemoteCommandConfigurationViewController.swift.md)

# MPRemoteCommandSample-macOS/WindowController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    `WindowController` is an `NSWindowController` subclass
 */

import Cocoa

class WindowController: NSWindowController {

    // MARK: Window Lifecycle

    override func windowDidLoad() {
        super.windowDidLoad()

        window?.setFrameAutosaveName("WindowController")
    }
}
```

[Next](MPRemoteCommandSample-macOS-AppDelegate.swift.md)[Previous](MPRemoteCommandSample-macOS-RemoteCommandConfigurationViewController.swift.md)
