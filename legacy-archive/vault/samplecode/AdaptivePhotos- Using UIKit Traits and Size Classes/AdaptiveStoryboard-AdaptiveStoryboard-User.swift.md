---
title: 'AdaptivePhotos: Using UIKit Traits and Size Classes'
apple_id: TP40014636
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AdaptivePhotos/Listings/AdaptiveStoryboard_AdaptiveStoryboard_User_swift.html
archived_at: '2026-07-18T03:00:45.275583Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AdaptivePhotos: Using UIKit Traits and Size Classes](AdaptivePhotos-%20Using%20UIKit%20Traits%20and%20Size%20Classes.md)


[Next](AdaptiveStoryboard-AdaptiveStoryboard-Photo.swift.md)[Previous](AdaptiveStoryboard-AdaptiveStoryboard-Text.txt.md)

# AdaptiveStoryboard/AdaptiveStoryboard/User.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The top level model object. Manages a list of conversations and the user's profile.
*/

import Foundation

struct User {
    // MARK: Properties

    var name = ""
    var conversations = [Conversation]()
    var lastPhoto: Photo?

    // MARK: Initialization

    init() { }

    init?(dictionary: [String: AnyObject]) {
        guard let name = dictionary["name"] as? String else { return nil }

        self.name = name

        if let conversationDictionaries = dictionary["conversations"] as? [[String: AnyObject]] {
            conversations = conversationDictionaries.flatMap { conversationDictionary in
                return Conversation(dictionary: conversationDictionary)
            }
        }
        else {
            conversations = []
        }

        if let lastPhotoDictionary = dictionary["lastPhoto"] as? [String: AnyObject] {
            lastPhoto = Photo(dictionary: lastPhotoDictionary)
        }
    }
}
```

[Next](AdaptiveStoryboard-AdaptiveStoryboard-Photo.swift.md)[Previous](AdaptiveStoryboard-AdaptiveStoryboard-Text.txt.md)

