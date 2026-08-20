---
title: 'MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control
  events'
apple_id: TP40017322
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/MPRemoteCommandSample/Listings/MPRemoteCommandSample_macOS_RemoteCommandView_swift.html
archived_at: '2026-07-27T06:57:10.508052Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control events](MPRemoteCommandSample-%20Using%20MPRemoteCommandCenter%20respond%20to%20remote%20control%20eve.md)


[Next](MPRemoteCommandSample-macOS-SplitViewController.swift.md)[Previous](MPRemoteCommandSample-macOS-AssetPlaybackViewController.swift.md)

# MPRemoteCommandSample-macOS/RemoteCommandView.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    `RemoteCommandView` is a `NSView` subclass that responds to the user toggling a specific `MPRemoteCommand` as enabled/disabled.
 */

import Cocoa

class RemoteCommandView: NSView {

    // MARK: Types

    /// The reuse identifier to use for retrieving this view.
    static let reuseIdentifier = "RemoteCommandViewIdentifier"

    // MARK: Properties

    /// The `NSButton` that is used for toggling an `MPRemoteCommand` as enabled or disabled.
    @IBOutlet weak var button: NSButton!

    /// The delegate that is used to respond to target-action calls.
    var delegate: RemoteCommandViewDelegate?

    // MARK: Target-Action

    @IBAction func userDidToggleCheckButton(_ sender: NSButton) {
        delegate?.remoteCommandView(self, didToggleTo: sender.state == NSOffState ? false : true)
    }
}

/// `RemoteCommandViewDelegate` provides a common interface for `RemoteCommandView` to provide callbacks to its `delegate`.
protocol RemoteCommandViewDelegate {

    /// This is called when the `NSButton` in a `RemoteCommandView` is clicked to reflect a change in state.
    func remoteCommandView(_ cell: RemoteCommandView, didToggleTo enabled: Bool)
}
```

[Next](MPRemoteCommandSample-macOS-SplitViewController.swift.md)[Previous](MPRemoteCommandSample-macOS-AssetPlaybackViewController.swift.md)
