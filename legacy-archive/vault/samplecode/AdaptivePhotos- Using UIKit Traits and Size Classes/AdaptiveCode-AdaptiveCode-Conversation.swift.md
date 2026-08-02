---
title: 'AdaptivePhotos: Using UIKit Traits and Size Classes'
apple_id: TP40014636
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AdaptivePhotos/Listings/AdaptiveCode_AdaptiveCode_Conversation_swift.html
archived_at: '2026-07-18T03:00:43.841635Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AdaptivePhotos: Using UIKit Traits and Size Classes](AdaptivePhotos-%20Using%20UIKit%20Traits%20and%20Size%20Classes.md)


[Next](AdaptiveCode-AdaptiveCode-AboutViewController.swift.md)[Previous](AdaptiveCode-AdaptiveCode-Photo.swift.md)

# AdaptiveCode/AdaptiveCode/Conversation.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The model object that represents a conversation.
*/

import Foundation

struct Conversation {
    // MARK: Properties

    var name = ""
    var photos = [Photo]()

    // MARK: Initialization

    init() {}

    init?(dictionary: [String: AnyObject]) {
        guard let name = dictionary["name"] as? String else { return nil }
        self.name = name

        if let photoDictionaries = dictionary["photos"] as? [[String: AnyObject]] {
            photos = photoDictionaries.flatMap { photoDictionary in
                return Photo(dictionary: photoDictionary)
            }
        }
        else {
            photos = []
        }
    }
}
```

[Next](AdaptiveCode-AdaptiveCode-AboutViewController.swift.md)[Previous](AdaptiveCode-AdaptiveCode-Photo.swift.md)

