---
title: 'AppChat: Using Peek and Pop APIs'
apple_id: TP40017298
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/AppChat/Listings/AppChat_ChatItem_swift.html
archived_at: '2026-07-18T03:01:05.651236Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppChat: Using Peek and Pop APIs](AppChat-%20Using%20Peek%20and%20Pop%20APIs.md)


[Next](AppChat-ChatReplyPresentAnimator.swift.md)[Previous](AppChat-ChatReplyPresentationController.swift.md)

# AppChat/ChatItem.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The struct that represents a received chat.
 */

import UIKit

typealias ChatItemIdentifier = String

struct ChatItem {
    var identifier: ChatItemIdentifier
    var sender: Friend
    var date: Date
    var image: UIImage
    var saved: Bool
}
```

[Next](AppChat-ChatReplyPresentAnimator.swift.md)[Previous](AppChat-ChatReplyPresentationController.swift.md)

