---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Protocols_ContactNotifiableType_swift.html
archived_at: '2026-07-18T03:06:20.556263Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-LevelScene%2BPause.swift.md)[Previous](DemoBots-SceneLoaderResourcesReadyState.swift.md)

# DemoBots/Protocols/ContactNotifiableType.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A protocol representing the ability of a `GKEntity` to respond to the start and end of a physics contact with another `GKEntity`.
*/

import GameplayKit

protocol ContactNotifiableType {

    func contactWithEntityDidBegin(_ entity: GKEntity)

    func contactWithEntityDidEnd(_ entity: GKEntity)
}
```

[Next](DemoBots-LevelScene%2BPause.swift.md)[Previous](DemoBots-SceneLoaderResourcesReadyState.swift.md)

