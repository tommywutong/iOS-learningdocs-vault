---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_Photo_swift.html
archived_at: '2026-07-18T03:18:49.621119Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-CanvasScrollView.swift.md)[Previous](Photo%20Editor-SidebarClipView.swift.md)

# Photo Editor/Photo.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A basic model class representation that contains the actual image data and some meta data about the image.
*/

import Cocoa

class Photo : NSObject, NSCoding {

    var title = ""
    var image: NSImage?

    /// Initialize a Photo object with no title and no image
    override init() {
    }

    /// Initialize a Photo object with a particular title and image
    init(title: String, image: NSImage) {
        self.title = title
        self.image = image
    }

    required init?(coder: NSCoder) {
        precondition(coder.allowsKeyedCoding, "Non-keyed coding is not supported")

        if let title = coder.decodeObject(forKey: "PhotoTitle") as? String {
            self.title = title
        }

        self.image = coder.decodeObject(forKey: "PhotoImage") as? NSImage
    }

    func encode(with coder: NSCoder) {
        precondition(coder.allowsKeyedCoding, "Non-keyed coding is not supported")

        coder.encode(title, forKey: "PhotoTitle")
        coder.encode(image, forKey: "PhotoImage")
    }

}
```

[Next](Photo%20Editor-CanvasScrollView.swift.md)[Previous](Photo%20Editor-SidebarClipView.swift.md)

