---
title: 'MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control
  events'
apple_id: TP40017322
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/MPRemoteCommandSample/Listings/MPRemoteCommandSample_RemoteCommandListTableViewCell_swift.html
archived_at: '2026-07-27T06:57:10.360354Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control events](MPRemoteCommandSample-%20Using%20MPRemoteCommandCenter%20respond%20to%20remote%20control%20eve.md)


[Next](MPRemoteCommandSample-RemoteCommandListTableViewController.swift.md)[Previous](MPRemoteCommandSample-AssetListTableViewController.swift.md)

# MPRemoteCommandSample/RemoteCommandListTableViewCell.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    `RemoteCommandListTableViewCell` is a `UITableViewCell` subclass that responds to the user toggling a specific `MPRemoteCommand` as enabled/disabled.
 */

import UIKit

class RemoteCommandListTableViewCell: UITableViewCell {

    // MARK: Types

    /// The reuse identifier to use for retrieving this cell.
    static let reuseIdentifier = "RemoteCommandListTableViewCellIdentifier"

    // MARK: Properties

    /// The delegate that is used to respond to target-action calls.
    var delegate: RemoteCommandListTableViewCellDelegate?

    /// The `UILabel` for displaying the name of the command.
    @IBOutlet weak var commandTitleLabel: UILabel!

    // MARK: Target-Action Method

    @IBAction func userDidToggleSwitch(_ sender: UISwitch) {
        delegate?.remoteCommandListTableViewCell(self, didToggleTo: sender.isOn)
    }
}

/// `RemoteCommandListTableViewCellDelegate` provides a common interface for `RemoteCommandListTableViewCell` to provide callbacks to its `delegate`.
protocol RemoteCommandListTableViewCellDelegate {

    /// This is called when the `UISwitch` in a `RemoteCommandListTableViewCell` is toggled.
    func remoteCommandListTableViewCell(_ cell: RemoteCommandListTableViewCell, didToggleTo enabled: Bool)
}
```

[Next](MPRemoteCommandSample-RemoteCommandListTableViewController.swift.md)[Previous](MPRemoteCommandSample-AssetListTableViewController.swift.md)
