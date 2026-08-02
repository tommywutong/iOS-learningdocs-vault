---
title: 'MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control
  events'
apple_id: TP40017322
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/MPRemoteCommandSample/Listings/Shared_Model_Asset_swift.html
archived_at: '2026-07-27T06:57:10.517775Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control events](MPRemoteCommandSample-%20Using%20MPRemoteCommandCenter%20respond%20to%20remote%20control%20eve.md)


[Next](Shared-Managers-AssetPlaybackManager.swift.md)[Previous](MPRemoteCommandSample-macOS-SplitViewController.swift.md)

# Shared/Model/Asset.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    `Asset` is a wrapper struct around an `AVURLAsset` and its asset name.
 */

import Foundation
import AVFoundation

struct Asset {

    // MARK: Types
    static let nameKey = "AssetName"

    // MARK: Properties

    /// The name of the asset to present in the application.
    let assetName: String

    /// The `AVURLAsset` corresponding to an asset in either the application bundle or on the Internet.
    let urlAsset: AVURLAsset
}
```

[Next](Shared-Managers-AssetPlaybackManager.swift.md)[Previous](MPRemoteCommandSample-macOS-SplitViewController.swift.md)
