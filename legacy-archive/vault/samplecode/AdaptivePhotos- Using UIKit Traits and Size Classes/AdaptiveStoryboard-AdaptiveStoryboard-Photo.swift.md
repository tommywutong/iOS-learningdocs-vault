---
title: 'AdaptivePhotos: Using UIKit Traits and Size Classes'
apple_id: TP40014636
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AdaptivePhotos/Listings/AdaptiveStoryboard_AdaptiveStoryboard_Photo_swift.html
archived_at: '2026-07-18T03:00:44.934703Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AdaptivePhotos: Using UIKit Traits and Size Classes](AdaptivePhotos-%20Using%20UIKit%20Traits%20and%20Size%20Classes.md)


[Next](AdaptiveStoryboard-AdaptiveStoryboard-Conversation.swift.md)[Previous](AdaptiveStoryboard-AdaptiveStoryboard-User.swift.md)

# AdaptiveStoryboard/AdaptiveStoryboard/Photo.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The model object that represents an individual photo.
*/

import UIKit

class Photo: NSObject {
    // MARK: Properties

    var comment = ""
    var rating = 0

    var image: UIImage? {
        /*
            Custom implementation of the getter for the image property. The image
            property is a derived property. The image corresponding to `imageName`
            is loaded upon request. Note that if you had to load the image over a 
            network, you should instead define a method that takes a completion 
            handler, which is called when the image has been downloaded. See the
            LazyTableImages sample for an example.

            https://developer.apple.com/library/ios/samplecode/LazyTableImages/Introduction/Intro.html
        */
        if let path = Bundle.main.path(forResource: imageName, ofType: "jpg") {
            return UIImage(contentsOfFile: path)
        }
        else {
            return nil
        }
    }

    var imageName: String?

    // MARK: Initialization

    override init() { }

    init(dictionary: [String: AnyObject]) {
        imageName = dictionary["imageName"] as? String
        comment = dictionary["comment"] as? String ?? ""
        rating = dictionary["rating"] as? Int ?? 0
    }
}
```

[Next](AdaptiveStoryboard-AdaptiveStoryboard-Conversation.swift.md)[Previous](AdaptiveStoryboard-AdaptiveStoryboard-User.swift.md)

