---
title: 'AppChat: Using Peek and Pop APIs'
apple_id: TP40017298
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/AppChat/Listings/AppChat_Friend_swift.html
archived_at: '2026-07-18T03:01:06.359571Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppChat: Using Peek and Pop APIs](AppChat-%20Using%20Peek%20and%20Pop%20APIs.md)


[Next](AppChat-ChatReplyButton.swift.md)[Previous](AppChat-MathUtilities.swift.md)

# AppChat/Friend.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The struct that represents another user.
 */

import UIKit

typealias FriendIdentifier = String

struct Friend {
    var identifier: FriendIdentifier
    var name: String
    var profilePhoto: UIImage
}
```

[Next](AppChat-ChatReplyButton.swift.md)[Previous](AppChat-MathUtilities.swift.md)

