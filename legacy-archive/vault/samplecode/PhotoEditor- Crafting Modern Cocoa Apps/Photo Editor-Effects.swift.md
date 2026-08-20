---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_Effects_swift.html
archived_at: '2026-07-18T03:18:49.238698Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-ImageSizeViewController.swift.md)[Previous](Photo%20Editor-SidebarViewController.swift.md)

# Photo Editor/Effects.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Encapsulates the CoreImage filters that we expose through the Effects UI
 */

import Cocoa
import CoreImage

enum Effect {
    case blur
    case invert
    case monochrome

    var displayName: String {
        switch self {
            case .blur:
                return NSLocalizedString("Blur", comment: "Display name for the blur effect")

            case .invert:
                return NSLocalizedString("Invert Colors", comment: "Display name for the invert effect")

            case .monochrome:
                return NSLocalizedString("Black & White", comment: "Display name for the monochrome effect")
        }
    }

    private var filterName: String {
        switch self {
            case .blur:
                return "CIGaussianBlur"

            case .invert:
                return "CIColorInvert"

            case .monochrome:
                return "CIPhotoEffectMono"
        }
    }

    func createFilter() -> CIFilter {
        let filter = CIFilter(name: filterName)!
        filter.setDefaults()
        return filter
    }

    static var allEffects: [Effect] = [.blur, .invert, .monochrome]
}
```

[Next](Photo%20Editor-ImageSizeViewController.swift.md)[Previous](Photo%20Editor-SidebarViewController.swift.md)

